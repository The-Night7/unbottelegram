# -*- coding: utf-8 -*-

# Informations sur l'étage 5
FLOOR_5_INFO = {
    "name": "Floor 5 - Karluin",
    "description": "Un étage montagneux avec des falaises escarpées et des vallées profondes. La ville principale, Karluin, est construite à flanc de montagne.",
    "boss": {
        "name": "Fuscus the Vacant Colossus",
        "level": 40,
        "hp": 1800,
        "attack": 50,
        "defense": 45,
        "exp": 1000,
        "col": 5000,
        "drops": {"Stone Heart": 1.0, "Mountain Crusher": 0.3},
        "description": "Un golem de pierre colossal qui peut faire trembler le sol et provoquer des éboulements. Sa peau de pierre le rend très résistant aux attaques physiques.",
        "required_level": 35,
        "min_party_size": 4
    },
    "safe_zones": ["Karluin", "Mountain Refuge", "Miner's Camp"],
    "danger_level": 4,
    "recommended_level": 30,
    "biomes": [
        {
            "name": "Mountain Path",
            "description": "Des sentiers sinueux qui serpentent à travers les montagnes, où des créatures volantes guettent les voyageurs.",
            "monsters": ["Mountain Hawk", "Cliff Jumper"],
            "quests": ["q49", "q50"],
            "level_range": [30, 33],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Caves",
            "description": "Un réseau de grottes illuminées par des cristaux lumineux, habitées par des créatures cavernicoles.",
            "monsters": ["Cave Crawler", "Crystal Elemental"],
            "quests": ["q51", "q52"],
            "level_range": [33, 36],
            "unlock_requirements": {"level": 32}
        },
        {
            "name": "Stone Colosseum",
            "description": "Une ancienne arène taillée dans la montagne, où réside le boss et ses serviteurs de pierre.",
            "monsters": ["Stone Guardian", "Rock Beast"],
            "quests": ["q53", "q54"],
            "level_range": [36, 40],
            "unlock_requirements": {"level": 35, "quest_completed": "q52"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Wythege the Hippocampus"}
}