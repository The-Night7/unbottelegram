# -*- coding: utf-8 -*-

# Informations sur l'étage 9
FLOOR_9_INFO = {
    "name": "Floor 9 - Blackiron Forge",
    "description": "Un étage volcanique parsemé de rivières de lave et de montagnes fumantes. La ville principale, Blackiron Forge, est célèbre pour ses forgerons qui travaillent le métal rare extrait des volcans.",
    "boss": {
        "name": "Vulcanus the Molten Giant",
        "level": 48,
        "hp": 2600,
        "attack": 63,
        "defense": 58,
        "exp": 1400,
        "col": 7000,
        "drops": {"Molten Core": 1.0, "Vulcan Hammer": 0.3},
        "description": "Un géant de lave et de roche en fusion qui forge des armes dans son propre corps. Il peut projeter de la lave et créer des serviteurs de feu.",
        "required_level": 43,
        "min_party_size": 5
    },
    "safe_zones": ["Blackiron Forge", "Obsidian Haven", "Cooling Springs"],
    "danger_level": 5,
    "recommended_level": 38,
    "biomes": [
        {
            "name": "Smoldering Fields",
            "description": "Des plaines couvertes de cendres et de fumerolles, où la terre est chaude et où vivent des créatures résistantes à la chaleur.",
            "monsters": ["Ash Crawler", "Ember Wolf"],
            "quests": ["q115", "q116"],
            "level_range": [38, 41],
            "unlock_requirements": None
        },
        {
            "name": "Lava Rivers",
            "description": "Un réseau de rivières de lave qui parcourent l'étage, habité par des créatures de feu et des salamandres géantes.",
            "monsters": ["Lava Elemental", "Magma Serpent"],
            "quests": ["q117", "q118"],
            "level_range": [41, 44],
            "unlock_requirements": {"level": 40}
        },
        {
            "name": "Vulcan's Anvil",
            "description": "Le cœur d'un volcan actif où se trouve la forge du boss et ses serviteurs de feu.",
            "monsters": ["Fire Golem", "Flame Knight"],
            "quests": ["q119", "q120"],
            "level_range": [44, 48],
            "unlock_requirements": {"level": 43, "quest_completed": "q118"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Zelgius the Corrupted Archdruid"}
}