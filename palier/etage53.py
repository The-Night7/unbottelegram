# -*- coding: utf-8 -*-

# Informations sur l'étage 53
FLOOR_53_INFO = {
    "name": "Floor 53 - Morbidus",
    "description": "Un étage lugubre dominé par des marécages toxiques et des forêts mortes. La ville principale, Morbidus, est construite sur des pilotis au-dessus des marais et protégée par des barrières magiques.",
    "boss": {
        "name": "Pestilens the Plague Lord",
        "level": 71,
        "hp": 5600,
        "attack": 86,
        "defense": 76,
        "exp": 2800,
        "col": 12000,
        "drops": {"Plague Essence": 1.0, "Toxic Scythe": 0.3},
        "description": "Un être corrompu qui répand la maladie et la putréfaction. Son corps est partiellement décomposé et il peut libérer des nuages de miasmes toxiques et invoquer des serviteurs pestiférés.",
        "required_level": 66,
        "min_party_size": 7
    },
    "safe_zones": ["Morbidus", "Purified Sanctuary", "Healer's Camp"],
    "danger_level": 7,
    "recommended_level": 61,
    "biomes": [
        {
            "name": "Toxic Swamp",
            "description": "Des marécages où l'eau est empoisonnée et où des vapeurs toxiques s'élèvent constamment, habités par des créatures mutantes et des plantes carnivores.",
            "monsters": ["Swamp Mutant", "Poison Frog"],
            "quests": ["q349", "q350"],
            "level_range": [61, 64],
            "unlock_requirements": None
        },
        {
            "name": "Withered Forest",
            "description": "Une forêt morte où les arbres sont desséchés et où rôdent des créatures non-mortes et des esprits tourmentés.",
            "monsters": ["Withered Treant", "Plague Zombie"],
            "quests": ["q351", "q352"],
            "level_range": [64, 68],
            "unlock_requirements": {"level": 63}
        },
        {
            "name": "Plague Citadel",
            "description": "Une forteresse en ruines au centre du marais, où le seigneur de la peste conduit ses expériences macabres et attend les aventuriers.",
            "monsters": ["Plague Doctor", "Experiment Gone Wrong"],
            "quests": ["q353", "q354"],
            "level_range": [68, 71],
            "unlock_requirements": {"level": 67, "quest_completed": "q352"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Mechanicus the Clockwork Titan"}
}