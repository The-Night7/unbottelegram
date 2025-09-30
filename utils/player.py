#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# Data storage
DATA_FILE = "../player_data.json"

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


def get_online_players():
    """Get list of online players (simplified - all saved players are considered online)"""
    data = load_player_data()
    return data


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