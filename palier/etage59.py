# -*- coding: utf-8 -*-

# Informations sur l'étage 59
FLOOR_59_INFO = {
    "name": "Floor 59 - Danac",
    "description": "Un étage désertique avec des canyons profonds et des formations rocheuses spectaculaires. La ville principale, Danac, est construite dans une oasis au centre du désert.",
    "boss": {
        "name": "Sirocco the Desert Warlord",
        "level": 80,
        "hp": 6800,
        "attack": 95,
        "defense": 90,
        "exp": 3400,
        "col": 14500,
        "drops": {"Desert Wind Crystal": 1.0, "Dune Scimitar": 0.3},
        "description": "Un guerrier du désert monté sur un scorpion géant. Il peut créer des tempêtes de sable, faire surgir des piliers de roche du sol et commander une armée de créatures désertiques.",
        "required_level": 75,
        "min_party_size": 7
    },
    "safe_zones": ["Danac", "Oasis Rest", "Canyon Shelter"],
    "danger_level": 8,
    "recommended_level": 72,
    "biomes": [
        {
            "name": "Shifting Sands",
            "description": "De vastes étendues de dunes mouvantes où des tempêtes de sable peuvent surgir à tout moment, cachant des créatures prédatrices.",
            "monsters": ["Sand Worm", "Desert Stalker"],
            "quests": ["q379", "q380"],
            "level_range": [72, 75],
            "unlock_requirements": None
        },
        {
            "name": "Ancient Canyons",
            "description": "Des canyons profonds aux parois sculptées par le vent, où des ruines anciennes abritent des trésors et des dangers.",
            "monsters": ["Canyon Guardian", "Ruin Dweller"],
            "quests": ["q381", "q382"],
            "level_range": [75, 78],
            "unlock_requirements": {"level": 74}
        },
        {
            "name": "Warlord's Fortress",
            "description": "Une forteresse taillée dans la roche au sommet d'une mesa, où le seigneur de guerre du désert attend les aventuriers avec son armée.",
            "monsters": ["Desert Warrior", "Scorpion Guard"],
            "quests": ["q383", "q384"],
            "level_range": [78, 80],
            "unlock_requirements": {"level": 77, "quest_completed": "q382"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Gaia the Life Mother"}
}