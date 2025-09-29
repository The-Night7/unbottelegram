# -*- coding: utf-8 -*-

# Informations sur l'étage 29
FLOOR_29_INFO = {
    "name": "Floor 29 - Darkmoor",
    "description": "Un étage plongé dans une nuit perpétuelle, avec des landes désolées et des tourbières. La ville principale, Darkmoor, est éclairée par des lanternes magiques qui repoussent les créatures des ténèbres.",
    "boss": {
        "name": "Umbra the Shadow Lord",
        "level": 58,
        "hp": 3800,
        "attack": 73,
        "defense": 68,
        "exp": 1900,
        "col": 10000,
        "drops": {"Shadow Essence": 1.0, "Darkblade": 0.3},
        "description": "Un être fait d'ombre pure qui peut se fondre dans les ténèbres et en émerger à volonté. Il peut créer des clones d'ombre et absorber la lumière pour renforcer ses pouvoirs.",
        "required_level": 53,
        "min_party_size": 6
    },
    "safe_zones": ["Darkmoor", "Lantern Keep", "Sanctuary of Light"],
    "danger_level": 7,
    "recommended_level": 48,
    "biomes": [
        {
            "name": "Twilight Moors",
            "description": "Des landes brumeuses où la lumière du jour ne pénètre jamais, habitées par des créatures nocturnes et des spectres.",
            "monsters": ["Moor Stalker", "Twilight Wraith"],
            "quests": ["q217", "q218"],
            "level_range": [48, 51],
            "unlock_requirements": None
        },
        {
            "name": "Shadow Fens",
            "description": "Des marécages où l'eau est aussi noire que l'encre et où des créatures d'ombre se cachent sous la surface.",
            "monsters": ["Fen Lurker", "Shadow Beast"],
            "quests": ["q219", "q220"],
            "level_range": [51, 55],
            "unlock_requirements": {"level": 50}
        },
        {
            "name": "Obsidian Spire",
            "description": "Une tour d'obsidienne qui s'élève au centre de l'étage, absorbant toute lumière et servant de repaire au boss.",
            "monsters": ["Shadow Knight", "Void Elemental"],
            "quests": ["q221", "q222"],
            "level_range": [55, 58],
            "unlock_requirements": {"level": 54, "quest_completed": "q220"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Fenrir the Alpha King"}
}