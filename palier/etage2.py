# -*- coding: utf-8 -*-

# Informations sur l'étage 2
FLOOR_2_INFO = {
    "name": "Floor 2 - Urbus",
    "description": "Un étage rocheux avec des plaines et des collines. La ville principale est Urbus, creusée dans une montagne.",
    "boss": {
        "name": "Asterius the Taurus King",
        "level": 20,
        "hp": 800,
        "attack": 30,
        "defense": 25,
        "exp": 400,
        "col": 2000,
        "drops": {"Bullish Horns": 1.0, "Taurus Hammer": 0.3},
        "description": "Un minotaure géant armé d'un énorme marteau. Il devient enragé quand sa vie descend sous les 30%.",
        "required_level": 15,
        "min_party_size": 2
    },
    "safe_zones": ["Urbus", "Mountain Village"],
    "danger_level": 2,
    "recommended_level": 10,
    "biomes": [
        {
            "name": "Rocky Plains",
            "description": "Des plaines rocheuses où paissent des taureaux sauvages et où volent des guêpes géantes.",
            "monsters": ["Wind Wasp", "Bull"],
            "quests": ["q7", "q8"],
            "level_range": [10, 13],
            "unlock_requirements": None
        },
        {
            "name": "Mountain Pass",
            "description": "Un passage montagneux escarpé où des golems de pierre se confondent avec l'environnement.",
            "monsters": ["Rock Golem", "Mountain Wolf"],
            "quests": ["q9", "q10"],
            "level_range": [13, 16],
            "unlock_requirements": {"level": 12}
        },
        {
            "name": "Taurus Caves",
            "description": "Des grottes profondes dans la montagne où vivent les taureaux et leur roi.",
            "monsters": ["Taurus Warrior", "Cave Bat"],
            "quests": ["q11", "q12"],
            "level_range": [16, 20],
            "unlock_requirements": {"level": 15, "quest_completed": "q10"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Illfang the Kobold Lord"}
}