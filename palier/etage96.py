# -*- coding: utf-8 -*-

# Informations sur l'étage 96
FLOOR_96_INFO = {
    "name": "Floor 96 - Chronos Citadel",
    "description": "Un étage où le temps lui-même est instable, avec des zones figées dans différentes époques. La ville principale, Chronos Citadel, est protégée par une bulle temporelle où le temps s'écoule normalement.",
    "boss": {
        "name": "Eternus the Time Keeper",
        "level": 101,
        "hp": 13200,
        "attack": 142,
        "defense": 132,
        "exp": 6600,
        "col": 33000,
        "drops": {"Sands of Time": 1.0, "Chronometer Staff": 0.3},
        "description": "Le gardien du temps qui existe simultanément dans le passé, le présent et le futur. Il peut accélérer, ralentir ou même arrêter brièvement le temps pour lui ou ses adversaires, et invoquer des versions passées ou futures de lui-même.",
        "required_level": 96,
        "min_party_size": 10
    },
    "safe_zones": ["Chronos Citadel", "Time Haven", "Stable Point"],
    "danger_level": 10,
    "recommended_level": 91,
    "biomes": [
        {
            "name": "Past Echoes",
            "description": "Une zone figée dans un passé lointain, avec des paysages primitifs et des créatures préhistoriques qui errent parmi les vestiges d'anciennes civilisations.",
            "monsters": ["Ancient Guardian", "Primeval Beast"],
            "quests": ["q577", "q578"],
            "level_range": [91, 94],
            "unlock_requirements": None
        },
        {
            "name": "Future Visions",
            "description": "Une région bloquée dans un futur avancé, avec des structures cristallines et des technologies incompréhensibles, gardées par des constructions mécaniques avancées.",
            "monsters": ["Future Sentinel", "Quantum Entity"],
            "quests": ["q579", "q580"],
            "level_range": [94, 98],
            "unlock_requirements": {"level": 93}
        },
        {
            "name": "Temporal Nexus",
            "description": "Le cœur de l'étage où toutes les lignes temporelles convergent, créant un chaos de réalités superposées où le Gardien du Temps surveille le flux du temps.",
            "monsters": ["Chrono Guardian", "Paradox Entity"],
            "quests": ["q581", "q582"],
            "level_range": [98, 101],
            "unlock_requirements": {"level": 97, "quest_completed": "q580"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Astraeus the Star Lord"}
}