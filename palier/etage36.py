# -*- coding: utf-8 -*-

# Informations sur l'étage 36
FLOOR_36_INFO = {
    "name": "Floor 36 - Durenmar",
    "description": "Un étage composé de vastes plaines et de collines où d'anciennes ruines émergent du sol. La ville principale, Durenmar, est construite autour d'un portail mystérieux.",
    "boss": {
        "name": "Chronos the Timekeeper",
        "level": 72,
        "hp": 5200,
        "attack": 87,
        "defense": 82,
        "exp": 2600,
        "col": 13500,
        "drops": {"Temporal Crystal": 1.0, "Clockwork Blade": 0.3},
        "description": "Un être mystérieux qui contrôle le temps dans son domaine. Il peut accélérer, ralentir ou même arrêter brièvement le temps pour lui ou ses adversaires.",
        "required_level": 67,
        "min_party_size": 7
    },
    "safe_zones": ["Durenmar", "Clockwork Village", "Temporal Haven"],
    "danger_level": 8,
    "recommended_level": 62,
    "biomes": [
        {
            "name": "Ruined Fields",
            "description": "Des plaines parsemées de vestiges d'une ancienne civilisation, où des horloges brisées et des engrenages géants émergent du sol.",
            "monsters": ["Clockwork Construct", "Time-Lost Warrior"],
            "quests": ["q259", "q260"],
            "level_range": [62, 65],
            "unlock_requirements": None
        },
        {
            "name": "Hourglass Desert",
            "description": "Un désert où le sable s'écoule comme dans un sablier géant, créant des motifs changeants et piégeant les imprudents.",
            "monsters": ["Sand Chronometer", "Temporal Anomaly"],
            "quests": ["q261", "q262"],
            "level_range": [65, 69],
            "unlock_requirements": {"level": 64}
        },
        {
            "name": "Clocktower Spire",
            "description": "Une tour gigantesque au centre de l'étage, remplie de mécanismes complexes et de paradoxes temporels, où réside le boss.",
            "monsters": ["Gear Guardian", "Pendulum Knight"],
            "quests": ["q263", "q264"],
            "level_range": [69, 72],
            "unlock_requirements": {"level": 68, "quest_completed": "q262"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Nimbus the Cloud Sovereign"}
}