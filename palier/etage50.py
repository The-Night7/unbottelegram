# -*- coding: utf-8 -*-

# Informations sur l'étage 50
FLOOR_50_INFO = {
    "name": "Floor 50 - Algade",
    "description": "Un étage urbain avec la plus grande ville d'Aincrad, Algade. C'est une métropole animée avec de nombreux commerces.",
    "boss": {
        "name": "The Emperor of Darkness",
        "level": 65,
        "hp": 5000,
        "attack": 80,
        "defense": 70,
        "exp": 2500,
        "col": 10000,
        "drops": {"Emperor's Crown": 1.0, "Darkness Blade": 0.3},
        "description": "Un empereur déchu qui contrôle les ombres et peut invoquer des serviteurs des ténèbres.",
        "required_level": 60,
        "min_party_size": 6
    },
    "safe_zones": ["Algade", "Merchant District", "Residential Area"],
    "danger_level": 6,
    "recommended_level": 55,
    "biomes": [
        {
            "name": "City Outskirts",
            "description": "Les faubourgs d'Algade, où des bandits et des créatures des ténèbres rôdent.",
            "monsters": ["Shadow Knight", "Bandit Rogue"],
            "quests": ["q25", "q26"],
            "level_range": [55, 58],
            "unlock_requirements": None
        },
        {
            "name": "Underground Sewers",
            "description": "Un réseau de tunnels sous la ville, infesté de créatures sombres et de rats géants.",
            "monsters": ["Dark Dweller", "Plague Rat"],
            "quests": ["q27", "q28"],
            "level_range": [58, 62],
            "unlock_requirements": {"level": 57, "quest_completed": "q26"}
        },
        {
            "name": "Ancient Ruins",
            "description": "Des ruines antiques sous la ville, gardées par des élémentaires et menant au repaire du boss.",
            "monsters": ["Granite Elemental", "Ruin Guardian"],
            "quests": ["q29", "q30"],
            "level_range": [62, 65],
            "unlock_requirements": {"level": 60, "quest_completed": "q28"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Previous Boss", "level": 55}
}