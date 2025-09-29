# -*- coding: utf-8 -*-

# Système de quêtes
from main import *

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
            quest = ALL_QUESTS.get(quest_id)
            if quest:
                quest_text += f"- {quest['title']}: {quest['description']}\n"
                
                # Show progress if available
                if "progress" in player and quest_id in player["progress"]:
                    progress = player["progress"][quest_id]
                    target = quest["target"]["count"]
                    quest_text += f"  Progression: {progress}/{target} {quest['target']['monster']}\n"
                
                quest_text += "\n"
        
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
        # Get current location
        floor = player["location"]["floor"]
        biome = player["location"]["biome"]
        
        # Get quests for this biome
        floor_quests = FLOOR_QUESTS.get(floor, {})
        available_quests = []
        
        for quest_id, quest in floor_quests.items():
            # Check if quest is for this biome and not already active or completed
            if (quest["biome"] == biome and 
                quest_id not in player.get("quests", []) and 
                quest_id not in player.get("completed_quests", []) and
                player["level"] >= quest["level_requirement"]):
                available_quests.append(quest)
        
        if not available_quests:
            await update.message.reply_text(
                "Il n'y a pas de nouvelles quêtes disponibles dans ce biome pour votre niveau.",
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
        
        # Format rewards
        rewards_text = f"{new_quest['reward']['exp']} EXP, {new_quest['reward']['col']} Col"
        if new_quest['reward']['items']:
            items_text = ", ".join([f"{item} x{count}" for item, count in new_quest['reward']['items'].items()])
            rewards_text += f", {items_text}"
        
        await update.message.reply_text(
            f"Nouvelle quête acceptée: {new_quest['title']}\n"
            f"{new_quest['description']}\n\n"
            f"Cible: {new_quest['target']['count']} {new_quest['target']['monster']}\n"
            f"Récompenses: {rewards_text}",
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
        quest = ALL_QUESTS.get(quest_id)
        if quest and quest["target"]["monster"] == monster_name:
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
                
                # Add to completed quests
                if "completed_quests" not in player:
                    player["completed_quests"] = []
                player["completed_quests"].append(quest_id)
                
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
                
                # Check for biome unlocks based on completed quests
                await check_biome_unlocks(player)
            
            save_player(user_id, player)
    
    # Notify about completed quests
    if completed_quests:
        for quest in completed_quests:
            # Format rewards
            rewards_text = f"{quest['reward']['exp']} EXP, {quest['reward']['col']} Col"
            if quest['reward']['items']:
                items_text = ", ".join([f"{item} x{count}" for item, count in quest['reward']['items'].items()])
                rewards_text += f", {items_text}"
            
            await update.message.reply_text(
                f"Quête terminée: {quest['title']}\n"
                f"Vous avez reçu: {rewards_text}"
            )