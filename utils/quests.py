# -*- coding: utf-8 -*-

# Quêtes du jeu organisées par étage et par biome

# Quêtes de l'étage 1
FLOOR_1_QUESTS = {
    # Biome: Plains of Beginning
    "q1": {
        "id": "q1",
        "title": "Boar Hunt",
        "description": "Défaites 5 Frenzy Boars dans les plaines autour de la Ville des Débuts.",
        "target": {"monster": "Frenzy Boar", "count": 5},
        "reward": {"exp": 50, "col": 100, "items": {"Health Potion": 2}},
        "biome": "Plains of Beginning",
        "level_requirement": 1
    },
    "q4": {
        "id": "q4",
        "title": "Nepent Clearing",
        "description": "Éliminez 3 Little Nepents qui envahissent les chemins des plaines.",
        "target": {"monster": "Little Nepent", "count": 3},
        "reward": {"exp": 60, "col": 120, "items": {"Antidote Crystal": 1}},
        "biome": "Plains of Beginning",
        "level_requirement": 2
    },
    
    # Biome: Tolbana Forest
    "q2": {
        "id": "q2",
        "title": "Wolf Menace",
        "description": "Éliminez 3 Dire Wolves qui menacent les voyageurs dans la forêt de Tolbana.",
        "target": {"monster": "Dire Wolf", "count": 3},
        "reward": {"exp": 100, "col": 200, "items": {"Teleport Crystal": 1}},
        "biome": "Tolbana Forest",
        "level_requirement": 3
    },
    "q5": {
        "id": "q5",
        "title": "Forest Patrol",
        "description": "Patrouille dans la forêt de Tolbana et éliminez 4 Forest Kobolds.",
        "target": {"monster": "Forest Kobold", "count": 4},
        "reward": {"exp": 120, "col": 220, "items": {"Forest Map": 1}},
        "biome": "Tolbana Forest",
        "level_requirement": 4
    },
    
    # Biome: Kobold Caves
    "q3": {
        "id": "q3",
        "title": "Kobold Invasion",
        "description": "Défaites 2 Kobold Sentinels qui ont envahi le village.",
        "target": {"monster": "Kobold Sentinel", "count": 2},
        "reward": {"exp": 150, "col": 300, "items": {"Strength Potion": 1}},
        "biome": "Kobold Caves",
        "level_requirement": 5
    },
    "q6": {
        "id": "q6",
        "title": "Mining Disruption",
        "description": "Perturbez les opérations minières des kobolds en éliminant 3 Kobold Miners.",
        "target": {"monster": "Kobold Miner", "count": 3},
        "reward": {"exp": 180, "col": 350, "items": {"Iron Ore": 5}},
        "biome": "Kobold Caves",
        "level_requirement": 6
    }
}

# Quêtes de l'étage 2
FLOOR_2_QUESTS = {
    # Biome: Rocky Plains
    "q7": {
        "id": "q7",
        "title": "Wasp Extermination",
        "description": "Éliminez 6 Wind Wasps qui perturbent les voyageurs dans les plaines rocheuses.",
        "target": {"monster": "Wind Wasp", "count": 6},
        "reward": {"exp": 200, "col": 400, "items": {"Wasp Honey": 3}},
        "biome": "Rocky Plains",
        "level_requirement": 10
    },
    "q8": {
        "id": "q8",
        "title": "Bull Run",
        "description": "Chassez 4 Bulls qui sont devenus trop agressifs près d'Urbus.",
        "target": {"monster": "Bull", "count": 4},
        "reward": {"exp": 220, "col": 450, "items": {"Bull Hide": 2}},
        "biome": "Rocky Plains",
        "level_requirement": 11
    },
    
    # Biome: Mountain Pass
    "q9": {
        "id": "q9",
        "title": "Golem Crusher",
        "description": "Détruisez 3 Rock Golems qui bloquent le passage dans les montagnes.",
        "target": {"monster": "Rock Golem", "count": 3},
        "reward": {"exp": 250, "col": 500, "items": {"Golem Core": 1}},
        "biome": "Mountain Pass",
        "level_requirement": 13
    },
    "q10": {
        "id": "q10",
        "title": "Wolf Pack",
        "description": "Éliminez la meute de 5 Mountain Wolves qui terrorise les mineurs.",
        "target": {"monster": "Mountain Wolf", "count": 5},
        "reward": {"exp": 280, "col": 550, "items": {"Wolf Alpha Fang": 1}},
        "biome": "Mountain Pass",
        "level_requirement": 14
    },
    
    # Biome: Taurus Caves
    "q11": {
        "id": "q11",
        "title": "Taurus Warriors",
        "description": "Infiltrez les grottes des taureaux et éliminez 3 Taurus Warriors.",
        "target": {"monster": "Taurus Warrior", "count": 3},
        "reward": {"exp": 320, "col": 600, "items": {"Taurus Horn": 2}},
        "biome": "Taurus Caves",
        "level_requirement": 16
    },
    "q12": {
        "id": "q12",
        "title": "Bat Swarm",
        "description": "Éliminez 8 Cave Bats qui perturbent l'exploration des grottes.",
        "target": {"monster": "Cave Bat", "count": 8},
        "reward": {"exp": 350, "col": 650, "items": {"Bat Wing": 5}},
        "biome": "Taurus Caves",
        "level_requirement": 17
    }
}

