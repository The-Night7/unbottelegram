# -*- coding: utf-8 -*-

# Informations sur l'étage 71
FLOOR_71_INFO = {
    "name": "Floor 71 - Chronos",
    "description": "Un étage où le temps semble fluctuer de façon imprévisible, avec des zones figées dans le passé ou le futur. La ville principale, Chronos, est construite autour d'une immense horloge qui régule le flux temporel.",
    "boss": {
        "name": "Temporis the Timeless One",
        "level": 91,
        "hp": 9000,
        "attack": 112,
        "defense": 102,
        "exp": 4500,
        "col": 20000,
        "drops": {"Chronos Crystal": 1.0, "Timekeeper's Staff": 0.3},
        "description": "Un être qui existe simultanément dans plusieurs époques. Il peut accélérer, ralentir ou même arrêter brièvement le temps pour lui ou ses adversaires, et invoquer des versions passées ou futures de lui-même.",
        "required_level": 86,
        "min_party_size": 9
    },
    "safe_zones": ["Chronos", "Time Haven", "Clockwork Sanctuary"],
    "danger_level": 9,
    "recommended_level": 83,
    "biomes": [
        {
            "name": "Ancient Ruins",
            "description": "Des zones où le temps est figé dans un passé lointain, avec des ruines anciennes habitées par des créatures d'une autre époque.",
            "monsters": ["Ancient Guardian", "Temporal Anomaly"],
            "quests": ["q445", "q446"],
            "level_range": [83, 86],
            "unlock_requirements": None
        },
        {
            "name": "Future Wasteland",
            "description": "Des régions qui semblent appartenir à un futur dévasté, où des constructions mécaniques avancées patrouillent parmi les décombres.",
            "monsters": ["Future Sentinel", "Chrono Construct"],
            "quests": ["q447", "q448"],
            "level_range": [86, 89],
            "unlock_requirements": {"level": 85}
        },
        {
            "name": "Temporal Nexus",
            "description": "Le point central où toutes les lignes temporelles convergent, une zone instable où la réalité fluctue constamment et où le Maître du Temps attend les aventuriers.",
            "monsters": ["Time Wraith", "Paradox Guardian"],
            "quests": ["q449", "q450"],
            "level_range": [89, 91],
            "unlock_requirements": {"level": 88, "quest_completed": "q448"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Luminaris the Radiant Judge"}
}