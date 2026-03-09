#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mise à jour: Ce module utilise maintenant SQLite au lieu d'un fichier JSON
pour une meilleure sécurité des données et de meilleures performances.
"""

import database

def get_player_data(user_id):
    """
    Récupère les données d'un joueur spécifique.
    (Remplacement transparent de l'ancienne fonction JSON)
    """
    return database.get_player(str(user_id))


def save_player(user_id, player_data):
    """
    Sauvegarde les données d'un joueur spécifique dans la base de données.
    """
    database.save_player(str(user_id), player_data)


def get_online_players():
    """
    Récupère la liste de tous les joueurs.
    Dans une version plus avancée, on pourrait filtrer par "dernière activité".
    """
    return database.get_all_players()


def level_up_check(player):
    """Vérifie si le joueur peut monter de niveau et applique les changements"""
    # Formule simple de montée de niveau : niveau * 100 exp requis
    exp_needed = player["level"] * 100

    if player["exp"] >= exp_needed:
        player["level"] += 1
        player["exp"] -= exp_needed
        player["max_hp"] += 20
        player["hp"] = player["max_hp"]  # Soin complet lors d'une montée de niveau
        player["attack"] += 3
        player["defense"] += 2
        player["agility"] += 2
        return True
    return False

def format_player_stats(player):
    """Formate les statistiques du joueur pour l'affichage (Profil)"""
    stats = (
        f"👤 Nom: {player['name']}\n"
        f"📊 Niveau: {player['level']}\n"
        f"✨ EXP: {player['exp']}/{player['level'] * 100}\n"
        f"❤️ HP: {player['hp']}/{player['max_hp']}\n"
        f"⚔️ Attaque: {player['attack']}\n"
        f"🛡️ Défense: {player['defense']}\n"
        f"🏃 Agilité: {player['agility']}\n"
        f"🗡️ Arme: {player['weapon']}\n"
        f"📍 Localisation: {player['location']}\n"
        f"💰 Col: {player['col']}\n"
        f"🎒 Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()]) if player['items'] else 'Vide'}"
    )
    return stats