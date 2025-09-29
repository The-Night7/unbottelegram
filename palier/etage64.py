# -*- coding: utf-8 -*-

# Informations sur l'étage 64
FLOOR_64_INFO = {
    "name": "Floor 64 - Rubel",
    "description": "Un étage composé d'îles volcaniques reliées par des ponts de pierre. La ville principale, Rubel, est construite dans le cratère d'un volcan éteint.",
    "boss": {
        "name": "Magmarus the Flame Titan",
        "level": 84,
        "hp": 7600,
        "attack": 99,
        "defense": 94,
        "exp": 3800,
        "col": 16500,
        "drops": {"Titan's Heart": 1.0, "Magma Greatsword": 0.3},
        "description": "Un titan de lave et de roche en fusion qui peut faire entrer les volcans en éruption à volonté. Son corps dégage une chaleur si intense qu'elle peut faire fondre les armes et armures.",
        "required_level": 79,
        "min_party_size": 8
    },
    "safe_zones": ["Rubel", "Cooling Springs", "Obsidian Haven"],
    "danger_level": 9,
    "recommended_level": 76,
    "biomes": [
        {
            "name": "Volcanic Shores",
            "description": "Des plages de sable noir et des côtes rocheuses où la lave rencontre l'océan, créant des nuages de vapeur et des formations de roche étranges.",
            "monsters": ["Lava Crawler", "Steam Elemental"],
            "quests": ["q403", "q404"],
            "level_range": [76, 79],
            "unlock_requirements": None
        },
        {
            "name": "Magma Chambers",
            "description": "Des cavernes souterraines où coule la lave en fusion et où la température est presque insupportable, habitées par des créatures résistantes à la chaleur extrême.",
            "monsters": ["Fire Elemental", "Magma Beast"],
            "quests": ["q405", "q406"],
            "level_range": [79, 82],
            "unlock_requirements": {"level": 78}
        },
        {
            "name": "Titan's Forge",
            "description": "Le cœur d'un volcan actif où le Titan de Flamme forge ses armes et attend les aventuriers dans un océan de lave bouillonnante.",
            "monsters": ["Flame Knight", "Lava Golem"],
            "quests": ["q407", "q408"],
            "level_range": [82, 84],
            "unlock_requirements": {"level": 81, "quest_completed": "q406"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Thornlash the Jungle Tyrant"}
}