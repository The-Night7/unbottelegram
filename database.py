# -*- coding: utf-8 -*-

import os
import json
import logging
import psycopg2
from psycopg2.extras import DictCursor
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Scalingo injecte automatiquement l'URL de la base de données via cette variable
DATABASE_URL = os.environ.get("SCALINGO_POSTGRESQL_URL") or os.environ.get("DATABASE_URL")

def get_db_connection():
    """Crée et retourne une connexion à la base de données PostgreSQL de Scalingo."""
    if not DATABASE_URL:
        logger.error("Aucune URL de base de données trouvée ! Vérifiez vos addons Scalingo.")
        return None
    # sslmode='require' est souvent nécessaire sur les serveurs distants
    return psycopg2.connect(DATABASE_URL, sslmode='prefer')

def init_db():
    """Initialise la table des joueurs pour Postgres."""
    conn = get_db_connection()
    if not conn:
        return
        
    cursor = conn.cursor()
    
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
        completed_quests_json TEXT DEFAULT '[]',
        defeated_bosses_json TEXT DEFAULT '[]',
        unlocked_floors_json TEXT DEFAULT '[]',
        unlocked_biomes_json TEXT DEFAULT '{}',
        last_battle DOUBLE PRECISION DEFAULT 0,
        created_at DOUBLE PRECISION
    )
    ''')
    
    # Tentative d'ajout des colonnes si la table existait déjà avec un vieux format
    colonnes_a_ajouter = [
        ("completed_quests_json", "TEXT DEFAULT '[]'"),
        ("defeated_bosses_json", "TEXT DEFAULT '[]'"),
        ("unlocked_floors_json", "TEXT DEFAULT '[]'"),
        ("unlocked_biomes_json", "TEXT DEFAULT '{}'")
    ]
    for col, col_type in colonnes_a_ajouter:
        try:
            # Postgres: on utilise le savepoint pour éviter que l'erreur bloque la transaction
            cursor.execute("SAVEPOINT sp1")
            cursor.execute(f"ALTER TABLE players ADD COLUMN {col} {col_type}")
            cursor.execute("RELEASE SAVEPOINT sp1")
        except psycopg2.errors.DuplicateColumn:
            cursor.execute("ROLLBACK TO SAVEPOINT sp1")
            
    conn.commit()
    cursor.close()
    conn.close()
    logger.info("Base de données PostgreSQL initialisée avec succès sur Scalingo.")

def _row_to_dict(row) -> Dict[str, Any]:
    """Convertit une ligne Postgres en dictionnaire utilisable par le bot."""
    if not row:
        return None
        
    player_dict = dict(row)
    
    json_fields = {
        'items': '{}', 'skills': '[]', 'quests': '[]',
        'completed_quests': '[]', 'defeated_bosses': '[]',
        'unlocked_floors': '[]', 'unlocked_biomes': '{}'
    }
    
    for key, default in json_fields.items():
        json_val = player_dict.pop(f"{key}_json", default)
        try:
            player_dict[key] = json.loads(json_val if json_val else default)
        except:
            player_dict[key] = json.loads(default)
            
    try:
        if isinstance(player_dict['location'], str) and player_dict['location'].startswith('{'):
            player_dict['location'] = json.loads(player_dict['location'])
    except:
        pass

    return player_dict

def get_player(user_id: str) -> Optional[Dict[str, Any]]:
    """Récupère les données d'un joueur."""
    conn = get_db_connection()
    if not conn: return None
    
    cursor = conn.cursor(cursor_factory=DictCursor)
    # Postgres utilise %s au lieu de ? pour les variables
    cursor.execute("SELECT * FROM players WHERE user_id = %s", (str(user_id),))
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if row:
        return _row_to_dict(row)
    return None

def save_player(user_id: str, player_data: Dict[str, Any]):
    """Insère ou met à jour les données d'un joueur (Upsert Postgres)."""
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    def safe_json(val, default):
        if val is None: return default
        return json.dumps(val)

    items_json = safe_json(player_data.get('items'), '{}')
    skills_json = safe_json(player_data.get('skills'), '[]')
    quests_json = safe_json(player_data.get('quests'), '[]')
    completed_quests_json = safe_json(player_data.get('completed_quests'), '[]')
    defeated_bosses_json = safe_json(player_data.get('defeated_bosses'), '[]')
    unlocked_floors_json = safe_json(player_data.get('unlocked_floors'), '[]')
    unlocked_biomes_json = safe_json(player_data.get('unlocked_biomes'), '{}')
    
    location_val = player_data.get('location', 'Town of Beginnings')
    if isinstance(location_val, dict):
        location_val = json.dumps(location_val)

    # Upsert syntax for PostgreSQL (ON CONFLICT)
    cursor.execute('''
    INSERT INTO players (
        user_id, name, weapon, level, exp, hp, max_hp, attack, defense, agility, 
        location, col, items_json, skills_json, quests_json, 
        completed_quests_json, defeated_bosses_json, unlocked_floors_json, unlocked_biomes_json,
        last_battle, created_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(user_id) DO UPDATE SET
        name=EXCLUDED.name, weapon=EXCLUDED.weapon, level=EXCLUDED.level, exp=EXCLUDED.exp,
        hp=EXCLUDED.hp, max_hp=EXCLUDED.max_hp, attack=EXCLUDED.attack, defense=EXCLUDED.defense,
        agility=EXCLUDED.agility, location=EXCLUDED.location, col=EXCLUDED.col,
        items_json=EXCLUDED.items_json, skills_json=EXCLUDED.skills_json, quests_json=EXCLUDED.quests_json,
        completed_quests_json=EXCLUDED.completed_quests_json, defeated_bosses_json=EXCLUDED.defeated_bosses_json,
        unlocked_floors_json=EXCLUDED.unlocked_floors_json, unlocked_biomes_json=EXCLUDED.unlocked_biomes_json,
        last_battle=EXCLUDED.last_battle
    ''', (
        str(user_id), player_data.get('name'), player_data.get('weapon'), player_data.get('level', 1),
        player_data.get('exp', 0), player_data.get('hp', 100), player_data.get('max_hp', 100),
        player_data.get('attack', 10), player_data.get('defense', 5), player_data.get('agility', 5),
        location_val, player_data.get('col', 500),
        items_json, skills_json, quests_json,
        completed_quests_json, defeated_bosses_json, unlocked_floors_json, unlocked_biomes_json,
        player_data.get('last_battle', 0), player_data.get('created_at', 0)
    ))
    
    conn.commit()
    cursor.close()
    conn.close()

def get_all_players() -> Dict[str, Dict[str, Any]]:
    """Récupère tous les joueurs."""
    conn = get_db_connection()
    if not conn: return {}
    
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT * FROM players")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return {row['user_id']: _row_to_dict(row) for row in rows}

# Initialise la base de données au lancement
init_db()