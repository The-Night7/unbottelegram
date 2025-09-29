# -*- coding: utf-8 -*-

# Informations sur l'étage 19
FLOOR_19_INFO = {
    "name": "Floor 19 - Ralback",
    "description": "Un étage dominé par des montagnes escarpées et des canyons profonds. La ville principale, Ralback, est construite à flanc de falaise avec des bâtiments taillés directement dans la roche.",
    "boss": {
        "name": "Terravore the Mountain Eater",
        "level": 63,
        "hp": 4400,
        "attack": 85,
        "defense": 80,
        "exp": 2300,
        "col": 11500,
        "drops": {"Earth Core": 1.0, "Mountain Splitter": 0.3},
        "description": "Un ver titanesque qui peut creuser à travers la roche solide et provoquer des tremblements de terre. Sa carapace est presque impénétrable et sa gueule peut broyer même les métaux les plus durs.",
        "required_level": 58,
        "min_party_size": 7
    },
    "safe_zones": ["Ralback", "Miner's Rest", "Eagle's Nest"],
    "danger_level": 7,
    "recommended_level": 56,
    "biomes": [
        {
            "name": "Rugged Highlands",
            "description": "Des plateaux rocheux balayés par des vents violents, où des créatures robustes ont élu domicile et où des ressources précieuses peuvent être trouvées.",
            "monsters": ["Highland Troll", "Mountain Eagle"],
            "quests": ["q169", "q170"],
            "level_range": [56, 58],
            "unlock_requirements": None
        },
        {
            "name": "Winding Canyons",
            "description": "Un labyrinthe de canyons étroits où l'écho peut attirer des prédateurs, et où des bandits ont établi leurs repaires.",
            "monsters": ["Canyon Stalker", "Rock Bandit"],
            "quests": ["q171", "q172"],
            "level_range": [58, 61],
            "unlock_requirements": {"level": 57}
        },
        {
            "name": "Trembling Depths",
            "description": "Les profondeurs de la montagne où le boss a creusé son repaire, un réseau de tunnels instables qui peuvent s'effondrer à tout moment.",
            "monsters": ["Earth Elemental", "Tunnel Crusher"],
            "quests": ["q173", "q174"],
            "level_range": [61, 63],
            "unlock_requirements": {"level": 60, "quest_completed": "q172"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Prismatica the Crystal Queen"}
}