# Quêtes de l'étage 3
FLOOR_3_QUESTS = {
    # Biome: Forest Entrance
    "q13": {
        "id": "q13",
        "title": "Spider Nest",
        "description": "Détruisez un nid de Venomous Spiders en éliminant 5 d'entre elles.",
        "target": {"monster": "Venomous Spider", "count": 5},
        "reward": {"exp": 400, "col": 700, "items": {"Spider Silk": 3}},
        "biome": "Forest Entrance",
        "level_requirement": 20
    },
    "q14": {
        "id": "q14",
        "title": "Forest Wolves",
        "description": "Chassez 4 Forest Wolves qui attaquent les voyageurs à l'entrée de la forêt.",
        "target": {"monster": "Forest Wolf", "count": 4},
        "reward": {"exp": 420, "col": 750, "items": {"Wolf Meat": 4}},
        "biome": "Forest Entrance",
        "level_requirement": 21
    },
    
    # Biome: Elven Territory
    "q15": {
        "id": "q15",
        "title": "Elven Conflict",
        "description": "Affrontez 3 Forest Elves qui vous empêchent de traverser leur territoire.",
        "target": {"monster": "Forest Elf", "count": 3},
        "reward": {"exp": 450, "col": 800, "items": {"Elven Bow": 1}},
        "biome": "Elven Territory",
        "level_requirement": 23
    },
    "q16": {
        "id": "q16",
        "title": "Scout Elimination",
        "description": "Éliminez 4 Elven Scouts qui surveillent les intrus dans la forêt.",
        "target": {"monster": "Elven Scout", "count": 4},
        "reward": {"exp": 480, "col": 850, "items": {"Forest Map": 1}},
        "biome": "Elven Territory",
        "level_requirement": 24
    },
    
    # Biome: Deep Forest
    "q17": {
        "id": "q17",
        "title": "Living Trees",
        "description": "Combattez 3 Treant Saplings qui bloquent le chemin vers le cœur de la forêt.",
        "target": {"monster": "Treant Sapling", "count": 3},
        "reward": {"exp": 520, "col": 900, "items": {"Ancient Wood": 2}},
        "biome": "Deep Forest",
        "level_requirement": 26
    },
    "q18": {
        "id": "q18",
        "title": "Forest Stalkers",
        "description": "Traquez et éliminez 2 Forest Stalkers, des créatures furtives qui attaquent par surprise.",
        "target": {"monster": "Forest Stalker", "count": 2},
        "reward": {"exp": 550, "col": 950, "items": {"Stalker Cloak": 1}},
        "biome": "Deep Forest",
        "level_requirement": 27
    }
}

# Quêtes de l'étage 22
FLOOR_22_QUESTS = {
    # Biome: Peaceful Lake
    "q19": {
        "id": "q19",
        "title": "Fishing Trouble",
        "description": "Capturez 3 Lake Fish agressifs qui attaquent les pêcheurs.",
        "target": {"monster": "Lake Fish", "count": 3},
        "reward": {"exp": 700, "col": 1200, "items": {"Fish Scale Armor": 1}},
        "biome": "Peaceful Lake",
        "level_requirement": 35
    },
    "q20": {
        "id": "q20",
        "title": "Water Sprites",
        "description": "Apaisez 4 Water Sprites en colère qui perturbent l'équilibre du lac.",
        "target": {"monster": "Water Sprite", "count": 4},
        "reward": {"exp": 730, "col": 1250, "items": {"Water Crystal": 2}},
        "biome": "Peaceful Lake",
        "level_requirement": 36
    },
    
    # Biome: Dense Woods
    "q21": {
        "id": "q21",
        "title": "Bear Hunt",
        "description": "Chassez 2 Forest Bears qui menacent les habitants de la forêt.",
        "target": {"monster": "Forest Bear", "count": 2},
        "reward": {"exp": 760, "col": 1300, "items": {"Bear Pelt": 1}},
        "biome": "Dense Woods",
        "level_requirement": 38
    },
    "q22": {
        "id": "q22",
        "title": "Alpha Boar",
        "description": "Traquez et éliminez 1 Wild Boar Alpha, le chef d'une harde de sangliers.",
        "target": {"monster": "Wild Boar Alpha", "count": 1},
        "reward": {"exp": 800, "col": 1400, "items": {"Alpha Tusk": 1}},
        "biome": "Dense Woods",
        "level_requirement": 40
    },
    
    # Biome: Cloudy Peaks
    "q23": {
        "id": "q23",
        "title": "Wind Riders",
        "description": "Affrontez 3 Wind Riders qui créent des tempêtes dangereuses.",
        "target": {"monster": "Wind Rider", "count": 3},
        "reward": {"exp": 850, "col": 1500, "items": {"Wind Crystal": 2}},
        "biome": "Cloudy Peaks",
        "level_requirement": 42
    },
    "q24": {
        "id": "q24",
        "title": "Cloud Elementals",
        "description": "Dispersez 4 Cloud Elementals qui obscurcissent le ciel.",
        "target": {"monster": "Cloud Elemental", "count": 4},
        "reward": {"exp": 900, "col": 1600, "items": {"Cloud Essence": 3}},
        "biome": "Cloudy Peaks",
        "level_requirement": 43
    }
}

