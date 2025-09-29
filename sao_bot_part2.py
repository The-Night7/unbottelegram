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


# Floors command
async def floors_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show information about available floors."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
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


async def floor_info_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle floor info button callback."""
    query = update.callback_query
    await query.answer()
    
    # Extract floor name from callback data
    _, floor_name = query.data.split(":", 1)
    
    # Generate floor info message
    floor_info = generate_floor_info_message(floor_name)
    
    await query.message.reply_text(floor_info)


async def floor_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show detailed information about a specific floor."""
    if not context.args:
        await update.message.reply_text(
            "Veuillez spécifier un étage. Exemple: /floor_info \"Floor 1 - Tolbana\""
        )
        return
    
    floor_name = " ".join(context.args)
    
    # Generate floor info message
    floor_info = generate_floor_info_message(floor_name)
    
    await update.message.reply_text(floor_info)


async def biome_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show detailed information about a specific biome."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return

    if not context.args:
        await update.message.reply_text(
            "Veuillez spécifier un biome. Exemple: /biome_info \"Plains of Beginning\""
        )
        return
    
    biome_name = " ".join(context.args)
    floor_name = player["location"]["floor"]
    
    # Generate biome info message
    biome_info = generate_biome_info_message(floor_name, biome_name)
    
    await update.message.reply_text(biome_info)


# Explore command
async def explore_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Explore the current biome to find monsters."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return

    floor_name = player["location"]["floor"]
    biome_name = player["location"]["biome"]
    
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


# Battle command
async def battle_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start a battle with a monster."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return ConversationHandler.END

    # Get available monsters in the current biome
    floor_name = player["location"]["floor"]
    biome_name = player["location"]["biome"]
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

    shop_text = f"Bienvenue à la boutique! Vous avez {player['col']} Col.\n\n"
    shop_text += "Articles disponibles:\n"

    for item, price in SHOP_ITEMS.items():
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


# Boss command
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
    floor_name = player["location"]["floor"]
    
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


