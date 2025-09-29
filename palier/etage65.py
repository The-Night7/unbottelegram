# -*- coding: utf-8 -*-

# Informations sur l'étage 65
FLOOR_65_INFO = {
    "name": "Floor 65 - Elysium",
    "description": "Un étage paradisiaque avec des plaines fertiles et des collines verdoyantes. La ville principale, Elysium, est construite autour d'un lac aux eaux cristallines.",
    "boss": {
        "name": "Harmonia the Peace Corruptor",
        "level": 85,
        "hp": 7800,
        "attack": 100,
        "defense": 95,
        "exp": 3900,
        "col": 17000,
        "drops": {"Corrupted Harmony": 1.0, "Deceptive Beauty": 0.3},
        "description": "Une entité d'apparence angélique qui cache une nature démoniaque. Elle peut créer des illusions parfaites et manipuler les émotions pour tourner les alliés les uns contre les autres.",
        "required_level": 80,
        "min_party_size": 8
    },
    "safe_zones": ["Elysium", "Tranquil Meadows", "Serene Heights"],
    "danger_level": 9,
    "recommended_level": 77,
    "biomes": [
        {
            "name": "Golden Fields",
            "description": "Des plaines fertiles où poussent des céréales dorées et où paissent des créatures paisibles, mais où se cachent aussi des prédateurs rusés.",
            "monsters": ["Field Stalker", "Golden Beast"],
            "quests": ["q409", "q410"],
            "level_range": [77, 80],
            "unlock_requirements": None
        },
        {
            "name": "Mirage Woods",
            "description": "Une forêt où la réalité semble fluctuer et où des illusions peuvent égarer les voyageurs, habitée par des créatures qui peuvent changer d'apparence.",
            "monsters": ["Shapeshifter", "Illusion Weaver"],
            "quests": ["q411", "q412"],
            "level_range": [80, 83],
            "unlock_requirements": {"level": 79}
        },
        {
            "name": "Temple of Deception",
            "description": "Un temple d'une beauté éblouissante qui cache des horreurs indicibles, où la Corruptrice de la Paix attend les aventuriers dans une chambre aux mille miroirs.",
            "monsters": ["Fallen Angel", "Mirror Guardian"],
            "quests": ["q413", "q414"],
            "level_range": [83, 85],
            "unlock_requirements": {"level": 82, "quest_completed": "q412"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Magmarus the Flame Titan"}
}