#!/usr/bin/env python
# -*- coding: utf-8 -*-

from palier import (
    FLOORS_INFO, get_floor_info, get_biome_info, 
    check_floor_unlock_requirements, check_biome_unlock_requirements
)

def get_accessible_floors(player):
    """
    Récupère la liste des étages accessibles pour un joueur.
    
    Args:
        player (dict): Les données du joueur
        
    Returns:
        list: La liste des noms d'étages accessibles
    """
    accessible_floors = []
    
    for floor_name in FLOORS_INFO.keys():
        can_access, _ = check_floor_unlock_requirements(player, floor_name)
        if can_access:
            accessible_floors.append(floor_name)
    
    return accessible_floors


def get_accessible_biomes(player, floor_name):
    """
    Récupère la liste des biomes accessibles pour un joueur sur un étage donné.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage
        
    Returns:
        list: La liste des noms de biomes accessibles
    """
    accessible_biomes = []
    
    # Vérifier si l'étage est accessible
    can_access_floor, _ = check_floor_unlock_requirements(player, floor_name)
    if not can_access_floor:
        return accessible_biomes
    
    # Récupérer les informations sur l'étage
    floor_info = get_floor_info(floor_name)
    if not floor_info:
        return accessible_biomes
    
    # Parcourir les biomes de l'étage
    for biome in floor_info.get('biomes', []):
        biome_name = biome.get('name')
        if biome_name:
            can_access, _ = can_access_biome(player, floor_name, biome_name)
            if can_access:
                accessible_biomes.append(biome_name)
    
    return accessible_biomes


def can_access_biome(player, floor_name, biome_name):
    """
    Vérifie si un joueur peut accéder à un biome spécifique.
    
    Args:
        player (dict): Les données du joueur
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        tuple: (bool, str) - Un booléen indiquant si le biome est accessible et un message explicatif
    """
    # Vérifier si l'étage est accessible
    can_access_floor, floor_message = check_floor_unlock_requirements(player, floor_name)
    if not can_access_floor:
        return False, floor_message
    
    # Vérifier si le biome est accessible
    can_access_biome, biome_message = check_biome_unlock_requirements(player, floor_name, biome_name)
    if not can_access_biome:
        return False, biome_message
    
    # Vérifier si le joueur a déjà débloqué ce biome
    if "unlocked_biomes" in player:
        if floor_name in player["unlocked_biomes"]:
            if biome_name in player["unlocked_biomes"][floor_name]:
                return True, "Biome déjà débloqué"
    
    # Pour le premier biome de chaque étage, accès automatique
    floor_info = get_floor_info(floor_name)
    if floor_info and floor_info.get('biomes'):
        first_biome = floor_info['biomes'][0].get('name')
        if biome_name == first_biome:
            return True, "Premier biome de l'étage"
    
    # Par défaut, accès refusé
    return False, "Vous devez d'abord explorer les biomes précédents"


def generate_floor_info_message(floor_name):
    """
    Génère un message d'information détaillé sur un étage.
    
    Args:
        floor_name (str): Le nom de l'étage
        
    Returns:
        str: Le message d'information sur l'étage
    """
    floor_info = get_floor_info(floor_name)
    
    if not floor_info:
        return f"Aucune information disponible pour l'étage {floor_name}."
    
    # Construire le message d'information
    message = f"Informations sur {floor_name}:\n\n"
    message += f"Description: {floor_info.get('description', 'Aucune description disponible.')}\n\n"
    
    # Ajouter les informations sur les biomes
    message += "Biomes:\n"
    for biome in floor_info.get('biomes', []):
        biome_name = biome.get('name', 'Biome inconnu')
        biome_desc = biome.get('description', 'Aucune description disponible.')
        message += f"- {biome_name}: {biome_desc}\n"
    
    # Ajouter les informations sur le boss
    boss = floor_info.get('boss')
    if boss:
        message += f"\nBoss: {boss.get('name', 'Boss inconnu')}\n"
        message += f"Niveau requis: {boss.get('required_level', 'Non spécifié')}\n"
        message += f"Description: {boss.get('description', 'Aucune description disponible.')}\n"
    
    # Ajouter les conditions de déblocage pour l'étage suivant
    next_floor_name = None
    for name in FLOORS_INFO.keys():
        if name.startswith(f"Floor {int(floor_name.split(' ')[1]) + 1}"):
            next_floor_name = name
            break
    
    if next_floor_name and next_floor_name in FLOORS_INFO:
        next_floor = FLOORS_INFO[next_floor_name]
        requirements = next_floor.get('unlock_requirements', {})
        
        message += f"\nPour débloquer {next_floor_name}:\n"
        if "boss_defeated" in requirements:
            message += f"- Vaincre le boss: {requirements['boss_defeated']}\n"
        if "level" in requirements:
            message += f"- Atteindre le niveau: {requirements['level']}\n"
    
    return message


def generate_biome_info_message(floor_name, biome_name):
    """
    Génère un message d'information détaillé sur un biome.
    
    Args:
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        str: Le message d'information sur le biome
    """
    biome_info = get_biome_info(floor_name, biome_name)
    
    if not biome_info:
        return f"Aucune information disponible pour le biome {biome_name} dans {floor_name}."
    
    # Construire le message d'information
    message = f"Informations sur {biome_name} ({floor_name}):\n\n"
    message += f"Description: {biome_info.get('description', 'Aucune description disponible.')}\n\n"
    
    # Ajouter les informations sur les monstres
    monsters = biome_info.get('monsters', [])
    if monsters:
        message += "Monstres présents:\n"
        for monster_name in monsters:
            message += f"- {monster_name}\n"
    else:
        message += "Aucun monstre connu dans ce biome.\n"
    
    # Ajouter les informations sur les quêtes disponibles
    quests = biome_info.get('quests', [])
    if quests:
        message += "\nQuêtes disponibles:\n"
        for quest in quests:
            message += f"- {quest}\n"
    
    # Ajouter les informations sur les ressources disponibles
    resources = biome_info.get('resources', [])
    if resources:
        message += "\nRessources disponibles:\n"
        for resource in resources:
            message += f"- {resource}\n"
    
    return message