# -*- coding: utf-8 -*-

# Informations sur l'étage 76
FLOOR_76_INFO = {
    "name": "Floor 76 - Skyreach",
    "description": "Un étage situé au-dessus des nuages, avec des tours flottantes et des jardins suspendus. La ville principale, Skyreach, est construite sur une immense plateforme de cristal.",
    "boss": {
        "name": "Aetheria the Sky Empress",
        "level": 91,
        "hp": 10200,
        "attack": 122,
        "defense": 102,
        "exp": 5100,
        "col": 25500,
        "drops": {"Celestial Feather": 1.0, "Skyborn Staff": 0.3},
        "description": "Une impératrice céleste aux ailes de cristal qui règne sur les cieux. Elle peut contrôler les vents, invoquer des tempêtes de foudre et créer des tornades dévastatrices.",
        "required_level": 86,
        "min_party_size": 10
    },
    "safe_zones": ["Skyreach", "Cloud Haven", "Crystal Observatory"],
    "danger_level": 10,
    "recommended_level": 81,
    "biomes": [
        {
            "name": "Cloud Gardens",
            "description": "Des jardins luxuriants qui flottent sur des nuages solides, où poussent des plantes célestes et où vivent des créatures aériennes.",
            "monsters": ["Cloud Sprite", "Sky Gardener"],
            "quests": ["q463", "q464"],
            "level_range": [81, 84],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Spires",
            "description": "D'immenses tours de cristal qui s'élèvent vers le ciel, habitées par des êtres de lumière et gardées par des constructions volantes.",
            "monsters": ["Light Elemental", "Crystal Guardian"],
            "quests": ["q465", "q466"],
            "level_range": [84, 88],
            "unlock_requirements": {"level": 83}
        },
        {
            "name": "Empress's Sanctum",
            "description": "Le palais céleste de l'Impératrice, situé au sommet de la plus haute tour, où elle attend les aventuriers entourée de sa cour céleste.",
            "monsters": ["Royal Wind Knight", "Storm Herald"],
            "quests": ["q467", "q468"],
            "level_range": [88, 91],
            "unlock_requirements": {"level": 87, "quest_completed": "q466"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Skull Reaper"}
}