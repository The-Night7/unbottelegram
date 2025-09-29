# -*- coding: utf-8 -*-

# Informations sur l'étage 62
FLOOR_62_INFO = {
    "name": "Floor 62 - Kamdet",
    "description": "Un étage dominé par des canyons de cristal et des formations minérales aux couleurs chatoyantes. La ville principale, Kamdet, est taillée directement dans un gigantesque cristal bleu.",
    "boss": {
        "name": "Crystallis the Gem Lord",
        "level": 82,
        "hp": 7200,
        "attack": 97,
        "defense": 92,
        "exp": 3600,
        "col": 15500,
        "drops": {"Perfect Crystal": 1.0, "Prismatic Blade": 0.3},
        "description": "Un être de cristal vivant qui peut manipuler la lumière et l'énergie. Son corps est composé de gemmes précieuses et il peut se fragmenter en multiples copies plus petites.",
        "required_level": 77,
        "min_party_size": 8
    },
    "safe_zones": ["Kamdet", "Gem Haven", "Crystal Refuge"],
    "danger_level": 8,
    "recommended_level": 74,
    "biomes": [
        {
            "name": "Crystal Canyon",
            "description": "Des canyons aux parois de cristal qui réfractent la lumière en créant des arcs-en-ciel permanents, habités par des créatures cristallines.",
            "monsters": ["Crystal Golem", "Prism Beast"],
            "quests": ["q391", "q392"],
            "level_range": [74, 77],
            "unlock_requirements": None
        },
        {
            "name": "Gemstone Mines",
            "description": "Des mines profondes où l'on extrait des gemmes aux propriétés magiques, gardées par des constructions minérales et des élémentaires.",
            "monsters": ["Gem Elemental", "Mine Guardian"],
            "quests": ["q393", "q394"],
            "level_range": [77, 80],
            "unlock_requirements": {"level": 76}
        },
        {
            "name": "Crystalline Throne",
            "description": "Une salle du trône faite entièrement de cristaux parfaits, où le Seigneur des Gemmes attend les aventuriers entouré de ses serviteurs de cristal.",
            "monsters": ["Crystal Knight", "Light Weaver"],
            "quests": ["q395", "q396"],
            "level_range": [80, 82],
            "unlock_requirements": {"level": 79, "quest_completed": "q394"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Mycelia the Spore Queen"}
}