async def confirm_boss_battle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Confirm boss battle."""
    choice = update.message.text
    
    if choice == "Annuler":
        await update.message.reply_text(
            "Vous décidez de ne pas affronter le boss pour le moment.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    if choice != "Défier le boss":
        await update.message.reply_text(
            "Action non reconnue. Le combat contre le boss est annulé.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "boss_battle" not in context.user_data:
        await update.message.reply_text("Erreur: Combat de boss non initialisé.")
        return ConversationHandler.END
    
    boss_battle = context.user_data["boss_battle"]
    boss_name = boss_battle["boss_name"]
    boss = boss_battle["boss"]
    
    # Start the boss battle
    await update.message.reply_text(
        f"Le combat contre {boss_name} commence!\n\n"
        f"HP du boss: {boss['hp']}\n"
        f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
        "Que voulez-vous faire?",
        reply_markup=ReplyKeyboardMarkup([
            ["Attaquer", "Utiliser Potion"],
            ["Utiliser Skill", "Fuir"]
        ], one_time_keyboard=True)
    )
    
    return CHOOSING_BOSS_ACTION


async def handle_boss_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle player's action during boss battle."""
    action = update.message.text
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player or "boss_battle" not in context.user_data:
        await update.message.reply_text("Erreur: Combat de boss non initialisé.")
        return ConversationHandler.END
    
    boss_battle = context.user_data["boss_battle"]
    boss_name = boss_battle["boss_name"]
    boss = boss_battle["boss"]
    
    if action == "Fuir":
        # Only 20% chance to escape from a boss
        if random.random() < 0.2:
            await update.message.reply_text(
                f"Par miracle, vous avez réussi à fuir le combat contre {boss_name}!",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                f"Vous ne pouvez pas fuir un combat de boss! {boss_name} vous attaque!"
            )
            # Boss attacks
            damage = max(1, boss["attack"] - player["defense"] // 2)
            player["hp"] -= damage
            save_player(user_id, player)
            
            if player["hp"] <= 0:
                player["hp"] = 1  # Prevent death, just leave at 1 HP
                save_player(user_id, player)
                
                await update.message.reply_text(
                    f"{boss_name} vous a vaincu! Vous êtes gravement blessé.\n"
                    "Vous avez été téléporté en ville avec 1 HP.",
                    reply_markup=ReplyKeyboardRemove()
                )
                return ConversationHandler.END
            
            await update.message.reply_text(
                f"{boss_name} vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n"
                f"HP du boss: {boss['hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Skill", "Fuir"]
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
                f"{boss_name} vous attaque et vous inflige {damage} points de dégâts!\n"
                f"Vos HP: {player['hp']}/{player['max_hp']}\n"
                f"HP du boss: {boss['hp']}\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Skill", "Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BOSS_ACTION
        else:
            await update.message.reply_text(
                "Vous n'avez pas de potions de soin!\n\n"
                "Que voulez-vous faire?",
                reply_markup=ReplyKeyboardMarkup([
                    ["Attaquer", "Utiliser Potion"],
                    ["Utiliser Skill", "Fuir"]
                ], one_time_keyboard=True)
            )
            return CHOOSING_BOSS_ACTION
    
    elif action == "Utiliser Skill":
        # Simplified skill system
        if player["level"] >= 10:
            # Special attack with 1.5x damage
            player_damage = int(max(1, player["attack"] * 1.5 - boss["defense"] // 2))
            boss["hp"] -= player_damage
            
            await update.message.reply_text(
                f"Vous utilisez une compétence spéciale et infligez {player_damage} points de dégâts à {boss_name}!\n"
                f"HP du boss: {boss['hp']}"
            )
        else:
            await update.message.reply_text(
                "Vous n'avez pas encore débloqué de compétences spéciales. Vous devez être au moins niveau 10."
            )
            return CHOOSING_BOSS_ACTION
        
        # Check if boss is defeated
        if boss["hp"] <= 0:
            # Calculate rewards
            exp_gain = boss["exp"]
            col_gain = boss["col"]
            
            # Add exp and col
            player["exp"] += exp_gain
            player["col"] += col_gain
            
            # Add boss to defeated bosses
            if "defeated_bosses" not in player:
                player["defeated_bosses"] = []
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
            
            # Save player data
            save_player(user_id, player)
            
            # Prepare victory message
            victory_text = f"Vous avez vaincu {boss_name}!\n"
            victory_text += f"Vous gagnez {exp_gain} EXP et {col_gain} Col.\n"
            
            if drops:
                victory_text += f"Objets obtenus: {', '.join(drops)}\n"
            
            if leveled_up:
                victory_text += f"\nFélicitations! Vous avez atteint le niveau {player['level']}!"
            
            # Check if new floor is unlocked
            floor_name = player["location"]["floor"]
            for next_floor_name, next_floor_data in FLOORS_INFO.items():
                requirements = next_floor_data.get("unlock_requirements", {})
                if requirements.get("boss_defeated") == boss_name:
                    if next_floor_name not in player["unlocked_floors"]:
                        player["unlocked_floors"].append(next_floor_name)
                        victory_text += f"\n\nVous avez débloqué l'accès à {next_floor_name}!"
                        save_player(user_id, player)
            
            await update.message.reply_text(
                victory_text,
                reply_markup=ReplyKeyboardRemove()
            )
            
            return ConversationHandler.END
        
        # Boss attacks
        damage = max(1, boss["attack"] - player["defense"] // 2)
        player["hp"] -= damage
        save_player(user_id, player)
        
        if player["hp"] <= 0:
            player["hp"] = 1  # Prevent death, just leave at 1 HP
            save_player(user_id, player)
            
            await update.message.reply_text(
                f"{boss_name} vous a vaincu! Vous êtes gravement blessé.\n"
                "Vous avez été téléporté en ville avec 1 HP.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        await update.message.reply_text(
            f"{boss_name} vous attaque et vous inflige {damage} points de dégâts!\n"
            f"Vos HP: {player['hp']}/{player['max_hp']}\n"
            f"HP du boss: {boss['hp']}\n\n"
            "Que voulez-vous faire?",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Skill", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION
    
    elif action == "Attaquer":
        # Player attacks
        player_damage = max(1, player["attack"] - boss["defense"] // 2)
        boss["hp"] -= player_damage
        
        battle_text = f"Vous attaquez {boss_name} et infligez {player_damage} points de dégâts!\n"
        battle_text += f"HP du boss: {boss['hp']}\n\n"
        
        # Check if boss is defeated
        if boss["hp"] <= 0:
            # Calculate rewards
            exp_gain = boss["exp"]
            col_gain = boss["col"]
            
            # Add exp and col
            player["exp"] += exp_gain
            player["col"] += col_gain
            
            # Add boss to defeated bosses
            if "defeated_bosses" not in player:
                player["defeated_bosses"] = []
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
            
            # Save player data
            save_player(user_id, player)
            
            # Prepare victory message
            victory_text = f"Vous avez vaincu {boss_name}!\n"
            victory_text += f"Vous gagnez {exp_gain} EXP et {col_gain} Col.\n"
            
            if drops:
                victory_text += f"Objets obtenus: {', '.join(drops)}\n"
            
            if leveled_up:
                victory_text += f"\nFélicitations! Vous avez atteint le niveau {player['level']}!"
            
            # Check if new floor is unlocked
            floor_name = player["location"]["floor"]
            for next_floor_name, next_floor_data in FLOORS_INFO.items():
                requirements = next_floor_data.get("unlock_requirements", {})
                if requirements.get("boss_defeated") == boss_name:
                    if next_floor_name not in player["unlocked_floors"]:
                        player["unlocked_floors"].append(next_floor_name)
                        victory_text += f"\n\nVous avez débloqué l'accès à {next_floor_name}!"
                        save_player(user_id, player)
            
            await update.message.reply_text(
                battle_text + victory_text,
                reply_markup=ReplyKeyboardRemove()
            )
            
            return ConversationHandler.END
        
        # Boss attacks
        boss_damage = max(1, boss["attack"] - player["defense"] // 2)
        player["hp"] -= boss_damage
        save_player(user_id, player)
        
        battle_text += f"{boss_name} vous attaque et vous inflige {boss_damage} points de dégâts!\n"
        battle_text += f"Vos HP: {player['hp']}/{player['max_hp']}\n\n"
        
        # Check if player is defeated
        if player["hp"] <= 0:
            player["hp"] = 1  # Prevent death, just leave at 1 HP
            save_player(user_id, player)
            
            await update.message.reply_text(
                battle_text + f"{boss_name} vous a vaincu! Vous êtes gravement blessé.\n"
                              "Vous avez été téléporté en ville avec 1 HP.",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        # Continue battle
        await update.message.reply_text(
            battle_text + "Que voulez-vous faire?",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Skill", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION
    
    else:
        await update.message.reply_text(
            "Action non reconnue. Veuillez choisir parmi les options proposées.",
            reply_markup=ReplyKeyboardMarkup([
                ["Attaquer", "Utiliser Potion"],
                ["Utiliser Skill", "Fuir"]
            ], one_time_keyboard=True)
        )
        return CHOOSING_BOSS_ACTION


# Players command
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


# Interact command
async def interact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Interact with another player."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)

    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return

    await update.message.reply_text(
        "Cette fonctionnalité sera disponible prochainement."
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