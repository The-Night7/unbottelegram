# -*- coding: utf-8 -*-

# Informations sur l'étage 57
FLOOR_57_INFO = {
    "name": "Floor 57 - Marten",
    "description": "Un étage dominé par des forêts de conifères géants et des montagnes enneigées. La ville principale, Marten, est construite dans les arbres et reliée par des ponts suspendus.",
    "boss": {
        "name": "Silvanus the Forest Ancient",
        "level": 78,
        "hp": 6400,
        "attack": 93,
        "defense": 88,
        "exp": 3200,
        "col": 13500,
        "drops": {"Ancient Heartwood": 1.0, "Living Bow": 0.3},
        "description": "Un esprit de la forêt primordiale qui a pris la forme d'un immense cerf aux bois ramifiés comme des arbres. Il peut contrôler la végétation et invoquer les animaux de la forêt.",
        "required_level": 73,
        "min_party_size": 7
    },
    "safe_zones": ["Marten", "Treetop Haven", "Hunter's Lodge"],
    "danger_level": 8,
    "recommended_level": 68,
    "biomes": [
        {
            "name": "Pine Forest",
            "description": "Une forêt dense de pins et de sapins géants, où vivent des créatures sylvestres et des chasseurs solitaires.",
            "monsters": ["Forest Wolf", "Pine Guardian"],
            "quests": ["q367", "q368"],
            "level_range": [68, 71],
            "unlock_requirements": None
        },
        {
            "name": "Snowy Peaks",
            "description": "Les sommets enneigés des montagnes qui entourent la forêt, habités par des créatures adaptées au froid et gardés par des élémentaires de glace.",
            "monsters": ["Frost Elemental", "Snow Beast"],
            "quests": ["q369", "q370"],
            "level_range": [71, 75],
            "unlock_requirements": {"level": 70}
        },
        {
            "name": "Sacred Grove",
            "description": "Un bosquet ancien au cœur de la forêt, où les arbres les plus vieux murmurent des secrets et où l'ancien de la forêt attend les aventuriers.",
            "monsters": ["Ancient Treant", "Spirit Deer"],
            "quests": ["q371", "q372"],
            "level_range": [75, 78],
            "unlock_requirements": {"level": 74, "quest_completed": "q370"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Oceanus the Tidal Lord"}
}