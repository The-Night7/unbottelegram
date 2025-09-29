# -*- coding: utf-8 -*-

import json
import random

# Data storage
DATA_FILE = "player_data.json"

def load_player_data():
    """Load player data from file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_player_data(data):
    """Save player data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_player_data(user_id):
    """Get player data for a specific user"""
    data = load_player_data()
    return data.get(str(user_id))

def save_player(user_id, player_data):
    """Save player data for a specific user"""
    data = load_player_data()
    data[str(user_id)] = player_data
    save_player_data(data)

def level_up_check(player):
    """Check if player can level up and apply changes"""
    # Simple level up formula: level * 100 exp needed
    exp_needed = player["level"] * 100
    
    if player["exp"] >= exp_needed:
        player["level"] += 1
        player["exp"] -= exp_needed
        player["max_hp"] += 20
        player["hp"] = player["max_hp"]  # Heal on level up
        player["attack"] += 3
        player["defense"] += 2
        player["agility"] += 2
        return True
    return False

def get_monster_for_player(player):
    """Get an appropriate monster for player's level"""
    from monstres.monstre_manager import MONSTERS
    
    player_level = player["level"]
    suitable_monsters = []
    
    for name, monster in MONSTERS.items():
        # Select monsters that are at most 5 levels higher than player
        if monster["level"] <= player_level + 5:
            suitable_monsters.append((name, monster))
    
    # If no suitable monsters found, use the lowest level monster
    if not suitable_monsters:
        name = list(MONSTERS.keys())[0]
        return name, MONSTERS[name]
    
    # Weighted selection favoring monsters closer to player's level
    weights = []
    for name, monster in suitable_monsters:
        # The closer the monster level is to player level, the higher the weight
        level_diff = abs(monster["level"] - player_level)
        weight = 10 - min(level_diff, 9)  # Max weight 10, min weight 1
        weights.append(weight)
    
    # Select monster based on weights
    total_weight = sum(weights)
    rand = random.uniform(0, total_weight)
    cumulative_weight = 0
    
    for i, (name, monster) in enumerate(suitable_monsters):
        cumulative_weight += weights[i]
        if rand <= cumulative_weight:
            return name, monster
    
    # Fallback
    name, monster = random.choice(suitable_monsters)
    return name, monster

def get_online_players():
    """Get list of online players (simplified - all saved players are considered online)"""
    data = load_player_data()
    return data

def format_player_stats(player):
    """Format player stats for display"""
    stats = (
        f"Nom: {player['name']}\n"
        f"Niveau: {player['level']}\n"
        f"EXP: {player['exp']}/{player['level'] * 100}\n"
        f"HP: {player['hp']}/{player['max_hp']}\n"
        f"Attaque: {player['attack']}\n"
        f"Défense: {player['defense']}\n"
        f"Agilité: {player['agility']}\n"
        f"Arme: {player['weapon']}\n"
        f"Localisation: {player['location']}\n"
        f"Col: {player['col']}\n"
        f"Objets: {', '.join([f'{item} x{count}' for item, count in player['items'].items()])}"
    )
    return stats