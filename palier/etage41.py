# -*- coding: utf-8 -*-

# Informations sur l'étage 41
FLOOR_41_INFO = {
    "name": "Floor 41 - Taft",
    "description": "Un étage dominé par d'immenses arbres millénaires qui s'élèvent jusqu'aux nuages. La ville principale, Taft, est construite dans les branches des arbres les plus imposants.",
    "boss": {
        "name": "Sylvanus the Ancient",
        "level": 62,
        "hp": 4200,
        "attack": 77,
        "defense": 67,
        "exp": 2100,
        "col": 9500,
        "drops": {"Ancient Heartwood": 1.0, "Verdant Staff": 0.3},
        "description": "Un esprit de la forêt primordiale qui a pris la forme d'un immense treant. Il peut contrôler les racines et les branches des arbres environnants et invoquer des serviteurs végétaux.",
        "required_level": 57,
        "min_party_size": 6
    },
    "safe_zones": ["Taft", "Canopy Village", "Root Haven"],
    "danger_level": 6,
    "recommended_level": 52,
    "biomes": [
        {
            "name": "Forest Floor",
            "description": "Le sol de la forêt, plongé dans une semi-obscurité permanente, où des champignons géants et des créatures souterraines ont élu domicile.",
            "monsters": ["Root Crawler", "Mushroom Beast"],
            "quests": ["q283", "q284"],
            "level_range": [52, 55],
            "unlock_requirements": None
        },
        {
            "name": "Middle Canopy",
            "description": "Les branches intermédiaires des arbres géants, où vivent des créatures arboricoles et où l'on trouve des plantes rares.",
            "monsters": ["Tree Jumper", "Canopy Hunter"],
            "quests": ["q285", "q286"],
            "level_range": [55, 59],
            "unlock_requirements": {"level": 54}
        },
        {
            "name": "Crown Heights",
            "description": "Les plus hautes branches des arbres géants, baignées de soleil et balayées par des vents violents, où le boss a établi son sanctuaire.",
            "monsters": ["Sky Sentinel", "Wind Sprite"],
            "quests": ["q287", "q288"],
            "level_range": [59, 62],
            "unlock_requirements": {"level": 58, "quest_completed": "q286"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Vemacitrin the Absolute"}
}