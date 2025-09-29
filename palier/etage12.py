# -*- coding: utf-8 -*-

# Informations sur l'étage 12
FLOOR_12_INFO = {
    "name": "Floor 12 - Polaris",
    "description": "Un étage où règne une nuit perpétuelle, illuminé seulement par des aurores boréales et des constellations brillantes. La ville principale, Polaris, est construite autour d'un observatoire géant.",
    "boss": {
        "name": "Astraeus the Celestial Watcher",
        "level": 49,
        "hp": 3000,
        "attack": 68,
        "defense": 62,
        "exp": 1600,
        "col": 8000,
        "drops": {"Star Fragment": 1.0, "Celestial Staff": 0.3},
        "description": "Un être céleste composé d'étoiles et de constellations vivantes. Il peut invoquer des météorites et manipuler la gravité pour désorienter ses adversaires.",
        "required_level": 44,
        "min_party_size": 5
    },
    "safe_zones": ["Polaris", "Starlight Haven", "Moon Shrine"],
    "danger_level": 5,
    "recommended_level": 42,
    "biomes": [
        {
            "name": "Aurora Fields",
            "description": "Des plaines baignées par la lumière des aurores boréales, où des créatures nocturnes chassent dans l'obscurité.",
            "monsters": ["Night Stalker", "Aurora Fox"],
            "quests": ["q127", "q128"],
            "level_range": [42, 44],
            "unlock_requirements": None
        },
        {
            "name": "Constellation Forest",
            "description": "Une forêt où les arbres brillent comme des constellations, habitée par des êtres de lumière et d'ombre.",
            "monsters": ["Starlight Deer", "Shadow Hunter"],
            "quests": ["q129", "q130"],
            "level_range": [44, 47],
            "unlock_requirements": {"level": 43}
        },
        {
            "name": "Observatory Peak",
            "description": "Le sommet d'une montagne où se trouve un ancien observatoire, lieu de résidence du boss.",
            "monsters": ["Gravity Manipulator", "Cosmic Guardian"],
            "quests": ["q131", "q132"],
            "level_range": [47, 49],
            "unlock_requirements": {"level": 46, "quest_completed": "q130"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Bullbous the Stampede King"}
}