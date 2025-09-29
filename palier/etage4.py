# -*- coding: utf-8 -*-

# Informations sur l'étage 4
FLOOR_4_INFO = {
    "name": "Floor 4 - Rovia",
    "description": "Un étage principalement aquatique avec des canaux et des rivières. La ville principale, Rovia, est construite sur l'eau et les déplacements s'y font en gondole.",
    "boss": {
        "name": "Wythege the Hippocampus",
        "level": 35,
        "hp": 1500,
        "attack": 45,
        "defense": 40,
        "exp": 800,
        "col": 4000,
        "drops": {"Aqua Scale": 1.0, "Trident of Storms": 0.3},
        "description": "Un hippocampe géant capable de créer des tourbillons d'eau et de convoquer des serviteurs aquatiques. Il peut plonger sous l'eau pour éviter les attaques.",
        "required_level": 30,
        "min_party_size": 4
    },
    "safe_zones": ["Rovia", "Fisherman's Dock", "Canal Bridge"],
    "danger_level": 4,
    "recommended_level": 25,
    "biomes": [
        {
            "name": "Canal City",
            "description": "Le réseau de canaux et de ponts qui forme la ville de Rovia. Des créatures aquatiques s'aventurent parfois dans les canaux.",
            "monsters": ["Canal Lurker", "Water Strider"],
            "quests": ["q43", "q44"],
            "level_range": [25, 27],
            "unlock_requirements": None
        },
        {
            "name": "Misty Marshlands",
            "description": "Des marécages brumeux entourant la ville, où vivent des grenouilles géantes et des créatures amphibies.",
            "monsters": ["Giant Toad", "Marsh Stalker"],
            "quests": ["q45", "q46"],
            "level_range": [27, 30],
            "unlock_requirements": {"level": 26}
        },
        {
            "name": "Deep Lake",
            "description": "Un lac profond au centre de l'étage, repaire de créatures aquatiques dangereuses et du boss.",
            "monsters": ["Deep Swimmer", "Razor Fin"],
            "quests": ["q47", "q48"],
            "level_range": [30, 35],
            "unlock_requirements": {"level": 29, "quest_completed": "q46"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Nerius the Evil Treant"}
}