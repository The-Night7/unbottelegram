# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters

# Import main configuration and helpers
from main import *

# Import command modules
from commands.basic_commands import start, help_command, profile
from commands.character_commands import create_character, choose_name, choose_weapon, confirm_character, cancel
from commands.travel_commands import travel_command, choose_floor, choose_biome, floors_command
from commands.battle_commands import battle_command, handle_battle_action
from commands.boss_commands import boss_command, confirm_boss_battle, handle_boss_action
from commands.quest_commands import quest_command, handle_quest_action
from commands.utility_commands import inventory_command, shop_command, buy_command, heal_command
from commands.player_commands import players_command, interact_command, choose_interaction, handle_interaction, choose_trade_item, choose_trade_amount, confirm_trade

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
    
    # Travel conversation
    travel_handler = ConversationHandler(
        entry_points=[CommandHandler("travel", travel_command), CommandHandler("location", travel_command)],
        states={
            CHOOSING_FLOOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_floor)],
            CHOOSING_BIOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_biome)],
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
    
    # Boss battle conversation
    boss_handler = ConversationHandler(
        entry_points=[CommandHandler("boss", boss_command)],
        states={
            CONFIRMING_BOSS_BATTLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_boss_battle)],
            CHOOSING_BOSS_ACTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_boss_action)],
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
    application.add_handler(travel_handler)
    application.add_handler(battle_handler)
    application.add_handler(boss_handler)
    application.add_handler(CommandHandler("quest", quest_command))
    application.add_handler(CommandHandler("floors", floors_command))
    application.add_handler(CommandHandler("inventory", inventory_command))
    application.add_handler(CommandHandler("shop", shop_command))
    application.add_handler(CommandHandler("buy", buy_command))
    application.add_handler(CommandHandler("heal", heal_command))
    application.add_handler(CommandHandler("players", players_command))
    application.add_handler(interaction_handler)
    
    # Add message handlers
    application.add_handler(MessageHandler(
        filters.Regex('^(Nouvelle quête|Retour)$'),
        handle_quest_action
    ))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()