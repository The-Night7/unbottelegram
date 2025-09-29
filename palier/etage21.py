# -*- coding: utf-8 -*-

# Informations sur l'étage 21
FLOOR_21_INFO = {
    "name": "Floor 21 - Solaris",
    "description": "Un étage composé de vastes plaines et de collines verdoyantes parsemées de lacs cristallins. La ville principale, Solaris, est construite sur les rives du plus grand lac.",
    "boss": {
        "name": "Hydrus the Lake Guardian",
        "level": 67,
        "hp": 4800,
        "attack": 90,
        "defense": 85,
        "exp": 2500,
        "col": 12500,
        "drops": {"Pure Water Crystal": 1.0, "Tidal Trident": 0.3},
        "description": "Un serpent d'eau colossal qui peut contrôler les courants et créer des vagues dévastatrices. Il peut se fondre dans l'eau pour devenir presque invisible et attaquer par surprise.",
        "required_level": 62,
        "min_party_size": 7
    },
    "safe_zones": ["Solaris", "Lakeside Village", "Fisher's Haven"],
    "danger_level": 7,
    "recommended_level": 60,
    "biomes": [
        {
            "name": "Verdant Plains",
            "description": "De vastes plaines herbeuses où paissent des troupeaux d'herbivores et où chassent des prédateurs agiles.",
            "monsters": ["Plains Runner", "Grass Stalker"],
            "quests": ["q181", "q182"],
            "level_range": [60, 62],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Lakes",
            "description": "Un réseau de lacs aux eaux si pures qu'on peut voir jusqu'au fond, habités par des créatures aquatiques dangereuses.",
            "monsters": ["Lake Serpent", "Crystal Fish"],
            "quests": ["q183", "q184"],
            "level_range": [62, 65],
            "unlock_requirements": {"level": 61}
        },
        {
            "name": "Sacred Spring",
            "description": "La source d'eau magique qui alimente tous les lacs de l'étage, protégée par le boss et ses serviteurs aquatiques.",
            "monsters": ["Water Guardian", "Spring Sprite"],
            "quests": ["q185", "q186"],
            "level_range": [65, 67],
            "unlock_requirements": {"level": 64, "quest_completed": "q184"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Solarius the Radiant"}
}