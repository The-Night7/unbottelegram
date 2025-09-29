#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import json
import time
import random
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes

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
    "col": 560,  # SAO currency
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

# Monster data
MONSTERS = {
    "Frenzy Boar": {
        "level": 1,
        "hp": 50,
        "attack": 5,
        "defense": 2,
        "exp": 10,
        "col": 30,
        "drops": {"Boar Meat": 0.8, "Boar Tusk": 0.3}
    },
    "Dire Wolf": {
        "level": 5,
        "hp": 120,
        "attack": 12,
        "defense": 5,
        "exp": 25,
        "col": 60,
        "drops": {"Wolf Pelt": 0.7, "Wolf Fang": 0.4}
    },
    "Kobold Sentinel": {
        "level": 10,
        "hp": 200,
        "attack": 18,
        "defense": 10,
        "exp": 50,
        "col": 100,
        "drops": {"Kobold Leather": 0.6, "Bronze Sword": 0.2}
    }
}

# Boss data
BOSSES = {
    "Illfang the Kobold Lord": {
        "level": 10,
        "hp": 500,
        "attack": 20,
        "defense": 15,
        "exp": 200,
        "col": 1000,
        "drops": {"Coat of Midnight": 1.0, "Kobold Lord's Talwar": 0.3},
        "description": "Un grand kobold armé d'une hache et d'un bouclier. Quand sa dernière barre de vie atteint le rouge, il change d'arme pour un talwar.",
        "required_level": 8,
        "floor": "Floor 1 - Tolbana"
    }
}

# Floor data
FLOORS = {
    "Floor 1 - Tolbana": {
        "unlocked": True,
        "boss": "Illfang the Kobold Lord",
        "boss_defeated": False
    },
    "Floor 2 - Urbus": {
        "unlocked": False,
        "boss": "Asterius the Taurus King",
        "boss_defeated": False,
        "unlock_requirement": "Vaincre Illfang the Kobold Lord"
    },
    "Floor 3 - Forest of Wandering": {
        "unlocked": False,
        "boss": "Asterius the Taurus King",
        "boss_defeated": False,
        "unlock_requirement": "Vaincre Asterius the Taurus King"
    },
    "Floor 22 - Forest House": {
        "unlocked": False,
        "boss": "The Storm Griffin",
        "boss_defeated": False,
        "unlock_requirement": "Niveau 35"
    },
    "Floor 50 - Algade": {
        "unlocked": False,
        "boss": "The Emperor of Darkness",
        "boss_defeated": False,
        "unlock_requirement": "Niveau 55"
    },
    "Floor 55 - Grandzam": {
        "unlocked": False,
        "boss": "The Adamantine Sentinel",
        "boss_defeated": False,
        "unlock_requirement": "Vaincre The Emperor of Darkness"
    },
    "Floor 75 - Boss Room": {
        "unlocked": False,
        "boss": "The Skull Reaper",
        "boss_defeated": False,
        "unlock_requirement": "Vaincre The Adamantine Sentinel"
    }
}

# Shop items
SHOP_ITEMS = {
    "Health Potion": 50,
    "Teleport Crystal": 200,
    "Strength Potion": 100,
    "Basic Armor": 300,
    "Enhanced Sword": 500
}

# Helper functions
def load_player_data():
    """Load player data from file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_player_data(data):
    """Save player data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_player_data(user_id):
    """Get player data for a specific user"""
    data = load_player_data()
    return data.get(str(user_id))

def save_player(user_id, player_data):
    """Save player data for a specific user"""
    data = load_player_data()
    data[str(user_id)] = player_data
    save_player_data(data)

def get_online_players():
    """Get list of online players (simplified - all saved players are considered online)"""
    data = load_player_data()
    return data

def level_up_check(player):
    """Check if player can level up and apply changes"""
    # Simple level up formula: level * 100 exp needed
    exp_needed = player["level"] * 100
    
    if player["exp"] >= exp_needed:
        player["level"] += 1
        player["exp"] -= exp_needed
        player["max_hp"] += 20
        player["hp"] = player["max_hp"]  # Heal on level up
        player["attack"] += 3
        player["defense"] += 2
        player["agility"] += 2
        return True
    return False

