# -*- coding: utf-8 -*-

# Commandes d'interaction entre joueurs
from main import *

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
            player_list += f"- {p['name']} (Niveau {p['level']}) - {p['location']['floor']}, {p['location']['biome']}\n"
    
    await update.message.reply_text(player_list)

async def interact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Interact with another player."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Get all players in same location
    all_players = get_online_players()
    nearby_players = []
    
    for pid, p in all_players.items():
        if (pid != user_id and 
            p["location"]["floor"] == player["location"]["floor"] and
            p["location"]["biome"] == player["location"]["biome"]):
            nearby_players.append(p)
    
    if not nearby_players:
        await update.message.reply_text(
            f"Il n'y a pas d'autres joueurs à {player['location']['floor']}, {player['location']['biome']}."
        )
        return ConversationHandler.END
    
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