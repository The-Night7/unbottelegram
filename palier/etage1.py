# -*- coding: utf-8 -*-

# Informations sur l'étage 1
FLOOR_1_INFO = {
    "name": "Floor 1 - Tolbana",
    "description": "Le premier étage d'Aincrad, où tout a commencé. C'est ici que se trouve la ville de départ et les premières zones de chasse.",
    "boss": {
        "name": "Illfang the Kobold Lord",
        "level": 10,
        "hp": 500,
        "attack": 20,
        "defense": 15,
        "exp": 200,
        "col": 1000,
        "drops": {"Coat of Midnight": 1.0, "Kobold Lord's Talwar": 0.3},
        "description": "Le boss du premier étage, un grand kobold armé d'une hache et d'un bouclier. Quand sa dernière barre de vie atteint le rouge, il change d'arme pour un talwar.",
        "required_level": 8,
        "min_party_size": 1
    },
    "safe_zones": ["Town of Beginnings", "Tolbana"],
    "danger_level": 1,
    "recommended_level": 1,
    "biomes": [
        {
            "name": "Plains of Beginning",
            "description": "Vastes plaines verdoyantes entourant la Ville des Débuts. Parfait pour les débutants.",
            "monsters": ["Frenzy Boar", "Little Nepent"],
            "quests": ["q1", "q4"],
            "level_range": [1, 3],
            "unlock_requirements": None
        },
        {
            "name": "Tolbana Forest",
            "description": "Une forêt dense à l'est de Tolbana, où des loups et des créatures plus dangereuses rôdent.",
            "monsters": ["Dire Wolf", "Forest Kobold"],
            "quests": ["q2", "q5"],
            "level_range": [3, 5],
            "unlock_requirements": {"level": 3}
        },
        {
            "name": "Kobold Caves",
            "description": "Un réseau de grottes au nord de l'étage, habité par des kobolds et menant à la salle du boss.",
            "monsters": ["Kobold Sentinel", "Kobold Miner"],
            "quests": ["q3", "q6"],
            "level_range": [5, 8],
            "unlock_requirements": {"level": 5, "quest_completed": "q5"}
        }
    ],
    "unlock_requirements": None
}