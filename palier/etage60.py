# -*- coding: utf-8 -*-

# Informations sur l'étage 60
FLOOR_60_INFO = {
    "name": "Floor 60 - Selmburg",
    "description": "Un étage céleste avec des îles flottantes reliées par des ponts de cristal. La ville principale, Selmburg, est construite sur la plus grande des îles flottantes.",
    "boss": {
        "name": "The Dimensional Reaper",
        "level": 80,
        "hp": 6000,
        "attack": 95,
        "defense": 85,
        "exp": 3000,
        "col": 12000,
        "drops": {"Dimensional Shard": 1.0, "Void Blade": 0.3},
        "description": "Un être capable de manipuler l'espace et le temps. Il peut ouvrir des portails dimensionnels pour attaquer de plusieurs directions à la fois et se téléporter pour éviter les attaques.",
        "required_level": 75,
        "min_party_size": 7
    },
    "safe_zones": ["Selmburg", "Crystal Haven", "Sky Temple"],
    "danger_level": 8,
    "recommended_level": 65,
    "biomes": [
        {
            "name": "Floating Gardens",
            "description": "Des jardins luxuriants suspendus dans les airs, où vivent des créatures célestes et des plantes exotiques.",
            "monsters": ["Sky Butterfly", "Cloud Sprite"],
            "quests": ["q73", "q74"],
            "level_range": [65, 68],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Bridges",
            "description": "Un réseau de ponts de cristal reliant les îles flottantes, gardé par des constructions de cristal vivantes.",
            "monsters": ["Crystal Golem", "Bridge Guardian"],
            "quests": ["q75", "q76"],
            "level_range": [68, 73],
            "unlock_requirements": {"level": 67}
        },
        {
            "name": "Void Temple",
            "description": "Un temple ancien situé sur l'île la plus élevée, où les dimensions se croisent et où réside le boss.",
            "monsters": ["Void Walker", "Time Distortion"],
            "quests": ["q77", "q78"],
            "level_range": [73, 80],
            "unlock_requirements": {"level": 72, "quest_completed": "q76"}
        }
    ],
    "unlock_requirements": {"level": 65}
}