# -*- coding: utf-8 -*-

"""
Module d'informations sur les étages d'Aincrad.
Ce package contient les données détaillées sur les différents étages du jeu Sword Art Online.
"""

from .etage1 import FLOOR_1_INFO
from .etage2 import FLOOR_2_INFO
from .etage3 import FLOOR_3_INFO
from .etage22 import FLOOR_22_INFO
from .etage50 import FLOOR_50_INFO
from .etage55 import FLOOR_55_INFO
from .etage75 import FLOOR_75_INFO

# Dictionnaire regroupant toutes les informations des étages
FLOORS_INFO = {
    "Floor 1 - Tolbana": FLOOR_1_INFO,
    "Floor 2 - Urbus": FLOOR_2_INFO,
    "Floor 3 - Forest of Wandering": FLOOR_3_INFO,
    "Floor 22 - Forest House": FLOOR_22_INFO,
    "Floor 50 - Algade": FLOOR_50_INFO,
    "Floor 55 - Grandzam": FLOOR_55_INFO,
    "Floor 75 - Boss Room": FLOOR_75_INFO,
}

# Fonction pour obtenir les informations d'un étage spécifique
def get_floor_info(floor_name):
    """
    Récupère les informations détaillées d'un étage spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage (ex: "Floor 1 - Tolbana")
        
    Returns:
        dict: Les informations de l'étage ou None si l'étage n'existe pas
    """
    return FLOORS_INFO.get(floor_name)

# Fonction pour obtenir les informations du boss d'un étage spécifique
def get_boss_info(floor_name):
    """
    Récupère les informations du boss d'un étage spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage (ex: "Floor 1 - Tolbana")
        
    Returns:
        dict: Les informations du boss ou None si l'étage n'existe pas
    """
    floor_info = get_floor_info(floor_name)
    if floor_info:
        return floor_info.get("boss")
    return None

# Fonction pour obtenir les biomes d'un étage spécifique
def get_biomes(floor_name):
    """
    Récupère la liste des biomes d'un étage spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage (ex: "Floor 1 - Tolbana")
        
    Returns:
        list: La liste des biomes ou une liste vide si l'étage n'existe pas
    """
    floor_info = get_floor_info(floor_name)
    if floor_info:
        return [biome["name"] for biome in floor_info.get("biomes", [])]
    return []

# Fonction pour obtenir les informations d'un biome spécifique
def get_biome_info(floor_name, biome_name):
    """
    Récupère les informations détaillées d'un biome spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage (ex: "Floor 1 - Tolbana")
        biome_name (str): Le nom du biome (ex: "Plains of Beginning")
        
    Returns:
        dict: Les informations du biome ou None si le biome n'existe pas
    """
    floor_info = get_floor_info(floor_name)
    if floor_info:
        for biome in floor_info.get("biomes", []):
            if biome["name"] == biome_name:
                return biome
    return None

# Fonction pour obtenir les monstres d'un biome spécifique
def get_biome_monsters(floor_name, biome_name):
    """
    Récupère la liste des monstres d'un biome spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage (ex: "Floor 1 - Tolbana")
        biome_name (str): Le nom du biome (ex: "Plains of Beginning")
        
    Returns:
        list: La liste des monstres ou une liste vide si le biome n'existe pas
    """
    biome_info = get_biome_info(floor_name, biome_name)
    if biome_info:
        return biome_info.get("monsters", [])
    return []

# Fonction pour vérifier les conditions de déblocage d'un étage
def check_floor_unlock_requirements(player, floor_name):
    """
    Vérifie si un joueur remplit les conditions pour débloquer un étage.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage à vérifier
        
    Returns:
        tuple: (bool, str) - Un tuple contenant un booléen indiquant si l'étage est débloqué
               et un message explicatif
    """
    floor_info = get_floor_info(floor_name)
    if not floor_info:
        return False, "Étage inconnu"
    
    requirements = floor_info.get("unlock_requirements")
    if not requirements:
        return True, "Aucune condition requise"
    
    if "boss_defeated" in requirements:
        boss_name = requirements["boss_defeated"]
        if boss_name not in player.get("defeated_bosses", []):
            return False, f"Vous devez d'abord vaincre {boss_name}"
    
    if "level" in requirements and player.get("level", 1) < requirements["level"]:
        return False, f"Vous devez être au moins niveau {requirements['level']}"
    
    return True, "Conditions remplies"

# Fonction pour vérifier les conditions de déblocage d'un biome
def check_biome_unlock_requirements(player, floor_name, biome_name):
    """
    Vérifie si un joueur remplit les conditions pour débloquer un biome.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome à vérifier
        
    Returns:
        tuple: (bool, str) - Un tuple contenant un booléen indiquant si le biome est débloqué
               et un message explicatif
    """
    biome_info = get_biome_info(floor_name, biome_name)
    if not biome_info:
        return False, "Biome inconnu"
    
    requirements = biome_info.get("unlock_requirements")
    if not requirements:
        return True, "Aucune condition requise"
    
    if "level" in requirements and player.get("level", 1) < requirements["level"]:
        return False, f"Vous devez être au moins niveau {requirements['level']}"
    
    if "quest_completed" in requirements:
        quest_id = requirements["quest_completed"]
        if quest_id not in player.get("completed_quests", []):
            return False, f"Vous devez d'abord terminer la quête {quest_id}"
    
    return True, "Conditions remplies"