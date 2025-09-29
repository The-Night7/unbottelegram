# -*- coding: utf-8 -*-

# Informations sur l'étage 17
FLOOR_17_INFO = {
    "name": "Floor 17 - Barrowdell",
    "description": "Un étage lugubre composé de marécages brumeux et de collines funéraires. La ville principale, Barrowdell, est construite sur des pilotis au-dessus des marais.",
    "boss": {
        "name": "Mortuus the Grave Lord",
        "level": 59,
        "hp": 4000,
        "attack": 80,
        "defense": 75,
        "exp": 2100,
        "col": 10500,
        "drops": {"Soul Essence": 1.0, "Grave Lord's Scythe": 0.3},
        "description": "Un nécromancien entouré d'une aura de mort qui peut invoquer les âmes des défunts pour combattre à ses côtés et drainer la vie de ses adversaires.",
        "required_level": 54,
        "min_party_size": 6
    },
    "safe_zones": ["Barrowdell", "Dry Haven", "Lighthouse"],
    "danger_level": 7,
    "recommended_level": 52,
    "biomes": [
        {
            "name": "Misty Marshes",
            "description": "Des marécages où une brume épaisse limite la visibilité, cachant des créatures amphibies dangereuses et des pièges naturels.",
            "monsters": ["Bog Lurker", "Mist Phantom"],
            "quests": ["q157", "q158"],
            "level_range": [52, 54],
            "unlock_requirements": None
        },
        {
            "name": "Burial Mounds",
            "description": "Des collines parsemées de tombes anciennes et de cryptes, où des morts-vivants errent sans repos.",
            "monsters": ["Restless Dead", "Grave Guardian"],
            "quests": ["q159", "q160"],
            "level_range": [54, 57],
            "unlock_requirements": {"level": 53}
        },
        {
            "name": "Necropolis",
            "description": "Une cité des morts au centre de l'étage, où le boss a établi son domaine et pratique ses arts interdits.",
            "monsters": ["Death Knight", "Soul Harvester"],
            "quests": ["q161", "q162"],
            "level_range": [57, 59],
            "unlock_requirements": {"level": 56, "quest_completed": "q160"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Archaeos the Ancient Guardian"}
}