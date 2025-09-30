#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Correctifs pour les fonctions de sao_bot_part2.py
pour résoudre les problèmes de détection des personnages des joueurs.
"""

import random
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

# Import des données du jeu et des fonctions utilitaires
from palier import FLOORS_INFO
from palier.palier import SHOP_ITEMS
from utils.player import get_player_data, save_player, level_up_check
from utils.monster import get_monster_info, get_available_monsters, get_boss_info
from utils.floor import get_accessible_floors, generate_floor_info_message, generate_biome_info_message, get_accessible_biomes, can_access_biome
from utils.player import get_online_players

from sao_bot_part1 import CHOOSING_BOSS_ACTION, CONFIRMING_BOSS_BATTLE, CHOOSING_BATTLE_ACTION

# Fonction utilitaire pour vérifier si un joueur existe
def check_player_exists(update, user_id, player):
    """Vérifie si le joueur existe et envoie un message si ce n'est pas le cas."""
    if not player:
        update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return False
    return True


# Inventory command (version corrigée)
async def inventory_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show player inventory."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    if not player.get("items", {}):
        await update.message.reply_text("Votre inventaire est vide.")
        return

    inventory_text = "Votre inventaire:\n\n"
    for item, count in player.get("items", {}).items():
        inventory_text += f"- {item}: {count}\n"

    inventory_text += f"\nCol: {player.get('col', 0)}"

    await update.message.reply_text(inventory_text)


