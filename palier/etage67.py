# -*- coding: utf-8 -*-

# Informations sur l'étage 67
FLOOR_67_INFO = {
    "name": "Floor 67 - Necropolis",
    "description": "Un étage lugubre dominé par des cimetières sans fin et des mausolées imposants. La ville principale, Necropolis, est construite autour d'une cathédrale gothique et protégée par des barrières sacrées.",
    "boss": {
        "name": "Mortis the Undying King",
        "level": 87,
        "hp": 8200,
        "attack": 104,
        "defense": 97,
        "exp": 4100,
        "col": 18000,
        "drops": {"Soul Fragment": 1.0, "Reaper's Scythe": 0.3},
        "description": "Un roi-liche qui a conquis la mort elle-même. Il peut invoquer des armées de morts-vivants, lancer des sorts nécromantiques et drainer la vie de ses adversaires.",
        "required_level": 82,
        "min_party_size": 8
    },
    "safe_zones": ["Necropolis", "Sanctuary of Light", "Hallowed Ground"],
    "danger_level": 9,
    "recommended_level": 79,
    "biomes": [
        {
            "name": "Endless Graveyard",
            "description": "Un vaste cimetière qui semble s'étendre à l'infini, où des tombes anciennes abritent des morts qui ne reposent pas en paix.",
            "monsters": ["Restless Dead", "Grave Guardian"],
            "quests": ["q421", "q422"],
            "level_range": [79, 82],
            "unlock_requirements": None
        },
        {
            "name": "Haunted Crypts",
            "description": "Un réseau de mausolées et de cryptes interconnectés, où des fantômes tourmentés et des créatures non-mortes plus puissantes ont élu domicile.",
            "monsters": ["Vengeful Spirit", "Crypt Lord"],
            "quests": ["q423", "q424"],
            "level_range": [82, 85],
            "unlock_requirements": {"level": 81}
        },
        {
            "name": "Throne of Bones",
            "description": "Un palais macabre fait d'ossements et de crânes, où le Roi Immortel siège sur un trône d'âmes tourmentées et attend les aventuriers.",
            "monsters": ["Death Knight", "Soul Harvester"],
            "quests": ["q425", "q426"],
            "level_range": [85, 87],
            "unlock_requirements": {"level": 84, "quest_completed": "q424"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Tempestus the Storm Emperor"}
}