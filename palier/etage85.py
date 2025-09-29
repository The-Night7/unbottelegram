# -*- coding: utf-8 -*-

# Informations sur l'étage 85
FLOOR_85_INFO = {
    "name": "Floor 85 - Crystalline Wasteland",
    "description": "Un étage composé de vastes plaines de cristal et de formations minérales géantes. La ville principale, Crystalline Wasteland, est taillée dans un gigantesque cristal bleu et scintille de mille feux.",
    "boss": {
        "name": "Adamantius the Crystal Tyrant",
        "level": 100,
        "hp": 12000,
        "attack": 140,
        "defense": 120,
        "exp": 6000,
        "col": 30000,
        "drops": {"Perfect Crystal": 1.0, "Diamond Edge": 0.3},
        "description": "Un colosse de cristal vivant dont le corps reflète et amplifie la lumière. Il peut créer des clones de cristal, lancer des éclats tranchants et absorber l'énergie des attaques pour se renforcer.",
        "required_level": 95,
        "min_party_size": 10
    },
    "safe_zones": ["Crystalline Wasteland", "Prism Haven", "Refraction Point"],
    "danger_level": 10,
    "recommended_level": 90,
    "biomes": [
        {
            "name": "Crystal Plains",
            "description": "Des plaines où le sol est fait de cristal transparent et où d'étranges formations minérales s'élèvent vers le ciel, habitées par des créatures cristallines.",
            "monsters": ["Crystal Golem", "Prism Beast"],
            "quests": ["q517", "q518"],
            "level_range": [90, 93],
            "unlock_requirements": None
        },
        {
            "name": "Gemstone Caverns",
            "description": "Un réseau de grottes aux parois incrustées de pierres précieuses, où la lumière crée des motifs hypnotiques et où des gardiens minéraux protègent des trésors.",
            "monsters": ["Gem Guardian", "Living Diamond"],
            "quests": ["q519", "q520"],
            "level_range": [93, 97],
            "unlock_requirements": {"level": 92}
        },
        {
            "name": "Tyrant's Palace",
            "description": "Un palais éblouissant fait entièrement de cristaux parfaits, où le Tyran de Cristal règne sur son domaine minéral et attend les aventuriers.",
            "monsters": ["Crystal Knight", "Light Elemental"],
            "quests": ["q521", "q522"],
            "level_range": [97, 100],
            "unlock_requirements": {"level": 96, "quest_completed": "q520"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Thanatos the Death Lord"}
}