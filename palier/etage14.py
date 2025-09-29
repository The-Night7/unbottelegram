# -*- coding: utf-8 -*-

# Informations sur l'étage 14
FLOOR_14_INFO = {
    "name": "Floor 14 - Sandoria",
    "description": "Un étage désertique aux vastes dunes dorées et aux oasis luxuriantes. La ville principale, Sandoria, est construite autour d'une immense oasis et protégée par de hauts murs contre les tempêtes de sable.",
    "boss": {
        "name": "Scorpius the Desert Emperor",
        "level": 53,
        "hp": 3400,
        "attack": 73,
        "defense": 67,
        "exp": 1800,
        "col": 9000,
        "drops": {"Emperor's Stinger": 1.0, "Scorpion Shield": 0.3},
        "description": "Un scorpion géant couronné qui règne sur les dunes. Sa carapace dorée reflète la lumière du soleil pour aveugler ses adversaires, et son dard contient un poison mortel.",
        "required_level": 48,
        "min_party_size": 6
    },
    "safe_zones": ["Sandoria", "Oasis Rest", "Caravan Stop"],
    "danger_level": 6,
    "recommended_level": 46,
    "biomes": [
        {
            "name": "Endless Dunes",
            "description": "Un océan de sable doré où les dunes changent constamment sous l'effet du vent, abritant des créatures adaptées à la chaleur extrême.",
            "monsters": ["Sand Worm", "Desert Lizard"],
            "quests": ["q139", "q140"],
            "level_range": [46, 48],
            "unlock_requirements": None
        },
        {
            "name": "Hidden Oases",
            "description": "Des points d'eau entourés de végétation luxuriante, où se rassemblent les créatures du désert et où se cachent des bandits.",
            "monsters": ["Oasis Guardian", "Desert Bandit"],
            "quests": ["q141", "q142"],
            "level_range": [48, 51],
            "unlock_requirements": {"level": 47}
        },
        {
            "name": "Ancient Pyramid",
            "description": "Une pyramide à moitié ensevelie sous le sable, qui sert de repaire au boss et à ses serviteurs.",
            "monsters": ["Mummified Guardian", "Sand Golem"],
            "quests": ["q143", "q144"],
            "level_range": [51, 53],
            "unlock_requirements": {"level": 50, "quest_completed": "q142"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Lumina the Radiant Queen"}
}