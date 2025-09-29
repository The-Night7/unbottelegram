# -*- coding: utf-8 -*-

# Informations sur l'étage 20
FLOOR_20_INFO = {
    "name": "Floor 20 - Sunshine Forest",
    "description": "Un étage baigné d'une lumière dorée perpétuelle, avec des forêts aux feuilles dorées et des clairières ensoleillées. La ville principale, Sunshine Forest, est construite dans une immense clairière.",
    "boss": {
        "name": "Solarius the Radiant",
        "level": 65,
        "hp": 4600,
        "attack": 88,
        "defense": 82,
        "exp": 2400,
        "col": 12000,
        "drops": {"Sun Fragment": 1.0, "Radiant Sword": 0.3},
        "description": "Un chevalier d'or vivant dont l'armure brille comme le soleil. Il peut aveugler ses adversaires avec des explosions de lumière et utiliser la chaleur pour renforcer ses attaques.",
        "required_level": 60,
        "min_party_size": 7
    },
    "safe_zones": ["Sunshine Forest", "Golden Glade", "Sunray Temple"],
    "danger_level": 7,
    "recommended_level": 58,
    "biomes": [
        {
            "name": "Golden Woods",
            "description": "Une forêt aux feuilles dorées qui scintillent sous la lumière perpétuelle, abritant des créatures bénéfiques et d'autres corrompues par trop de lumière.",
            "monsters": ["Sun Deer", "Blinded Wolf"],
            "quests": ["q175", "q176"],
            "level_range": [58, 60],
            "unlock_requirements": None
        },
        {
            "name": "Sunlight Meadows",
            "description": "Des prairies baignées d'une lumière si intense qu'elle peut brûler les imprudents, où vivent des créatures adaptées à cette luminosité extrême.",
            "monsters": ["Light Elemental", "Radiant Butterfly"],
            "quests": ["q177", "q178"],
            "level_range": [60, 63],
            "unlock_requirements": {"level": 59}
        },
        {
            "name": "Solar Shrine",
            "description": "Un temple ancien dédié au soleil, où le boss médite et absorbe l'énergie solaire pour augmenter sa puissance.",
            "monsters": ["Sun Priest", "Light Guardian"],
            "quests": ["q179", "q180"],
            "level_range": [63, 65],
            "unlock_requirements": {"level": 62, "quest_completed": "q178"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Terravore the Mountain Eater"}
}