# -*- coding: utf-8 -*-

# Informations sur l'étage 44
FLOOR_44_INFO = {
    "name": "Floor 44 - Arachnid",
    "description": "Un étage envahi par des toiles d'araignées géantes et des structures en forme de dômes. La ville principale, Arachnid, est construite dans un immense cocon renforcé.",
    "boss": {
        "name": "Araneae the Weaver Queen",
        "level": 68,
        "hp": 4800,
        "attack": 83,
        "defense": 73,
        "exp": 2400,
        "col": 11000,
        "drops": {"Silken Thread": 1.0, "Venomous Fang": 0.3},
        "description": "Une araignée géante à l'intelligence humaine qui règne sur toutes les créatures à huit pattes de l'étage. Elle peut tisser des toiles magiques et injecter un poison paralysant.",
        "required_level": 63,
        "min_party_size": 6
    },
    "safe_zones": ["Arachnid", "Silk Haven", "Web Fortress"],
    "danger_level": 7,
    "recommended_level": 58,
    "biomes": [
        {
            "name": "Silk Forest",
            "description": "Une forêt entièrement recouverte de toiles d'araignées, où les arbres sont reliés par des fils de soie et où se déplacer sans se faire repérer est presque impossible.",
            "monsters": ["Silk Spinner", "Web Lurker"],
            "quests": ["q301", "q302"],
            "level_range": [58, 61],
            "unlock_requirements": None
        },
        {
            "name": "Venom Caves",
            "description": "Un réseau de grottes où les araignées élèvent leurs petits et stockent leurs proies, l'air y est saturé de spores toxiques.",
            "monsters": ["Poison Spider", "Egg Guardian"],
            "quests": ["q303", "q304"],
            "level_range": [61, 65],
            "unlock_requirements": {"level": 60}
        },
        {
            "name": "Queen's Web",
            "description": "Le centre de la plus grande toile de l'étage, où la reine araignée a établi son domaine et attend les aventuriers imprudents.",
            "monsters": ["Spider Knight", "Venom Priest"],
            "quests": ["q305", "q306"],
            "level_range": [65, 68],
            "unlock_requirements": {"level": 64, "quest_completed": "q304"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Cryos the Frost Monarch"}
}