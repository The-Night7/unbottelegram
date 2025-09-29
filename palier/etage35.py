# -*- coding: utf-8 -*-

# Informations sur l'étage 35
FLOOR_35_INFO = {
    "name": "Floor 35 - Mishe",
    "description": "Un étage composé d'îles flottant dans les nuages, reliées par des ponts arc-en-ciel. La ville principale, Mishe, est construite sur l'île centrale et est connue pour son observatoire.",
    "boss": {
        "name": "Nimbus the Cloud Sovereign",
        "level": 70,
        "hp": 5000,
        "attack": 85,
        "defense": 80,
        "exp": 2500,
        "col": 13000,
        "drops": {"Cloud Essence": 1.0, "Sky Ruler's Staff": 0.3},
        "description": "Un être éthéré fait de nuages et d'air pur qui peut contrôler les vents et la foudre. Il peut se dissiper pour éviter les attaques et créer des tornades dévastatrices.",
        "required_level": 65,
        "min_party_size": 7
    },
    "safe_zones": ["Mishe", "Rainbow Bridge", "Cloud Harbor"],
    "danger_level": 8,
    "recommended_level": 60,
    "biomes": [
        {
            "name": "Floating Isles",
            "description": "Des îles de taille variable qui flottent dans les nuages, habitées par des créatures aériennes et des plantes exotiques.",
            "monsters": ["Cloud Sprite", "Sky Raptor"],
            "quests": ["q253", "q254"],
            "level_range": [60, 63],
            "unlock_requirements": None
        },
        {
            "name": "Rainbow Paths",
            "description": "Des ponts arc-en-ciel qui relient les îles entre elles, gardés par des sentinelles élémentaires et parfois instables.",
            "monsters": ["Prism Guardian", "Wind Walker"],
            "quests": ["q255", "q256"],
            "level_range": [63, 67],
            "unlock_requirements": {"level": 62}
        },
        {
            "name": "Sovereign's Sanctum",
            "description": "Le palais de nuages où réside le souverain des cieux, constamment entouré de tempêtes et de gardiens aériens.",
            "monsters": ["Storm Elemental", "Cloud Knight"],
            "quests": ["q257", "q258"],
            "level_range": [67, 70],
            "unlock_requirements": {"level": 66, "quest_completed": "q256"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Castellan the Siege Lord"}
}