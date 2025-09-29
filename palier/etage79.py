# -*- coding: utf-8 -*-

# Informations sur l'étage 79
FLOOR_79_INFO = {
    "name": "Floor 79 - Elemental Nexus",
    "description": "Un étage divisé en quatre régions distinctes représentant les quatre éléments primaires. La ville principale, Elemental Nexus, est située au centre exact où les quatre éléments se rencontrent en harmonie.",
    "boss": {
        "name": "Primordius the Elemental Lord",
        "level": 94,
        "hp": 10800,
        "attack": 128,
        "defense": 108,
        "exp": 5400,
        "col": 27000,
        "drops": {"Elemental Core": 1.0, "Primal Staff": 0.3},
        "description": "Un être primordial qui maîtrise les quatre éléments fondamentaux. Il peut changer sa forme et ses attaques pour adopter les propriétés de n'importe quel élément, exploitant les faiblesses de ses adversaires.",
        "required_level": 89,
        "min_party_size": 10
    },
    "safe_zones": ["Elemental Nexus", "Harmony Point", "Balance Temple"],
    "danger_level": 10,
    "recommended_level": 84,
    "biomes": [
        {
            "name": "Quadrant of Elements",
            "description": "Une zone divisée en quatre sections distinctes : terres de feu, océans profonds, montagnes de pierre et cieux venteux, chacune habitée par des créatures élémentaires.",
            "monsters": ["Fire Elemental", "Water Sprite"],
            "quests": ["q481", "q482"],
            "level_range": [84, 87],
            "unlock_requirements": None
        },
        {
            "name": "Elemental Chaos",
            "description": "Une région où les quatre éléments se mélangent de façon chaotique, créant des phénomènes dangereux comme des tempêtes de feu ou des avalanches liquides.",
            "monsters": ["Chaos Elemental", "Fusion Beast"],
            "quests": ["q483", "q484"],
            "level_range": [87, 91],
            "unlock_requirements": {"level": 86}
        },
        {
            "name": "Primal Sanctum",
            "description": "Le temple au centre de l'étage où le Seigneur Élémentaire attend les aventuriers, entouré de quatre gardiens représentant chacun un élément pur.",
            "monsters": ["Elemental Guardian", "Primal Servant"],
            "quests": ["q485", "q486"],
            "level_range": [91, 94],
            "unlock_requirements": {"level": 90, "quest_completed": "q484"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Aeternalis the Timeless"}
}