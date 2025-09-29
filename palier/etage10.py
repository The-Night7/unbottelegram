# -*- coding: utf-8 -*-

# Informations sur l'étage 10
FLOOR_10_INFO = {
    "name": "Floor 10 - Coral",
    "description": "Un étage au climat tropical avec des plages de sable blanc et des récifs coralliens. La ville principale, Coral, est construite sur pilotis au-dessus de l'eau.",
    "boss": {
        "name": "Kagachi the Samurai Lord",
        "level": 45,
        "hp": 2200,
        "attack": 55,
        "defense": 50,
        "exp": 1200,
        "col": 6000,
        "drops": {"Samurai Helmet": 1.0, "Kagachi's Katana": 0.3},
        "description": "Un seigneur de guerre samouraï accompagné de quatre gardes. Il maîtrise diverses techniques d'épée et peut exécuter des attaques rapides et précises.",
        "required_level": 40,
        "min_party_size": 5
    },
    "safe_zones": ["Coral", "Fisherman's Village", "Palm Beach"],
    "danger_level": 5,
    "recommended_level": 35,
    "biomes": [
        {
            "name": "Tropical Beach",
            "description": "Des plages de sable blanc bordées de palmiers, où vivent des crabes géants et des tortues.",
            "monsters": ["Giant Crab", "Shell Turtle"],
            "quests": ["q55", "q56"],
            "level_range": [35, 38],
            "unlock_requirements": None
        },
        {
            "name": "Coral Reef",
            "description": "Un vaste récif corallien aux couleurs vives, habité par des poissons exotiques et des créatures marines dangereuses.",
            "monsters": ["Reef Shark", "Poisonous Jellyfish"],
            "quests": ["q57", "q58"],
            "level_range": [38, 42],
            "unlock_requirements": {"level": 37}
        },
        {
            "name": "Samurai Fortress",
            "description": "Une forteresse japonaise traditionnelle située sur une île au centre de l'étage, gardée par des samouraïs et des ninjas.",
            "monsters": ["Ronin Warrior", "Shadow Ninja"],
            "quests": ["q59", "q60"],
            "level_range": [42, 45],
            "unlock_requirements": {"level": 40, "quest_completed": "q58"}
        }
    ],
    "unlock_requirements": {"level": 35}
}