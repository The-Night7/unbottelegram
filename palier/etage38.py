# -*- coding: utf-8 -*-

# Informations sur l'étage 38
FLOOR_38_INFO = {
    "name": "Floor 38 - Crestfall",
    "description": "Un étage montagneux avec des falaises abruptes et des vallées profondes. La ville principale, Crestfall, est construite à flanc de montagne avec des bâtiments en terrasses.",
    "boss": {
        "name": "Avalanche the Mountain King",
        "level": 75,
        "hp": 5600,
        "attack": 91,
        "defense": 86,
        "exp": 2800,
        "col": 14500,
        "drops": {"Mountain's Heart": 1.0, "Earthshaker Hammer": 0.3},
        "description": "Un géant de pierre vivante qui peut provoquer des tremblements de terre et des avalanches. Sa peau de roche est extrêmement résistante et il peut absorber les minéraux du sol pour se renforcer.",
        "required_level": 70,
        "min_party_size": 8
    },
    "safe_zones": ["Crestfall", "Miner's Refuge", "Summit Camp"],
    "danger_level": 8,
    "recommended_level": 66,
    "biomes": [
        {
            "name": "Jagged Peaks",
            "description": "Des montagnes aux sommets acérés où nichent des créatures volantes et où le vent souffle avec violence.",
            "monsters": ["Mountain Roc", "Wind Elemental"],
            "quests": ["q271", "q272"],
            "level_range": [66, 69],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Mines",
            "description": "Des mines profondes où sont extraits des cristaux magiques, habitées par des golems et des créatures souterraines.",
            "monsters": ["Crystal Golem", "Cave Troll"],
            "quests": ["q273", "q274"],
            "level_range": [69, 72],
            "unlock_requirements": {"level": 68}
        },
        {
            "name": "Stone Throne",
            "description": "Le sommet de la plus haute montagne, où le Roi des Montagnes a établi son domaine et attend les aventuriers.",
            "monsters": ["Rock Guardian", "Avalanche Beast"],
            "quests": ["q275", "q276"],
            "level_range": [72, 75],
            "unlock_requirements": {"level": 71, "quest_completed": "q274"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Viridis the Garden Keeper"}
}