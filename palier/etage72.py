# -*- coding: utf-8 -*-

# Informations sur l'étage 72
FLOOR_72_INFO = {
    "name": "Floor 72 - Glacialis",
    "description": "Un étage entièrement gelé, avec des montagnes de glace éternelle et des palais de cristal. La ville principale, Glacialis, est taillée dans un glacier millénaire et protégée des blizzards par des barrières magiques.",
    "boss": {
        "name": "Boreas the Winter Monarch",
        "level": 92,
        "hp": 9200,
        "attack": 114,
        "defense": 104,
        "exp": 4600,
        "col": 20500,
        "drops": {"Eternal Ice Shard": 1.0, "Frost King's Crown": 0.3},
        "description": "Le souverain absolu de l'hiver, capable de déchaîner des blizzards dévastateurs. Il peut geler instantanément ses adversaires, créer des constructions de glace et absorber la chaleur environnante pour se renforcer.",
        "required_level": 87,
        "min_party_size": 9
    },
    "safe_zones": ["Glacialis", "Warm Haven", "Crystal Lodge"],
    "danger_level": 9,
    "recommended_level": 84,
    "biomes": [
        {
            "name": "Frozen Wastes",
            "description": "Des plaines balayées par des blizzards perpétuels, où seules les créatures les plus résistantes au froid peuvent survivre.",
            "monsters": ["Frost Giant", "Snow Stalker"],
            "quests": ["q451", "q452"],
            "level_range": [84, 87],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Forest",
            "description": "Une forêt où les arbres sont entièrement faits de glace cristalline, habitée par des élémentaires de glace et des créatures translucides.",
            "monsters": ["Ice Elemental", "Crystal Wolf"],
            "quests": ["q453", "q454"],
            "level_range": [87, 90],
            "unlock_requirements": {"level": 86}
        },
        {
            "name": "Frozen Throne",
            "description": "Un palais majestueux fait de glace éternelle, où le Monarque de l'Hiver règne sur son domaine gelé et attend les aventuriers.",
            "monsters": ["Frost Knight", "Blizzard Spirit"],
            "quests": ["q455", "q456"],
            "level_range": [90, 92],
            "unlock_requirements": {"level": 89, "quest_completed": "q454"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Temporis the Timeless One"}
}