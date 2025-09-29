# -*- coding: utf-8 -*-

# Informations sur l'étage 95
FLOOR_95_INFO = {
    "name": "Floor 95 - Celestial Realm",
    "description": "Un étage situé parmi les étoiles, avec des îles flottantes reliées par des ponts de lumière. La ville principale, Celestial Realm, est construite sur la plus grande des îles et semble faite de lumière solidifiée.",
    "boss": {
        "name": "Astraeus the Star Lord",
        "level": 100,
        "hp": 13000,
        "attack": 140,
        "defense": 130,
        "exp": 6500,
        "col": 32500,
        "drops": {"Star Fragment": 1.0, "Celestial Bow": 0.3},
        "description": "Le seigneur des étoiles dont le corps est parsemé de constellations. Il peut invoquer des météores, manipuler la gravité et créer des trous noirs miniatures qui aspirent tout ce qui les entoure.",
        "required_level": 95,
        "min_party_size": 10
    },
    "safe_zones": ["Celestial Realm", "Starlight Haven", "Cosmic Sanctuary"],
    "danger_level": 10,
    "recommended_level": 90,
    "biomes": [
        {
            "name": "Astral Islands",
            "description": "Des îles flottantes dans un océan d'étoiles, où la gravité est plus faible et où des créatures célestes se déplacent avec grâce.",
            "monsters": ["Star Elemental", "Cosmic Beast"],
            "quests": ["q571", "q572"],
            "level_range": [90, 93],
            "unlock_requirements": None
        },
        {
            "name": "Constellation Paths",
            "description": "Des chemins formés par des constellations vivantes qui relient les îles entre elles, gardés par des entités stellaires et des gardiens de lumière.",
            "monsters": ["Constellation Guardian", "Light Weaver"],
            "quests": ["q573", "q574"],
            "level_range": [93, 97],
            "unlock_requirements": {"level": 92}
        },
        {
            "name": "Cosmic Throne",
            "description": "Le centre de l'étage, où les étoiles sont si denses qu'elles forment un palais de lumière pure, et où le Seigneur des Étoiles attend les aventuriers.",
            "monsters": ["Stellar Knight", "Nova Entity"],
            "quests": ["q575", "q576"],
            "level_range": [97, 100],
            "unlock_requirements": {"level": 96, "quest_completed": "q574"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Poseidon the Ocean Emperor"}
}