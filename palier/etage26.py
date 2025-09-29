# -*- coding: utf-8 -*-

# Informations sur l'étage 26
FLOOR_26_INFO = {
    "name": "Floor 26 - Mistmoor",
    "description": "Un étage perpétuellement enveloppé dans un brouillard épais et traversé par des rivières sinueuses. La ville principale, Mistmoor, est construite sur pilotis au-dessus d'un marais.",
    "boss": {
        "name": "Fogwalker the Phantom",
        "level": 52,
        "hp": 3200,
        "attack": 67,
        "defense": 62,
        "exp": 1600,
        "col": 8500,
        "drops": {"Phantom Essence": 1.0, "Mist Walker's Cloak": 0.3},
        "description": "Un spectre insaisissable qui peut se matérialiser et se dématérialiser à volonté. Il utilise le brouillard pour créer des illusions et attaquer depuis des directions inattendues.",
        "required_level": 47,
        "min_party_size": 6
    },
    "safe_zones": ["Mistmoor", "Foggy Haven", "Riverside Camp"],
    "danger_level": 6,
    "recommended_level": 42,
    "biomes": [
        {
            "name": "Misty Marshes",
            "description": "Des marécages où le brouillard est si épais qu'on ne voit pas à deux mètres, habités par des créatures amphibies et des fantômes.",
            "monsters": ["Marsh Wraith", "Bog Creature"],
            "quests": ["q199", "q200"],
            "level_range": [42, 45],
            "unlock_requirements": None
        },
        {
            "name": "Phantom Forest",
            "description": "Une forêt où les arbres semblent se déplacer dans la brume et où des esprits errants attaquent les voyageurs.",
            "monsters": ["Wandering Spirit", "Mist Wolf"],
            "quests": ["q201", "q202"],
            "level_range": [45, 49],
            "unlock_requirements": {"level": 44}
        },
        {
            "name": "Ghost Ruins",
            "description": "Les vestiges d'une ancienne cité engloutie par le marais, où le boss et ses serviteurs fantomatiques ont établi leur domaine.",
            "monsters": ["Ruined Guardian", "Phantom Knight"],
            "quests": ["q203", "q204"],
            "level_range": [49, 52],
            "unlock_requirements": {"level": 48, "quest_completed": "q202"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Demonic Servant"}
}