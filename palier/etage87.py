# -*- coding: utf-8 -*-

# Informations sur l'étage 87
FLOOR_87_INFO = {
    "name": "Floor 87 - Pandemonium",
    "description": "Un étage chaotique où la réalité elle-même semble instable, avec des paysages qui se transforment et des lois physiques qui changent aléatoirement. La ville principale, Pandemonium, est le seul endroit stable de l'étage.",
    "boss": {
        "name": "Discordia the Chaos Bringer",
        "level": 102,
        "hp": 12400,
        "attack": 144,
        "defense": 124,
        "exp": 6200,
        "col": 31000,
        "drops": {"Chaos Shard": 1.0, "Reality Warper": 0.3},
        "description": "Une entité qui incarne le chaos primordial. Elle peut altérer la réalité autour d'elle, transformer le terrain de combat et changer constamment de forme et de capacités.",
        "required_level": 97,
        "min_party_size": 10
    },
    "safe_zones": ["Pandemonium", "Order Sanctuary", "Stability Point"],
    "danger_level": 10,
    "recommended_level": 92,
    "biomes": [
        {
            "name": "Shifting Lands",
            "description": "Des terres où le paysage change constamment, passant de déserts brûlants à des toundras gelées en quelques minutes, peuplées de créatures qui s'adaptent à ces changements.",
            "monsters": ["Chaos Shapeshifter", "Adaptive Predator"],
            "quests": ["q529", "q530"],
            "level_range": [92, 95],
            "unlock_requirements": None
        },
        {
            "name": "Reality Fractures",
            "description": "Des zones où la réalité est brisée, créant des phénomènes impossibles comme des chutes d'eau qui coulent vers le haut ou des arbres qui poussent à l'envers.",
            "monsters": ["Reality Aberration", "Paradox Entity"],
            "quests": ["q531", "q532"],
            "level_range": [95, 99],
            "unlock_requirements": {"level": 94}
        },
        {
            "name": "Heart of Chaos",
            "description": "L'épicentre du chaos, où rien n'est stable et où la Porteuse du Chaos règne sur son domaine en constante évolution.",
            "monsters": ["Chaos Guardian", "Entropy Elemental"],
            "quests": ["q533", "q534"],
            "level_range": [99, 102],
            "unlock_requirements": {"level": 98, "quest_completed": "q532"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Tempestas the Storm Lord"}
}