# Basic commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    user_id = str(user.id)
    
    player = get_player_data(user_id)
    
    if player:
        await update.message.reply_text(
            f"Bienvenue de retour dans Sword Art Online, {player['name']}!\n\n"
            "Utilisez /help pour voir les commandes disponibles."
        )
    else:
        await update.message.reply_text(
            f"Bienvenue dans Sword Art Online, {user.mention_html()}!\n\n"
            "Vous venez d'être piégé dans le jeu mortel Sword Art Online. "
            "Le seul moyen de vous échapper est de terminer les 100 étages.\n\n"
            "Pour commencer, créez votre personnage avec /create_character."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Commandes disponibles:\n"
        "/start - Démarrer le bot\n"
        "/help - Afficher ce message d'aide\n"
        "/create_character - Créer un nouveau personnage\n"
        "/profile - Afficher votre profil\n"
        "/location - Voyager vers un lieu\n"
        "/inventory - Voir votre inventaire\n"
        "/floors - Voir les étages disponibles\n"
        "/battle - Combattre un monstre\n"
        "/shop - Accéder à la boutique\n"
        "/buy <article> <quantité> - Acheter un article\n"
        "/boss - Défier le boss de l'étage\n"
        "/players - Voir les autres joueurs\n"
        "/interact - Interagir avec un autre joueur\n"
        "/heal - Se soigner avec une potion"
    )
    await update.message.reply_text(help_text)

