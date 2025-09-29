# -*- coding: utf-8 -*-

# Informations sur l'étage 91
FLOOR_91_INFO = {
    "name": "Floor 91 - Avalon",
    "description": "Un étage paradisiaque baigné dans une lumière dorée perpétuelle, avec des jardins luxuriants et des palais de marbre blanc. La ville principale, Avalon, est construite autour d'un lac aux eaux curatives.",
    "boss": {
        "name": "Elysium the Divine Guardian",
        "level": 96,
        "hp": 12200,
        "attack": 132,
        "defense": 122,
        "exp": 6100,
        "col": 30500,
        "drops": {"Divine Light": 1.0, "Guardian's Halo": 0.3},
        "description": "Un gardien céleste à l'apparence angélique qui protège les portes du paradis. Il manie une épée de lumière pure et peut invoquer des rayons divins qui purifient tout ce qu'ils touchent.",
        "required_level": 91,
        "min_party_size": 10
    },
    "safe_zones": ["Avalon", "Divine Gardens", "Healing Springs"],
    "danger_level": 10,
    "recommended_level": 86,
    "biomes": [
        {
            "name": "Blessed Fields",
            "description": "Des plaines où l'herbe semble faite d'or et où des créatures célestes se promènent paisiblement, mais attaquent ceux qu'elles jugent indignes.",
            "monsters": ["Celestial Guardian", "Light Elemental"],
            "quests": ["q547", "q548"],
            "level_range": [86, 89],
            "unlock_requirements": None
        },
        {
            "name": "Sacred Groves",
            "description": "Des forêts aux arbres argentés dont les feuilles chantent au vent, gardées par des esprits de la nature et des protecteurs divins.",
            "monsters": ["Grove Warden", "Divine Beast"],
            "quests": ["q549", "q550"],
            "level_range": [89, 93],
            "unlock_requirements": {"level": 88}
        },
        {
            "name": "Gates of Paradise",
            "description": "Un temple majestueux entouré de cascades de lumière, où le Gardien Divin attend les aventuriers pour juger s'ils sont dignes de continuer.",
            "monsters": ["Angelic Warrior", "Divine Judge"],
            "quests": ["q551", "q552"],
            "level_range": [93, 96],
            "unlock_requirements": {"level": 92, "quest_completed": "q550"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Crimson King"}
}