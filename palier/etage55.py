# -*- coding: utf-8 -*-

# Informations sur l'étage 55
FLOOR_55_INFO = {
    "name": "Floor 55 - Grandzam",
    "description": "Un étage dominé par une immense forteresse, Grandzam, qui sert de quartier général aux Chevaliers du Sang.",
    "boss": {
        "name": "The Adamantine Sentinel",
        "level": 75,
        "hp": 7000,
        "attack": 90,
        "defense": 85,
        "exp": 3500,
        "col": 15000,
        "drops": {"Adamantine Core": 1.0, "Sentinel Shield": 0.3},
        "description": "Un gardien colossal fait d'adamantium, armé d'une épée et d'un bouclier impénétrables.",
        "required_level": 70,
        "min_party_size": 7
    },
    "safe_zones": ["Grandzam", "Iron Fort", "Knights' Quarters"],
    "danger_level": 7,
    "recommended_level": 65,
    "biomes": [
        {
            "name": "Fortress Outskirts",
            "description": "Les terres entourant la forteresse, patrouillées par des chevaliers corrompus.",
            "monsters": ["Knight of Blood", "Corrupted Squire"],
            "quests": ["q31", "q32"],
            "level_range": [65, 68],
            "unlock_requirements": None
        },
        {
            "name": "Iron Mines",
            "description": "Des mines profondes où l'on extrait le métal pour forger les armes et armures des chevaliers.",
            "monsters": ["Iron Golem", "Mine Dweller"],
            "quests": ["q33", "q34"],
            "level_range": [68, 72],
            "unlock_requirements": {"level": 67, "quest_completed": "q32"}
        },
        {
            "name": "Fortress Interior",
            "description": "L'intérieur de la forteresse, gardé par des statues animées et des constructions métalliques.",
            "monsters": ["Steel Gargoyle", "Animated Armor"],
            "quests": ["q35", "q36"],
            "level_range": [72, 75],
            "unlock_requirements": {"level": 70, "quest_completed": "q34"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Emperor of Darkness", "level": 65}
}