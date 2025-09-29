# -*- coding: utf-8 -*-

# Commandes utilitaires (inventaire, boutique, soins)
from main import *

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