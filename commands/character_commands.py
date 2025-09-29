# -*- coding: utf-8 -*-

# Système de création de personnage
from main import *

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