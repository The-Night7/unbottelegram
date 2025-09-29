# -*- coding: utf-8 -*-

# Informations sur l'étage 49
FLOOR_49_INFO = {
    "name": "Floor 49 - Myujen",
    "description": "Un étage composé de vastes plaines et de collines verdoyantes, parsemé de ruines anciennes. La ville principale, Myujen, est construite autour d'une source thermale aux propriétés curatives.",
    "boss": {
        "name": "Chronos the Guardian of Ages",
        "level": 77,
        "hp": 5800,
        "attack": 93,
        "defense": 83,
        "exp": 2900,
        "col": 13500,
        "drops": {"Hourglass Shard": 1.0, "Timeworn Blade": 0.3},
        "description": "Un être mystérieux qui semble exister hors du temps. Il peut accélérer, ralentir ou même arrêter brièvement le temps pour lui ou ses adversaires, et invoquer des échos du passé.",
        "required_level": 72,
        "min_party_size": 7
    },
    "safe_zones": ["Myujen", "Hot Springs", "Traveler's Rest"],
    "danger_level": 8,
    "recommended_level": 68,
    "biomes": [
        {
            "name": "Ancient Plains",
            "description": "Des plaines où émergent les vestiges d'une civilisation oubliée, habitées par des créatures qui semblent venues d'une autre époque.",
            "monsters": ["Timeless Beast", "Ruin Guardian"],
            "quests": ["q331", "q332"],
            "level_range": [68, 71],
            "unlock_requirements": None
        },
        {
            "name": "Forgotten City",
            "description": "Les ruines d'une cité autrefois grandiose, où le temps semble s'écouler différemment et où des fantômes du passé errent sans fin.",
            "monsters": ["Temporal Anomaly", "Ancient Construct"],
            "quests": ["q333", "q334"],
            "level_range": [71, 74],
            "unlock_requirements": {"level": 70}
        },
        {
            "name": "Clocktower Spire",
            "description": "Une tour mystérieuse qui semble exister simultanément dans plusieurs époques, où le gardien des âges attend les aventuriers.",
            "monsters": ["Chrono Knight", "Time Elemental"],
            "quests": ["q335", "q336"],
            "level_range": [74, 77],
            "unlock_requirements": {"level": 73, "quest_completed": "q334"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Petra the Stone Sovereign"}
}