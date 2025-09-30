#!/usr/bin/env python
# -*- coding: utf-8 -*-

from monstres.monstre_manager import MONSTERS
from palier import get_floor_info, get_biome_info, get_biome_monsters, get_boss_info as get_boss_info_from_palier

def get_monster_info(monster_name):
    """
    Récupère les informations d'un monstre spécifique.
    
    Args:
        monster_name (str): Le nom du monstre
        
    Returns:
        dict: Les informations du monstre ou None si le monstre n'existe pas
    """
    return MONSTERS.get(monster_name, None)


def get_available_monsters(floor_name, biome_name):
    """
    Récupère la liste des monstres disponibles dans un biome spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage
        biome_name (str): Le nom du biome
        
    Returns:
        list: La liste des noms de monstres disponibles dans ce biome
    """
    biome_monsters = get_biome_monsters(floor_name, biome_name)
    return biome_monsters


def get_boss_info(floor_name):
    """
    Récupère les informations du boss d'un étage spécifique.
    
    Args:
        floor_name (str): Le nom de l'étage
        
    Returns:
        dict: Les informations du boss ou None si l'étage n'a pas de boss
    """
    return get_boss_info_from_palier(floor_name)