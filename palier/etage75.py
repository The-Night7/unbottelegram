# -*- coding: utf-8 -*-

# Informations sur l'étage 75
FLOOR_75_INFO = {
    "name": "Floor 75 - Boss Room",
    "description": "L'un des étages les plus difficiles d'Aincrad. C'est ici que les joueurs ont affronté le terrible Skull Reaper.",
    "boss": {
        "name": "The Skull Reaper",
        "level": 90,
        "hp": 10000,
        "attack": 120,
        "defense": 100,
        "exp": 5000,
        "col": 25000,
        "drops": {"Skull Reaper Bone": 1.0, "Death Scythe": 0.3},
        "description": "Une créature cauchemardesque ressemblant à un centipède géant avec des faux en guise de pattes. Un seul coup peut tuer un joueur.",
        "required_level": 85,
        "min_party_size": 10
    },
    "safe_zones": ["Collinia", "Forward Base"],
    "danger_level": 10,
    "recommended_level": 80,
    "biomes": [
        {
            "name": "Desolate Plains",
            "description": "Des plaines stériles balayées par des vents glacials, où rôdent des chevaliers d'élite corrompus.",
            "monsters": ["Shadow Knight Elite", "Deathbringer"],
            "quests": ["q37", "q38"],
            "level_range": [80, 83],
            "unlock_requirements": None
        },
        {
            "name": "Bone Valley",
            "description": "Une vallée jonchée d'ossements de créatures gigantesques, habitée par des serviteurs du Skull Reaper.",
            "monsters": ["Skull Reaper Minion", "Bone Collector"],
            "quests": ["q39", "q40"],
            "level_range": [83, 87],
            "unlock_requirements": {"level": 82, "quest_completed": "q38"}
        },
        {
            "name": "Path to the Boss",
            "description": "Le chemin menant à la salle du boss, gardé par les plus puissantes créatures de l'étage.",
            "monsters": ["Gleam Eyes", "Death Knight"],
            "quests": ["q41", "q42"],
            "level_range": [87, 90],
            "unlock_requirements": {"level": 85, "quest_completed": "q40"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Adamantine Sentinel", "level": 80}
}