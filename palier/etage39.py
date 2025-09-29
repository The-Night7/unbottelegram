# -*- coding: utf-8 -*-

# Informations sur l'étage 39
FLOOR_39_INFO = {
    "name": "Floor 39 - Vespera",
    "description": "Un étage plongé dans un crépuscule perpétuel, avec des forêts de champignons luminescents et des lacs phosphorescents. La ville principale, Vespera, est éclairée par des lanternes bioluminescentes.",
    "boss": {
        "name": "Noctis the Twilight Sovereign",
        "level": 77,
        "hp": 5800,
        "attack": 93,
        "defense": 88,
        "exp": 2900,
        "col": 15000,
        "drops": {"Twilight Essence": 1.0, "Duskblade": 0.3},
        "description": "Un être mystérieux qui existe entre la lumière et l'ombre. Il peut manipuler la luminosité pour aveugler ou plonger ses adversaires dans l'obscurité totale.",
        "required_level": 72,
        "min_party_size": 8
    },
    "safe_zones": ["Vespera", "Glowshroom Haven", "Phosphor Camp"],
    "danger_level": 8,
    "recommended_level": 68,
    "biomes": [
        {
            "name": "Luminous Forest",
            "description": "Une forêt de champignons géants qui émettent une douce lueur bleue, habitée par des créatures bioluminescentes.",
            "monsters": ["Glowshroom Guardian", "Luminous Moth"],
            "quests": ["q277", "q278"],
            "level_range": [68, 71],
            "unlock_requirements": None
        },
        {
            "name": "Twilight Lakes",
            "description": "Des lacs dont l'eau semble capturer la lumière du crépuscule, où nagent des poissons phosphorescents et des créatures des profondeurs.",
            "monsters": ["Phosphor Fish", "Twilight Lurker"],
            "quests": ["q279", "q280"],
            "level_range": [71, 74],
            "unlock_requirements": {"level": 70}
        },
        {
            "name": "Dusk Cathedral",
            "description": "Un temple ancien construit pour vénérer l'équilibre entre la lumière et l'obscurité, où le souverain du crépuscule attend les aventuriers.",
            "monsters": ["Shadow Priest", "Light Acolyte"],
            "quests": ["q281", "q282"],
            "level_range": [74, 77],
            "unlock_requirements": {"level": 73, "quest_completed": "q280"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Avalanche the Mountain King"}
}