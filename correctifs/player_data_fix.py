#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Correctifs pour les fonctions de sao_bot_part1.py et sao_bot_part2.py
pour gérer correctement la nouvelle structure de données des joueurs.
"""

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

from utils.player import get_player_data, save_player
from utils.floor import get_accessible_floors, get_accessible_biomes, can_access_biome, generate_biome_info_message


# Profile command (version corrigée)
async def profile_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show player profile."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return

    # Format location based on the structure
    if isinstance(player['location'], dict):
        location_str = f"{player['location']['floor']}, {player['location']['biome']}"
    else:
        location_str = player['location']  # Fallback au cas où

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
        f"Localisation: {location_str}\n"
        f"Col: {player['col']}\n"
        f"Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()])}\n\n"
        f"Étages débloqués: {len(player.get('unlocked_floors', []))}\n"
        f"Boss vaincus: {len(player.get('defeated_bosses', []))}\n"
        f"Quêtes terminées: {len(player.get('completed_quests', []))}"
    )

    await update.message.reply_text(
        f"Profil de votre personnage:\n\n{stats}"
    )


# Travel/Location command (version corrigée)
async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Travel to a location."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END

    # Format location based on the structure
    if isinstance(player['location'], dict):
        location_str = f"{player['location']['floor']}, {player['location']['biome']}"
    else:
        location_str = player['location']  # Fallback au cas où

    # Get accessible floors for the player
    accessible_floors = get_accessible_floors(player)

    keyboard = [[floor] for floor in accessible_floors]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        f"Vous êtes actuellement à {location_str}.\n"
        "Vers quel étage souhaitez-vous voyager?",
        reply_markup=reply_markup
    )

    return CHOOSING_FLOOR


# Fonction utilitaire pour vérifier si un joueur existe et initialiser les champs manquants si nécessaire
def ensure_player_data(player):
    """Vérifie si les données du joueur sont complètes et les initialise si nécessaire."""
    if not player:
        return None
    
    # Vérifier et initialiser les champs manquants
    if not isinstance(player.get('location'), dict):
        # Convertir la location en dictionnaire
        location_str = player.get('location', 'Floor 1 - Tolbana, Plains of Beginning')
        parts = location_str.split(', ')
        if len(parts) == 2:
            floor_name, biome_name = parts
        else:
            floor_name = location_str
            biome_name = "Plains of Beginning"
        
        player['location'] = {
            'floor': floor_name,
            'biome': biome_name
        }
    
    # Initialiser les autres champs s'ils sont manquants
    if 'unlocked_floors' not in player:
        player['unlocked_floors'] = ["Floor 1 - Tolbana"]
    
    if 'unlocked_biomes' not in player:
        player['unlocked_biomes'] = {"Floor 1 - Tolbana": ["Plains of Beginning"]}
    
    if 'defeated_bosses' not in player:
        player['defeated_bosses'] = []
    
    if 'completed_quests' not in player:
        player['completed_quests'] = []
    
    if 'quests' not in player:
        player['quests'] = []
    
    if 'skills' not in player:
        player['skills'] = []
    
    if 'last_battle' not in player:
        player['last_battle'] = 0
    
    return player


# Wrapper pour get_player_data qui assure que les données sont complètes
def get_player_data_safe(user_id):
    """Récupère les données du joueur et s'assure qu'elles sont complètes."""
    player = get_player_data(user_id)
    return ensure_player_data(player)