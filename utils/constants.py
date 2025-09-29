# -*- coding: utf-8 -*-

# Conversation states
CONVERSATION_STATES = range(9)

# Default stats for new characters
DEFAULT_STATS = {
    "level": 1,
    "exp": 0,
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "defense": 5,
    "agility": 5,
    "location": "Town of Beginnings",
    "items": {"Health Potion": 3, "Teleport Crystal": 1},
    "col": 500,  # SAO currency
    "skills": [],
    "quests": []
}

# Available weapons
WEAPONS = [
    "One-Handed Sword",
    "Rapier",
    "Two-Handed Sword",
    "Dagger",
    "Mace",
    "Spear",
    "Axe",
    "Bow"
]

# SAO locations
SAO_LOCATIONS = [
    "Town of Beginnings",
    "Floor 1 - Tolbana",
    "Floor 2 - Urbus",
    "Floor 3 - Forest of Wandering",
    "Floor 22 - Forest House",
    "Floor 50 - Algade",
    "Floor 55 - Grandzam",
    "Floor 75 - Boss Room"
]

# Quests
QUESTS = [
    {
        "id": "q1",
        "title": "Boar Hunt",
        "description": "Defeat 5 Frenzy Boars in the fields outside the Town of Beginnings.",
        "target": {"monster": "Frenzy Boar", "count": 5},
        "reward": {"exp": 50, "col": 100, "items": {"Health Potion": 2}}
    },
    {
        "id": "q2",
        "title": "Wolf Menace",
        "description": "Clear the forest of 3 Dire Wolves that are threatening travelers.",
        "target": {"monster": "Dire Wolf", "count": 3},
        "reward": {"exp": 100, "col": 200, "items": {"Teleport Crystal": 1}}
    },
    {
        "id": "q3",
        "title": "Kobold Invasion",
        "description": "Defeat 2 Kobold Sentinels that have invaded the village.",
        "target": {"monster": "Kobold Sentinel", "count": 2},
        "reward": {"exp": 150, "col": 300, "items": {"Strength Potion": 1}}
    }
]