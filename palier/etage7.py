# -*- coding: utf-8 -*-

# Informations sur l'étage 7
FLOOR_7_INFO = {
    "name": "Floor 7 - Iceveil",
    "description": "Un étage glacial couvert de neige et de glace éternelles. La ville principale, Iceveil, est construite dans une gigantesque caverne de glace qui la protège des blizzards.",
    "boss": {
        "name": "Frostclaw the Winter Beast",
        "level": 44,
        "hp": 2200,
        "attack": 58,
        "defense": 52,
        "exp": 1200,
        "col": 6000,
        "drops": {"Frozen Heart": 1.0, "Ice Fang Dagger": 0.3},
        "description": "Un loup géant de glace avec des griffes acérées comme des rasoirs. Il peut geler ses adversaires d'un souffle et créer des clones de glace pour l'assister.",
        "required_level": 39,
        "min_party_size": 4
    },
    "safe_zones": ["Iceveil", "Frost Lodge", "Warmhearth"],
    "danger_level": 5,
    "recommended_level": 34,
    "biomes": [
        {
            "name": "Frozen Tundra",
            "description": "Une vaste plaine gelée où le blizzard souffle sans cesse, habitée par des créatures adaptées au froid extrême.",
            "monsters": ["Snow Wolf", "Frost Golem"],
            "quests": ["q103", "q104"],
            "level_range": [34, 37],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Glacier",
            "description": "Un immense glacier aux reflets bleutés, où des créatures de glace se confondent avec le paysage.",
            "monsters": ["Ice Elemental", "Glacier Crab"],
            "quests": ["q105", "q106"],
            "level_range": [37, 40],
            "unlock_requirements": {"level": 36}
        },
        {
            "name": "Frozen Fortress",
            "description": "Une forteresse taillée dans la glace éternelle, où réside le boss et ses serviteurs gelés.",
            "monsters": ["Frozen Knight", "Ice Wraith"],
            "quests": ["q107", "q108"],
            "level_range": [40, 44],
            "unlock_requirements": {"level": 39, "quest_completed": "q106"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Tempestus the Storm Lord"}
}