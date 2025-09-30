#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script pour mettre à jour la structure de données des joueurs existants.
Transforme la propriété 'location' de chaîne en dictionnaire avec les clés 'floor' et 'biome'.
Ajoute également les clés manquantes nécessaires au bon fonctionnement du bot.
"""

import json
import os
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Chemin du fichier de données des joueurs
DATA_FILE = "../player_data.json"
BACKUP_FILE = "../player_data_backup.json"

# Valeurs par défaut pour les champs manquants
DEFAULT_VALUES = {
    "unlocked_floors": ["Floor 1 - Tolbana"],
    "unlocked_biomes": {"Floor 1 - Tolbana": ["Plains of Beginning"]},
    "defeated_bosses": [],
    "completed_quests": [],
    "quests": [],
    "skills": [],
    "last_battle": 0
}


def backup_data():
    """Crée une sauvegarde du fichier de données des joueurs."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            
            with open(BACKUP_FILE, 'w') as f:
                json.dump(data, f, indent=4)
            
            logger.info(f"Sauvegarde créée: {BACKUP_FILE}")
            return True
        else:
            logger.warning(f"Le fichier {DATA_FILE} n'existe pas. Aucune sauvegarde créée.")
            return False
    except Exception as e:
        logger.error(f"Erreur lors de la création de la sauvegarde: {e}")
        return False


def load_player_data():
    """Charge les données des joueurs depuis le fichier."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Erreur lors du chargement des données: {e}")
        return {}


def save_player_data(data):
    """Sauvegarde les données des joueurs dans le fichier."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info("Données sauvegardées avec succès.")
        return True
    except Exception as e:
        logger.error(f"Erreur lors de la sauvegarde des données: {e}")
        return False


def update_player_locations(data):
    """Met à jour la structure de location pour tous les joueurs."""
    updated_count = 0
    already_updated_count = 0
    
    for user_id, player in data.items():
        player_updated = False
        
        # Vérifier si la location est déjà un dictionnaire
        if isinstance(player.get("location"), dict):
            already_updated_count += 1
        else:
            # Si la location est une chaîne, la convertir en dictionnaire
            if isinstance(player.get("location"), str):
                location_str = player["location"]
                
                # Essayer de séparer l'étage et le biome
                parts = location_str.split(", ")
                
                if len(parts) == 2:
                    # Format attendu: "Floor X - Name, Biome Name"
                    floor_name = parts[0]
                    biome_name = parts[1]
                else:
                    # Si le format n'est pas celui attendu, utiliser une valeur par défaut
                    floor_name = location_str
                    biome_name = "Plains of Beginning"
                    logger.warning(f"Format de location inattendu pour {player['name']}: {location_str}")
                
                # Mettre à jour la structure
                player["location"] = {
                    "floor": floor_name,
                    "biome": biome_name
                }
                
                player_updated = True
                updated_count += 1
        
        # Vérifier et ajouter les champs manquants
        fields_added = []
        for field, default_value in DEFAULT_VALUES.items():
            if field not in player:
                player[field] = default_value
                fields_added.append(field)
                player_updated = True
        
        if fields_added:
            logger.info(f"Champs ajoutés pour {player.get('name', 'joueur inconnu')}: {', '.join(fields_added)}")
    
    return updated_count, already_updated_count


def main():
    """Fonction principale."""
    logger.info("Démarrage de la mise à jour des données des joueurs...")
    
    # Créer une sauvegarde
    if not backup_data():
        logger.error("Échec de la création de la sauvegarde. Arrêt du processus.")
        return
    
    # Charger les données
    data = load_player_data()
    
    if not data:
        logger.error("Aucune donnée de joueur trouvée ou erreur lors du chargement. Arrêt du processus.")
        return
    
    # Mettre à jour les locations et les champs manquants
    updated_count, already_updated_count = update_player_locations(data)
    
    # Sauvegarder les données mises à jour
    if save_player_data(data):
        logger.info(f"Mise à jour terminée. {updated_count} joueurs ont eu leur location mise à jour, {already_updated_count} avaient déjà le bon format.")
    else:
        logger.error("Échec de la sauvegarde des données mises à jour.")


if __name__ == "__main__":
    main()