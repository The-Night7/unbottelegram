# -*- coding: utf-8 -*-

# Informations sur l'étage 32
FLOOR_32_INFO = {
    "name": "Floor 32 - Fallhaven",
    "description": "Un étage où règne un automne perpétuel, avec des forêts aux feuilles dorées et rouges. La ville principale, Fallhaven, est construite dans une vallée entourée d'arbres majestueux.",
    "boss": {
        "name": "Autumnus the Harvest King",
        "level": 64,
        "hp": 4400,
        "attack": 79,
        "defense": 74,
        "exp": 2200,
        "col": 11500,
        "drops": {"Autumn Crown": 1.0, "Harvest Scythe": 0.3},
        "description": "Un esprit de la nature qui incarne l'automne. Il peut contrôler les vents et les feuilles mortes pour créer des tempêtes dévastatrices et drainer la vitalité de ses adversaires.",
        "required_level": 59,
        "min_party_size": 7
    },
    "safe_zones": ["Fallhaven", "Amber Lodge", "Maple Village"],
    "danger_level": 7,
    "recommended_level": 54,
    "biomes": [
        {
            "name": "Golden Woods",
            "description": "Des forêts aux feuilles dorées où le sol est couvert d'un épais tapis de feuilles mortes, cachant parfois des créatures dangereuses.",
            "monsters": ["Leaf Stalker", "Autumn Wolf"],
            "quests": ["q235", "q236"],
            "level_range": [54, 57],
            "unlock_requirements": None
        },
        {
            "name": "Harvest Fields",
            "description": "Des champs où poussent d'étranges cultures automnales, gardés par des épouvantails animés et des esprits de la moisson.",
            "monsters": ["Living Scarecrow", "Harvest Spirit"],
            "quests": ["q237", "q238"],
            "level_range": [57, 61],
            "unlock_requirements": {"level": 56}
        },
        {
            "name": "King's Grove",
            "description": "Un cercle d'arbres anciens aux couleurs flamboyantes, où le roi de l'automne tient sa cour et attend les aventuriers.",
            "monsters": ["Ancient Treant", "Wind Elemental"],
            "quests": ["q239", "q240"],
            "level_range": [61, 64],
            "unlock_requirements": {"level": 60, "quest_completed": "q238"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Floramancer the Bloom Lord"}
}