# Floors command (version corrigée)
async def floors_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show information about available floors."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    # Get accessible floors for the player
    accessible_floors = get_accessible_floors(player)
    
    floors_text = "Étages d'Aincrad:\n\n"
    
    for floor_name, floor_data in FLOORS_INFO.items():
        if floor_name in accessible_floors:
            status = "✅ Débloqué"
        else:
            requirements = floor_data.get("unlock_requirements", {})
            if requirements:
                if "boss_defeated" in requirements:
                    status = f"🔒 Verrouillé | Requis: Vaincre {requirements['boss_defeated']}"
                elif "level" in requirements:
                    status = f"🔒 Verrouillé | Requis: Niveau {requirements['level']}"
                else:
                    status = "🔒 Verrouillé"
            else:
                status = "🔒 Verrouillé"
        
        floors_text += f"- {floor_name}: {status}\n"
    
    # Add inline keyboard for floor details
    keyboard = []
    for floor_name in FLOORS_INFO.keys():
        if floor_name in accessible_floors:
            keyboard.append([InlineKeyboardButton(f"Détails: {floor_name}", callback_data=f"floor_info:{floor_name}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    
    await update.message.reply_text(floors_text, reply_markup=reply_markup)


# Biome info command (version corrigée)
async def biome_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show detailed information about a specific biome."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    if not context.args:
        await update.message.reply_text(
            "Veuillez spécifier un biome. Exemple: /biome_info \"Plains of Beginning\""
        )
        return
    
    biome_name = " ".join(context.args)
    
    # S'assurer que player["location"] est un dictionnaire
    if isinstance(player.get("location"), dict):
        floor_name = player["location"].get("floor", "Floor 1 - Tolbana")
    else:
        floor_name = "Floor 1 - Tolbana"  # Valeur par défaut
    
    # Generate biome info message
    biome_info = generate_biome_info_message(floor_name, biome_name)
    
    await update.message.reply_text(biome_info)


# Explore command (version corrigée)
async def explore_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Explore the current biome to find monsters."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    # S'assurer que player["location"] est un dictionnaire
    if not isinstance(player.get("location"), dict):
        # Migration à la volée si location n'est pas un dictionnaire
        location_str = player.get("location", "Floor 1 - Tolbana, Plains of Beginning")
        parts = location_str.split(", ")
        if len(parts) == 2:
            floor_name = parts[0]
            biome_name = parts[1]
        else:
            floor_name = "Floor 1 - Tolbana"
            biome_name = "Plains of Beginning"
        
        player["location"] = {
            "floor": floor_name,
            "biome": biome_name
        }
        save_player(user_id, player)
    
    floor_name = player["location"].get("floor", "Floor 1 - Tolbana")
    biome_name = player["location"].get("biome", "Plains of Beginning")
    
    # Get available monsters in this biome
    available_monsters = get_available_monsters(floor_name, biome_name)
    
    if not available_monsters:
        await update.message.reply_text(
            f"Vous explorez {biome_name}, mais vous ne trouvez aucun monstre."
        )
        return
    
    # Randomly select a monster
    monster_name = random.choice(available_monsters)
    monster_info = get_monster_info(monster_name)
    
    if not monster_info:
        await update.message.reply_text(
            f"Vous trouvez un {monster_name}, mais vous ne parvenez pas à l'identifier."
        )
        return
    
    # Store monster in context for battle
    context.user_data["battle"] = {
        "monster_name": monster_name,
        "monster": monster_info.copy(),
        "round": 1
    }
    
    # Create keyboard for battle actions
    keyboard = [
        ["Attaquer", "Utiliser Potion"],
        ["Fuir"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"En explorant {biome_name}, vous rencontrez un {monster_name} (Niveau {monster_info['level']})!\n\n"
        f"HP du monstre: {monster_info['hp']}\n"
        f"Attaque: {monster_info['attack']}\n"
        f"Défense: {monster_info['defense']}\n\n"
        "Que voulez-vous faire?",
        reply_markup=reply_markup
    )


# Battle command (version corrigée)
async def battle_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start a battle with a monster."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return ConversationHandler.END

    # S'assurer que player["location"] est un dictionnaire
    if not isinstance(player.get("location"), dict):
        # Migration à la volée si location n'est pas un dictionnaire
        location_str = player.get("location", "Floor 1 - Tolbana, Plains of Beginning")
        parts = location_str.split(", ")
        if len(parts) == 2:
            floor_name = parts[0]
            biome_name = parts[1]
        else:
            floor_name = "Floor 1 - Tolbana"
            biome_name = "Plains of Beginning"
        
        player["location"] = {
            "floor": floor_name,
            "biome": biome_name
        }
        save_player(user_id, player)
    
    floor_name = player["location"].get("floor", "Floor 1 - Tolbana")
    biome_name = player["location"].get("biome", "Plains of Beginning")
    
    # Get available monsters in the current biome
    available_monsters = get_available_monsters(floor_name, biome_name)
    
    if not available_monsters:
        await update.message.reply_text(
            f"Il n'y a pas de monstres dans {biome_name}. Essayez d'explorer un autre biome."
        )
        return ConversationHandler.END
    
    # Randomly select a monster
    monster_name = random.choice(available_monsters)
    monster_info = get_monster_info(monster_name)
    
    if not monster_info:
        await update.message.reply_text(
            "Erreur: Informations sur le monstre non disponibles."
        )
        return ConversationHandler.END
    
    # Store monster in context for the battle
    context.user_data["battle"] = {
        "monster_name": monster_name,
        "monster": monster_info.copy(),
        "round": 1
    }

    await update.message.reply_text(
        "Vous partez à la recherche de monstres à combattre...\n\n"
        f"Vous avez rencontré un {monster_name} (Niveau {monster_info['level']})!\n"
        f"HP du monstre: {monster_info['hp']}\n"
        f"Attaque: {monster_info['attack']}\n"
        f"Défense: {monster_info['defense']}\n\n"
        "Que voulez-vous faire?",
        reply_markup=ReplyKeyboardMarkup([
            ["Attaquer", "Utiliser Potion"],
            ["Fuir"]
        ], one_time_keyboard=True)
    )

    return CHOOSING_BATTLE_ACTION


# Shop command (version corrigée)
async def shop_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Access the shop."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    shop_text = f"Bienvenue à la boutique! Vous avez {player.get('col', 0)} Col.\n\n"
    shop_text += "Articles disponibles:\n"

    for item, price in SHOP_ITEMS.items():
        shop_text += f"- {item}: {price} Col\n"

    shop_text += "\nPour acheter un article, utilisez /buy <article> <quantité>"

    await update.message.reply_text(shop_text)


# Buy command (version corrigée)
async def buy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Buy items from the shop."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
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

    if player.get('col', 0) < total_cost:
        await update.message.reply_text(
            f"Vous n'avez pas assez de Col. Il vous faut {total_cost} Col."
        )
        return

    # Process purchase
    player['col'] -= total_cost

    if "items" not in player:
        player["items"] = {}
    
    if item_name not in player["items"]:
        player["items"][item_name] = 0
    player["items"][item_name] += quantity

    save_player(user_id, player)

    await update.message.reply_text(
        f"Vous avez acheté {quantity} {item_name} pour {total_cost} Col.\n"
        f"Col restant: {player['col']}"
    )


# Boss command (version corrigée)
async def boss_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Challenge the boss of the current floor."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return ConversationHandler.END

    # S'assurer que player["location"] est un dictionnaire
    if not isinstance(player.get("location"), dict):
        # Migration à la volée si location n'est pas un dictionnaire
        location_str = player.get("location", "Floor 1 - Tolbana, Plains of Beginning")
        parts = location_str.split(", ")
        if len(parts) == 2:
            floor_name = parts[0]
            biome_name = parts[1]
        else:
            floor_name = "Floor 1 - Tolbana"
            biome_name = "Plains of Beginning"
        
        player["location"] = {
            "floor": floor_name,
            "biome": biome_name
        }
        save_player(user_id, player)
    
    # Get current floor
    floor_name = player["location"].get("floor", "Floor 1 - Tolbana")
    
    # Get boss info
    boss_info = get_boss_info(floor_name)
    
    if not boss_info:
        await update.message.reply_text(
            f"Aucun boss trouvé pour l'étage {floor_name}."
        )
        return ConversationHandler.END
    
    boss_name = boss_info["name"]
    
    # Check if player has already defeated this boss
    if boss_name in player.get("defeated_bosses", []):
        await update.message.reply_text(
            f"Vous avez déjà vaincu {boss_name}!"
        )
        return ConversationHandler.END
    
    # Check if player meets the level requirement
    if player["level"] < boss_info["required_level"]:
        await update.message.reply_text(
            f"Vous n'êtes pas assez fort pour affronter {boss_name}.\n"
            f"Niveau requis: {boss_info['required_level']} (Vous êtes niveau {player['level']})."
        )
        return ConversationHandler.END
    
    # Store boss in context for the battle
    context.user_data["boss_battle"] = {
        "boss_name": boss_name,
        "boss": boss_info.copy(),
        "round": 1
    }

    # Show boss information
    boss_text = (
        f"Vous êtes sur le point d'affronter {boss_name}, le boss de {floor_name}!\n\n"
        f"Niveau du boss: {boss_info['level']}\n"
        f"HP: {boss_info['hp']}\n"
        f"Attaque: {boss_info['attack']}\n"
        f"Défense: {boss_info['defense']}\n\n"
        f"{boss_info['description']}\n\n"
        f"Niveau minimum requis: {boss_info['required_level']}\n"
        f"Taille minimale du groupe: {boss_info['min_party_size']}\n\n"
        "Êtes-vous sûr de vouloir défier ce boss? Cette bataille sera difficile!"
    )

    keyboard = [["Défier le boss", "Annuler"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        boss_text,
        reply_markup=reply_markup
    )

    return CONFIRMING_BOSS_BATTLE


# Players command (version corrigée)
async def players_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show other players."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
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
            # Format location based on structure
            if isinstance(p.get('location'), dict):
                location_str = f"{p['location'].get('floor', 'Inconnu')}, {p['location'].get('biome', 'Inconnu')}"
            else:
                location_str = p.get('location', 'Inconnu')
                
            player_list += f"- {p.get('name', 'Inconnu')} (Niveau {p.get('level', 1)}) - {location_str}\n"

    await update.message.reply_text(player_list)


# Interact command (version corrigée)
async def interact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Interact with another player."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    await update.message.reply_text(
        "Cette fonctionnalité sera disponible prochainement."
    )


# Heal command (version corrigée)
async def heal_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Use a health potion to heal."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not check_player_exists(update, user_id, player):
        return

    if player.get("hp", 0) >= player.get("max_hp", 100):
        await update.message.reply_text("Vous avez déjà tous vos points de vie.")
        return

    if not player.get("items", {}).get("Health Potion", 0) > 0:
        await update.message.reply_text(
            "Vous n'avez pas de potions de soin. Achetez-en à la boutique avec /shop."
        )
        return

    # Use potion
    heal_amount = 50
    player["hp"] = min(player.get("max_hp", 100), player.get("hp", 0) + heal_amount)
    
    if "items" not in player:
        player["items"] = {}
    
    player["items"]["Health Potion"] -= 1

    if player["items"]["Health Potion"] <= 0:
        del player["items"]["Health Potion"]

    save_player(user_id, player)

    await update.message.reply_text(
        f"Vous utilisez une potion de soin et récupérez {heal_amount} HP!\n"
        f"Vos HP: {player['hp']}/{player['max_hp']}\n"
        f"Potions restantes: {player['items'].get('Health Potion', 0)}"
    )