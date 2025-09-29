# -*- coding: utf-8 -*-

# Informations sur l'étage 99
FLOOR_99_INFO = {
    "name": "Floor 99 - Empyrean",
    "description": "L'avant-dernier étage d'Aincrad, un royaume céleste aux confins de la réalité. La ville principale, Empyrean, semble construite à partir de lumière solidifiée et de matériaux impossibles.",
    "boss": {
        "name": "Metatron the Voice of God",
        "level": 104,
        "hp": 13800,
        "attack": 148,
        "defense": 138,
        "exp": 6900,
        "col": 34500,
        "drops": {"Divine Scripture": 1.0, "Voice of Creation": 0.3},
        "description": "Le plus puissant des anges, dont les paroles peuvent altérer la réalité. Il est entouré d'yeux flottants qui voient tout et peut prononcer des mots de pouvoir qui causent des effets dévastateurs.",
        "required_level": 99,
        "min_party_size": 10
    },
    "safe_zones": ["Empyrean", "Final Haven", "Gateway Sanctuary"],
    "danger_level": 10,
    "recommended_level": 94,
    "biomes": [
        {
            "name": "Crystal Spires",
            "description": "Des tours de cristal qui s'élèvent jusqu'aux nuages, reflétant la lumière en mille couleurs et abritant des créatures faites de lumière pure.",
            "monsters": ["Light Elemental", "Crystal Guardian"],
            "quests": ["q595", "q596"],
            "level_range": [94, 97],
            "unlock_requirements": None
        },
        {
            "name": "Ethereal Plains",
            "description": "Des plaines où la matière semble à peine solide, où les aventuriers peuvent flotter légèrement au-dessus du sol et où des entités éthérées se déplacent gracieusement.",
            "monsters": ["Ethereal Entity", "Transcendent Being"],
            "quests": ["q597", "q598"],
            "level_range": [97, 101],
            "unlock_requirements": {"level": 96}
        },
        {
            "name": "Gates of Destiny",
            "description": "L'ultime épreuve avant le dernier étage, un sanctuaire où Metatron juge ceux qui cherchent à défier le créateur d'Aincrad.",
            "monsters": ["Destiny Weaver", "Divine Herald"],
            "quests": ["q599", "q600"],
            "level_range": [101, 104],
            "unlock_requirements": {"level": 100, "quest_completed": "q598"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Seraphim the Archangel"}
}