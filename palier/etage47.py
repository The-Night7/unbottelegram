# -*- coding: utf-8 -*-

# Informations sur l'étage 47
FLOOR_47_INFO = {
    "name": "Floor 47 - Floria",
    "description": "Un étage couvert de prairies fleuries et de jardins luxuriants. La ville principale, Floria, est connue pour son festival des fleurs et ses jardins botaniques.",
    "boss": {
        "name": "Anthea the Bloom Queen",
        "level": 73,
        "hp": 5400,
        "attack": 89,
        "defense": 79,
        "exp": 2700,
        "col": 12500,
        "drops": {"Eternal Bloom": 1.0, "Thorn Whip": 0.3},
        "description": "Une fée majestueuse qui règne sur les fleurs et les plantes. Elle peut libérer des pollens paralysants, contrôler les plantes environnantes et se régénérer au contact de la nature.",
        "required_level": 68,
        "min_party_size": 7
    },
    "safe_zones": ["Floria", "Garden Sanctuary", "Petal Village"],
    "danger_level": 7,
    "recommended_level": 64,
    "biomes": [
        {
            "name": "Flower Fields",
            "description": "D'immenses prairies couvertes de fleurs multicolores où vivent des créatures pacifiques et des esprits de la nature.",
            "monsters": ["Pollen Sprite", "Flower Guardian"],
            "quests": ["q319", "q320"],
            "level_range": [64, 67],
            "unlock_requirements": None
        },
        {
            "name": "Enchanted Gardens",
            "description": "Des jardins magiques où poussent des plantes aux propriétés extraordinaires, gardés par des créatures végétales conscientes.",
            "monsters": ["Garden Golem", "Sentient Vine"],
            "quests": ["q321", "q322"],
            "level_range": [67, 70],
            "unlock_requirements": {"level": 66}
        },
        {
            "name": "Queen's Sanctuary",
            "description": "Un jardin secret au centre de l'étage, où les fleurs les plus rares et les plus dangereuses sont cultivées par la reine elle-même.",
            "monsters": ["Royal Gardener", "Carnivorous Bloom"],
            "quests": ["q323", "q324"],
            "level_range": [70, 73],
            "unlock_requirements": {"level": 69, "quest_completed": "q322"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Abyssus the Deep One"}
}