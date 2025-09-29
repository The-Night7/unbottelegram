# -*- coding: utf-8 -*-

# Informations sur l'étage 43
FLOOR_43_INFO = {
    "name": "Floor 43 - Glaciem",
    "description": "Un étage gelé avec des montagnes de glace éternelle et des vallées enneigées. La ville principale, Glaciem, est construite dans une caverne de glace qui la protège des blizzards.",
    "boss": {
        "name": "Cryos the Frost Monarch",
        "level": 66,
        "hp": 4600,
        "attack": 81,
        "defense": 71,
        "exp": 2300,
        "col": 10500,
        "drops": {"Eternal Ice Shard": 1.0, "Glacier Blade": 0.3},
        "description": "Un roi de glace qui règne sur l'hiver éternel. Il peut créer des tempêtes de neige, lancer des pics de glace et geler instantanément ses adversaires.",
        "required_level": 61,
        "min_party_size": 6
    },
    "safe_zones": ["Glaciem", "Warm Haven", "Frost Lodge"],
    "danger_level": 7,
    "recommended_level": 56,
    "biomes": [
        {
            "name": "Frozen Tundra",
            "description": "Des plaines gelées balayées par des vents glaciaux, où seules les créatures les plus résistantes au froid peuvent survivre.",
            "monsters": ["Frost Wolf", "Ice Golem"],
            "quests": ["q295", "q296"],
            "level_range": [56, 59],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Glacier",
            "description": "Un immense glacier aux reflets bleutés, où des créatures de glace se confondent avec le paysage et où des crevasses mortelles s'ouvrent sans prévenir.",
            "monsters": ["Ice Elemental", "Glacier Crab"],
            "quests": ["q297", "q298"],
            "level_range": [59, 63],
            "unlock_requirements": {"level": 58}
        },
        {
            "name": "Winter Palace",
            "description": "Un palais majestueux taillé dans la glace éternelle, où le roi des glaces attend les aventuriers sur son trône de givre.",
            "monsters": ["Frozen Knight", "Snow Wraith"],
            "quests": ["q299", "q300"],
            "level_range": [63, 66],
            "unlock_requirements": {"level": 62, "quest_completed": "q298"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Igneus the Flame Tyrant"}
}