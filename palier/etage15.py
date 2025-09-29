# -*- coding: utf-8 -*-

# Informations sur l'étage 15
FLOOR_15_INFO = {
    "name": "Floor 15 - Myujen",
    "description": "Un étage composé d'îles flottantes reliées par des ponts suspendus au-dessus d'un abîme sans fond. La ville principale, Myujen, est construite sur la plus grande des îles.",
    "boss": {
        "name": "Skyripper the Cloud Dragon",
        "level": 55,
        "hp": 3600,
        "attack": 75,
        "defense": 70,
        "exp": 1900,
        "col": 9500,
        "drops": {"Cloud Dragon Scale": 1.0, "Skyripper's Talon": 0.3},
        "description": "Un dragon majestueux dont le corps est partiellement composé de nuages. Il peut voler à grande vitesse et créer des tornades avec ses ailes puissantes.",
        "required_level": 50,
        "min_party_size": 6
    },
    "safe_zones": ["Myujen", "Sky Harbor", "Floating Market"],
    "danger_level": 6,
    "recommended_level": 48,
    "biomes": [
        {
            "name": "Floating Islands",
            "description": "Un archipel d'îles flottantes couvertes de végétation luxuriante, où vivent des créatures volantes et des animaux adaptés à la vie dans les airs.",
            "monsters": ["Sky Raptor", "Cloud Fox"],
            "quests": ["q145", "q146"],
            "level_range": [48, 50],
            "unlock_requirements": None
        },
        {
            "name": "Wind Tunnels",
            "description": "Des passages entre les îles où soufflent des vents violents qui peuvent projeter les imprudents dans le vide, habités par des créatures élémentaires.",
            "monsters": ["Air Elemental", "Wind Banshee"],
            "quests": ["q147", "q148"],
            "level_range": [50, 53],
            "unlock_requirements": {"level": 49}
        },
        {
            "name": "Dragon's Aerie",
            "description": "L'île la plus haute et la plus isolée, où se trouve le nid du boss et ses trésors accumulés.",
            "monsters": ["Young Skydragon", "Nest Guardian"],
            "quests": ["q149", "q150"],
            "level_range": [53, 55],
            "unlock_requirements": {"level": 52, "quest_completed": "q148"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Scorpius the Desert Emperor"}
}