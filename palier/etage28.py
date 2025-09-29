# -*- coding: utf-8 -*-

# Informations sur l'étage 28
FLOOR_28_INFO = {
    "name": "Floor 28 - Wolfswood",
    "description": "Un étage couvert de forêts denses où vivent d'innombrables meutes de loups. La ville principale, Wolfswood, est construite dans les arbres pour se protéger des prédateurs.",
    "boss": {
        "name": "Fenrir the Alpha King",
        "level": 56,
        "hp": 3600,
        "attack": 71,
        "defense": 66,
        "exp": 1800,
        "col": 9500,
        "drops": {"Alpha's Fang": 1.0, "Wolfpelt Armor": 0.3},
        "description": "Un loup gigantesque à la fourrure noire comme la nuit, chef de toutes les meutes de l'étage. Il peut appeler ses subordonnés et coordonner des attaques de groupe dévastatrices.",
        "required_level": 51,
        "min_party_size": 6
    },
    "safe_zones": ["Wolfswood", "Hunter's Lodge", "Treetop Haven"],
    "danger_level": 6,
    "recommended_level": 46,
    "biomes": [
        {
            "name": "Outer Woods",
            "description": "La lisière de la forêt, où les arbres sont moins denses et où chassent les loups solitaires et d'autres prédateurs.",
            "monsters": ["Lone Wolf", "Forest Hunter"],
            "quests": ["q211", "q212"],
            "level_range": [46, 49],
            "unlock_requirements": None
        },
        {
            "name": "Pack Territories",
            "description": "Le cœur de la forêt divisé en territoires appartenant à différentes meutes de loups, chacune défendant férocement son domaine.",
            "monsters": ["Wolf Pack Hunter", "Dire Wolf"],
            "quests": ["q213", "q214"],
            "level_range": [49, 53],
            "unlock_requirements": {"level": 48}
        },
        {
            "name": "Alpha's Den",
            "description": "Une clairière sacrée au plus profond de la forêt, où le roi alpha a établi son repaire et où se rassemblent toutes les meutes lors de la pleine lune.",
            "monsters": ["Elite Wolf Guard", "Shadow Wolf"],
            "quests": ["q215", "q216"],
            "level_range": [53, 56],
            "unlock_requirements": {"level": 52, "quest_completed": "q214"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Glacius the Frost Monarch"}
}