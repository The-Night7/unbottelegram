# -*- coding: utf-8 -*-

# Informations sur l'étage 66
FLOOR_66_INFO = {
    "name": "Floor 66 - Aetheria",
    "description": "Un étage composé d'îles flottant dans les nuages, reliées par des ponts arc-en-ciel. La ville principale, Aetheria, est construite sur la plus grande des îles et semble faite de nuages solidifiés.",
    "boss": {
        "name": "Tempestus the Storm Emperor",
        "level": 86,
        "hp": 8000,
        "attack": 102,
        "defense": 96,
        "exp": 4000,
        "col": 17500,
        "drops": {"Emperor's Lightning": 1.0, "Tempest Blade": 0.3},
        "description": "Un empereur des cieux qui contrôle les éléments atmosphériques. Il peut invoquer la foudre, créer des tornades et manipuler les vents pour repousser ou attirer ses adversaires.",
        "required_level": 81,
        "min_party_size": 8
    },
    "safe_zones": ["Aetheria", "Cloud Haven", "Rainbow Bridge"],
    "danger_level": 9,
    "recommended_level": 78,
    "biomes": [
        {
            "name": "Floating Isles",
            "description": "Des îles de taille variable qui flottent dans les nuages, habitées par des créatures aériennes et balayées par des vents puissants.",
            "monsters": ["Sky Raptor", "Cloud Elemental"],
            "quests": ["q415", "q416"],
            "level_range": [78, 81],
            "unlock_requirements": None
        },
        {
            "name": "Storm Fields",
            "description": "Des zones où des orages perpétuels font rage, créant des conditions extrêmes et attirant des créatures d'énergie pure.",
            "monsters": ["Lightning Sprite", "Thunder Beast"],
            "quests": ["q417", "q418"],
            "level_range": [81, 84],
            "unlock_requirements": {"level": 80}
        },
        {
            "name": "Emperor's Citadel",
            "description": "Une forteresse majestueuse au sommet de la plus haute île, entourée de nuages d'orage et de gardiens des tempêtes, où l'empereur attend les aventuriers.",
            "monsters": ["Storm Knight", "Wind Guardian"],
            "quests": ["q419", "q420"],
            "level_range": [84, 86],
            "unlock_requirements": {"level": 83, "quest_completed": "q418"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Harmonia the Peace Corruptor"}
}