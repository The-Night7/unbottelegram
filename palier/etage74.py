# -*- coding: utf-8 -*-

# Informations sur l'étage 74
FLOOR_74_INFO = {
    "name": "Floor 74 - Dreadmist Peak",
    "description": "Un étage montagneux enveloppé d'un brouillard perpétuel. C'est ici que Kirito a affronté et vaincu le boss Gleam Eyes en solo, un exploit légendaire.",
    "boss": {
        "name": "Fogbinder the Mist Wraith",
        "level": 85,
        "hp": 9000,
        "attack": 110,
        "defense": 95,
        "exp": 4500,
        "col": 20000,
        "drops": {"Mist Essence": 1.0, "Fogbinder's Cloak": 0.3},
        "description": "Un spectre éthéré qui peut se fondre dans le brouillard et devenir presque invisible. Il contrôle le brouillard pour aveugler ses adversaires et les attaquer par surprise.",
        "required_level": 80,
        "min_party_size": 8
    },
    "safe_zones": ["Misthaven", "Foggy Refuge", "Mountaineer's Camp"],
    "danger_level": 9,
    "recommended_level": 75,
    "biomes": [
        {
            "name": "Misty Foothills",
            "description": "Les contreforts de la montagne, où le brouillard commence à s'épaissir et où des créatures rôdent dans la brume.",
            "monsters": ["Mist Wolf", "Fog Stalker"],
            "quests": ["q79", "q80"],
            "level_range": [75, 78],
            "unlock_requirements": None
        },
        {
            "name": "Haunted Forest",
            "description": "Une forêt dense et brumeuse à mi-hauteur de la montagne, hantée par des spectres et des créatures cauchemardesques.",
            "monsters": ["Mist Phantom", "Haunted Tree"],
            "quests": ["q81", "q82"],
            "level_range": [78, 82],
            "unlock_requirements": {"level": 77}
        },
        {
            "name": "Summit Shrine",
            "description": "Le sommet de la montagne, où le brouillard est si épais qu'on ne voit pas à un mètre. C'est ici que se trouve le boss.",
            "monsters": ["Gleam Eyes", "Mist Wraith"],
            "quests": ["q83", "q84"],
            "level_range": [82, 85],
            "unlock_requirements": {"level": 80, "quest_completed": "q82"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Thornlash the Jungle Tyrant", "level": 75}
}