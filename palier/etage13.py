# -*- coding: utf-8 -*-

# Informations sur l'étage 13
FLOOR_13_INFO = {
    "name": "Floor 13 - Caerulas",
    "description": "Un étage recouvert d'une jungle dense aux plantes bioluminescentes. La ville principale, Caerulas, est construite dans les arbres géants et brille de mille feux la nuit.",
    "boss": {
        "name": "Lumina the Radiant Queen",
        "level": 51,
        "hp": 3200,
        "attack": 70,
        "defense": 65,
        "exp": 1700,
        "col": 8500,
        "drops": {"Bioluminescent Crystal": 1.0, "Light Weaver's Bow": 0.3},
        "description": "Une reine fée entourée d'un essaim de lucioles magiques. Elle peut aveugler ses adversaires avec des flashs de lumière intense et créer des illusions.",
        "required_level": 46,
        "min_party_size": 5
    },
    "safe_zones": ["Caerulas", "Glowing Haven", "Luminous Camp"],
    "danger_level": 6,
    "recommended_level": 44,
    "biomes": [
        {
            "name": "Bioluminescent Jungle",
            "description": "Une jungle dense où les plantes et les champignons émettent une lumière bleutée, habitée par des créatures adaptées à cet environnement unique.",
            "monsters": ["Glow Beetle", "Luminous Panther"],
            "quests": ["q133", "q134"],
            "level_range": [44, 46],
            "unlock_requirements": None
        },
        {
            "name": "Firefly Valley",
            "description": "Une vallée où des millions de lucioles créent un spectacle féerique, mais où se cachent aussi des prédateurs dangereux.",
            "monsters": ["Light Eater", "Glowmoth"],
            "quests": ["q135", "q136"],
            "level_range": [46, 49],
            "unlock_requirements": {"level": 45}
        },
        {
            "name": "Radiant Throne",
            "description": "Un palais de cristal lumineux au cœur de la jungle, où réside la reine et sa cour féerique.",
            "monsters": ["Royal Lightguard", "Prism Elemental"],
            "quests": ["q137", "q138"],
            "level_range": [49, 51],
            "unlock_requirements": {"level": 48, "quest_completed": "q136"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Astraeus the Celestial Watcher"}
}