# -*- coding: utf-8 -*-

# Dictionnaire regroupant tous les monstres
MONSTERS = {
    # Étage 1
    "Frenzy Boar": {
        "level": 1,
        "hp": 50,
        "attack": 5,
        "defense": 2,
        "exp": 10,
        "col": 30,
        "drops": {"Boar Meat": 0.8, "Boar Tusk": 0.3},
        "description": "Un sanglier sauvage qui erre dans les plaines autour de la Ville des Débuts. Parfait pour les débutants.",
        "floor": 1,
        "type": "Beast"
    },
    "Dire Wolf": {
        "level": 5,
        "hp": 120,
        "attack": 12,
        "defense": 5,
        "exp": 25,
        "col": 60,
        "drops": {"Wolf Pelt": 0.7, "Wolf Fang": 0.4},
        "description": "Un loup féroce qui chasse en meute dans les forêts du premier étage.",
        "floor": 1,
        "type": "Beast"
    },
    "Little Nepent": {
        "level": 3,
        "hp": 80,
        "attack": 8,
        "defense": 3,
        "exp": 15,
        "col": 40,
        "drops": {"Nepent Seed": 0.6, "Little Flower": 0.5},
        "description": "Une plante carnivore qui attaque les joueurs imprudents dans les forêts.",
        "floor": 1,
        "type": "Plant"
    },

    # Étage 2
    "Wind Wasp": {
        "level": 7,
        "hp": 100,
        "attack": 15,
        "defense": 4,
        "exp": 30,
        "col": 70,
        "drops": {"Wasp Stinger": 0.7, "Wasp Wing": 0.5},
        "description": "Un insecte volant agressif qui attaque en groupe.",
        "floor": 2,
        "type": "Insect"
    },
    "Bull": {
        "level": 8,
        "hp": 180,
        "attack": 18,
        "defense": 8,
        "exp": 35,
        "col": 80,
        "drops": {"Bull Horn": 0.6, "Bull Hide": 0.5},
        "description": "Un taureau massif qui charge les joueurs dans les plaines rocheuses.",
        "floor": 2,
        "type": "Beast"
    },
    "Rock Golem": {
        "level": 10,
        "hp": 250,
        "attack": 15,
        "defense": 15,
        "exp": 45,
        "col": 90,
        "drops": {"Rock Fragment": 0.8, "Golem Core": 0.3},
        "description": "Un monstre de pierre qui se confond avec les rochers jusqu'à ce qu'il attaque.",
        "floor": 2,
        "type": "Elemental"
    },

    # Étage 3
    "Venomous Spider": {
        "level": 12,
        "hp": 150,
        "attack": 20,
        "defense": 8,
        "exp": 55,
        "col": 110,
        "drops": {"Spider Silk": 0.7, "Venom Sac": 0.4},
        "description": "Une araignée géante dont le venin peut affaiblir les joueurs.",
        "floor": 3,
        "type": "Insect"
    },
    "Forest Elf": {
        "level": 15,
        "hp": 180,
        "attack": 22,
        "defense": 12,
        "exp": 70,
        "col": 150,
        "drops": {"Elven Bow": 0.3, "Forest Herb": 0.6},
        "description": "Un elfe hostile qui protège la forêt avec son arc.",
        "floor": 3,
        "type": "Humanoid"
    },
    "Treant Sapling": {
        "level": 14,
        "hp": 220,
        "attack": 18,
        "defense": 15,
        "exp": 65,
        "col": 130,
        "drops": {"Ancient Wood": 0.5, "Life Seed": 0.2},
        "description": "Un jeune arbre animé qui frappe avec ses branches.",
        "floor": 3,
        "type": "Plant"
    },
    
    # Étage 22
    "Forest Bear": {
        "level": 30,
        "hp": 400,
        "attack": 35,
        "defense": 25,
        "exp": 150,
        "col": 250,
        "drops": {"Bear Pelt": 0.7, "Bear Claw": 0.5},
        "description": "Un ours massif qui rôde dans les forêts paisibles de l'étage 22.",
        "floor": 22,
        "type": "Beast"
    },
    "Lake Fish": {
        "level": 28,
        "hp": 300,
        "attack": 30,
        "defense": 20,
        "exp": 130,
        "col": 220,
        "drops": {"Fish Scale": 0.8, "Fish Fin": 0.4},
        "description": "Un poisson géant qui attaque les joueurs qui nagent dans le lac.",
        "floor": 22,
        "type": "Aquatic"
    },
    "Wind Rider": {
        "level": 32,
        "hp": 350,
        "attack": 38,
        "defense": 22,
        "exp": 160,
        "col": 280,
        "drops": {"Wind Crystal": 0.5, "Feather": 0.7},
        "description": "Une créature volante qui utilise le vent pour attaquer.",
        "floor": 22,
        "type": "Avian"
    },
    
    # Étage 50
    "Shadow Knight": {
        "level": 60,
        "hp": 700,
        "attack": 65,
        "defense": 50,
        "exp": 300,
        "col": 450,
        "drops": {"Shadow Armor": 0.4, "Dark Sword": 0.3},
        "description": "Un chevalier corrompu qui utilise des attaques d'ombre.",
        "floor": 50,
        "type": "Humanoid"
    },
    "Dark Dweller": {
        "level": 58,
        "hp": 650,
        "attack": 60,
        "defense": 45,
        "exp": 280,
        "col": 420,
        "drops": {"Shadow Essence": 0.6, "Dark Crystal": 0.4},
        "description": "Une créature des ténèbres qui se cache dans les ombres d'Algade.",
        "floor": 50,
        "type": "Demon"
    },
    "Granite Elemental": {
        "level": 62,
        "hp": 800,
        "attack": 55,
        "defense": 60,
        "exp": 320,
        "col": 480,
        "drops": {"Earth Crystal": 0.5, "Stone Fragment": 0.9},
        "description": "Un élémentaire de pierre massive qui ébranle le sol à chaque pas.",
        "floor": 50,
        "type": "Elemental"
    },
    
    # Étage 55
    "Iron Golem": {
        "level": 65,
        "hp": 900,
        "attack": 70,
        "defense": 65,
        "exp": 350,
        "col": 520,
        "drops": {"Iron Ingot": 0.8, "Golem Core": 0.4},
        "description": "Un golem de fer forgé par les meilleurs artisans pour protéger Grandzam.",
        "floor": 55,
        "type": "Construct"
    },
    "Knight of Blood": {
        "level": 68,
        "hp": 850,
        "attack": 75,
        "defense": 60,
        "exp": 370,
        "col": 550,
        "drops": {"Blood Crystal": 0.5, "Knight's Sword": 0.3},
        "description": "Un chevalier corrompu qui utilise des attaques de sang.",
        "floor": 55,
        "type": "Humanoid"
    },
    "Steel Gargoyle": {
        "level": 67,
        "hp": 800,
        "attack": 72,
        "defense": 68,
        "exp": 360,
        "col": 540,
        "drops": {"Steel Wing": 0.6, "Gargoyle Stone": 0.5},
        "description": "Une statue animée qui garde les toits de Grandzam.",
        "floor": 55,
        "type": "Construct"
    },
    
    # Étage 75
    "Gleam Eyes": {
        "level": 85,
        "hp": 1500,
        "attack": 100,
        "defense": 80,
        "exp": 500,
        "col": 1000,
        "drops": {"Boss Crystal": 1.0, "Gleaming Sword": 0.3},
        "description": "Un démon massif armé d'une épée géante, boss de l'étage 74.",
        "floor": 75,
        "type": "Boss"
    },
    "Skull Reaper Minion": {
        "level": 82,
        "hp": 1200,
        "attack": 95,
        "defense": 75,
        "exp": 450,
        "col": 800,
        "drops": {"Skull Fragment": 0.7, "Reaper Claw": 0.5},
        "description": "Un serviteur du redoutable Skull Reaper, boss de l'étage 75.",
        "floor": 75,
        "type": "Undead"
    },
    "Shadow Knight Elite": {
        "level": 80,
        "hp": 1100,
        "attack": 90,
        "defense": 70,
        "exp": 420,
        "col": 750,
        "drops": {"Elite Armor": 0.4, "Shadow Blade": 0.3},
        "description": "Un chevalier d'élite corrompu par les ténèbres, gardien de l'étage 75.",
        "floor": 75,
        "type": "Humanoid"
    }
}
