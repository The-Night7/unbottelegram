# -*- coding: utf-8 -*-

# Informations sur l'étage 81
FLOOR_81_INFO = {
    "name": "Floor 81 - Abyssal Depths",
    "description": "Un étage majoritairement submergé, avec d'immenses océans et des fosses abyssales. La ville principale, Abyssal Depths, est construite dans une bulle d'air au fond de l'océan.",
    "boss": {
        "name": "Leviathan the Deep Terror",
        "level": 96,
        "hp": 11200,
        "attack": 132,
        "defense": 112,
        "exp": 5600,
        "col": 28000,
        "drops": {"Abyssal Scale": 1.0, "Trident of the Depths": 0.3},
        "description": "Un monstre marin colossal qui règne sur les profondeurs. Il peut créer des tourbillons dévastateurs, manipuler la pression de l'eau pour écraser ses adversaires et invoquer des serviteurs des abysses.",
        "required_level": 91,
        "min_party_size": 10
    },
    "safe_zones": ["Abyssal Depths", "Coral Haven", "Pressure Dome"],
    "danger_level": 10,
    "recommended_level": 86,
    "biomes": [
        {
            "name": "Sunlit Shallows",
            "description": "Les eaux peu profondes où la lumière du soleil pénètre encore, habitées par des créatures colorées mais aussi par des prédateurs marins dangereux.",
            "monsters": ["Reef Guardian", "Hunter Shark"],
            "quests": ["q493", "q494"],
            "level_range": [86, 89],
            "unlock_requirements": None
        },
        {
            "name": "Twilight Zone",
            "description": "Les profondeurs intermédiaires où la lumière commence à s'estomper, peuplées de créatures bioluminescentes et de prédateurs adaptés à la faible visibilité.",
            "monsters": ["Luminous Squid", "Depth Stalker"],
            "quests": ["q495", "q496"],
            "level_range": [89, 93],
            "unlock_requirements": {"level": 88}
        },
        {
            "name": "Abyssal Plain",
            "description": "Les profondeurs ultimes où règne une obscurité totale et une pression écrasante, domaine du Léviathan et de ses serviteurs cauchemardesques.",
            "monsters": ["Abyssal Horror", "Deep One"],
            "quests": ["q497", "q498"],
            "level_range": [93, 96],
            "unlock_requirements": {"level": 92, "quest_completed": "q496"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Ascendius the Skyward Judge"}
}