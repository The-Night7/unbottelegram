# -*- coding: utf-8 -*-

# Informations sur l'étage 33
FLOOR_33_INFO = {
    "name": "Floor 33 - Arachnia",
    "description": "Un étage envahi par des toiles d'araignées géantes qui relient les arbres et les structures. La ville principale, Arachnia, est construite dans une immense toile renforcée.",
    "boss": {
        "name": "Arachne the Spider Queen",
        "level": 66,
        "hp": 4600,
        "attack": 81,
        "defense": 76,
        "exp": 2300,
        "col": 12000,
        "drops": {"Spider Silk": 1.0, "Venom Dagger": 0.3},
        "description": "Une femme-araignée gigantesque qui règne sur toutes les créatures à huit pattes de l'étage. Elle peut tisser des toiles magiques, injecter un poison paralysant et invoquer des essaims d'araignées.",
        "required_level": 61,
        "min_party_size": 7
    },
    "safe_zones": ["Arachnia", "Silk Haven", "Spinner's Rest"],
    "danger_level": 7,
    "recommended_level": 56,
    "biomes": [
        {
            "name": "Webbed Forest",
            "description": "Une forêt entièrement recouverte de toiles d'araignées, où se déplacer sans se faire repérer est presque impossible.",
            "monsters": ["Web Lurker", "Silk Spinner"],
            "quests": ["q241", "q242"],
            "level_range": [56, 59],
            "unlock_requirements": None
        },
        {
            "name": "Venom Caves",
            "description": "Un réseau de grottes où les araignées élèvent leurs petits et stockent leurs proies, l'air y est saturé de spores toxiques.",
            "monsters": ["Venom Spider", "Egg Guardian"],
            "quests": ["q243", "q244"],
            "level_range": [59, 63],
            "unlock_requirements": {"level": 58}
        },
        {
            "name": "Queen's Lair",
            "description": "Le centre de la plus grande toile de l'étage, où la reine araignée a établi son domaine et attend les aventuriers imprudents.",
            "monsters": ["Royal Spider Guard", "Broodmother"],
            "quests": ["q245", "q246"],
            "level_range": [63, 66],
            "unlock_requirements": {"level": 62, "quest_completed": "q244"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Autumnus the Harvest King"}
}