# -*- coding: utf-8 -*-

import sqlite3
import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

DB_FILE = "sao_players.db"

def get_db_connection():
    """Crée et retourne une connexion à la base de données."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par leur nom
    return conn

def init_db():
    """Initialise la table des joueurs si elle n'existe pas."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Création de la table avec les champs principaux
    # Les champs complexes (items, quests) sont stockés sous forme de texte JSON
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        user_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        weapon TEXT,
        level INTEGER DEFAULT 1,
        exp INTEGER DEFAULT 0,
        hp INTEGER DEFAULT 100,
        max_hp INTEGER DEFAULT 100,
        attack INTEGER DEFAULT 10,
        defense INTEGER DEFAULT 5,
        agility INTEGER DEFAULT 5,
        location TEXT DEFAULT 'Town of Beginnings',
        col INTEGER DEFAULT 500,
        items_json TEXT DEFAULT '{}',
        skills_json TEXT DEFAULT '[]',
        quests_json TEXT DEFAULT '[]',
        last_battle REAL DEFAULT 0,
        created_at REAL
    )
    ''')
    conn.commit()
    conn.close()
    logger.info("Base de données initialisée avec succès.")

def _row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    """Convertit une ligne de la base de données en dictionnaire utilisable par le bot."""
    player_dict = dict(row)
    # Reconversion des champs JSON en objets Python (dict / list)
    player_dict['items'] = json.loads(player_dict.pop('items_json', '{}'))
    player_dict['skills'] = json.loads(player_dict.pop('skills_json', '[]'))
    player_dict['quests'] = json.loads(player_dict.pop('quests_json', '[]'))
    return player_dict

def get_player(user_id: str) -> Optional[Dict[str, Any]]:
    """Récupère les données d'un joueur spécifique."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE user_id = ?", (str(user_id),))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return _row_to_dict(row)
    return None

def save_player(user_id: str, player_data: Dict[str, Any]):
    """Insère ou met à jour les données d'un joueur."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Préparation des données complexes en JSON
    items_json = json.dumps(player_data.get('items', {}))
    skills_json = json.dumps(player_data.get('skills', []))
    quests_json = json.dumps(player_data.get('quests', []))
    
    cursor.execute('''
    INSERT INTO players (
        user_id, name, weapon, level, exp, hp, max_hp, attack, defense, agility, 
        location, col, items_json, skills_json, quests_json, last_battle, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(user_id) DO UPDATE SET
        name=excluded.name,
        weapon=excluded.weapon,
        level=excluded.level,
        exp=excluded.exp,
        hp=excluded.hp,
        max_hp=excluded.max_hp,
        attack=excluded.attack,
        defense=excluded.defense,
        agility=excluded.agility,
        location=excluded.location,
        col=excluded.col,
        items_json=excluded.items_json,
        skills_json=excluded.skills_json,
        quests_json=excluded.quests_json,
        last_battle=excluded.last_battle
    ''', (
        str(user_id),
        player_data.get('name'),
        player_data.get('weapon'),
        player_data.get('level', 1),
        player_data.get('exp', 0),
        player_data.get('hp', 100),
        player_data.get('max_hp', 100),
        player_data.get('attack', 10),
        player_data.get('defense', 5),
        player_data.get('agility', 5),
        player_data.get('location', 'Town of Beginnings'),
        player_data.get('col', 500),
        items_json,
        skills_json,
        quests_json,
        player_data.get('last_battle', 0),
        player_data.get('created_at', 0)
    ))
    
    conn.commit()
    conn.close()

def get_all_players() -> Dict[str, Dict[str, Any]]:
    """Récupère tous les joueurs (pour la commande /players)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    rows = cursor.fetchall()
    conn.close()
    
    return {row['user_id']: _row_to_dict(row) for row in rows}

# Exécuter l'initialisation au chargement du module
init_db()