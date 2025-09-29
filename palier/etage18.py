# -*- coding: utf-8 -*-

# Informations sur l'étage 18
FLOOR_18_INFO = {
    "name": "Floor 18 - Crystalia",
    "description": "Un étage composé de formations cristallines géantes aux couleurs chatoyantes. La ville principale, Crystalia, est taillée directement dans un immense cristal bleu.",
    "boss": {
        "name": "Prismatica the Crystal Queen",
        "level": 61,
        "hp": 4200,
        "attack": 83,
        "defense": 77,
        "exp": 2200,
        "col": 11000,
        "drops": {"Perfect Prism": 1.0, "Rainbow Blade": 0.3},
        "description": "Une entité féminine faite de cristaux vivants qui peut manipuler la lumière pour créer des illusions et projeter des rayons d'énergie pure.",
        "required_level": 56,
        "min_party_size": 6
    },
    "safe_zones": ["Crystalia", "Prism Plaza", "Rainbow Falls"],
    "danger_level": 7,
    "recommended_level": 54,
    "biomes": [
        {
            "name": "Crystal Fields",
            "description": "Des plaines où poussent des cristaux multicolores qui réfractent la lumière, créant des arcs-en-ciel permanents et abritant des créatures cristallines.",
            "monsters": ["Crystal Beetle", "Prism Wolf"],
            "quests": ["q163", "q164"],
            "level_range": [54, 56],
            "unlock_requirements": None
        },
        {
            "name": "Gemstone Caves",
            "description": "Un réseau de grottes aux parois incrustées de pierres précieuses, où vivent des élémentaires de cristal et des mineurs corrompus.",
            "monsters": ["Gem Elemental", "Corrupted Miner"],
            "quests": ["q165", "q166"],
            "level_range": [56, 59],
            "unlock_requirements": {"level": 55}
        },
        {
            "name": "Diamond Spire",
            "description": "Une tour de cristal pur qui s'élève au centre de l'étage, où la reine et sa cour attendent les aventuriers.",
            "monsters": ["Crystal Knight", "Light Weaver"],
            "quests": ["q167", "q168"],
            "level_range": [59, 61],
            "unlock_requirements": {"level": 58, "quest_completed": "q166"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Mortuus the Grave Lord"}
}