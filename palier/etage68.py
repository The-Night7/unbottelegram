# -*- coding: utf-8 -*-

# Informations sur l'étage 68
FLOOR_68_INFO = {
    "name": "Floor 68 - Avalon",
    "description": "Un étage féerique avec des forêts enchantées et des lacs magiques. La ville principale, Avalon, est construite dans un cercle de pierres anciennes et semble changer d'apparence selon l'heure du jour.",
    "boss": {
        "name": "Oberon the Fairy King",
        "level": 88,
        "hp": 8400,
        "attack": 106,
        "defense": 98,
        "exp": 4200,
        "col": 18500,
        "drops": {"Fairy Dust": 1.0, "Enchanted Rapier": 0.3},
        "description": "Le souverain du peuple fée, aussi beau que cruel. Il maîtrise la magie féerique, peut voler et devenir invisible, et est capable de charmer ses adversaires pour les retourner contre leurs alliés.",
        "required_level": 83,
        "min_party_size": 8
    },
    "safe_zones": ["Avalon", "Enchanted Grove", "Fairy Ring"],
    "danger_level": 9,
    "recommended_level": 80,
    "biomes": [
        {
            "name": "Whispering Woods",
            "description": "Une forêt où les arbres semblent murmurer des secrets et où des lueurs féeriques dansent entre les branches, habitée par des créatures magiques.",
            "monsters": ["Will-o'-Wisp", "Forest Spirit"],
            "quests": ["q427", "q428"],
            "level_range": [80, 83],
            "unlock_requirements": None
        },
        {
            "name": "Enchanted Lakes",
            "description": "Des lacs aux eaux miroitantes qui peuvent montrer le passé ou l'avenir, gardés par des nymphes et des créatures aquatiques.",
            "monsters": ["Lake Guardian", "Water Nymph"],
            "quests": ["q429", "q430"],
            "level_range": [83, 86],
            "unlock_requirements": {"level": 82}
        },
        {
            "name": "Fairy Court",
            "description": "Le domaine royal où le Roi des Fées tient sa cour, entouré de ses sujets les plus puissants et de merveilles magiques.",
            "monsters": ["Royal Fairy", "Enchanted Knight"],
            "quests": ["q431", "q432"],
            "level_range": [86, 88],
            "unlock_requirements": {"level": 85, "quest_completed": "q430"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Mortis the Undying King"}
}