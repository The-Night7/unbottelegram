# -*- coding: utf-8 -*-

# Informations sur l'étage 25
FLOOR_25_INFO = {
    "name": "Floor 25 - Labyrinth",
    "description": "Un étage entièrement constitué d'un immense labyrinthe aux murs changeants. C'est l'un des étages les plus difficiles du premier quart d'Aincrad, ayant causé de nombreuses pertes parmi les joueurs.",
    "boss": {
        "name": "The Demonic Servant",
        "level": 50,
        "hp": 3000,
        "attack": 65,
        "defense": 60,
        "exp": 1500,
        "col": 8000,
        "drops": {"Demonic Horn": 1.0, "Servant's Scythe": 0.3},
        "description": "Un démon à quatre bras maniant simultanément différentes armes. Il peut invoquer des portails dimensionnels pour attaquer depuis n'importe quelle direction.",
        "required_level": 45,
        "min_party_size": 6
    },
    "safe_zones": ["Labyrinth Haven", "Central Plaza"],
    "danger_level": 6,
    "recommended_level": 40,
    "biomes": [
        {
            "name": "Outer Maze",
            "description": "La partie extérieure du labyrinthe, avec des murs moins hauts et quelques repères pour s'orienter.",
            "monsters": ["Maze Minotaur", "Living Wall"],
            "quests": ["q61", "q62"],
            "level_range": [40, 43],
            "unlock_requirements": None
        },
        {
            "name": "Shifting Corridors",
            "description": "Des couloirs dont la configuration change régulièrement, rendant l'orientation presque impossible.",
            "monsters": ["Corridor Phantom", "Lost Soul"],
            "quests": ["q63", "q64"],
            "level_range": [43, 47],
            "unlock_requirements": {"level": 42}
        },
        {
            "name": "Demon's Lair",
            "description": "Le cœur du labyrinthe, un dédale de salles sombres où résident le boss et ses serviteurs démoniaques.",
            "monsters": ["Lesser Demon", "Soul Harvester"],
            "quests": ["q65", "q66"],
            "level_range": [47, 50],
            "unlock_requirements": {"level": 45, "quest_completed": "q64"}
        }
    ],
    "unlock_requirements": {"level": 40}
}