# -*- coding: utf-8 -*-

import os
import logging
import json
import time
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters, ContextTypes

# Import étages
from palier.etage1 import FLOOR_1_INFO
from palier.etage2 import FLOOR_2_INFO
from palier.etage3 import FLOOR_3_INFO
from palier.etage22 import FLOOR_22_INFO
from palier.etage50 import FLOOR_50_INFO
from palier.etage55 import FLOOR_55_INFO
from palier.etage75 import FLOOR_75_INFO

# Import monstres
from monstres.monstre_manager import MONSTERS

# Import quêtes
from utils.quests import ALL_QUESTS, FLOOR_1_QUESTS, FLOOR_2_QUESTS, FLOOR_3_QUESTS, FLOOR_22_QUESTS, FLOOR_50_QUESTS, FLOOR_55_QUESTS, FLOOR_75_QUESTS

# Import constantes et utilitaires
from utils.helpers import (
    load_player_data,
    save_player_data,
    get_player_data,
    save_player,
    level_up_check,
    get_monster_for_player,
    get_online_players,
    format_player_stats
)

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Conversation states
(
    CHOOSING_NAME, 
    CHOOSING_WEAPON, 
    CHOOSING_STATS, 
    CONFIRMING_CHARACTER,
    CHOOSING_BATTLE_ACTION,
    CHOOSING_INTERACTION,
    CHOOSING_TRADE_ITEM,
    CHOOSING_TRADE_AMOUNT,
    CONFIRMING_TRADE,
    CHOOSING_FLOOR,
    CHOOSING_BIOME,
    CONFIRMING_BOSS_BATTLE,
    CHOOSING_BOSS_ACTION
) = range(13)

# Data storage
DATA_FILE = "player_data.json"

# Default stats for new characters
DEFAULT_STATS = {
    "level": 1,
    "exp": 0,
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "defense": 5,
    "agility": 5,
    "location": {"floor": "Floor 1 - Tolbana", "biome": "Plains of Beginning"},
    "items": {"Health Potion": 3, "Teleport Crystal": 1},
    "col": 500,  # SAO currency
    "skills": [],
    "quests": [],
    "completed_quests": [],
    "defeated_bosses": [],
    "unlocked_floors": ["Floor 1 - Tolbana"],
    "unlocked_biomes": {"Floor 1 - Tolbana": ["Plains of Beginning"]}
}

# Available weapons
WEAPONS = [
    "One-Handed Sword",
    "Rapier",
    "Two-Handed Sword",
    "Dagger",
    "Mace",
    "Spear",
    "Axe",
    "Bow"
]

# Floors information
FLOORS_INFO = {
    "Floor 1 - Tolbana": FLOOR_1_INFO,
    "Floor 2 - Urbus": FLOOR_2_INFO,
    "Floor 3 - Forest of Wandering": FLOOR_3_INFO,
    "Floor 22 - Forest House": FLOOR_22_INFO,
    "Floor 50 - Algade": FLOOR_50_INFO,
    "Floor 55 - Grandzam": FLOOR_55_INFO,
    "Floor 75 - Boss Room": FLOOR_75_INFO
}

# Floor quests mapping
FLOOR_QUESTS = {
    "Floor 1 - Tolbana": FLOOR_1_QUESTS,
    "Floor 2 - Urbus": FLOOR_2_QUESTS,
    "Floor 3 - Forest of Wandering": FLOOR_3_QUESTS,
    "Floor 22 - Forest House": FLOOR_22_QUESTS,
    "Floor 50 - Algade": FLOOR_50_QUESTS,
    "Floor 55 - Grandzam": FLOOR_55_QUESTS,
    "Floor 75 - Boss Room": FLOOR_75_QUESTS
}

# Helper functions for progression
async def check_biome_unlocks(player):
    """Check and unlock biomes based on player level and completed quests."""
    for floor_name, floor_info in FLOORS_INFO.items():
        if floor_name in player["unlocked_floors"]:
            for biome in floor_info["biomes"]:
                biome_name = biome["name"]
                
                # Skip already unlocked biomes
                if biome_name in player["unlocked_biomes"].get(floor_name, []):
                    continue
                
                # Check requirements
                requirements = biome["unlock_requirements"]
                if requirements:
                    meets_requirements = True
                    
                    if "level" in requirements and player["level"] < requirements["level"]:
                        meets_requirements = False
                    
                    if "quest_completed" in requirements:
                        if requirements["quest_completed"] not in player.get("completed_quests", []):
                            meets_requirements = False
                    
                    if meets_requirements:
                        # Unlock the biome
                        if floor_name not in player["unlocked_biomes"]:
                            player["unlocked_biomes"][floor_name] = []
                        player["unlocked_biomes"][floor_name].append(biome_name)

async def unlock_next_floor(player, defeated_boss):
    """Unlock the next floor if requirements are met."""
    current_floor = player["location"]["floor"]
    floor_index = list(FLOORS_INFO.keys()).index(current_floor)
    
    # Check if there's a next floor
    if floor_index + 1 < len(FLOORS_INFO):
        next_floor = list(FLOORS_INFO.keys())[floor_index + 1]
        next_floor_info = FLOORS_INFO[next_floor]
        
        # Check requirements
        requirements = next_floor_info["unlock_requirements"]
        if requirements:
            meets_requirements = True
            
            if "boss_defeated" in requirements and requirements["boss_defeated"] != defeated_boss:
                meets_requirements = False
            
            if "level" in requirements and player["level"] < requirements["level"]:
                meets_requirements = False
            
            if meets_requirements:
                # Unlock the floor
                if next_floor not in player["unlocked_floors"]:
                    player["unlocked_floors"].append(next_floor)
                
                # Unlock the first biome of the floor
                if next_floor not in player["unlocked_biomes"]:
                    player["unlocked_biomes"][next_floor] = []
                
                first_biome = next_floor_info["biomes"][0]["name"]
                if first_biome not in player["unlocked_biomes"][next_floor]:
                    player["unlocked_biomes"][next_floor].append(first_biome)