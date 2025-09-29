# -*- coding: utf-8 -*-

# Informations sur l'étage 88
FLOOR_88_INFO = {
    "name": "Floor 88 - Draconia",
    "description": "Un étage dominé par des montagnes volcaniques et des vallées brûlées, où règnent les dragons. La ville principale, Draconia, est construite dans une immense caverne à l'abri des créatures volantes.",
    "boss": {
        "name": "Draconius the Dragon Emperor",
        "level": 103,
        "hp": 12600,
        "attack": 146,
        "defense": 126,
        "exp": 6300,
        "col": 31500,
        "drops": {"Dragon Heart": 1.0, "Emperor's Talon": 0.3},
        "description": "Le plus puissant des dragons, capable de maîtriser tous les types de souffle draconique. Ses écailles sont pratiquement impénétrables et il peut voler à une vitesse incroyable malgré sa taille colossale.",
        "required_level": 98,
        "min_party_size": 10
    },
    "safe_zones": ["Draconia", "Hunter's Refuge", "Scale Shield"],
    "danger_level": 10,
    "recommended_level": 93,
    "biomes": [
        {
            "name": "Dragon's Valley",
            "description": "Une vallée où nichent différentes espèces de dragons, des plus petits aux plus imposants, et où le sol est jonché d'os de leurs proies.",
            "monsters": ["Young Drake", "Wyvern Hunter"],
            "quests": ["q535", "q536"],
            "level_range": [93, 96],
            "unlock_requirements": None
        },
        {
            "name": "Burning Mountains",
            "description": "Des montagnes volcaniques où la chaleur est presque insupportable, habitées par des dragons de feu et d'autres créatures résistantes aux températures extrêmes.",
            "monsters": ["Fire Dragon", "Lava Drake"],
            "quests": ["q537", "q538"],
            "level_range": [96, 100],
            "unlock_requirements": {"level": 95}
        },
        {
            "name": "Imperial Nest",
            "description": "L'immense nid de l'Empereur Dragon, situé au sommet du plus haut volcan, entouré de ses serviteurs les plus puissants et de son trésor accumulé.",
            "monsters": ["Dragon Knight", "Elder Wyrm"],
            "quests": ["q539", "q540"],
            "level_range": [100, 103],
            "unlock_requirements": {"level": 99, "quest_completed": "q538"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Discordia the Chaos Bringer"}
}