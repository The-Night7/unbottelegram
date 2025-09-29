# -*- coding: utf-8 -*-

# Informations sur l'étage 77
FLOOR_77_INFO = {
    "name": "Floor 77 - Umbral Depths",
    "description": "Un étage plongé dans une obscurité quasi-totale, avec des cavernes abyssales et des gouffres sans fond. La ville principale, Umbral Depths, est illuminée par des cristaux bioluminescents.",
    "boss": {
        "name": "Nocturn the Shadow King",
        "level": 92,
        "hp": 10400,
        "attack": 124,
        "defense": 104,
        "exp": 5200,
        "col": 26000,
        "drops": {"Shadow Essence": 1.0, "Void Blade": 0.3},
        "description": "Un roi des ténèbres dont le corps semble fait d'ombre pure. Il peut se fondre dans l'obscurité, créer des clones d'ombre et absorber la lumière pour renforcer ses pouvoirs.",
        "required_level": 87,
        "min_party_size": 10
    },
    "safe_zones": ["Umbral Depths", "Light Haven", "Crystal Refuge"],
    "danger_level": 10,
    "recommended_level": 82,
    "biomes": [
        {
            "name": "Glowing Caverns",
            "description": "Des grottes illuminées par des champignons et des cristaux bioluminescents, où la faible lumière attire des créatures dangereuses.",
            "monsters": ["Luminous Stalker", "Cave Dweller"],
            "quests": ["q469", "q470"],
            "level_range": [82, 85],
            "unlock_requirements": None
        },
        {
            "name": "Abyssal Chasms",
            "description": "Des gouffres si profonds que la lumière n'y pénètre jamais, habités par des créatures qui ont évolué dans l'obscurité totale.",
            "monsters": ["Void Creature", "Abyss Hunter"],
            "quests": ["q471", "q472"],
            "level_range": [85, 89],
            "unlock_requirements": {"level": 84}
        },
        {
            "name": "Shadow Throne",
            "description": "Le palais du Roi des Ombres, construit dans la partie la plus sombre de l'étage, où même la lumière magique est absorbée par les ténèbres.",
            "monsters": ["Shadow Knight", "Darkness Elemental"],
            "quests": ["q473", "q474"],
            "level_range": [89, 92],
            "unlock_requirements": {"level": 88, "quest_completed": "q472"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Aetheria the Sky Empress"}
}