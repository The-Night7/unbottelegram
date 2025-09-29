# -*- coding: utf-8 -*-

# Informations sur l'étage 94
FLOOR_94_INFO = {
    "name": "Floor 94 - Atlantis",
    "description": "Un étage majoritairement submergé, avec des cités sous-marines et des dômes de cristal. La ville principale, Atlantis, est une métropole sous-marine d'une technologie avancée.",
    "boss": {
        "name": "Poseidon the Ocean Emperor",
        "level": 99,
        "hp": 12800,
        "attack": 138,
        "defense": 128,
        "exp": 6400,
        "col": 32000,
        "drops": {"Trident of the Seas": 1.0, "Ocean's Heart": 0.3},
        "description": "L'empereur des océans qui règne sur toutes les créatures marines. Il peut créer des tsunamis, contrôler l'eau sous toutes ses formes et appeler à l'aide les monstres marins les plus puissants.",
        "required_level": 94,
        "min_party_size": 10
    },
    "safe_zones": ["Atlantis", "Coral Haven", "Pressure Dome"],
    "danger_level": 10,
    "recommended_level": 89,
    "biomes": [
        {
            "name": "Sunken City",
            "description": "Les ruines d'une ancienne civilisation engloutie par les flots, où des technologies oubliées sont gardées par des constructions mécaniques sous-marines.",
            "monsters": ["Mechanical Guardian", "Deep Dweller"],
            "quests": ["q565", "q566"],
            "level_range": [89, 92],
            "unlock_requirements": None
        },
        {
            "name": "Abyssal Trench",
            "description": "Les profondeurs obscures de l'océan où la pression est écrasante et où des créatures cauchemardesques rôdent dans l'obscurité.",
            "monsters": ["Abyssal Horror", "Pressure Beast"],
            "quests": ["q567", "q568"],
            "level_range": [92, 96],
            "unlock_requirements": {"level": 91}
        },
        {
            "name": "Emperor's Palace",
            "description": "Le palais sous-marin de l'Empereur des Océans, fait de corail et de nacre, où il siège sur un trône de perles entouré de sa cour marine.",
            "monsters": ["Royal Guard", "Sea Serpent"],
            "quests": ["q569", "q570"],
            "level_range": [96, 99],
            "unlock_requirements": {"level": 95, "quest_completed": "q568"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Odin the All-Father"}
}