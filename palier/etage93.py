# -*- coding: utf-8 -*-

# Informations sur l'étage 93
FLOOR_93_INFO = {
    "name": "Floor 93 - Valhalla",
    "description": "Un étage inspiré des mythes nordiques, avec des montagnes enneigées et des salles d'hydromel. La ville principale, Valhalla, est une immense forteresse où les guerriers se préparent pour la bataille finale.",
    "boss": {
        "name": "Odin the All-Father",
        "level": 98,
        "hp": 12600,
        "attack": 136,
        "defense": 126,
        "exp": 6300,
        "col": 31500,
        "drops": {"Divine Rune": 1.0, "Gungnir Spear": 0.3},
        "description": "Le père de tous les dieux nordiques, accompagné de ses deux loups et de ses deux corbeaux. Il manie une lance légendaire qui ne manque jamais sa cible et peut invoquer la foudre et les tempêtes.",
        "required_level": 93,
        "min_party_size": 10
    },
    "safe_zones": ["Valhalla", "Mead Hall", "Warrior's Rest"],
    "danger_level": 10,
    "recommended_level": 88,
    "biomes": [
        {
            "name": "Frozen Tundra",
            "description": "Des plaines glacées balayées par des blizzards, où des guerriers fantômes chassent les créatures géantes et mettent à l'épreuve les aventuriers.",
            "monsters": ["Frost Giant", "Ghost Warrior"],
            "quests": ["q559", "q560"],
            "level_range": [88, 91],
            "unlock_requirements": None
        },
        {
            "name": "World Tree",
            "description": "Un arbre colossal qui semble toucher le ciel, dont les branches abritent diverses créatures mythiques et dont les racines plongent dans des sources de sagesse.",
            "monsters": ["Tree Guardian", "Mythical Beast"],
            "quests": ["q561", "q562"],
            "level_range": [91, 95],
            "unlock_requirements": {"level": 90}
        },
        {
            "name": "Asgard",
            "description": "Le royaume des dieux, un palais majestueux où le Père de Toutes Choses siège sur son trône, entouré de ses plus fidèles guerriers.",
            "monsters": ["Valkyrie", "Divine Einherjar"],
            "quests": ["q563", "q564"],
            "level_range": [95, 98],
            "unlock_requirements": {"level": 94, "quest_completed": "q562"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Infernus the Hellfire King"}
}