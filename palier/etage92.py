# -*- coding: utf-8 -*-

# Informations sur l'étage 92
FLOOR_92_INFO = {
    "name": "Floor 92 - Tartarus",
    "description": "Un étage infernal avec des plaines de cendres et des rivières de feu. La ville principale, Tartarus, est construite dans une forteresse de métal noir qui résiste à la chaleur extrême.",
    "boss": {
        "name": "Infernus the Hellfire King",
        "level": 97,
        "hp": 12400,
        "attack": 134,
        "defense": 124,
        "exp": 6200,
        "col": 31000,
        "drops": {"Eternal Flame": 1.0, "Hellforged Blade": 0.3},
        "description": "Le souverain des flammes infernales, dont le corps est partiellement composé de feu vivant. Il peut créer des explosions dévastatrices, invoquer des piliers de feu et augmenter la température jusqu'à faire fondre les armes et armures.",
        "required_level": 92,
        "min_party_size": 10
    },
    "safe_zones": ["Tartarus", "Cooling Haven", "Ashen Refuge"],
    "danger_level": 10,
    "recommended_level": 87,
    "biomes": [
        {
            "name": "Ashen Wastes",
            "description": "Des plaines couvertes de cendres où rien ne pousse et où des vents brûlants transportent des particules incandescentes, habitées par des créatures de feu.",
            "monsters": ["Ash Elemental", "Fire Beast"],
            "quests": ["q553", "q554"],
            "level_range": [87, 90],
            "unlock_requirements": None
        },
        {
            "name": "Rivers of Fire",
            "description": "Un réseau de rivières de lave en fusion qui traversent l'étage, bordées de formations rocheuses où nichent des créatures résistantes à la chaleur extrême.",
            "monsters": ["Lava Elemental", "Magma Drake"],
            "quests": ["q555", "q556"],
            "level_range": [90, 94],
            "unlock_requirements": {"level": 89}
        },
        {
            "name": "King's Furnace",
            "description": "Le cœur ardent de l'étage, où la température est si élevée que seules les créatures les plus résistantes peuvent survivre, et où le Roi du Feu Infernal attend les aventuriers.",
            "monsters": ["Flame Knight", "Infernal Beast"],
            "quests": ["q557", "q558"],
            "level_range": [94, 97],
            "unlock_requirements": {"level": 93, "quest_completed": "q556"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Elysium the Divine Guardian"}
}