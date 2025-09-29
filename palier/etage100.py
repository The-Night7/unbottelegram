# -*- coding: utf-8 -*-

# Informations sur l'étage 100
FLOOR_100_INFO = {
    "name": "Floor 100 - Ruby Palace",
    "description": "L'étage final d'Aincrad, dominé par l'imposant Palais de Rubis. Cet étage légendaire est l'objectif ultime de tous les joueurs, car c'est ici que se trouve le boss final du jeu.",
    "boss": {
        "name": "Heathcliff, The Final Guardian",
        "level": 100,
        "hp": 15000,
        "attack": 150,
        "defense": 150,
        "exp": 10000,
        "col": 50000,
        "drops": {"Liberator's Sword": 1.0, "Shield of Immortality": 0.3},
        "description": "Le créateur même du jeu, Akihiko Kayaba, sous sa forme d'avatar. Il maîtrise parfaitement l'épée et le bouclier, possède une vitesse de réaction surhumaine et dispose d'un bouclier divin qui le rend presque invincible.",
        "required_level": 95,
        "min_party_size": 12
    },
    "safe_zones": ["Final Haven", "Knights' Rest", "Last Sanctuary"],
    "danger_level": 10,
    "recommended_level": 95,
    "biomes": [
        {
            "name": "Path of Heroes",
            "description": "Une route pavée de marbre blanc qui mène au Palais de Rubis, bordée de statues représentant les grands héros tombés au combat.",
            "monsters": ["Guardian Knight", "Immortal Sentinel"],
            "quests": ["q91", "q92"],
            "level_range": [95, 97],
            "unlock_requirements": None
        },
        {
            "name": "Crystal Gardens",
            "description": "Des jardins magnifiques entourant le palais, où des fleurs de cristal poussent et où des créatures d'une beauté mortelle rôdent.",
            "monsters": ["Crystal Fairy", "Diamond Beast"],
            "quests": ["q93", "q94"],
            "level_range": [97, 99],
            "unlock_requirements": {"level": 96}
        },
        {
            "name": "Ruby Throne Room",
            "description": "La salle du trône au cœur du Palais de Rubis, où le boss final attend les joueurs pour le combat ultime qui déterminera le sort de tous.",
            "monsters": ["Royal Protector", "Divine Guardian"],
            "quests": ["q95", "q96"],
            "level_range": [99, 100],
            "unlock_requirements": {"level": 98, "quest_completed": "q94"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Eternus the Timeless One", "level": 95}
}