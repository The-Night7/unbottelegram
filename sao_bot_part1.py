#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import json
import time
import random
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, filters, ContextTypes

# Import des modules d'intégration des étages
from palier import FLOORS_INFO
from floor_integration import (
    init_monster_data, get_available_monsters, get_monster_info, get_detailed_boss_info,
    generate_floor_info_message, generate_biome_info_message, can_access_biome,
    get_accessible_biomes, get_accessible_floors
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
    "items": {"Health Potion": 3, "Teleport Crystal": 1, "Boar Meat": 2},
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
        "/floor_info <étage> - Voir les détails d'un étage\n"
        "/biome_info <biome> - Voir les détails d'un biome\n"
        "/explore - Explorer un biome pour trouver des monstres\n"
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
async def profile_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        f"Localisation: {player['location']}\n"  # Modification ici - accès direct à location comme une chaîne
        f"Col: {player['col']}\n"
        f"Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()])}\n\n"
        f"Étages débloqués: {len(player.get('unlocked_floors', []))}\n"
        f"Boss vaincus: {len(player.get('defeated_bosses', []))}\n"
        f"Quêtes terminées: {len(player.get('completed_quests', []))}"
    )

    await update.message.reply_text(
        f"Profil de votre personnage:\n\n{stats}"
    )


# Travel/Location command
async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Travel to a location."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END

    # Get accessible floors for the player
    accessible_floors = get_accessible_floors(player)

    keyboard = [[floor] for floor in accessible_floors]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        f"Vous êtes actuellement à {player['location']}.\n"  # Modification ici - accès direct à location comme une chaîne
        "Vers quel étage souhaitez-vous voyager?",
        reply_markup=reply_markup
    )

    return CHOOSING_FLOOR


async def choose_floor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle floor selection."""
    floor_name = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END

    # Check if the selected floor is valid
    accessible_floors = get_accessible_floors(player)
    if floor_name not in accessible_floors:
        await update.message.reply_text(
            "Cet étage n'est pas accessible. Veuillez choisir parmi les options proposées."
        )
        return CHOOSING_FLOOR

    # Store the selected floor in context
    context.user_data["selected_floor"] = floor_name

    # Get accessible biomes for the player on this floor
    accessible_biomes = get_accessible_biomes(player, floor_name)

    keyboard = [[biome] for biome in accessible_biomes]
    keyboard.append(["Annuler"])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        f"Vous avez choisi l'étage {floor_name}.\n"
        "Vers quel biome souhaitez-vous aller?",
        reply_markup=reply_markup
    )

    return CHOOSING_BIOME


async def choose_biome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle biome selection."""
    biome_name = update.message.text

    if biome_name == "Annuler":
        await update.message.reply_text(
            "Voyage annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    floor_name = context.user_data.get("selected_floor")

    if not player or not floor_name:
        await update.message.reply_text(
            "Une erreur est survenue. Veuillez réessayer."
        )
        return ConversationHandler.END

    # Check if the player can access this biome
    can_access, message = can_access_biome(player, floor_name, biome_name)
    if not can_access:
        await update.message.reply_text(
            f"Vous ne pouvez pas accéder à ce biome: {message}"
        )
        return CHOOSING_BIOME

    # Update player location
    player["location"]["floor"] = floor_name
    player["location"]["biome"] = biome_name

    # Update unlocked floors and biomes
    if floor_name not in player["unlocked_floors"]:
        player["unlocked_floors"].append(floor_name)

    if floor_name not in player["unlocked_biomes"]:
        player["unlocked_biomes"][floor_name] = []

    if biome_name not in player["unlocked_biomes"][floor_name]:
        player["unlocked_biomes"][floor_name].append(biome_name)

    save_player(user_id, player)

    # Generate biome info message
    biome_info = generate_biome_info_message(floor_name, biome_name)

    await update.message.reply_text(
        f"Vous avez voyagé vers {biome_name} dans {floor_name}!\n\n"
        f"{biome_info}",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
