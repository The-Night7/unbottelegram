# -*- coding: utf-8 -*-

"""
Module d'intégration des informations des étages dans le bot SAO.
Ce module fournit des fonctions pour utiliser les données des étages dans le bot principal.
"""

from palier import (
    get_floor_info, get_boss_info, get_biomes, get_biome_info,
    get_biome_monsters, check_floor_unlock_requirements, check_biome_unlock_requirements
)

# Dictionnaire pour stocker les données des monstres par biome
MONSTERS_BY_BIOME = {}

# Initialisation des données de monstres
def init_monster_data():
    """
    Initialise les données des monstres pour chaque biome de chaque étage.
    Cette fonction doit être appelée au démarrage du bot.
    """
    from palier import FLOORS_INFO
    
    for floor_name, floor_data in FLOORS_INFO.items():
        for biome in floor_data.get("biomes", []):
            biome_name = biome["name"]
            monsters = biome.get("monsters", [])
            
            # Créer une clé unique pour chaque combinaison étage/biome
            key = f"{floor_name}:{biome_name}"
            MONSTERS_BY_BIOME[key] = monsters

# Fonction pour obtenir les monstres disponibles dans un biome spécifique
def get_available_monsters(floor_name, biome_name):
    """
    Récupère la liste des monstres disponibles dans un biome spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        list: La liste des noms des monstres disponibles
    """
    key = f"{floor_name}:{biome_name}"
    return MONSTERS_BY_BIOME.get(key, [])

