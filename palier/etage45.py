# -*- coding: utf-8 -*-

# Informations sur l'étage 45
FLOOR_45_INFO = {
    "name": "Floor 45 - Granzam",
    "description": "Un étage dominé par des montagnes métalliques et des vallées remplies de minerai. La ville principale, Granzam, est une cité fortifiée entièrement construite en métal.",
    "boss": {
        "name": "Ferrum the Iron Colossus",
        "level": 70,
        "hp": 5000,
        "attack": 85,
        "defense": 75,
        "exp": 2500,
        "col": 11500,
        "drops": {"Perfect Alloy": 1.0, "Colossus Hammer": 0.3},
        "description": "Un géant de métal vivant qui peut absorber le minerai environnant pour renforcer son armure. Ses poings sont comme des marteaux et il peut lancer des projectiles métalliques.",
        "required_level": 65,
        "min_party_size": 6
    },
    "safe_zones": ["Granzam", "Forge Town", "Miner's Rest"],
    "danger_level": 7,
    "recommended_level": 60,
    "biomes": [
        {
            "name": "Iron Hills",
            "description": "Des collines riches en minerai de fer où travaillent des mineurs et où rôdent des constructions métalliques hostiles.",
            "monsters": ["Iron Golem", "Ore Elemental"],
            "quests": ["q307", "q308"],
            "level_range": [60, 63],
            "unlock_requirements": None
        },
        {
            "name": "Forge Valley",
            "description": "Une vallée remplie de forges où le métal est travaillé jour et nuit, gardée par des sentinelles mécaniques.",
            "monsters": ["Forge Guardian", "Steel Construct"],
            "quests": ["q309", "q310"],
            "level_range": [63, 67],
            "unlock_requirements": {"level": 62}
        },
        {
            "name": "Colossus Workshop",
            "description": "Un immense atelier où sont créées des armes et des armures légendaires, et où le boss supervise la création de son armée mécanique.",
            "monsters": ["Mechanical Knight", "Living Armor"],
            "quests": ["q311", "q312"],
            "level_range": [67, 70],
            "unlock_requirements": {"level": 66, "quest_completed": "q310"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Araneae the Weaver Queen"}
}