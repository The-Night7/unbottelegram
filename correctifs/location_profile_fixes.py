#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Correctifs pour les fonctions profile_command et location_command
pour gérer correctement la nouvelle structure de localisation (dictionnaire au lieu de chaîne).
"""

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from utils.player import get_player_data
from utils.floor import get_accessible_floors


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

    return CHOOSING_FLOOR  # Assurez-vous que cette constante est importée ou définie