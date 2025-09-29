# -*- coding: utf-8 -*-

# Informations sur l'étage 46
FLOOR_46_INFO = {
    "name": "Floor 46 - Aquaria",
    "description": "Un étage majoritairement submergé, avec des îles flottantes et des dômes sous-marins. La ville principale, Aquaria, est construite dans un gigantesque dôme transparent au fond de l'océan.",
    "boss": {
        "name": "Abyssus the Deep One",
        "level": 72,
        "hp": 5200,
        "attack": 87,
        "defense": 77,
        "exp": 2600,
        "col": 12000,
        "drops": {"Abyssal Pearl": 1.0, "Trident of the Depths": 0.3},
        "description": "Un seigneur des abysses mi-homme mi-poisson qui règne sur les profondeurs. Il peut contrôler l'eau, créer des tourbillons et invoquer des créatures marines.",
        "required_level": 67,
        "min_party_size": 6
    },
    "safe_zones": ["Aquaria", "Coral Haven", "Surface Outpost"],
    "danger_level": 7,
    "recommended_level": 62,
    "biomes": [
        {
            "name": "Floating Islands",
            "description": "Des îles qui flottent à la surface de l'océan, reliées par des ponts suspendus et habitées par des créatures volantes et marines.",
            "monsters": ["Sea Bird", "Beach Predator"],
            "quests": ["q313", "q314"],
            "level_range": [62, 65],
            "unlock_requirements": None
        },
        {
            "name": "Coral Reefs",
            "description": "Des récifs coralliens colorés où vivent d'innombrables créatures marines et où sont cachés des trésors engloutis.",
            "monsters": ["Reef Guardian", "Electric Eel"],
            "quests": ["q315", "q316"],
            "level_range": [65, 69],
            "unlock_requirements": {"level": 64}
        },
        {
            "name": "Abyssal Trench",
            "description": "Les profondeurs obscures de l'océan où la pression est écrasante et où des créatures cauchemardesques rôdent dans l'obscurité.",
            "monsters": ["Deep One", "Angler Beast"],
            "quests": ["q317", "q318"],
            "level_range": [69, 72],
            "unlock_requirements": {"level": 68, "quest_completed": "q316"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Ferrum the Iron Colossus"}
}