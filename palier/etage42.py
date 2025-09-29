# -*- coding: utf-8 -*-

# Informations sur l'étage 42
FLOOR_42_INFO = {
    "name": "Floor 42 - Vulcania",
    "description": "Un étage volcanique avec des rivières de lave et des geysers de vapeur brûlante. La ville principale, Vulcania, est construite dans le cratère d'un volcan éteint.",
    "boss": {
        "name": "Igneus the Flame Tyrant",
        "level": 64,
        "hp": 4400,
        "attack": 79,
        "defense": 69,
        "exp": 2200,
        "col": 10000,
        "drops": {"Molten Core": 1.0, "Inferno Blade": 0.3},
        "description": "Un démon de feu colossal dont le corps est partiellement composé de lave en fusion. Il peut projeter des flammes, créer des explosions et faire surgir des geysers de lave du sol.",
        "required_level": 59,
        "min_party_size": 6
    },
    "safe_zones": ["Vulcania", "Ashen Refuge", "Cooling Springs"],
    "danger_level": 7,
    "recommended_level": 54,
    "biomes": [
        {
            "name": "Lava Fields",
            "description": "Des plaines où coulent des rivières de lave et où le sol est constamment secoué par des tremblements de terre mineurs.",
            "monsters": ["Lava Elemental", "Ash Walker"],
            "quests": ["q289", "q290"],
            "level_range": [54, 57],
            "unlock_requirements": None
        },
        {
            "name": "Obsidian Mines",
            "description": "Des mines profondes où l'on extrait de l'obsidienne et d'autres matériaux volcaniques précieux, habitées par des créatures résistantes à la chaleur.",
            "monsters": ["Magma Golem", "Fire Salamander"],
            "quests": ["q291", "q292"],
            "level_range": [57, 61],
            "unlock_requirements": {"level": 56}
        },
        {
            "name": "Tyrant's Caldera",
            "description": "Le cœur d'un volcan actif où la température est si élevée que seules les créatures les plus résistantes peuvent survivre, et où le boss a établi son domaine.",
            "monsters": ["Flame Knight", "Ember Drake"],
            "quests": ["q293", "q294"],
            "level_range": [61, 64],
            "unlock_requirements": {"level": 60, "quest_completed": "q292"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Sylvanus the Ancient"}
}