# -*- coding: utf-8 -*-

# Informations sur l'étage 69
FLOOR_69_INFO = {
    "name": "Floor 69 - Abyssia",
    "description": "Un étage plongé dans l'obscurité perpétuelle, avec des gouffres sans fond et des cavernes labyrinthiques. La ville principale, Abyssia, est illuminée par des cristaux luminescents et construite au bord d'un abîme vertigineux.",
    "boss": {
        "name": "Tenebris the Void Walker",
        "level": 89,
        "hp": 8600,
        "attack": 108,
        "defense": 99,
        "exp": 4300,
        "col": 19000,
        "drops": {"Void Crystal": 1.0, "Shadow Blade": 0.3},
        "description": "Un être des ténèbres qui peut se fondre dans l'obscurité et en émerger à volonté. Il peut créer des zones de ténèbres absolues où même la lumière magique ne pénètre pas et invoquer des serviteurs de l'ombre.",
        "required_level": 84,
        "min_party_size": 8
    },
    "safe_zones": ["Abyssia", "Light Haven", "Crystal Refuge"],
    "danger_level": 9,
    "recommended_level": 81,
    "biomes": [
        {
            "name": "Darkened Plains",
            "description": "Des plaines plongées dans une nuit sans fin, où des créatures adaptées à l'obscurité chassent ceux qui osent s'aventurer sans lumière.",
            "monsters": ["Night Stalker", "Shadow Beast"],
            "quests": ["q433", "q434"],
            "level_range": [81, 84],
            "unlock_requirements": None
        },
        {
            "name": "Abyssal Caverns",
            "description": "Un réseau de grottes profondes où l'obscurité est presque tangible, habité par des créatures qui n'ont jamais vu la lumière du jour.",
            "monsters": ["Cave Horror", "Void Dweller"],
            "quests": ["q435", "q436"],
            "level_range": [84, 87],
            "unlock_requirements": {"level": 83}
        },
        {
            "name": "Void Gate",
            "description": "Un portail mystérieux qui semble mener vers une dimension de ténèbres pures, gardé par le Marcheur du Vide et ses serviteurs les plus puissants.",
            "monsters": ["Gate Guardian", "Void Elemental"],
            "quests": ["q437", "q438"],
            "level_range": [87, 89],
            "unlock_requirements": {"level": 86, "quest_completed": "q436"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Oberon the Fairy King"}
}