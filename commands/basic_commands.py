# -*- coding: utf-8 -*-

# Commandes de base et système de voyage
from main import *

# Bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    user_id = str(user.id)
    
    player = get_player_data(user_id)
    
    if player:
        await update.message.reply_text(
            f"Bienvenue de retour dans Sword Art Online, {player['name']}!\n\n"
            "Utilisez /help pour voir les commandes disponibles."
        )
    else:
        await update.message.reply_text(
            f"Bienvenue dans Sword Art Online, {user.mention_html()}!\n\n"
            "Vous venez d'être piégé dans le jeu mortel Sword Art Online. "
            "Le seul moyen de vous échapper est de terminer les 100 étages.\n\n"
            "Pour commencer, créez votre personnage avec /create_character."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Commandes disponibles:\n"
        "/start - Démarrer le bot\n"
        "/help - Afficher ce message d'aide\n"
        "/create_character - Créer un nouveau personnage\n"
        "/profile - Afficher votre profil\n"
        "/travel - Voyager vers un étage ou un biome\n"
        "/quest - Obtenir ou consulter des quêtes\n"
        "/battle - Combattre un monstre dans votre biome actuel\n"
        "/boss - Défier le boss de l'étage actuel\n"
        "/players - Voir les autres joueurs\n"
        "/interact - Interagir avec un autre joueur\n"
        "/shop - Accéder à la boutique\n"
        "/heal - Se soigner (utiliser une potion)\n"
        "/inventory - Voir votre inventaire\n"
        "/floors - Voir les étages disponibles et leur statut"
    )
    await update.message.reply_text(help_text)

# Profile command
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show player profile."""
    user_id = str(update.effective_user.id)
    player = get_player_data(user_id)
    
    if not player:
        await update.message.reply_text(
            "Vous n'avez pas encore de personnage. Utilisez /create_character pour en créer un."
        )
        return
    
    # Format player stats
    stats = (
        f"Nom: {player['name']}\n"
        f"Niveau: {player['level']}\n"
        f"EXP: {player['exp']}/{player['level'] * 100}\n"
        f"HP: {player['hp']}/{player['max_hp']}\n"
        f"Attaque: {player['attack']}\n"
        f"Défense: {player['defense']}\n"
        f"Agilité: {player['agility']}\n"
        f"Arme: {player['weapon']}\n"
        f"Localisation: {player['location']['floor']}, {player['location']['biome']}\n"
        f"Col: {player['col']}\n"
        f"Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()])}\n\n"
        f"Étages débloqués: {len(player['unlocked_floors'])}\n"
        f"Boss vaincus: {len(player['defeated_bosses'])}\n"
        f"Quêtes terminées: {len(player['completed_quests'])}"
    )
    
    await update.message.reply_text(
        f"Profil de votre personnage:\n\n{stats}"
    )