#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bot Telegram pour Sword Art Online
Ce bot permet aux joueurs de vivre l'aventure de SAO en explorant les étages d'Aincrad,
en combattant des monstres et des boss, et en progressant dans le jeu.
"""

import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, filters

# Import des modules d'intégration des étages
from palier import FLOORS_INFO
from floor_integration import init_monster_data

# Import des parties du bot
from sao_bot_part1 import (
    start, help_command, create_character, choose_name, choose_weapon, confirm_character,
    cancel, profile_command, location_command, choose_floor, choose_biome,
    CHOOSING_NAME, CHOOSING_WEAPON, CONFIRMING_CHARACTER, CHOOSING_FLOOR, CHOOSING_BIOME
)

from sao_bot_part2 import (
    floors_command, floor_info_callback, floor_info_command, biome_info_command,
    explore_command, battle_command, handle_battle_action,
    boss_command, confirm_boss_battle, handle_boss_action, players_command, interact_command,
    CHOOSING_BATTLE_ACTION, CONFIRMING_BOSS_BATTLE, CHOOSING_BOSS_ACTION
)

# Import des commandes utilitaires
from commands.utility_commands import (
    inventory_command, shop_command, buy_command, heal_command
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Initialize monster data
    init_monster_data()

    # Load environment variables
    load_dotenv()

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

    # Location/travel conversation
    location_handler = ConversationHandler(
        entry_points=[CommandHandler("location", location_command), CommandHandler("travel", location_command)],
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

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(character_creation_handler)
    application.add_handler(CommandHandler("profile", profile_command))
    application.add_handler(location_handler)
    application.add_handler(CommandHandler("inventory", inventory_command))
    application.add_handler(CommandHandler("floors", floors_command))
    application.add_handler(CommandHandler("floor_info", floor_info_command))
    application.add_handler(CommandHandler("biome_info", biome_info_command))
    application.add_handler(CommandHandler("explore", explore_command))
    application.add_handler(battle_handler)
    application.add_handler(CommandHandler("shop", shop_command))
    application.add_handler(CommandHandler("buy", buy_command))
    application.add_handler(boss_handler)
    application.add_handler(CommandHandler("players", players_command))
    application.add_handler(CommandHandler("interact", interact_command))
    application.add_handler(CommandHandler("heal", heal_command))

    # Add callback query handlers
    application.add_handler(CallbackQueryHandler(floor_info_callback, pattern=r"^floor_info:"))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()