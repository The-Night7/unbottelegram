# -*- coding: utf-8 -*-

# Informations sur l'étage 48
FLOOR_48_INFO = {
    "name": "Floor 48 - Lindas",
    "description": "Un étage dominé par des canyons profonds et des formations rocheuses spectaculaires. La ville principale, Lindas, est construite dans une falaise et connue pour ses forgerons d'élite.",
    "boss": {
        "name": "Petra the Stone Sovereign",
        "level": 75,
        "hp": 5600,
        "attack": 91,
        "defense": 81,
        "exp": 2800,
        "col": 13000,
        "drops": {"Perfect Gemstone": 1.0, "Earthbreaker Maul": 0.3},
        "description": "Un géant de pierre vivante dont le corps est incrusté de gemmes précieuses. Il peut provoquer des tremblements de terre, lancer des projectiles rocheux et se fondre dans la pierre.",
        "required_level": 70,
        "min_party_size": 7
    },
    "safe_zones": ["Lindas", "Canyon Rest", "Gem Haven"],
    "danger_level": 8,
    "recommended_level": 66,
    "biomes": [
        {
            "name": "Winding Canyons",
            "description": "Des canyons étroits aux parois abruptes où l'écho peut attirer des prédateurs, et où des bandits ont établi leurs repaires.",
            "monsters": ["Canyon Stalker", "Rock Bandit"],
            "quests": ["q325", "q326"],
            "level_range": [66, 69],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Caverns",
            "description": "Des grottes dont les parois sont incrustées de cristaux lumineux et de gemmes précieuses, gardées par des golems et des élémentaires.",
            "monsters": ["Crystal Golem", "Gem Elemental"],
            "quests": ["q327", "q328"],
            "level_range": [69, 72],
            "unlock_requirements": {"level": 68}
        },
        {
            "name": "Stone Throne",
            "description": "Un amphithéâtre naturel au centre d'un cercle de monolithes, où le souverain de pierre attend les aventuriers sur son trône de gemmes.",
            "monsters": ["Rock Guardian", "Gemstone Mage"],
            "quests": ["q329", "q330"],
            "level_range": [72, 75],
            "unlock_requirements": {"level": 71, "quest_completed": "q328"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Anthea the Bloom Queen"}
}