# -*- coding: utf-8 -*-

# Informations sur l'étage 31
FLOOR_31_INFO = {
    "name": "Floor 31 - Alne",
    "description": "Un étage composé de vastes prairies parsemées de fleurs géantes multicolores. La ville principale, Alne, est construite au centre d'une immense fleur de lotus.",
    "boss": {
        "name": "Floramancer the Bloom Lord",
        "level": 62,
        "hp": 4200,
        "attack": 77,
        "defense": 72,
        "exp": 2100,
        "col": 11000,
        "drops": {"Eternal Petal": 1.0, "Bloom Staff": 0.3},
        "description": "Un mage botaniste qui a fusionné avec les plantes qu'il étudiait. Il peut contrôler les fleurs géantes de l'étage et libérer des pollens toxiques ou des spores hallucinogènes.",
        "required_level": 57,
        "min_party_size": 7
    },
    "safe_zones": ["Alne", "Petal Village", "Nectar Springs"],
    "danger_level": 7,
    "recommended_level": 52,
    "biomes": [
        {
            "name": "Flower Fields",
            "description": "Des prairies couvertes de fleurs géantes aux couleurs vives, où butinent des insectes massifs et où se cachent des créatures végétales.",
            "monsters": ["Giant Bee", "Flower Sprite"],
            "quests": ["q229", "q230"],
            "level_range": [52, 55],
            "unlock_requirements": None
        },
        {
            "name": "Nectar Forest",
            "description": "Une forêt où les arbres produisent un nectar sucré qui attire des créatures dangereuses et où poussent des plantes carnivores.",
            "monsters": ["Nectar Drinker", "Carnivorous Bloom"],
            "quests": ["q231", "q232"],
            "level_range": [55, 59],
            "unlock_requirements": {"level": 54}
        },
        {
            "name": "Grand Lotus",
            "description": "Une fleur de lotus gigantesque au centre de l'étage, dont le cœur abrite le laboratoire du boss et ses créations botaniques.",
            "monsters": ["Plant Hybrid", "Pollen Guardian"],
            "quests": ["q233", "q234"],
            "level_range": [59, 62],
            "unlock_requirements": {"level": 58, "quest_completed": "q232"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Fulguris the Storm Emperor"}
}