# -*- coding: utf-8 -*-

# Informations sur l'étage 63
FLOOR_63_INFO = {
    "name": "Floor 63 - Zumfut",
    "description": "Un étage couvert de jungles denses et de ruines anciennes envahies par la végétation. La ville principale, Zumfut, est construite dans les arbres et reliée par des ponts suspendus.",
    "boss": {
        "name": "Thornlash the Jungle Tyrant",
        "level": 83,
        "hp": 7400,
        "attack": 98,
        "defense": 93,
        "exp": 3700,
        "col": 16000,
        "drops": {"Ancient Vine": 1.0, "Thorn Whip": 0.3},
        "description": "Une créature mi-plante mi-animal qui règne sur la jungle. Son corps est couvert d'épines venimeuses et il peut contrôler la végétation environnante pour piéger ses adversaires.",
        "required_level": 78,
        "min_party_size": 8
    },
    "safe_zones": ["Zumfut", "Canopy Village", "Explorer's Camp"],
    "danger_level": 8,
    "recommended_level": 75,
    "biomes": [
        {
            "name": "Dense Jungle",
            "description": "Une jungle luxuriante où la végétation est si dense que peu de lumière atteint le sol, habitée par des prédateurs furtifs et des insectes géants.",
            "monsters": ["Jungle Stalker", "Giant Mantis"],
            "quests": ["q397", "q398"],
            "level_range": [75, 78],
            "unlock_requirements": None
        },
        {
            "name": "Ancient Ruins",
            "description": "Les vestiges d'une civilisation oubliée, envahis par la végétation et gardés par des constructions animées et des pièges mortels.",
            "monsters": ["Stone Guardian", "Cursed Idol"],
            "quests": ["q399", "q400"],
            "level_range": [78, 81],
            "unlock_requirements": {"level": 77}
        },
        {
            "name": "Throne of Thorns",
            "description": "Un temple ancien au cœur de la jungle, transformé en un nid d'épines et de plantes carnivores, où le tyran de la jungle attend les aventuriers.",
            "monsters": ["Thorn Beast", "Plant Hybrid"],
            "quests": ["q401", "q402"],
            "level_range": [81, 83],
            "unlock_requirements": {"level": 80, "quest_completed": "q400"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Crystallis the Gem Lord"}
}