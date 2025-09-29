# -*- coding: utf-8 -*-

# Informations sur l'étage 24
FLOOR_24_INFO = {
    "name": "Floor 24 - Panareze",
    "description": "Un étage composé d'archipels reliés par des ponts suspendus. La ville principale, Panareze, est construite sur l'île centrale et est connue pour son grand marché.",
    "boss": {
        "name": "Poseidus the Island Titan",
        "level": 49,
        "hp": 2900,
        "attack": 64,
        "defense": 58,
        "exp": 1400,
        "col": 7000,
        "drops": {"Titan's Pearl": 1.0, "Coral Trident": 0.3},
        "description": "Un titan colossal qui émerge de l'océan, capable de provoquer des raz-de-marée et d'invoquer des créatures marines. Son corps est partiellement fait de corail et de roche.",
        "required_level": 44,
        "min_party_size": 5
    },
    "safe_zones": ["Panareze", "Fisher's Harbor", "Lighthouse Point"],
    "danger_level": 5,
    "recommended_level": 39,
    "biomes": [
        {
            "name": "Trading Islands",
            "description": "Un groupe d'îles où se tiennent des marchés animés, mais où des pirates et des bandits rôdent à la recherche de butin.",
            "monsters": ["Island Bandit", "Market Thief"],
            "quests": ["q193", "q194"],
            "level_range": [39, 42],
            "unlock_requirements": None
        },
        {
            "name": "Coral Archipelago",
            "description": "Des îles entourées de récifs coralliens colorés, habitées par des créatures marines dangereuses qui s'aventurent parfois sur la terre ferme.",
            "monsters": ["Reef Guardian", "Beach Predator"],
            "quests": ["q195", "q196"],
            "level_range": [42, 46],
            "unlock_requirements": {"level": 41}
        },
        {
            "name": "Titan's Throne",
            "description": "Une île volcanique au centre de l'archipel, où le boss a établi son domaine et attend les aventuriers.",
            "monsters": ["Lava Crawler", "Ocean Sentinel"],
            "quests": ["q197", "q198"],
            "level_range": [46, 49],
            "unlock_requirements": {"level": 45, "quest_completed": "q196"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Harvester the Plant Lord"}
}