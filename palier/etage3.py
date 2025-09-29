# -*- coding: utf-8 -*-

# Informations sur l'étage 3
FLOOR_3_INFO = {
    "name": "Floor 3 - Forest of Wandering",
    "description": "Un étage couvert de forêts denses où il est facile de se perdre. Les sentiers changent constamment.",
    "boss": {
        "name": "Nerius the Evil Treant",
        "level": 30,
        "hp": 1200,
        "attack": 40,
        "defense": 35,
        "exp": 600,
        "col": 3000,
        "drops": {"Ancient Bark": 1.0, "Forest Staff": 0.3},
        "description": "Un arbre gigantesque animé qui contrôle les plantes de la forêt. Il peut régénérer sa vie et invoquer des serviteurs.",
        "required_level": 25,
        "min_party_size": 3
    },
    "safe_zones": ["Zumfut", "Forest House"],
    "danger_level": 3,
    "recommended_level": 20,
    "biomes": [
        {
            "name": "Forest Entrance",
            "description": "La lisière de la forêt, où les sentiers sont encore clairs mais où les araignées commencent à tisser leurs toiles.",
            "monsters": ["Venomous Spider", "Forest Wolf"],
            "quests": ["q13", "q14"],
            "level_range": [20, 23],
            "unlock_requirements": None
        },
        {
            "name": "Elven Territory",
            "description": "Une partie de la forêt revendiquée par des elfes hostiles qui défendent leur territoire.",
            "monsters": ["Forest Elf", "Elven Scout"],
            "quests": ["q15", "q16"],
            "level_range": [23, 26],
            "unlock_requirements": {"level": 22}
        },
        {
            "name": "Deep Forest",
            "description": "Le cœur de la forêt où les arbres sont vivants et où se cache le boss.",
            "monsters": ["Treant Sapling", "Forest Stalker"],
            "quests": ["q17", "q18"],
            "level_range": [26, 30],
            "unlock_requirements": {"level": 25, "quest_completed": "q16"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Asterius the Taurus King"}
}