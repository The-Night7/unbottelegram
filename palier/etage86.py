# -*- coding: utf-8 -*-

# Informations sur l'étage 86
FLOOR_86_INFO = {
    "name": "Floor 86 - Stormhold",
    "description": "Un étage perpétuellement balayé par des tempêtes électriques et des ouragans. La ville principale, Stormhold, est protégée par un dôme d'énergie qui repousse les vents violents et la foudre.",
    "boss": {
        "name": "Tempestas the Storm Lord",
        "level": 101,
        "hp": 12200,
        "attack": 142,
        "defense": 122,
        "exp": 6100,
        "col": 30500,
        "drops": {"Eye of the Storm": 1.0, "Thunderbolt Spear": 0.3},
        "description": "Le maître absolu des tempêtes, dont le corps est partiellement composé de nuages d'orage et de foudre. Il peut invoquer des tornades, frapper avec la puissance de la foudre et créer des tempêtes localisées.",
        "required_level": 96,
        "min_party_size": 10
    },
    "safe_zones": ["Stormhold", "Calm Haven", "Thunder Shelter"],
    "danger_level": 10,
    "recommended_level": 91,
    "biomes": [
        {
            "name": "Lightning Fields",
            "description": "Des plaines où la foudre frappe constamment, créant des formations de verre fulgurite et attirant des créatures d'énergie pure.",
            "monsters": ["Lightning Elemental", "Storm Stalker"],
            "quests": ["q523", "q524"],
            "level_range": [91, 94],
            "unlock_requirements": None
        },
        {
            "name": "Hurricane Wastes",
            "description": "Une zone balayée par des vents si puissants qu'ils peuvent soulever des rochers, habitée par des créatures aériennes et des élémentaires de vent.",
            "monsters": ["Wind Elemental", "Cyclone Beast"],
            "quests": ["q525", "q526"],
            "level_range": [94, 98],
            "unlock_requirements": {"level": 93}
        },
        {
            "name": "Eye of the Storm",
            "description": "Le centre de la plus grande tempête de l'étage, où règne un calme trompeur et où le Seigneur des Tempêtes a établi son domaine.",
            "monsters": ["Thunder Knight", "Living Hurricane"],
            "quests": ["q527", "q528"],
            "level_range": [98, 101],
            "unlock_requirements": {"level": 97, "quest_completed": "q526"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Adamantius the Crystal Tyrant"}
}