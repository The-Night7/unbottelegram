# -*- coding: utf-8 -*-

# Informations sur l'étage 78
FLOOR_78_INFO = {
    "name": "Floor 78 - Chronopolis",
    "description": "Un étage où le temps s'écoule de façon non linéaire, avec des zones figées dans différentes époques. La ville principale, Chronopolis, est protégée par une bulle temporelle stable.",
    "boss": {
        "name": "Aeternalis the Timeless",
        "level": 93,
        "hp": 10600,
        "attack": 126,
        "defense": 106,
        "exp": 5300,
        "col": 26500,
        "drops": {"Hourglass Shard": 1.0, "Chronos Blade": 0.3},
        "description": "Un être qui existe simultanément dans toutes les lignes temporelles. Il peut manipuler le temps à volonté, accélérant, ralentissant ou même arrêtant brièvement ses adversaires.",
        "required_level": 88,
        "min_party_size": 10
    },
    "safe_zones": ["Chronopolis", "Temporal Haven", "Clockwork Sanctuary"],
    "danger_level": 10,
    "recommended_level": 83,
    "biomes": [
        {
            "name": "Ancient Ruins",
            "description": "Une zone figée dans un passé lointain, avec des ruines anciennes et des créatures préhistoriques qui errent parmi les vestiges d'une civilisation oubliée.",
            "monsters": ["Temporal Anomaly", "Ancient Guardian"],
            "quests": ["q475", "q476"],
            "level_range": [83, 86],
            "unlock_requirements": None
        },
        {
            "name": "Future Wasteland",
            "description": "Une région bloquée dans un futur apocalyptique, où des machines avancées et des constructions mécaniques patrouillent parmi les décombres.",
            "monsters": ["Clockwork Sentinel", "Future Predator"],
            "quests": ["q477", "q478"],
            "level_range": [86, 90],
            "unlock_requirements": {"level": 85}
        },
        {
            "name": "Temporal Nexus",
            "description": "Le centre de convergence de toutes les lignes temporelles, où la réalité est instable et où l'Intemporel attend les aventuriers dans son sanctuaire hors du temps.",
            "monsters": ["Time Wraith", "Paradox Guardian"],
            "quests": ["q479", "q480"],
            "level_range": [90, 93],
            "unlock_requirements": {"level": 89, "quest_completed": "q478"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Nocturn the Shadow King"}
}