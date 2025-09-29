#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import json
import time
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

# Import constantes et utilitaires
from utils.constants import (
    CONVERSATION_STATES,
    DEFAULT_STATS,
    WEAPONS,
    SAO_LOCATIONS,
    QUESTS
)
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

# Unpacking conversation states
(
    CHOOSING_NAME, 
    CHOOSING_WEAPON, 
    CHOOSING_STATS, 
    CONFIRMING_CHARACTER,
    CHOOSING_BATTLE_ACTION,
    CHOOSING_INTERACTION,
    CHOOSING_TRADE_ITEM,
    CHOOSING_TRADE_AMOUNT,
    CONFIRMING_TRADE
) = CONVERSATION_STATES

# Data storage
DATA_FILE = "player_data.json"

# Bot commands
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
        "/quest - Obtenir une quête\n"
        "/battle - Combattre un monstre\n"
        "/players - Voir les autres joueurs\n"
        "/interact - Interagir avec un autre joueur\n"
        "/shop - Accéder à la boutique\n"
        "/heal - Se soigner (utiliser une potion)\n"
        "/inventory - Voir votre inventaire"
    )
    await update.message.reply_text(help_text)

# Character creation conversation
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
    """Store the weapon choice and ask for stat distribution."""
    weapon = update.message.text
    
    if weapon not in WEAPONS:
        await update.message.reply_text(
            "Cette arme n'est pas disponible. Veuillez choisir parmi les options proposées."
        )
        return CHOOSING_WEAPON
    
    context.user_data["weapon"] = weapon
    
    # We'll use default stats for simplicity
    context.user_data.update(DEFAULT_STATS)
    
    # Show character summary
    character_summary = (
        f"Nom: {context.user_data['character_name']}\n"
        f"Arme: {context.user_data['weapon']}\n"
        f"Niveau: {context.user_data['level']}\n"
        f"HP: {context.user_data['hp']}/{context.user_data['max_hp']}\n"
        f"Attaque: {context.user_data['attack']}\n"
        f"Défense: {context.user_data['defense']}\n"
        f"Agilité: {context.user_data['agility']}"
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
        "Création de personnage annulée.",
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
    
    stats = format_player_stats(player)
    
    await update.message.reply_text(
        f"Profil de votre personnage:\n\n{stats}"
    )

# Location command
async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Travel to a location."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    keyboard = [[location] for location in SAO_LOCATIONS]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Vous êtes actuellement à {player['location']}.\n"
        "Où souhaitez-vous aller?",
        reply_markup=reply_markup
    )

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle location selection."""
    location = update.message.text
    
    if location not in SAO_LOCATIONS:
        await update.message.reply_text("Cette localisation n'existe pas.")
        return
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    player["location"] = location
    save_player(user_id, player)
    
    await update.message.reply_text(
        f"Vous avez voyagé vers {location}!",
        reply_markup=ReplyKeyboardRemove()
    )

# Battle command
async def battle_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a battle with a monster."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Check if player can battle (cooldown of 30 seconds)
    current_time = time.time()
    if current_time - player.get("last_battle", 0) < 30:
        remaining = int(30 - (current_time - player.get("last_battle", 0)))
        await update.message.reply_text(
            f"Vous devez attendre encore {remaining} secondes avant de pouvoir combattre à nouveau."
        )
        return
    
    # Get appropriate monster
    monster_name, monster = get_monster_for_player(player)
    
    # Store monster in context for the battle
    context.user_data["battle"] = {
        "monster_name": monster_name,
        "monster": monster.copy(),
        "round": 1
    }
    
    # Update last battle timestamp
    player["last_battle"] = current_time
    save_player(user_id, player)
    
    await update.message.reply_text(
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
            
            # Update quest progress if applicable
            await update_quest_progress(update, context, monster_name)
            
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

# Quest system
async def quest_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get or view quests."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Show active quests
    active_quests = player.get("quests", [])
    
    if active_quests:
        quest_text = "Vos quêtes actives:\n\n"
        for quest_id in active_quests:
            for quest in QUESTS:
                if quest["id"] == quest_id:
                    quest_text += f"- {quest['title']}: {quest['description']}\n"
                    break
        
        keyboard = [["Nouvelle quête"], ["Retour"]]
    else:
        quest_text = "Vous n'avez pas de quêtes actives."
        keyboard = [["Nouvelle quête"], ["Retour"]]
    
    await update.message.reply_text(
        quest_text,
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

async def handle_quest_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle quest actions."""
    action = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un.",
            reply_markup=ReplyKeyboardRemove()
        )
        return
    
    if action == "Nouvelle quête":
        # Find quests that aren't already active
        active_quest_ids = player.get("quests", [])
        available_quests = [q for q in QUESTS if q["id"] not in active_quest_ids]
        
        if not available_quests:
            await update.message.reply_text(
                "Il n'y a pas de nouvelles quêtes disponibles pour le moment.",
                reply_markup=ReplyKeyboardRemove()
            )
            return
        
        # Select a random quest
        new_quest = random.choice(available_quests)
        
        # Add to player's quests
        if "quests" not in player:
            player["quests"] = []
        player["quests"].append(new_quest["id"])
        save_player(user_id, player)
        
        await update.message.reply_text(
            f"Nouvelle quête acceptée: {new_quest['title']}\n"
            f"{new_quest['description']}\n\n"
            f"Récompenses: {new_quest['reward']['exp']} EXP, {new_quest['reward']['col']} Col",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await update.message.reply_text(
            "Action annulée.",
            reply_markup=ReplyKeyboardRemove()
        )

async def update_quest_progress(update: Update, context: ContextTypes.DEFAULT_TYPE, monster_name: str) -> None:
    """Update quest progress after defeating a monster."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "quests" not in player:
        return
    
    completed_quests = []
    
    for quest_id in player["quests"]:
        for quest in QUESTS:
            if quest["id"] == quest_id and quest["target"]["monster"] == monster_name:
                # This quest targets the defeated monster
                if "progress" not in player:
                    player["progress"] = {}
                
                if quest_id not in player["progress"]:
                    player["progress"][quest_id] = 0
                
                player["progress"][quest_id] += 1
                
                # Check if quest is completed
                if player["progress"][quest_id] >= quest["target"]["count"]:
                    completed_quests.append(quest)
                    player["quests"].remove(quest_id)
                    
                    # Give rewards
                    player["exp"] += quest["reward"]["exp"]
                    player["col"] += quest["reward"]["col"]
                    
                    # Add items
                    for item, count in quest["reward"]["items"].items():
                        if item not in player["items"]:
                            player["items"][item] = 0
                        player["items"][item] += count
                    
                    # Check for level up
                    level_up_check(player)
                
                save_player(user_id, player)
                break
    
    # Notify about completed quests
    if completed_quests:
        for quest in completed_quests:
            await update.message.reply_text(
                f"Quête terminée: {quest['title']}\n"
                f"Vous avez reçu: {quest['reward']['exp']} EXP, {quest['reward']['col']} Col\n"
                f"Objets: {', '.join([f'{item} x{count}' for item, count in quest['reward']['items'].items()])}"
            )

# Player interaction
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
            player_list += f"- {p['name']} (Niveau {p['level']}) - {p['location']}\n"
    
    await update.message.reply_text(player_list)

async def interact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Interact with another player."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Get all players in same location
    all_players = get_online_players()
    nearby_players = []
    
    for pid, p in all_players.items():
        if pid != user_id and p["location"] == player["location"]:
            nearby_players.append(p)
    
    if not nearby_players:
        await update.message.reply_text(
            f"Il n'y a pas d'autres joueurs à {player['location']}."
        )
        return
    
    # Store nearby players in context
    context.user_data["nearby_players"] = nearby_players
    
    # Create keyboard with player names
    keyboard = [[p["name"]] for p in nearby_players]
    keyboard.append(["Annuler"])
    
    await update.message.reply_text(
        "Avec quel joueur souhaitez-vous interagir?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    
    return CHOOSING_INTERACTION

async def choose_interaction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle player selection for interaction."""
    choice = update.message.text
    
    if choice == "Annuler":
        await update.message.reply_text(
            "Interaction annulée.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    # Find selected player
    selected_player = None
    for p in context.user_data.get("nearby_players", []):
        if p["name"] == choice:
            selected_player = p
            break
    
    if not selected_player:
        await update.message.reply_text(
            "Joueur non trouvé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    # Store selected player
    context.user_data["selected_player"] = selected_player
    
    # Show interaction options
    keyboard = [
        ["Saluer", "Échanger"],
        ["Défier", "Annuler"]
    ]
    
    await update.message.reply_text(
        f"Que souhaitez-vous faire avec {selected_player['name']}?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    
    return CHOOSING_INTERACTION

async def handle_interaction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle interaction with another player."""
    action = update.message.text
    selected_player = context.user_data.get("selected_player")
    
    if not selected_player:
        await update.message.reply_text(
            "Erreur: Joueur non sélectionné.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    if action == "Annuler":
        await update.message.reply_text(
            "Interaction annulée.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    elif action == "Saluer":
        await update.message.reply_text(
            f"Vous saluez {selected_player['name']}.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    elif action == "Échanger":
        # Show player's inventory
        user_id = str(update.effective_user.id)
        player = get_player_data(user_id)
        
        if not player["items"]:
            await update.message.reply_text(
                "Vous n'avez pas d'objets à échanger.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        # Create keyboard with items
        keyboard = [[item] for item in player["items"].keys()]
        keyboard.append(["Annuler"])
        
        await update.message.reply_text(
            "Quel objet souhaitez-vous échanger?",
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        )
        
        return CHOOSING_TRADE_ITEM
    
    elif action == "Défier":
        await update.message.reply_text(
            f"Vous défiez {selected_player['name']} en duel!\n"
            "Cette fonctionnalité sera disponible prochainement.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    else:
        await update.message.reply_text(
            "Action non reconnue.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END

async def choose_trade_item(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle item selection for trade."""
    item = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if item == "Annuler":
        await update.message.reply_text(
            "Échange annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    if item not in player["items"]:
        await update.message.reply_text(
            "Vous ne possédez pas cet objet.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    # Store selected item
    context.user_data["trade_item"] = item
    
    # Ask for amount
    max_amount = player["items"][item]
    
    keyboard = [[str(i)] for i in range(1, min(max_amount + 1, 6))]
    keyboard.append(["Annuler"])
    
    await update.message.reply_text(
        f"Combien de {item} souhaitez-vous échanger? (Vous en avez {max_amount})",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    
    return CHOOSING_TRADE_AMOUNT

async def choose_trade_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle amount selection for trade."""
    try:
        amount = int(update.message.text)
    except ValueError:
        if update.message.text == "Annuler":
            await update.message.reply_text(
                "Échange annulé.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        await update.message.reply_text(
            "Veuillez entrer un nombre valide.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    item = context.user_data["trade_item"]
    
    if amount <= 0 or amount > player["items"].get(item, 0):
        await update.message.reply_text(
            "Quantité invalide.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    # Store trade amount
    context.user_data["trade_amount"] = amount
    
    # Ask for confirmation
    selected_player = context.user_data["selected_player"]
    
    keyboard = [["Confirmer", "Annuler"]]
    
    await update.message.reply_text(
        f"Vous allez échanger {amount} {item} avec {selected_player['name']}.\n"
        "Confirmez-vous cet échange?",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    
    return CONFIRMING_TRADE

async def confirm_trade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Confirm and execute trade."""
    choice = update.message.text
    
    if choice != "Confirmer":
        await update.message.reply_text(
            "Échange annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    # Get trade details
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    selected_player = context.user_data["selected_player"]
    item = context.user_data["trade_item"]
    amount = context.user_data["trade_amount"]
    
    # Execute trade (simplified - just remove from player)
    player["items"][item] -= amount
    if player["items"][item] <= 0:
        del player["items"][item]
    
    save_player(user_id, player)
    
    await update.message.reply_text(
        f"Vous avez échangé {amount} {item} avec {selected_player['name']}!",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

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
    
    # Shop items
    shop_items = {
        "Health Potion": 50,
        "Teleport Crystal": 200,
        "Strength Potion": 100,
        "Basic Armor": 300,
        "Enhanced Sword": 500
    }
    
    shop_text = f"Bienvenue à la boutique! Vous avez {player['col']} Col.\n\n"
    shop_text += "Articles disponibles:\n"
    
    for item, price in shop_items.items():
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
    
    # Shop items
    shop_items = {
        "Health Potion": 50,
        "Teleport Crystal": 200,
        "Strength Potion": 100,
        "Basic Armor": 300,
        "Enhanced Sword": 500
    }
    
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
    
    if item_name not in shop_items:
        await update.message.reply_text(
            f"Article non disponible: {item_name}\n"
            "Utilisez /shop pour voir les articles disponibles."
        )
        return
    
    # Calculate total cost
    price = shop_items[item_name]
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
    
    # Player interaction conversation
    interaction_handler = ConversationHandler(
        entry_points=[CommandHandler("interact", interact_command)],
        states={
            CHOOSING_INTERACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_interaction)],
            CHOOSING_TRADE_ITEM: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_trade_item)],
            CHOOSING_TRADE_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_trade_amount)],
            CONFIRMING_TRADE: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_trade)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(character_creation_handler)
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CommandHandler("location", location_command))
    application.add_handler(battle_handler)
    application.add_handler(CommandHandler("quest", quest_command))
    application.add_handler(CommandHandler("players", players_command))
    application.add_handler(interaction_handler)
    application.add_handler(CommandHandler("shop", shop_command))
    application.add_handler(CommandHandler("buy", buy_command))
    application.add_handler(CommandHandler("heal", heal_command))
    application.add_handler(CommandHandler("inventory", inventory_command))
    
    # Add message handlers
    application.add_handler(MessageHandler(
        filters.Regex('^(' + '|'.join(SAO_LOCATIONS) + ')$'), 
        handle_location
    ))
    application.add_handler(MessageHandler(
        filters.Regex('^(Nouvelle quête|Retour)$'),
        handle_quest_action
    ))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()