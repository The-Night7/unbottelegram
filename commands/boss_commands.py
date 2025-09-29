# -*- coding: utf-8 -*-

# Système de combat contre les boss
from main import *

# Boss battle system
async def boss_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Challenge the boss of the current floor."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Get current floor
    floor = player["location"]["floor"]
    floor_info = FLOORS_INFO[floor]
    boss = floor_info["boss"]
    
    # Check if boss is already defeated
    if boss["name"] in player["defeated_bosses"]:
        await update.message.reply_text(
            f"Vous avez déjà vaincu {boss['name']}!"
        )
        return ConversationHandler.END
    
    # Check requirements
    if player["level"] < boss["required_level"]:
        await update.message.reply_text(
            f"Vous n'êtes pas assez fort pour affronter {boss['name']}!\n"
            f"Niveau requis: {boss['required_level']} (Votre niveau: {player['level']})"
        )
        return ConversationHandler.END
    
    # Check if player is at full health
    if player["hp"] < player["max_hp"]:
        await update.message.reply_text(
            "Vous devez être en pleine forme pour affronter un boss!\n"
            "Utilisez /heal pour récupérer vos points de vie."
        )
        return ConversationHandler.END
    
    # Show boss information and ask for confirmation
    boss_text = (
        f"Vous êtes sur le point d'affronter {boss['name']}, le boss de l'étage {floor}!\n\n"
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
    
    # Store boss in context
    context.user_data["boss"] = boss.copy()
    context.user_data["boss_name"] = boss["name"]
    
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
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "boss" not in context.user_data:
        await update.message.reply_text("Erreur: Boss non initialisé.")
        return ConversationHandler.END
    
    boss = context.user_data["boss"]
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
    
    if action == "Fuir":
        # Only 20% chance to escape from boss
        if random.random() < 0.2:
            await update.message.reply_text(
                f"Par miracle, vous avez réussi à fuir le combat contre {boss_name}!",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                f"Vous ne pouvez pas fuir! Le {boss_name} vous bloque le passage!"
            )
            # Boss attacks
            damage = max(1, boss["attack"] - player["defense"] // 2)
            player["hp"] -= damage
            save_player(user_id, player)
            
            if player["hp"] <= 0:
                player["hp"] = 1  # Prevent death, just leave at 1 HP
                save_player(user_id, player)
                
                await update.message.reply_text(
                    f"Le {boss_name} vous a vaincu! Vous êtes gravement blessé.\n"
                    "Vous avez été téléporté en ville avec 1 HP.",
                    reply_markup=ReplyKeyboardRemove()
                )
                return ConversationHandler.END
            
            await update.message.reply_text(
                f"Le {boss_name} vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Compétence", "Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BOSS_ACTION
    
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
            
            # Boss still attacks
            damage = max(1, boss["attack"] - player["defense"] // 2)
            player["hp"] -= damage
            save_player(user_id, player)
            
            await update.message.reply_text(
                f"Le {boss_name} vous attaque et vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Compétence", "Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BOSS_ACTION
        else:
            await update.message.reply_text(
                "Vous n'avez pas de potions de soin!\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Compétence", "Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BOSS_ACTION
    
    elif action == "Utiliser Compétence":
        # Simplified skill system
        await update.message.reply_text(
            "Vous n'avez pas encore appris de compétences spéciales.\n\n"
            "Que voulez-vous faire?",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Compétence", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION
    
    elif action == "Attaquer":
        # Player attacks
        player_damage = max(1, player["attack"] - boss["defense"] // 2)
        boss["hp"] -= player_damage
        
        battle_text = f"Vous attaquez le {boss_name} et infligez {player_damage} points de dégâts!\n"
        battle_text += f"HP du {boss_name}: {boss['hp']}\n\n"
        
        # Check if boss is defeated
        if boss["hp"] <= 0:
            # Calculate rewards
            exp_gain = boss["exp"]
            col_gain = boss["col"]
            
            # Add exp and col
            player["exp"] += exp_gain
            player["col"] += col_gain
            
            # Add boss to defeated bosses
            player["defeated_bosses"].append(boss_name)
            
            # Check for drops
            drops = []
            for item, chance in boss["drops"].items():
                if random.random() < chance:
                    if item not in player["items"]:
                        player["items"][item] = 0
                    player["items"][item] += 1
                    drops.append(item)
            
            # Check for level up
            leveled_up = level_up_check(player)
            
            # Unlock next floor if available
            await unlock_next_floor(player, boss_name)
            
            # Save player data
            save_player(user_id, player)
            
            # Prepare victory message
            victory_text = f"Vous avez vaincu {boss_name}, le boss de l'étage!\n"
            victory_text += f"Vous gagnez {exp_gain} EXP et {col_gain} Col.\n"
            
            if drops:
                victory_text += f"Objets obtenus: {', '.join(drops)}\n"
            
            if leveled_up:
                victory_text += f"\nFélicitations! Vous avez atteint le niveau {player['level']}!"
            
            # Check if new floor was unlocked
            current_floor = player["location"]["floor"]
            next_floor_index = list(FLOORS_INFO.keys()).index(current_floor) + 1
            
            if next_floor_index < len(FLOORS_INFO):
                next_floor = list(FLOORS_INFO.keys())[next_floor_index]
                if next_floor in player["unlocked_floors"]:
                    victory_text += f"\n\nVous avez débloqué l'étage {next_floor}!"
            
            await update.message.reply_text(
                battle_text + victory_text,
                reply_markup=ReplyKeyboardRemove()
            )
            
            return ConversationHandler.END
        
        # Boss attacks
        boss_damage = max(1, boss["attack"] - player["defense"] // 2)
        player["hp"] -= boss_damage
        save_player(user_id, player)
        
        battle_text += f"Le {boss_name} vous attaque et vous inflige {boss_damage} points de dégâts!\n"
        battle_text += f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
        
        # Check if player is defeated
        if player["hp"] <= 0:
            player["hp"] = 1  # Prevent death, just leave at 1 HP
            save_player(user_id, player)
            
            await update.message.reply_text(
                battle_text + f"Le {boss_name} vous a vaincu! Vous êtes gravement blessé.\n"
                "Vous avez été téléporté en ville avec 1 HP.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        # Continue battle
        await update.message.reply_text(
            battle_text + "Que voulez-vous faire?",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Compétence", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION
    
    else:
        await update.message.reply_text(
            "Action non reconnue. Veuillez choisir parmi les options proposées.",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Compétence", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION