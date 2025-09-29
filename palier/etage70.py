# -*- coding: utf-8 -*-

# Informations sur l'étage 70
FLOOR_70_INFO = {
    "name": "Floor 70 - Celestia",
    "description": "Un étage baigné dans une lumière dorée perpétuelle, avec des temples majestueux et des jardins célestes. La ville principale, Celestia, est construite en marbre blanc et or, et semble flotter au-dessus des nuages.",
    "boss": {
        "name": "Luminaris the Radiant Judge",
        "level": 90,
        "hp": 8800,
        "attack": 110,
        "defense": 100,
        "exp": 4400,
        "col": 19500,
        "drops": {"Divine Light": 1.0, "Judgement Hammer": 0.3},
        "description": "Un juge céleste à l'apparence angélique qui pèse les âmes des mortels. Il peut aveugler ses adversaires avec des explosions de lumière divine et invoquer des rayons purificateurs qui infligent des dégâts massifs.",
        "required_level": 85,
        "min_party_size": 9
    },
    "safe_zones": ["Celestia", "Divine Gardens", "Temple of Light"],
    "danger_level": 9,
    "recommended_level": 82,
    "biomes": [
        {
            "name": "Golden Fields",
            "description": "Des plaines où l'herbe semble faite d'or et où des créatures célestes se promènent paisiblement, mais attaquent ceux qu'elles jugent indignes.",
            "monsters": ["Celestial Guardian", "Golden Beast"],
            "quests": ["q439", "q440"],
            "level_range": [82, 85],
            "unlock_requirements": None
        },
        {
            "name": "Heavenly Gardens",
            "description": "Des jardins parfaits où poussent des fleurs qui n'existent nulle part ailleurs, gardés par des serviteurs divins et des constructions animées.",
            "monsters": ["Garden Sentinel", "Divine Construct"],
            "quests": ["q441", "q442"],
            "level_range": [85, 88],
            "unlock_requirements": {"level": 84}
        },
        {
            "name": "Judgment Hall",
            "description": "Un temple colossal où les âmes sont jugées et où le Juge Radieux attend les aventuriers pour évaluer leur valeur.",
            "monsters": ["Angelic Warrior", "Light Elemental"],
            "quests": ["q443", "q444"],
            "level_range": [88, 90],
            "unlock_requirements": {"level": 87, "quest_completed": "q442"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Tenebris the Void Walker"}
}