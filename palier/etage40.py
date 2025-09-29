# -*- coding: utf-8 -*-

# Informations sur l'étage 40
FLOOR_40_INFO = {
    "name": "Floor 40 - Jaileum",
    "description": "Un étage sombre et oppressant, conçu comme une gigantesque prison. Des cellules et des couloirs s'étendent à perte de vue, et des chaînes pendent du plafond.",
    "boss": {
        "name": "Vemacitrin the Absolute",
        "level": 60,
        "hp": 4000,
        "attack": 75,
        "defense": 65,
        "exp": 2000,
        "col": 9000,
        "drops": {"Warden's Key": 1.0, "Chains of Binding": 0.3},
        "description": "Le gardien suprême de la prison, un géant enchaîné qui utilise ses propres chaînes comme armes. Il peut emprisonner les joueurs et les immobiliser pendant le combat.",
        "required_level": 55,
        "min_party_size": 6
    },
    "safe_zones": ["Jaileum Plaza", "Warden's Rest", "Forgotten Cell"],
    "danger_level": 6,
    "recommended_level": 50,
    "biomes": [
        {
            "name": "Prison Entrance",
            "description": "La zone d'entrée de la prison, avec des cellules abandonnées et des salles de garde. Des gardiens patrouillent encore les couloirs.",
            "monsters": ["Prison Guard", "Escaped Prisoner"],
            "quests": ["q67", "q68"],
            "level_range": [50, 53],
            "unlock_requirements": None
        },
        {
            "name": "Torture Chambers",
            "description": "Des salles sinistres remplies d'instruments de torture et hantées par les âmes des prisonniers torturés.",
            "monsters": ["Tortured Soul", "Sadistic Executioner"],
            "quests": ["q69", "q70"],
            "level_range": [53, 57],
            "unlock_requirements": {"level": 52}
        },
        {
            "name": "Maximum Security",
            "description": "La section la plus profonde de la prison, où sont enfermés les criminels les plus dangereux et où se trouve le boss.",
            "monsters": ["Chained Beast", "Shadow Warden"],
            "quests": ["q71", "q72"],
            "level_range": [57, 60],
            "unlock_requirements": {"level": 55, "quest_completed": "q70"}
        }
    ],
    "unlock_requirements": {"level": 50}
}