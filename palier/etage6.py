# -*- coding: utf-8 -*-

# Informations sur l'étage 6
FLOOR_6_INFO = {
    "name": "Floor 6 - Stormvale",
    "description": "Un étage balayé par des vents violents et des tempêtes fréquentes. La ville principale, Stormvale, est construite dans une vallée abritée des vents.",
    "boss": {
        "name": "Tempestus the Storm Lord",
        "level": 42,
        "hp": 2000,
        "attack": 55,
        "defense": 48,
        "exp": 1100,
        "col": 5500,
        "drops": {"Wind Crystal": 1.0, "Tempest Blade": 0.3},
        "description": "Un élémentaire d'air géant qui peut créer des tornades et projeter des éclairs. Il est capable de voler et de se déplacer très rapidement.",
        "required_level": 37,
        "min_party_size": 4
    },
    "safe_zones": ["Stormvale", "Windbreaker Village", "Calm Haven"],
    "danger_level": 4,
    "recommended_level": 32,
    "biomes": [
        {
            "name": "Windswept Plains",
            "description": "Des plaines constamment balayées par des vents violents, où vivent des créatures adaptées aux conditions extrêmes.",
            "monsters": ["Wind Serpent", "Storm Hawk"],
            "quests": ["q97", "q98"],
            "level_range": [32, 35],
            "unlock_requirements": None
        },
        {
            "name": "Lightning Ridge",
            "description": "Une chaîne de collines où s'abattent fréquemment des éclairs, habitée par des créatures électriques.",
            "monsters": ["Thunder Lizard", "Lightning Elemental"],
            "quests": ["q99", "q100"],
            "level_range": [35, 38],
            "unlock_requirements": {"level": 34}
        },
        {
            "name": "Eye of the Storm",
            "description": "Le centre d'une tempête perpétuelle où se trouve le repaire du boss, entouré de vents si violents qu'ils peuvent déchirer la chair.",
            "monsters": ["Cyclone Harpy", "Living Thundercloud"],
            "quests": ["q101", "q102"],
            "level_range": [38, 42],
            "unlock_requirements": {"level": 37, "quest_completed": "q100"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Fuscus the Vacant Colossus"}
}