#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module d'informations sur les étages d'Aincrad et les articles du magasin.
"""

# Import des données des étages depuis le package palier
from palier import (
    FLOORS_INFO, get_floor_info, get_boss_info, get_biomes,
    get_biome_info, get_biome_monsters, check_floor_unlock_requirements,
    check_biome_unlock_requirements
)

# Définition des articles disponibles dans la boutique
SHOP_ITEMS = {
    "Health Potion": 50,
    "Teleport Crystal": 200,
    "Strength Potion": 100,
    "Basic Armor": 300,
    "Enhanced Sword": 500,
    "Agility Potion": 100,
    "Defense Potion": 100,
    "Antidote": 30,
    "Revival Crystal": 1000,
    "Map Data Crystal": 150
}