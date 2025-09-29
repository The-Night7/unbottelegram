# -*- coding: utf-8 -*-

# Système de combat
from main import *

# Battle system
async def battle_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start a battle with a monster in the current biome."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END
    
    # Check if player can battle (cooldown of 30 seconds)
    current_time = time.time()
    if current_time - player.get("last_battle", 0) < 30:
        remaining = int(30 - (current_time - player.get("last_battle", 0)))
        await update.message.reply_text(
            f"Vous devez attendre encore {remaining} secondes avant de pouvoir combattre à nouveau."
        )
        return ConversationHandler.END
    
    # Get current location
    floor = player["location"]["floor"]
    biome = player["location"]["biome"]
    
    # Get biome monsters
    floor_info = FLOORS_INFO[floor]
    biome_info = None
    for b in floor_info["biomes"]:
        if b["name"] == biome:
            biome_info = b
            break
    
    if not biome_info:
        await update.message.reply_text(
            "Erreur: Biome non trouvé."
        )
        return ConversationHandler.END
    
    # Get a random monster from this biome
    available_monsters = biome_info["monsters"]
    if not available_monsters:
        await update.message.reply_text(
            "Il n'y a pas de monstres dans ce biome."
        )
        return ConversationHandler.END
    
    monster_name = random.choice(available_monsters)
    monster = MONSTERS.get(monster_name)
    
    if not monster:
        await update.message.reply_text(
            "Erreur: Monstre non trouvé."
        )
        return ConversationHandler.END
    
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
        f"{monster['description']}\n\n"
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
            
            # Check for biome unlocks based on level
            await check_biome_unlocks(player)
            
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