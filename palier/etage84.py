# -*- coding: utf-8 -*-

# Informations sur l'étage 84
FLOOR_84_INFO = {
    "name": "Floor 84 - Necropolis",
    "description": "Un étage dominé par d'immenses cimetières et des catacombes sans fin. La ville principale, Necropolis, est construite autour d'une cathédrale gothique et protégée contre les morts-vivants par des barrières sacrées.",
    "boss": {
        "name": "Thanatos the Death Lord",
        "level": 99,
        "hp": 11800,
        "attack": 138,
        "defense": 118,
        "exp": 5900,
        "col": 29500,
        "drops": {"Soul Crystal": 1.0, "Reaper's Scythe": 0.3},
        "description": "Le seigneur de la mort qui commande aux âmes des défunts. Il peut invoquer des armées de morts-vivants, drainer la vie de ses adversaires et temporairement bannir les âmes des vivants.",
        "required_level": 94,
        "min_party_size": 10
    },
    "safe_zones": ["Necropolis", "Sanctuary of Light", "Hallowed Ground"],
    "danger_level": 10,
    "recommended_level": 89,
    "biomes": [
        {
            "name": "Endless Graveyard",
            "description": "Un vaste cimetière qui semble s'étendre à l'infini, où les morts se relèvent la nuit et où des fantômes errent parmi les pierres tombales.",
            "monsters": ["Risen Dead", "Mourning Spirit"],
            "quests": ["q511", "q512"],
            "level_range": [89, 92],
            "unlock_requirements": None
        },
        {
            "name": "Ancient Catacombs",
            "description": "Un labyrinthe souterrain de tombes et d'ossuaires, où reposent les restes de puissants guerriers et mages dont les esprits protègent encore leurs trésors.",
            "monsters": ["Tomb Guardian", "Lich Mage"],
            "quests": ["q513", "q514"],
            "level_range": [92, 96],
            "unlock_requirements": {"level": 91}
        },
        {
            "name": "Death's Domain",
            "description": "Le royaume personnel du Seigneur de la Mort, où la frontière entre la vie et la mort est floue et où les âmes sont jugées avant de poursuivre leur voyage.",
            "monsters": ["Death Knight", "Soul Reaper"],
            "quests": ["q515", "q516"],
            "level_range": [96, 99],
            "unlock_requirements": {"level": 95, "quest_completed": "q514"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Archmagus the Spell Weaver"}
}