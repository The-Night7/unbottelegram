# -*- coding: utf-8 -*-

# Informations sur l'étage 61
FLOOR_61_INFO = {
    "name": "Floor 61 - Selmaria",
    "description": "Un étage composé d'immenses champignons géants et de forêts de spores luminescentes. La ville principale, Selmaria, est construite dans le chapeau d'un champignon colossal.",
    "boss": {
        "name": "Mycelia the Spore Queen",
        "level": 81,
        "hp": 7000,
        "attack": 96,
        "defense": 91,
        "exp": 3500,
        "col": 15000,
        "drops": {"Royal Spore": 1.0, "Fungal Staff": 0.3},
        "description": "Une entité féminine mi-humaine mi-champignon qui règne sur la flore fongique de l'étage. Elle peut libérer des nuages de spores aux effets variés et contrôler des créatures infectées par ses mycéliums.",
        "required_level": 76,
        "min_party_size": 7
    },
    "safe_zones": ["Selmaria", "Spore Haven", "Luminous Camp"],
    "danger_level": 8,
    "recommended_level": 73,
    "biomes": [
        {
            "name": "Mushroom Forest",
            "description": "Une forêt de champignons géants aux couleurs vives, où la lumière filtre à travers les chapeaux et où vivent des créatures adaptées à cet environnement unique.",
            "monsters": ["Mushroom Dweller", "Spore Sprite"],
            "quests": ["q385", "q386"],
            "level_range": [73, 76],
            "unlock_requirements": None
        },
        {
            "name": "Luminous Caverns",
            "description": "Des grottes souterraines illuminées par des champignons bioluminescents, habitées par des créatures aveugles et des entités fongiques.",
            "monsters": ["Cave Crawler", "Glowing Fungoid"],
            "quests": ["q387", "q388"],
            "level_range": [76, 79],
            "unlock_requirements": {"level": 75}
        },
        {
            "name": "Royal Spore Garden",
            "description": "Le domaine personnel de la Reine des Spores, où poussent les champignons les plus rares et les plus dangereux, et où elle attend les aventuriers.",
            "monsters": ["Fungal Guardian", "Spore Infected"],
            "quests": ["q389", "q390"],
            "level_range": [79, 81],
            "unlock_requirements": {"level": 78, "quest_completed": "q388"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Dimensional Reaper"}
}