# Character creation
async def create_character(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the character creation process."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if player:
        await update.message.reply_text(
            f"Vous avez déjà un personnage nommé {player['name']}.\n"
            "Vous ne pouvez pas en créer un nouveau pour le moment."
        )
        return ConversationHandler.END
    
    await update.message.reply_text(
        "Commençons la création de votre personnage SAO!\n"
        "Comment souhaitez-vous nommer votre personnage?"
    )
    
    return CHOOSING_NAME

async def choose_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store the character name and ask for weapon choice."""
    context.user_data["character_name"] = update.message.text
    
    keyboard = [[weapon] for weapon in WEAPONS]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Excellent, votre personnage s'appellera {context.user_data['character_name']}.\n"
        "Maintenant, choisissez votre arme principale:",
        reply_markup=reply_markup
    )
    
    return CHOOSING_WEAPON

async def choose_weapon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store the weapon choice and show character summary."""
    weapon = update.message.text
    
    if weapon not in WEAPONS:
        await update.message.reply_text(
            "Cette arme n'est pas disponible. Veuillez choisir parmi les options proposées."
        )
        return CHOOSING_WEAPON
    
    context.user_data["weapon"] = weapon
    context.user_data.update(DEFAULT_STATS)
    
    character_summary = (
        f"Nom: {context.user_data['character_name']}\n"
        f"Arme: {context.user_data['weapon']}\n"
        f"Niveau: {context.user_data['level']}\n"
        f"HP: {context.user_data['hp']}/{context.user_data['max_hp']}\n"
        f"Attaque: {context.user_data['attack']}\n"
        f"Défense: {context.user_data['defense']}\n"
        f"Agilité: {context.user_data['agility']}\n"
        f"Localisation: {context.user_data['location']['floor']}, {context.user_data['location']['biome']}"
    )
    
    keyboard = [["Confirmer", "Recommencer"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Voici le résumé de votre personnage:\n\n{character_summary}\n\n"
        "Confirmez-vous cette création?",
        reply_markup=reply_markup
    )
    
    return CONFIRMING_CHARACTER

async def confirm_character(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Confirm character creation and save data."""
    choice = update.message.text
    
    if choice == "Recommencer":
        await update.message.reply_text(
            "D'accord, recommençons. Comment souhaitez-vous nommer votre personnage?"
        )
        return CHOOSING_NAME
    
    # Create the character
    user_id = str(update.effective_user.id)
    player_data = {
        "name": context.user_data["character_name"],
        "weapon": context.user_data["weapon"],
        "level": context.user_data["level"],
        "exp": context.user_data["exp"],
        "hp": context.user_data["hp"],
        "max_hp": context.user_data["max_hp"],
        "attack": context.user_data["attack"],
        "defense": context.user_data["defense"],
        "agility": context.user_data["agility"],
        "location": context.user_data["location"],
        "items": context.user_data["items"],
        "col": context.user_data["col"],
        "skills": context.user_data["skills"],
        "quests": context.user_data["quests"],
        "completed_quests": context.user_data["completed_quests"],
        "defeated_bosses": context.user_data["defeated_bosses"],
        "unlocked_floors": context.user_data["unlocked_floors"],
        "unlocked_biomes": context.user_data["unlocked_biomes"],
        "last_battle": 0,  # Timestamp of last battle
        "created_at": time.time()
    }
    
    save_player(user_id, player_data)
    
    await update.message.reply_text(
        f"Félicitations! Votre personnage {player_data['name']} a été créé avec succès!\n"
        "Vous êtes maintenant prêt à explorer le monde d'Aincrad.\n\n"
        "Utilisez /help pour voir les commandes disponibles.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    # Clear user_data
    context.user_data.clear()
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation."""
    await update.message.reply_text(
        "Action annulée.",
        reply_markup=ReplyKeyboardRemove()
    )
    context.user_data.clear()
    return ConversationHandler.END

# Profile command
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show player profile."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Format player stats
    stats = (
        f"Nom: {player['name']}\n"
        f"Niveau: {player['level']}\n"
        f"EXP: {player['exp']}/{player['level'] * 100}\n"
        f"HP: {player['hp']}/{player['max_hp']}\n"
        f"Attaque: {player['attack']}\n"
        f"Défense: {player['defense']}\n"
        f"Agilité: {player['agility']}\n"
        f"Arme: {player['weapon']}\n"
        f"Localisation: {player['location']['floor']}, {player['location']['biome']}\n"
        f"Col: {player['col']}\n"
        f"Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()])}\n\n"
        f"Étages débloqués: {len(player['unlocked_floors'])}\n"
        f"Boss vaincus: {len(player['defeated_bosses'])}\n"
        f"Quêtes terminées: {len(player['completed_quests'])}"
    )
    
    await update.message.reply_text(
        f"Profil de votre personnage:\n\n{stats}"
    )

# Travel/Location command
async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Travel to a location."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Simplified location system
    locations = [
        "Town of Beginnings",
        "Floor 1 - Tolbana",
        "Floor 2 - Urbus",
        "Floor 3 - Forest of Wandering",
        "Floor 22 - Forest House",
        "Floor 50 - Algade",
        "Floor 55 - Grandzam",
        "Floor 75 - Boss Room"
    ]
    
    keyboard = [[location] for location in locations]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Vous êtes actuellement à {player['location']['floor']}, {player['location']['biome']}.\n"
        "Où souhaitez-vous aller?",
        reply_markup=reply_markup
    )

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle location selection."""
    location = update.message.text
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    player["location"]["floor"] = location
    player["location"]["biome"] = "Main Area"
    save_player(user_id, player)
    
    await update.message.reply_text(
        f"Vous avez voyagé vers {location}!"
    )

# Inventory command
async def inventory_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show player inventory."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    if not player["items"]:
        await update.message.reply_text("Votre inventaire est vide.")
        return
    
    inventory_text = "Votre inventaire:\n\n"
    for item, count in player["items"].items():
        inventory_text += f"- {item}: {count}\n"
    
    inventory_text += f"\nCol: {player['col']}"
    
    await update.message.reply_text(inventory_text)

# Floors command
async def floors_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show information about available floors."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    floors_text = "Étages d'Aincrad:\n\n"
    floors_text += "- Floor 1 - Tolbana: ✅ Débloqué\n"
    floors_text += "- Floor 2 - Urbus: 🔒 Verrouillé | Requis: Vaincre Illfang the Kobold Lord\n"
    floors_text += "- Floor 3 - Forest of Wandering: 🔒 Verrouillé | Requis: Vaincre Asterius the Taurus King\n"
    floors_text += "- Floor 22 - Forest House: 🔒 Verrouillé | Requis: Niveau 35\n"
    floors_text += "- Floor 50 - Algade: 🔒 Verrouillé | Requis: Niveau 55\n"
    floors_text += "- Floor 55 - Grandzam: 🔒 Verrouillé | Requis: Vaincre The Emperor of Darkness\n"
    floors_text += "- Floor 75 - Boss Room: 🔒 Verrouillé | Requis: Vaincre The Adamantine Sentinel\n"
    
    await update.message.reply_text(floors_text)

# Battle command
async def battle_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start a battle with a monster."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Simplified monster selection
    monster_name = "Frenzy Boar"
    monster = MONSTERS[monster_name].copy()
    
    # Store monster in context for the battle
    context.user_data["battle"] = {
        "monster_name": monster_name,
        "monster": monster,
        "round": 1
    }
    
    await update.message.reply_text(
        "Vous partez à la recherche de monstres à combattre...\n\n"
        f"Vous avez rencontré un {monster_name} (Niveau {monster['level']})!\n"
        f"HP du monstre: {monster['hp']}\n\n"
        "Que voulez-vous faire?",
        reply_markup=ReplyKeyboardMarkup([
            ["Attaquer", "Utiliser Potion"],
            ["Fuir"]
        ], one_time_keyboard=True)
    )
    
    return CHOOSING_BATTLE_ACTION

async def handle_battle_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle player's battle action."""
    action = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "battle" not in context.user_data:
        await update.message.reply_text("Erreur: Combat non initialisé.")
        return ConversationHandler.END
    
    battle = context.user_data["battle"]
    monster_name = battle["monster_name"]
    monster = battle["monster"]
    
    if action == "Fuir":
        # 50% chance to escape
        if random.random() < 0.5:
            await update.message.reply_text(
                f"Vous avez réussi à fuir le combat contre {monster_name}!",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                f"Vous n'avez pas réussi à fuir! Le {monster_name} vous attaque!"
            )
            # Monster attacks
            damage = max(1, monster["attack"] - player["defense"] // 2)
            player["hp"] -= damage
            save_player(user_id, player)
            
            if player["hp"] <= 0:
                player["hp"] = 1  # Prevent death, just leave at 1 HP
                save_player(user_id, player)
                
                await update.message.reply_text(
                    f"Le {monster_name} vous a vaincu! Vous êtes gravement blessé.\n"
                    "Vous avez été téléporté en ville avec 1 HP.",
                    reply_markup=ReplyKeyboardRemove()
                )
                return ConversationHandler.END
            
            await update.message.reply_text(
                f"Le {monster_name} vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BATTLE_ACTION
    
    elif action == "Utiliser Potion":
        if player["items"].get("Health Potion", 0) > 0:
            heal_amount = 50
            player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
            player["items"]["Health Potion"] -= 1
            save_player(user_id, player)
            
            await update.message.reply_text(
                f"Vous utilisez une potion de soin et récupérez {heal_amount} HP!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n"
                f"Potions restantes: {player['items'].get('Health Potion', 0)}"
            )
            
            # Monster still attacks
            damage = max(1, monster["attack"] - player["defense"] // 2)
            player["hp"] -= damage
            save_player(user_id, player)
            
            await update.message.reply_text(
                f"Le {monster_name} vous attaque et vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BATTLE_ACTION
        else:
            await update.message.reply_text(
                "Vous n'avez pas de potions de soin!\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BATTLE_ACTION
    
    elif action == "Attaquer":
        # Player attacks
        player_damage = max(1, player["attack"] - monster["defense"] // 2)
        monster["hp"] -= player_damage
        
        battle_text = f"Vous attaquez le {monster_name} et infligez {player_damage} points de dégâts!\n"
        battle_text += f"HP du {monster_name}: {monster['hp']}\n\n"
        
        # Check if monster is defeated
        if monster["hp"] <= 0:
            # Calculate rewards
            exp_gain = monster["exp"]
            col_gain = monster["col"]
            
            # Add exp and col
            player["exp"] += exp_gain
            player["col"] += col_gain
            
            # Check for drops
            drops = []
            for item, chance in monster["drops"].items():
                if random.random() < chance:
                    if item not in player["items"]:
                        player["items"][item] = 0
                    player["items"][item] += 1
                    drops.append(item)
            
            # Check for level up
            leveled_up = level_up_check(player)
            
            # Save player data
            save_player(user_id, player)
            
            # Prepare victory message
            victory_text = f"Vous avez vaincu le {monster_name}!\n"
            victory_text += f"Vous gagnez {exp_gain} EXP et {col_gain} Col.\n"
            
            if drops:
                victory_text += f"Objets obtenus: {', '.join(drops)}\n"
            
            if leveled_up:
                victory_text += f"\nFélicitations! Vous avez atteint le niveau {player['level']}!"
            
            await update.message.reply_text(
                battle_text + victory_text,
                reply_markup=ReplyKeyboardRemove()
            )
            
            return ConversationHandler.END
        
        # Monster attacks
        monster_damage = max(1, monster["attack"] - player["defense"] // 2)
        player["hp"] -= monster_damage
        save_player(user_id, player)
        
        battle_text += f"Le {monster_name} vous attaque et vous inflige {monster_damage} points de dégâts!\n"
        battle_text += f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
        
        # Check if player is defeated
        if player["hp"] <= 0:
            player["hp"] = 1  # Prevent death, just leave at 1 HP
            save_player(user_id, player)
            
            await update.message.reply_text(
                battle_text + f"Le {monster_name} vous a vaincu! Vous êtes gravement blessé.\n"
                "Vous avez été téléporté en ville avec 1 HP.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        # Continue battle
        await update.message.reply_text(
            battle_text + "Que voulez-vous faire?",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BATTLE_ACTION
    
    else:
        await update.message.reply_text(
            "Action non reconnue. Veuillez choisir parmi les options proposées.",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BATTLE_ACTION

# Shop command
async def shop_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Access the shop."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    shop_text = f"Bienvenue à la boutique! Vous avez {player['col']} Col.\n\n"
    shop_text += "Articles disponibles:\n"
    
    for item, price in SHOP_ITEMS.items():
        shop_text += f"- {item}: {price} Col\n"
    
    shop_text += "\nPour acheter un article, utilisez /buy <article> <quantité>"
    
    await update.message.reply_text(shop_text)

async def buy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Buy items from the shop."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Parse arguments
    args = context.args
    if len(args) < 2:
        await update.message.reply_text(
            "Usage: /buy <article> <quantité>\n"
            "Exemple: /buy Health Potion 3"
        )
        return
    
    # Handle multi-word item names
    quantity_str = args[-1]
    item_name = " ".join(args[:-1])
    
    try:
        quantity = int(quantity_str)
    except ValueError:
        await update.message.reply_text("La quantité doit être un nombre.")
        return
    
    if quantity <= 0:
        await update.message.reply_text("La quantité doit être positive.")
        return
    
    if item_name not in SHOP_ITEMS:
        await update.message.reply_text(
            f"Article non disponible: {item_name}\n"
            "Utilisez /shop pour voir les articles disponibles."
        )
        return
    
    # Calculate total cost
    price = SHOP_ITEMS[item_name]
    total_cost = price * quantity
    
    if player["col"] < total_cost:
        await update.message.reply_text(
            f"Vous n'avez pas assez de Col. Il vous faut {total_cost} Col."
        )
        return
    
    # Process purchase
    player["col"] -= total_cost
    
    if item_name not in player["items"]:
        player["items"][item_name] = 0
    player["items"][item_name] += quantity
    
    save_player(user_id, player)
    
    await update.message.reply_text(
        f"Vous avez acheté {quantity} {item_name} pour {total_cost} Col.\n"
        f"Col restant: {player['col']}"
    )

# Boss command
async def boss_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Challenge the boss of the current floor."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Get current floor boss
    current_floor = player["location"]["floor"]
    boss_name = "Illfang the Kobold Lord"  # Simplified for now
    boss = BOSSES[boss_name]
    
    # Store boss in context
    context.user_data["boss"] = boss.copy()
    context.user_data["boss_name"] = boss_name
    
    # Show boss information
    boss_text = (
        f"Vous êtes sur le point d'affronter {boss_name}, le boss du premier étage!\n\n"
        f"Niveau du boss: {boss['level']}\n"
        f"HP: {boss['hp']}\n"
        f"Attaque: {boss['attack']}\n"
        f"Défense: {boss['defense']}\n\n"
        f"{boss['description']}\n\n"
        "Êtes-vous sûr de vouloir défier ce boss? Cette bataille sera difficile!"
    )
    
    keyboard = [["Défier le boss", "Annuler"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        boss_text,
        reply_markup=reply_markup
    )
    
    return CONFIRMING_BOSS_BATTLE

async def confirm_boss_battle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Confirm and start boss battle."""
    choice = update.message.text
    
    if choice != "Défier le boss":
        await update.message.reply_text(
            "Vous avez décidé de ne pas affronter le boss pour le moment.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    boss_name = context.user_data["boss_name"]
    
    # Start the boss battle
    await update.message.reply_text(
        f"Le combat contre {boss_name} commence!\n\n"
        f"Le {boss_name} vous fixe du regard, prêt à attaquer.\n"
        "Que voulez-vous faire?",
        reply_markup=ReplyKeyboardMarkup([
            ["Attaquer", "Utiliser Potion"],
            ["Utiliser Compétence", "Fuir"]
        ], one_time_keyboard=True)
    )
    
    return CHOOSING_BOSS_ACTION

async def handle_boss_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle player's action in boss battle."""
    action = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "boss" not in context.user_data:
        await update.message.reply_text("Erreur: Combat de boss non initialisé.")
        return ConversationHandler.END
    
    boss = context.user_data["boss"]
    boss_name = context.user_data["boss_name"]
    
    # Simplified boss battle - just end it
    await update.message.reply_text(
        "Cette fonctionnalité sera pleinement implémentée prochainement.\n"
        "Pour l'instant, le combat est interrompu.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

# Players command
async def players_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show other players."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Get all players
    all_players = get_online_players()
    
    if len(all_players) <= 1:
        await update.message.reply_text(
            "Il n'y a pas d'autres joueurs en ligne actuellement."
        )
        return
    
    # List players except self
    player_list = "Joueurs en ligne:\n\n"
    for pid, p in all_players.items():
        if pid != user_id:
            player_list += f"- {p['name']} (Niveau {p['level']}) - {p['location']['floor']}, {p['location']['biome']}\n"
    
    await update.message.reply_text(player_list)

# Interact command
async def interact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Interact with another player."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    await update.message.reply_text(
        "Cette fonctionnalité sera disponible prochainement."
    )

# Heal command
async def heal_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Use a health potion to heal."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    if player["hp"] >= player["max_hp"]:
        await update.message.reply_text("Vous avez déjà tous vos points de vie.")
        return
    
    if player["items"].get("Health Potion", 0) <= 0:
        await update.message.reply_text(
            "Vous n'avez pas de potions de soin. Achetez-en à la boutique avec /shop."
        )
        return
    
    # Use potion
    heal_amount = 50
    player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
    player["items"]["Health Potion"] -= 1
    
    if player["items"]["Health Potion"] <= 0:
        del player["items"]["Health Potion"]
    
    save_player(user_id, player)
    
    await update.message.reply_text(
        f"Vous utilisez une potion de soin et récupérez {heal_amount} HP!\n"
        f"Vos HP: {player['hp']}/{player['max_hp']}\n"
        f"Potions restantes: {player['items'].get('Health Potion', 0)}"
    )

def main() -> None:
    """Start the bot."""
    # Create the Application
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("No token provided. Set TELEGRAM_BOT_TOKEN in .env file")
        return
        
    application = Application.builder().token(token).build()

    # Character creation conversation
    character_creation_handler = ConversationHandler(
        entry_points=[CommandHandler("create_character", create_character)],
        states={
            CHOOSING_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_name)],
            CHOOSING_WEAPON: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_weapon)],
            CONFIRMING_CHARACTER: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_character)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    # Battle conversation
    battle_handler = ConversationHandler(
        entry_points=[CommandHandler("battle", battle_command)],
        states={
            CHOOSING_BATTLE_ACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_battle_action)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    # Boss battle conversation
    boss_handler = ConversationHandler(
        entry_points=[CommandHandler("boss", boss_command)],
        states={
            CONFIRMING_BOSS_BATTLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_boss_battle)],
            CHOOSING_BOSS_ACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_boss_action)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(character_creation_handler)
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CommandHandler("location", location_command))
    application.add_handler(CommandHandler("travel", location_command))
    application.add_handler(CommandHandler("inventory", inventory_command))
    application.add_handler(CommandHandler("floors", floors_command))
    application.add_handler(battle_handler)
    application.add_handler(CommandHandler("shop", shop_command))
    application.add_handler(CommandHandler("buy", buy_command))
    application.add_handler(boss_handler)
    application.add_handler(CommandHandler("players", players_command))
    application.add_handler(CommandHandler("interact", interact_command))
    application.add_handler(CommandHandler("heal", heal_command))
    
    # Add message handlers for location selection
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        handle_location
    ))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()