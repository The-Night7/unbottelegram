# -*- coding: utf-8 -*-

# Informations sur l'étage 27
FLOOR_27_INFO = {
    "name": "Floor 27 - Roneal",
    "description": "Un étage au climat hivernal avec des montagnes enneigées et des forêts de conifères. La ville principale, Roneal, est construite dans une vallée abritée et connue pour ses sources chaudes.",
    "boss": {
        "name": "Glacius the Frost Monarch",
        "level": 54,
        "hp": 3400,
        "attack": 69,
        "defense": 64,
        "exp": 1700,
        "col": 9000,
        "drops": {"Eternal Ice Crystal": 1.0, "Frost Monarch's Crown": 0.3},
        "description": "Un roi de glace siégeant sur un trône de givre éternel. Il peut créer des tempêtes de neige, lancer des pics de glace et geler instantanément ses adversaires.",
        "required_level": 49,
        "min_party_size": 6
    },
    "safe_zones": ["Roneal", "Hot Springs Village", "Mountain Lodge"],
    "danger_level": 6,
    "recommended_level": 44,
    "biomes": [
        {
            "name": "Snow Fields",
            "description": "De vastes étendues de neige où sévissent des blizzards imprévisibles et où rôdent des créatures adaptées au froid extrême.",
            "monsters": ["Snow Wolf", "Frost Golem"],
            "quests": ["q205", "q206"],
            "level_range": [44, 47],
            "unlock_requirements": None
        },
        {
            "name": "Frozen Forest",
            "description": "Une forêt de pins et de sapins couverts de givre, où des créatures de glace se cachent parmi les arbres.",
            "monsters": ["Ice Elemental", "Frozen Treant"],
            "quests": ["q207", "q208"],
            "level_range": [47, 51],
            "unlock_requirements": {"level": 46}
        },
        {
            "name": "Glacier Palace",
            "description": "Un palais majestueux taillé dans un glacier millénaire, où le roi des glaces attend les aventuriers sur son trône de givre.",
            "monsters": ["Ice Guardian", "Frost Knight"],
            "quests": ["q209", "q210"],
            "level_range": [51, 54],
            "unlock_requirements": {"level": 50, "quest_completed": "q208"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Fogwalker the Phantom"}
}