# -*- coding: utf-8 -*-

# Informations sur l'étage 83
FLOOR_83_INFO = {
    "name": "Floor 83 - Arcane Academy",
    "description": "Un étage consacré à la magie et au savoir, avec des bibliothèques flottantes et des tours d'invocation. La ville principale, Arcane Academy, est une immense université magique où les plus grands mages d'Aincrad étudient les arcanes.",
    "boss": {
        "name": "Archmagus the Spell Weaver",
        "level": 98,
        "hp": 11600,
        "attack": 136,
        "defense": 116,
        "exp": 5800,
        "col": 29000,
        "drops": {"Archmage's Crystal": 1.0, "Staff of Infinite Spells": 0.3},
        "description": "Le plus puissant des mages, maître de toutes les écoles de magie. Il peut lancer plusieurs sorts simultanément, créer des barrières magiques impénétrables et invoquer des constructions arcanes pour le protéger.",
        "required_level": 93,
        "min_party_size": 10
    },
    "safe_zones": ["Arcane Academy", "Scholar's Haven", "Meditation Gardens"],
    "danger_level": 10,
    "recommended_level": 88,
    "biomes": [
        {
            "name": "Floating Libraries",
            "description": "Des bibliothèques immenses qui flottent dans les airs, gardées par des livres animés et des golems de papier, contenant des connaissances dangereuses.",
            "monsters": ["Animated Tome", "Knowledge Guardian"],
            "quests": ["q505", "q506"],
            "level_range": [88, 91],
            "unlock_requirements": None
        },
        {
            "name": "Elemental Laboratories",
            "description": "Des zones d'expérimentation où les éléments sont étudiés et manipulés, créant des phénomènes dangereux et des créatures élémentaires instables.",
            "monsters": ["Experiment Gone Wrong", "Elemental Fusion"],
            "quests": ["q507", "q508"],
            "level_range": [91, 95],
            "unlock_requirements": {"level": 90}
        },
        {
            "name": "Archmage's Sanctum",
            "description": "Le sanctuaire personnel de l'Archimage, où convergent des lignes de force magique et où il conduit ses recherches les plus secrètes.",
            "monsters": ["Arcane Construct", "Spell Guardian"],
            "quests": ["q509", "q510"],
            "level_range": [95, 98],
            "unlock_requirements": {"level": 94, "quest_completed": "q508"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Vulcanus the Forge God"}
}