# -*- coding: utf-8 -*-

# Informations sur l'étage 34
FLOOR_34_INFO = {
    "name": "Floor 34 - Castellia",
    "description": "Un étage dominé par des châteaux et des forteresses médiévales. La ville principale, Castellia, est une cité fortifiée entourée de hauts remparts.",
    "boss": {
        "name": "Castellan the Siege Lord",
        "level": 68,
        "hp": 4800,
        "attack": 83,
        "defense": 78,
        "exp": 2400,
        "col": 12500,
        "drops": {"Commander's Insignia": 1.0, "Siege Breaker": 0.3},
        "description": "Un général immortel dans une armure imposante qui commande une armée de soldats mécaniques. Il maîtrise toutes les tactiques de siège et peut invoquer des machines de guerre.",
        "required_level": 63,
        "min_party_size": 7
    },
    "safe_zones": ["Castellia", "Knight's Rest", "Merchant's Quarter"],
    "danger_level": 8,
    "recommended_level": 58,
    "biomes": [
        {
            "name": "Outer Bailey",
            "description": "Les terres entourant les châteaux, parsemées de camps militaires et patrouillées par des soldats mécaniques.",
            "monsters": ["Clockwork Soldier", "Iron Knight"],
            "quests": ["q247", "q248"],
            "level_range": [58, 61],
            "unlock_requirements": None
        },
        {
            "name": "Siege Fields",
            "description": "Une zone de guerre perpétuelle où des machines de siège attaquent sans cesse les fortifications et où des combats font rage.",
            "monsters": ["Siege Golem", "Ballista Operator"],
            "quests": ["q249", "q250"],
            "level_range": [61, 65],
            "unlock_requirements": {"level": 60}
        },
        {
            "name": "Commander's Keep",
            "description": "La forteresse centrale où le Seigneur du Siège a établi son quartier général et planifie ses conquêtes.",
            "monsters": ["Elite Guard", "War Strategist"],
            "quests": ["q251", "q252"],
            "level_range": [65, 68],
            "unlock_requirements": {"level": 64, "quest_completed": "q250"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Arachne the Spider Queen"}
}