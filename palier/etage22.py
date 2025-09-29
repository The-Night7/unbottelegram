# -*- coding: utf-8 -*-

# Informations sur l'étage 22
FLOOR_22_INFO = {
    "name": "Floor 22 - Forest House",
    "description": "Un étage paisible avec des lacs et des forêts. C'est ici que Kirito et Asuna ont acheté leur maison.",
    "boss": {
        "name": "The Storm Griffin",
        "level": 45,
        "hp": 2500,
        "attack": 60,
        "defense": 50,
        "exp": 1200,
        "col": 6000,
        "drops": {"Griffin Feather": 1.0, "Storm Bow": 0.3},
        "description": "Un griffon majestueux qui contrôle les vents et peut créer des tempêtes dévastatrices.",
        "required_level": 40,
        "min_party_size": 4
    },
    "safe_zones": ["Coral Village", "Lake Shore", "Forest Cabin"],
    "danger_level": 4,
    "recommended_level": 35,
    "biomes": [
        {
            "name": "Peaceful Lake",
            "description": "Un grand lac entouré de collines verdoyantes où vivent des poissons géants et des créatures aquatiques.",
            "monsters": ["Lake Fish", "Water Sprite"],
            "quests": ["q19", "q20"],
            "level_range": [35, 38],
            "unlock_requirements": None
        },
        {
            "name": "Dense Woods",
            "description": "Une forêt dense où vivent des ours et d'autres créatures sauvages.",
            "monsters": ["Forest Bear", "Wild Boar Alpha"],
            "quests": ["q21", "q22"],
            "level_range": [38, 42],
            "unlock_requirements": {"level": 37}
        },
        {
            "name": "Cloudy Peaks",
            "description": "Les sommets des collines où les vents sont forts et où volent des créatures aériennes.",
            "monsters": ["Wind Rider", "Cloud Elemental"],
            "quests": ["q23", "q24"],
            "level_range": [42, 45],
            "unlock_requirements": {"level": 40, "quest_completed": "q22"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Previous Boss", "level": 35}
}