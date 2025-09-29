# -*- coding: utf-8 -*-

# Informations sur l'étage 73
FLOOR_73_INFO = {
    "name": "Floor 73 - Inferno",
    "description": "Un étage infernal avec des rivières de lave et des montagnes en éruption constante. La ville principale, Inferno, est construite dans une caverne protégée par des barrières magiques résistantes à la chaleur.",
    "boss": {
        "name": "Ignis the Flame Emperor",
        "level": 93,
        "hp": 9400,
        "attack": 116,
        "defense": 106,
        "exp": 4700,
        "col": 21000,
        "drops": {"Emperor's Flame": 1.0, "Infernal Greatsword": 0.3},
        "description": "L'empereur absolu du feu, dont le corps est partiellement composé de flammes vivantes. Il peut créer des explosions dévastatrices, invoquer des serviteurs de feu et augmenter la température environnante jusqu'à des niveaux insupportables.",
        "required_level": 88,
        "min_party_size": 9
    },
    "safe_zones": ["Inferno", "Cooling Cavern", "Ashen Refuge"],
    "danger_level": 9,
    "recommended_level": 85,
    "biomes": [
        {
            "name": "Burning Plains",
            "description": "Des plaines où le sol est brûlant et où des geysers de lave surgissent sans prévenir, habitées par des créatures résistantes à la chaleur extrême.",
            "monsters": ["Lava Elemental", "Flame Beast"],
            "quests": ["q457", "q458"],
            "level_range": [85, 88],
            "unlock_requirements": None
        },
        {
            "name": "Volcanic Mountains",
            "description": "Des montagnes en éruption constante, où coulent des rivières de lave et où vivent des dragons de feu et d'autres créatures puissantes.",
            "monsters": ["Fire Drake", "Magma Giant"],
            "quests": ["q459", "q460"],
            "level_range": [88, 91],
            "unlock_requirements": {"level": 87}
        },
        {
            "name": "Emperor's Forge",
            "description": "Une forge colossale au cœur d'un volcan actif, où l'Empereur des Flammes forge ses armes et attend les aventuriers dans un océan de feu.",
            "monsters": ["Flame Knight", "Infernal Smith"],
            "quests": ["q461", "q462"],
            "level_range": [91, 93],
            "unlock_requirements": {"level": 90, "quest_completed": "q460"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Boreas the Winter Monarch"}
}