# Quêtes de l'étage 50
FLOOR_50_QUESTS = {
    # Biome: City Outskirts
    "q25": {
        "id": "q25",
        "title": "Shadow Knights",
        "description": "Éliminez 3 Shadow Knights qui terrorisent les faubourgs d'Algade.",
        "target": {"monster": "Shadow Knight", "count": 3},
        "reward": {"exp": 1100, "col": 2000, "items": {"Shadow Essence": 2}},
        "biome": "City Outskirts",
        "level_requirement": 55
    },
    "q26": {
        "id": "q26",
        "title": "Bandit Cleanup",
        "description": "Capturez ou éliminez 5 Bandit Rogues qui volent les marchands.",
        "target": {"monster": "Bandit Rogue", "count": 5},
        "reward": {"exp": 1150, "col": 2100, "items": {"Thief's Dagger": 1}},
        "biome": "City Outskirts",
        "level_requirement": 56
    },
    
    # Biome: Underground Sewers
    "q27": {
        "id": "q27",
        "title": "Sewer Cleaning",
        "description": "Nettoyez les égouts en éliminant 4 Dark Dwellers.",
        "target": {"monster": "Dark Dweller", "count": 4},
        "reward": {"exp": 1200, "col": 2200, "items": {"Dark Crystal": 2}},
        "biome": "Underground Sewers",
        "level_requirement": 58
    },
    "q28": {
        "id": "q28",
        "title": "Plague Control",
        "description": "Éliminez 6 Plague Rats qui propagent une maladie dans les égouts.",
        "target": {"monster": "Plague Rat", "count": 6},
        "reward": {"exp": 1250, "col": 2300, "items": {"Antidote Crystal": 3}},
        "biome": "Underground Sewers",
        "level_requirement": 60
    },
    
    # Biome: Ancient Ruins
    "q29": {
        "id": "q29",
        "title": "Elemental Disruption",
        "description": "Détruisez 2 Granite Elementals qui gardent l'entrée des ruines.",
        "target": {"monster": "Granite Elemental", "count": 2},
        "reward": {"exp": 1300, "col": 2500, "items": {"Earth Crystal": 3}},
        "biome": "Ancient Ruins",
        "level_requirement": 62
    },
    "q30": {
        "id": "q30",
        "title": "Guardian Challenge",
        "description": "Affrontez et vainquez 1 Ruin Guardian, le protecteur des secrets anciens.",
        "target": {"monster": "Ruin Guardian", "count": 1},
        "reward": {"exp": 1400, "col": 2800, "items": {"Guardian's Shield": 1}},
        "biome": "Ancient Ruins",
        "level_requirement": 64
    }
}

