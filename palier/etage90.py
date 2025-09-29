# -*- coding: utf-8 -*-

# Informations sur l'étage 90
FLOOR_90_INFO = {
    "name": "Floor 90 - Crimson Keep",
    "description": "Un étage dominé par un immense château aux murs rouges comme le sang. Le ciel y est perpétuellement teinté de rouge et des éclairs cramoisis zèbrent l'horizon.",
    "boss": {
        "name": "The Crimson King",
        "level": 95,
        "hp": 12000,
        "attack": 130,
        "defense": 120,
        "exp": 6000,
        "col": 30000,
        "drops": {"Crimson Crown": 1.0, "Bloodthirst Blade": 0.3},
        "description": "Un roi déchu dont l'âme a été corrompue par la soif de pouvoir. Il manie une épée qui absorbe la vie de ses victimes et peut invoquer des vagues de flammes écarlates.",
        "required_level": 90,
        "min_party_size": 10
    },
    "safe_zones": ["Crimson Village", "Sanctuary of Light", "Mercenary Camp"],
    "danger_level": 9,
    "recommended_level": 85,
    "biomes": [
        {
            "name": "Bloodstained Fields",
            "description": "Des plaines où l'herbe est teintée de rouge et où des guerriers maudits errent sans fin, à la recherche de nouveaux adversaires.",
            "monsters": ["Blood Knight", "Crimson Reaper"],
            "quests": ["q85", "q86"],
            "level_range": [85, 88],
            "unlock_requirements": None
        },
        {
            "name": "Burning Forest",
            "description": "Une forêt en flammes éternelles, où des créatures de feu et des esprits tourmentés attaquent les intrus.",
            "monsters": ["Flame Elemental", "Burning Wraith"],
            "quests": ["q87", "q88"],
            "level_range": [88, 92],
            "unlock_requirements": {"level": 87}
        },
        {
            "name": "Crimson Throne Room",
            "description": "La salle du trône au cœur du château écarlate, où le Roi Cramoisi attend les aventuriers assez courageux pour le défier.",
            "monsters": ["Royal Guard", "Blood Mage"],
            "quests": ["q89", "q90"],
            "level_range": [92, 95],
            "unlock_requirements": {"level": 90, "quest_completed": "q88"}
        }
    ],
    "unlock_requirements": {"level": 85}
}