# Fonction pour obtenir les informations d'un monstre spécifique
def get_monster_info(monster_name):
    """
    Récupère les informations d'un monstre spécifique.
    Cette fonction doit être complétée avec les données réelles des monstres.
    
    Args:
        monster_name (str): Le nom du monstre
        
    Returns:
        dict: Les informations du monstre ou None si le monstre n'existe pas
    """
    # Ces données devraient être complétées avec les informations réelles des monstres
    # Voici quelques exemples basés sur les monstres mentionnés dans les fichiers d'étages
    monster_data = {
        # Étage 1
        "Frenzy Boar": {
            "level": 1,
            "hp": 50,
            "attack": 5,
            "defense": 2,
            "exp": 10,
            "col": 30,
            "drops": {"Boar Meat": 0.8, "Boar Tusk": 0.3}
        },
        "Little Nepent": {
            "level": 2,
            "hp": 70,
            "attack": 7,
            "defense": 3,
            "exp": 15,
            "col": 40,
            "drops": {"Nepent Seed": 0.7, "Little Flower": 0.4}
        },
        "Dire Wolf": {
            "level": 3,
            "hp": 100,
            "attack": 10,
            "defense": 5,
            "exp": 25,
            "col": 60,
            "drops": {"Wolf Pelt": 0.7, "Wolf Fang": 0.4}
        },
        "Forest Kobold": {
            "level": 4,
            "hp": 120,
            "attack": 12,
            "defense": 6,
            "exp": 30,
            "col": 70,
            "drops": {"Kobold Fur": 0.6, "Kobold Claw": 0.3}
        },
        "Kobold Sentinel": {
            "level": 5,
            "hp": 150,
            "attack": 15,
            "defense": 8,
            "exp": 40,
            "col": 90,
            "drops": {"Kobold Leather": 0.6, "Bronze Sword": 0.2}
        },
        "Kobold Miner": {
            "level": 6,
            "hp": 170,
            "attack": 16,
            "defense": 9,
            "exp": 45,
            "col": 100,
            "drops": {"Kobold Ore": 0.7, "Mining Pick": 0.3}
        },
        
        # Étage 2
        "Wind Wasp": {
            "level": 10,
            "hp": 200,
            "attack": 20,
            "defense": 10,
            "exp": 60,
            "col": 120,
            "drops": {"Wasp Stinger": 0.7, "Wind Essence": 0.3}
        },
        "Bull": {
            "level": 12,
            "hp": 250,
            "attack": 25,
            "defense": 15,
            "exp": 80,
            "col": 150,
            "drops": {"Bull Horn": 0.6, "Bull Hide": 0.5}
        },
        "Rock Golem": {
            "level": 14,
            "hp": 300,
            "attack": 30,
            "defense": 25,
            "exp": 100,
            "col": 200,
            "drops": {"Rock Fragment": 0.8, "Earth Crystal": 0.2}
        },
        "Mountain Wolf": {
            "level": 15,
            "hp": 280,
            "attack": 32,
            "defense": 18,
            "exp": 110,
            "col": 220,
            "drops": {"Mountain Wolf Pelt": 0.7, "Sharp Fang": 0.4}
        },
        "Taurus Warrior": {
            "level": 18,
            "hp": 350,
            "attack": 35,
            "defense": 25,
            "exp": 130,
            "col": 250,
            "drops": {"Taurus Horn": 0.6, "Warrior Axe": 0.2}
        },
        "Cave Bat": {
            "level": 16,
            "hp": 200,
            "attack": 28,
            "defense": 15,
            "exp": 90,
            "col": 180,
            "drops": {"Bat Wing": 0.8, "Echo Crystal": 0.3}
        },
        
        # Étage 3
        "Venomous Spider": {
            "level": 20,
            "hp": 300,
            "attack": 35,
            "defense": 20,
            "exp": 150,
            "col": 280,
            "drops": {"Spider Silk": 0.7, "Venom Sac": 0.4}
        },
        "Forest Wolf": {
            "level": 22,
            "hp": 350,
            "attack": 38,
            "defense": 22,
            "exp": 170,
            "col": 300,
            "drops": {"Forest Wolf Pelt": 0.7, "Wolf Heart": 0.3}
        },
        "Forest Elf": {
            "level": 24,
            "hp": 400,
            "attack": 40,
            "defense": 25,
            "exp": 200,
            "col": 350,
            "drops": {"Elven Bow": 0.3, "Elven Cloth": 0.5}
        },
        "Elven Scout": {
            "level": 25,
            "hp": 380,
            "attack": 45,
            "defense": 20,
            "exp": 210,
            "col": 370,
            "drops": {"Scout Dagger": 0.3, "Elven Map": 0.2}
        },
        "Treant Sapling": {
            "level": 28,
            "hp": 500,
            "attack": 42,
            "defense": 30,
            "exp": 250,
            "col": 400,
            "drops": {"Living Wood": 0.8, "Forest Essence": 0.4}
        },
        "Forest Stalker": {
            "level": 30,
            "hp": 550,
            "attack": 48,
            "defense": 28,
            "exp": 280,
            "col": 450,
            "drops": {"Stalker Cloak": 0.3, "Shadow Essence": 0.2}
        },
        
        # Quelques exemples pour les autres étages
        "Lake Fish": {
            "level": 35,
            "hp": 600,
            "attack": 50,
            "defense": 30,
            "exp": 300,
            "col": 500,
            "drops": {"Fresh Fish": 0.9, "Fish Scale": 0.5}
        },
        "Water Sprite": {
            "level": 37,
            "hp": 550,
            "attack": 55,
            "defense": 25,
            "exp": 320,
            "col": 550,
            "drops": {"Water Essence": 0.7, "Sprite Dust": 0.4}
        },
        "Shadow Knight": {
            "level": 55,
            "hp": 1200,
            "attack": 75,
            "defense": 60,
            "exp": 600,
            "col": 1000,
            "drops": {"Shadow Armor": 0.3, "Dark Sword": 0.2}
        },
        "Bandit Rogue": {
            "level": 57,
            "hp": 1100,
            "attack": 80,
            "defense": 50,
            "exp": 620,
            "col": 1100,
            "drops": {"Thief's Dagger": 0.4, "Stolen Goods": 0.6}
        },
        "Death Knight": {
            "level": 90,
            "hp": 3000,
            "attack": 120,
            "defense": 100,
            "exp": 1500,
            "col": 3000,
            "drops": {"Death Blade": 0.2, "Cursed Armor": 0.3}
        }
    }
    
    return monster_data.get(monster_name)

# Fonction pour obtenir les informations d'un boss
def get_detailed_boss_info(boss_name):
    """
    Récupère les informations détaillées d'un boss spécifique.
    
    Args:
        boss_name (str): Le nom du boss
        
    Returns:
        dict: Les informations du boss ou None si le boss n'existe pas
    """
    # Parcourir tous les étages pour trouver le boss
    from palier import FLOORS_INFO
    
    for floor_name, floor_data in FLOORS_INFO.items():
        boss = floor_data.get("boss")
        if boss and boss.get("name") == boss_name:
            return boss
    
    return None

