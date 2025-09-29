# -*- coding: utf-8 -*-

# Système de voyage et d'exploration
from main import *

# Travel system
async def travel_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the travel process."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Show available floors
    keyboard = [[floor] for floor in player["unlocked_floors"]]
    keyboard.append(["Annuler"])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Vous êtes actuellement à {player['location']['floor']}, {player['location']['biome']}.\n"
        "Vers quel étage souhaitez-vous voyager?",
        reply_markup=reply_markup
    )
    
    return CHOOSING_FLOOR

async def choose_floor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle floor selection."""
    floor = update.message.text
    
    if floor == "Annuler":
        await update.message.reply_text(
            "Voyage annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    if floor not in player["unlocked_floors"]:
        await update.message.reply_text(
            "Vous n'avez pas encore débloqué cet étage."
        )
        return CHOOSING_FLOOR
    
    # Store selected floor
    context.user_data["selected_floor"] = floor
    
    # Show available biomes for this floor
    available_biomes = player["unlocked_biomes"].get(floor, [])
    
    if not available_biomes:
        await update.message.reply_text(
            "Erreur: Aucun biome disponible sur cet étage."
        )
        return ConversationHandler.END
    
    keyboard = [[biome] for biome in available_biomes]
    keyboard.append(["Annuler"])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        f"Vous avez choisi l'étage {floor}.\n"
        "Vers quel biome souhaitez-vous voyager?",
        reply_markup=reply_markup
    )
    
    return CHOOSING_BIOME

async def choose_biome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle biome selection."""
    biome = update.message.text
    
    if biome == "Annuler":
        await update.message.reply_text(
            "Voyage annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    floor = context.user_data["selected_floor"]
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    if biome not in player["unlocked_biomes"].get(floor, []):
        await update.message.reply_text(
            "Vous n'avez pas encore débloqué ce biome."
        )
        return CHOOSING_BIOME
    
    # Update player location
    player["location"] = {"floor": floor, "biome": biome}
    save_player(user_id, player)
    
    # Get biome description
    floor_info = FLOORS_INFO[floor]
    biome_info = None
    for b in floor_info["biomes"]:
        if b["name"] == biome:
            biome_info = b
            break
    
    biome_description = biome_info["description"] if biome_info else "Un lieu mystérieux."
    
    await update.message.reply_text(
        f"Vous avez voyagé vers {floor}, {biome}!\n\n"
        f"{biome_description}\n\n"
        "Que souhaitez-vous faire maintenant? Utilisez /battle pour combattre des monstres, "
        "/quest pour obtenir des quêtes, ou /boss pour défier le boss de l'étage.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

# Floors information command
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
    
    for floor_name, floor_info in FLOORS_INFO.items():
        if floor_name in player["unlocked_floors"]:
            status = "✅ Débloqué"
            if floor_info["boss"]["name"] in player["defeated_bosses"]:
                status += " | Boss vaincu"
            else:
                status += " | Boss non vaincu"
        else:
            status = "🔒 Verrouillé"
            
            # Check unlock requirements
            requirements = floor_info["unlock_requirements"]
            if requirements:
                status += " | Requis: "
                if "boss_defeated" in requirements:
                    status += f"Vaincre {requirements['boss_defeated']}"
                if "level" in requirements:
                    status += f", Niveau {requirements['level']}"
        
        floors_text += f"{floor_name}: {status}\n"
        
        # Show biomes if floor is unlocked
        if floor_name in player["unlocked_floors"]:
            floors_text += "  Biomes:\n"
            for biome in floor_info["biomes"]:
                biome_name = biome["name"]
                if biome_name in player["unlocked_biomes"].get(floor_name, []):
                    biome_status = "✅ Débloqué"
                else:
                    biome_status = "🔒 Verrouillé"
                    
                    # Check biome unlock requirements
                    requirements = biome["unlock_requirements"]
                    if requirements:
                        biome_status += " | Requis: "
                        if "level" in requirements:
                            biome_status += f"Niveau {requirements['level']}"
                        if "quest_completed" in requirements:
                            biome_status += f", Quête {requirements['quest_completed']}"
                
                floors_text += f"    - {biome_name}: {biome_status}\n"
            
            floors_text += "\n"
    
    await update.message.reply_text(floors_text)