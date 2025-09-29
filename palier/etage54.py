# -*- coding: utf-8 -*-

# Informations sur l'étage 54
FLOOR_54_INFO = {
    "name": "Floor 54 - Serras",
    "description": "Un étage montagneux avec des pics acérés et des vallées escarpées. La ville principale, Serras, est construite dans une vallée protégée et connue pour ses forgerons qui travaillent le métal rare extrait des montagnes.",
    "boss": {
        "name": "Avalus the Mountain Tyrant",
        "level": 73,
        "hp": 5800,
        "attack": 88,
        "defense": 78,
        "exp": 2900,
        "col": 12500,
        "drops": {"Mountain's Heart": 1.0, "Tyrant's Axe": 0.3},
        "description": "Un géant de pierre vivante qui règne sur les montagnes. Il peut provoquer des avalanches, lancer d'énormes rochers et faire trembler le sol sous ses pas.",
        "required_level": 68,
        "min_party_size": 7
    },
    "safe_zones": ["Serras", "Miner's Haven", "Summit Refuge"],
    "danger_level": 7,
    "recommended_level": 63,
    "biomes": [
        {
            "name": "Jagged Peaks",
            "description": "Des montagnes aux sommets acérés où nichent des créatures volantes et où le vent souffle avec violence.",
            "monsters": ["Mountain Eagle", "Wind Elemental"],
            "quests": ["q355", "q356"],
            "level_range": [63, 66],
            "unlock_requirements": None
        },
        {
            "name": "Deep Mines",
            "description": "Un réseau de mines profondes où l'on extrait des métaux précieux et des gemmes, habité par des créatures souterraines et des golems.",
            "monsters": ["Mine Dweller", "Crystal Golem"],
            "quests": ["q357", "q358"],
            "level_range": [66, 70],
            "unlock_requirements": {"level": 65}
        },
        {
            "name": "Tyrant's Peak",
            "description": "Le plus haut sommet de l'étage, balayé par des vents violents et des tempêtes de neige, où le tyran des montagnes a établi son domaine.",
            "monsters": ["Frost Giant", "Avalanche Beast"],
            "quests": ["q359", "q360"],
            "level_range": [70, 73],
            "unlock_requirements": {"level": 69, "quest_completed": "q358"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Pestilens the Plague Lord"}
}