# -*- coding: utf-8 -*-

# Informations sur l'étage 16
FLOOR_16_INFO = {
    "name": "Floor 16 - Antique",
    "description": "Un étage qui abrite les ruines d'une ancienne civilisation. La ville principale, Antique, est construite au milieu des vestiges d'une cité autrefois grandiose.",
    "boss": {
        "name": "Archaeos the Ancient Guardian",
        "level": 57,
        "hp": 3800,
        "attack": 78,
        "defense": 72,
        "exp": 2000,
        "col": 10000,
        "drops": {"Ancient Artifact": 1.0, "Guardian's Halberd": 0.3},
        "description": "Une statue colossale animée par une magie ancienne. Il peut invoquer des armes enchantées et des gardiens plus petits pour le protéger.",
        "required_level": 52,
        "min_party_size": 6
    },
    "safe_zones": ["Antique", "Scholar's Camp", "Restoration Site"],
    "danger_level": 6,
    "recommended_level": 50,
    "biomes": [
        {
            "name": "Fallen City",
            "description": "Les ruines d'une vaste cité aux bâtiments effondrés et aux rues envahies par la végétation, où des créatures ont fait leur repaire.",
            "monsters": ["Ruin Dweller", "Stone Golem"],
            "quests": ["q151", "q152"],
            "level_range": [50, 52],
            "unlock_requirements": None
        },
        {
            "name": "Ancient Library",
            "description": "Une bibliothèque gigantesque partiellement préservée, gardée par des constructions magiques et des pièges.",
            "monsters": ["Animated Book", "Knowledge Guardian"],
            "quests": ["q153", "q154"],
            "level_range": [52, 55],
            "unlock_requirements": {"level": 51}
        },
        {
            "name": "Temple of Ages",
            "description": "Un temple majestueux au centre des ruines, où le temps semble s'écouler différemment et où réside le boss.",
            "monsters": ["Timeless Sentinel", "Chrono Wraith"],
            "quests": ["q155", "q156"],
            "level_range": [55, 57],
            "unlock_requirements": {"level": 54, "quest_completed": "q154"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Skyripper the Cloud Dragon"}
}