# Quêtes de l'étage 55
FLOOR_55_QUESTS = {
    # Biome: Fortress Outskirts
    "q31": {
        "id": "q31",
        "title": "Corrupted Knights",
        "description": "Éliminez 3 Knights of Blood corrompus qui patrouillent autour de la forteresse.",
        "target": {"monster": "Knight of Blood", "count": 3},
        "reward": {"exp": 1500, "col": 3000, "items": {"Blood Crystal": 2}},
        "biome": "Fortress Outskirts",
        "level_requirement": 65
    },
    "q32": {
        "id": "q32",
        "title": "Squire Hunt",
        "description": "Traquez et éliminez 5 Corrupted Squires qui servent les chevaliers corrompus.",
        "target": {"monster": "Corrupted Squire", "count": 5},
        "reward": {"exp": 1550, "col": 3100, "items": {"Squire's Sword": 1}},
        "biome": "Fortress Outskirts",
        "level_requirement": 66
    },
    
    # Biome: Iron Mines
    "q33": {
        "id": "q33",
        "title": "Golem Destruction",
        "description": "Détruisez 2 Iron Golems qui empêchent l'accès aux mines.",
        "target": {"monster": "Iron Golem", "count": 2},
        "reward": {"exp": 1600, "col": 3300, "items": {"Iron Ingot": 5}},
        "biome": "Iron Mines",
        "level_requirement": 68
    },
    "q34": {
        "id": "q34",
        "title": "Mine Clearance",
        "description": "Nettoyez les mines en éliminant 4 Mine Dwellers.",
        "target": {"monster": "Mine Dweller", "count": 4},
        "reward": {"exp": 1650, "col": 3500, "items": {"Rare Ore": 3}},
        "biome": "Iron Mines",
        "level_requirement": 70
    },
    
    # Biome: Fortress Interior
    "q35": {
        "id": "q35",
        "title": "Gargoyle Hunt",
        "description": "Détruisez 3 Steel Gargoyles qui gardent les couloirs de la forteresse.",
        "target": {"monster": "Steel Gargoyle", "count": 3},
        "reward": {"exp": 1700, "col": 3800, "items": {"Steel Wing": 2}},
        "biome": "Fortress Interior",
        "level_requirement": 72
    },
    "q36": {
        "id": "q36",
        "title": "Animated Armor",
        "description": "Affrontez et détruisez 2 Animated Armors, des armures enchantées qui protègent la salle du boss.",
        "target": {"monster": "Animated Armor", "count": 2},
        "reward": {"exp": 1800, "col": 4000, "items": {"Enchanted Plate": 1}},
        "biome": "Fortress Interior",
        "level_requirement": 74
    }
}

# Quêtes de l'étage 75
FLOOR_75_QUESTS = {
    # Biome: Desolate Plains
    "q37": {
        "id": "q37",
        "title": "Elite Knights",
        "description": "Affrontez et vainquez 2 Shadow Knight Elites, les plus puissants chevaliers corrompus.",
        "target": {"monster": "Shadow Knight Elite", "count": 2},
        "reward": {"exp": 2000, "col": 5000, "items": {"Elite Shadow Crystal": 1}},
        "biome": "Desolate Plains",
        "level_requirement": 80
    },
    "q38": {
        "id": "q38",
        "title": "Deathbringer Challenge",
        "description": "Éliminez 1 Deathbringer, un puissant serviteur du Skull Reaper.",
        "target": {"monster": "Deathbringer", "count": 1},
        "reward": {"exp": 2200, "col": 5500, "items": {"Death Essence": 2}},
        "biome": "Desolate Plains",
        "level_requirement": 82
    },
    
    # Biome: Bone Valley
    "q39": {
        "id": "q39",
        "title": "Reaper's Minions",
        "description": "Éliminez 3 Skull Reaper Minions qui préparent l'arrivée de leur maître.",
        "target": {"monster": "Skull Reaper Minion", "count": 3},
        "reward": {"exp": 2400, "col": 6000, "items": {"Reaper Fragment": 3}},
        "biome": "Bone Valley",
        "level_requirement": 84
    },
    "q40": {
        "id": "q40",
        "title": "Bone Collector",
        "description": "Affrontez et vainquez 1 Bone Collector, une créature qui rassemble des ossements pour le Skull Reaper.",
        "target": {"monster": "Bone Collector", "count": 1},
        "reward": {"exp": 2600, "col": 6500, "items": {"Ancient Bone": 5}},
        "biome": "Bone Valley",
        "level_requirement": 86
    },
    
    # Biome: Path to the Boss
    "q41": {
        "id": "q41",
        "title": "Gleam Eyes",
        "description": "Affrontez et vainquez le terrible Gleam Eyes, un démon qui garde le chemin vers le boss final.",
        "target": {"monster": "Gleam Eyes", "count": 1},
        "reward": {"exp": 3000, "col": 8000, "items": {"Gleaming Crystal": 1}},
        "biome": "Path to the Boss",
        "level_requirement": 88
    },
    "q42": {
        "id": "q42",
        "title": "Death Knight",
        "description": "Éliminez 1 Death Knight, le dernier obstacle avant d'atteindre le Skull Reaper.",
        "target": {"monster": "Death Knight", "count": 1},
        "reward": {"exp": 3200, "col": 9000, "items": {"Death Knight's Sword": 1}},
        "biome": "Path to the Boss",
        "level_requirement": 89
    }
}

# Regroupement de toutes les quêtes
ALL_QUESTS = {}
ALL_QUESTS.update(FLOOR_1_QUESTS)
ALL_QUESTS.update(FLOOR_2_QUESTS)
ALL_QUESTS.update(FLOOR_3_QUESTS)
ALL_QUESTS.update(FLOOR_22_QUESTS)
ALL_QUESTS.update(FLOOR_50_QUESTS)
ALL_QUESTS.update(FLOOR_55_QUESTS)
ALL_QUESTS.update(FLOOR_75_QUESTS)