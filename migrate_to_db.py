#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script utilitaire pour migrer les données existantes de player_data.json
vers la nouvelle base de données SQLite (sao_players.db).
À exécuter une seule fois.
"""

import json
import os
import database

DATA_FILE = "player_data.json"

def migrate():
    print("Démarrage de la migration des données...")
    
    if not os.path.exists(DATA_FILE):
        print(f"Erreur: Le fichier {DATA_FILE} est introuvable.")
        return

    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Erreur lors de la lecture du JSON : {e}")
        return

    count = 0
    for user_id, player_data in data.items():
        try:
            database.save_player(user_id, player_data)
            count += 1
            print(f"Joueur {player_data.get('name', user_id)} migré avec succès.")
        except Exception as e:
            print(f"Erreur lors de la migration du joueur {user_id}: {e}")

    print(f"\nMigration terminée ! {count} joueurs ont été transférés dans la base de données.")
    print("Vous pouvez maintenant renommer ou supprimer votre ancien fichier player_data.json.")

if __name__ == "__main__":
    migrate()