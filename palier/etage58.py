# -*- coding: utf-8 -*-

# Informations sur l'étage 58
FLOOR_58_INFO = {
    "name": "Floor 58 - Arcadia",
    "description": "Un étage paradisiaque avec des jardins luxuriants et des cascades cristallines. La ville principale, Arcadia, est construite autour d'un lac aux propriétés curatives.",
    "boss": {
        "name": "Gaia the Life Mother",
        "level": 79,
        "hp": 6600,
        "attack": 94,
        "defense": 89,
        "exp": 3300,
        "col": 14000,
        "drops": {"Life Essence": 1.0, "Staff of Renewal": 0.3},
        "description": "Une entité féminine qui incarne la force vitale de la nature. Elle peut guérir ses blessures, faire pousser des plantes instantanément et communiquer avec toutes les créatures vivantes.",
        "required_level": 74,
        "min_party_size": 7
    },
    "safe_zones": ["Arcadia", "Healing Springs", "Garden Sanctuary"],
    "danger_level": 8,
    "recommended_level": 70,
    "biomes": [
        {
            "name": "Eternal Gardens",
            "description": "Des jardins parfaitement entretenus où poussent des fleurs aux propriétés magiques et où vivent des créatures paisibles.",
            "monsters": ["Garden Guardian", "Flower Sprite"],
            "quests": ["q373", "q374"],
            "level_range": [70, 73],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Falls",
            "description": "Une série de cascades aux eaux pures qui possèdent des propriétés curatives, gardées par des élémentaires d'eau et des nymphes.",
            "monsters": ["Water Elemental", "Cascade Nymph"],
            "quests": ["q375", "q376"],
            "level_range": [73, 76],
            "unlock_requirements": {"level": 72}
        },
        {
            "name": "Life Shrine",
            "description": "Un temple ancien au centre de l'étage, où la force vitale est à son apogée et où la Mère de la Vie attend les aventuriers.",
            "monsters": ["Nature's Warden", "Sacred Beast"],
            "quests": ["q377", "q378"],
            "level_range": [76, 79],
            "unlock_requirements": {"level": 75, "quest_completed": "q376"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Silvanus the Forest Ancient"}
}