# Fonction pour générer un message d'information sur un étage
def generate_floor_info_message(floor_name):
    """
    Génère un message formaté avec les informations d'un étage.
    
    Args:
        floor_name (str): Le nom de l'étage
        
    Returns:
        str: Le message formaté ou un message d'erreur si l'étage n'existe pas
    """
    floor_info = get_floor_info(floor_name)
    if not floor_info:
        return "Informations sur cet étage non disponibles."
    
    boss_info = floor_info.get("boss", {})
    
    message = f"📜 **{floor_info['name']}** 📜\n\n"
    message += f"{floor_info['description']}\n\n"
    
    message += f"🔶 **Niveau de danger**: {floor_info['danger_level']}/10\n"
    message += f"🔶 **Niveau recommandé**: {floor_info['recommended_level']}+\n\n"
    
    message += "🏙️ **Zones sûres**:\n"
    for zone in floor_info.get("safe_zones", []):
        message += f"  • {zone}\n"
    
    message += "\n🌍 **Biomes**:\n"
    for biome in floor_info.get("biomes", []):
        message += f"  • {biome['name']} (Niv. {biome['level_range'][0]}-{biome['level_range'][1]})\n"
    
    message += f"\n👹 **Boss**: {boss_info.get('name')}\n"
    message += f"  Niveau: {boss_info.get('level')}\n"
    message += f"  HP: {boss_info.get('hp')}\n"
    message += f"  Niveau requis: {boss_info.get('required_level')}\n"
    message += f"  Taille minimale du groupe: {boss_info.get('min_party_size')}\n"
    message += f"  Description: {boss_info.get('description')}\n"
    
    return message

# Fonction pour générer un message d'information sur un biome
def generate_biome_info_message(floor_name, biome_name):
    """
    Génère un message formaté avec les informations d'un biome.
    
    Args:
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        str: Le message formaté ou un message d'erreur si le biome n'existe pas
    """
    biome_info = get_biome_info(floor_name, biome_name)
    if not biome_info:
        return "Informations sur ce biome non disponibles."
    
    message = f"🌿 **{biome_name}** 🌿\n\n"
    message += f"{biome_info['description']}\n\n"
    
    message += f"🔶 **Niveau**: {biome_info['level_range'][0]}-{biome_info['level_range'][1]}\n\n"
    
    message += "🐺 **Monstres**:\n"
    for monster in biome_info.get("monsters", []):
        monster_info = get_monster_info(monster)
        if monster_info:
            message += f"  • {monster} (Niv. {monster_info['level']})\n"
        else:
            message += f"  • {monster}\n"
    
    message += "\n📋 **Quêtes disponibles**:\n"
    for quest in biome_info.get("quests", []):
        message += f"  • {quest}\n"
    
    return message

# Fonction pour vérifier si un joueur peut accéder à un biome
def can_access_biome(player, floor_name, biome_name):
    """
    Vérifie si un joueur peut accéder à un biome spécifique.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        tuple: (bool, str) - Un tuple contenant un booléen indiquant si le joueur peut accéder au biome
               et un message explicatif
    """
    # Vérifier d'abord si le joueur peut accéder à l'étage
    can_access_floor, floor_message = check_floor_unlock_requirements(player, floor_name)
    if not can_access_floor:
        return False, floor_message
    
    # Ensuite, vérifier si le joueur peut accéder au biome
    return check_biome_unlock_requirements(player, floor_name, biome_name)

# Fonction pour obtenir les biomes accessibles pour un joueur sur un étage
def get_accessible_biomes(player, floor_name):
    """
    Récupère la liste des biomes accessibles pour un joueur sur un étage spécifique.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage
        
    Returns:
        list: La liste des noms des biomes accessibles
    """
    floor_info = get_floor_info(floor_name)
    if not floor_info:
        return []
    
    accessible_biomes = []
    for biome in floor_info.get("biomes", []):
        can_access, _ = check_biome_unlock_requirements(player, floor_name, biome["name"])
        if can_access:
            accessible_biomes.append(biome["name"])
    
    return accessible_biomes

# Fonction pour obtenir les étages accessibles pour un joueur
def get_accessible_floors(player):
    """
    Récupère la liste des étages accessibles pour un joueur.
    
    Args:
        player (dict): Les données du joueur
        
    Returns:
        list: La liste des noms des étages accessibles
    """
    from palier import FLOORS_INFO
    
    accessible_floors = []
    for floor_name in FLOORS_INFO.keys():
        can_access, _ = check_floor_unlock_requirements(player, floor_name)
        if can_access:
            accessible_floors.append(floor_name)
    
    return accessible_floors