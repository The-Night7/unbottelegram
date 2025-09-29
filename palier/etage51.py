# -*- coding: utf-8 -*-

# Informations sur l'étage 51
FLOOR_51_INFO = {
    "name": "Floor 51 - Penumbra",
    "description": "Un étage où le jour et la nuit se côtoient en permanence, divisé en deux moitiés distinctes. La ville principale, Penumbra, est construite exactement à la frontière entre la lumière et l'ombre.",
    "boss": {
        "name": "Dualius the Twilight Lord",
        "level": 67,
        "hp": 5200,
        "attack": 82,
        "defense": 72,
        "exp": 2600,
        "col": 11000,
        "drops": {"Twilight Crystal": 1.0, "Duality Blade": 0.3},
        "description": "Un être mi-ange mi-démon qui maîtrise à la fois la lumière et les ténèbres. Il peut changer de forme selon qu'il combat du côté jour ou du côté nuit de l'étage.",
        "required_level": 62,
        "min_party_size": 6
    },
    "safe_zones": ["Penumbra", "Daylight Haven", "Night Refuge"],
    "danger_level": 7,
    "recommended_level": 57,
    "biomes": [
        {
            "name": "Eternal Day",
            "description": "La moitié de l'étage baignée dans une lumière perpétuelle, où vivent des créatures célestes et des plantes luxuriantes.",
            "monsters": ["Light Elemental", "Solar Guardian"],
            "quests": ["q337", "q338"],
            "level_range": [57, 60],
            "unlock_requirements": None
        },
        {
            "name": "Eternal Night",
            "description": "La moitié de l'étage plongée dans une nuit sans fin, où rôdent des créatures nocturnes et des êtres des ténèbres.",
            "monsters": ["Shadow Stalker", "Void Creature"],
            "quests": ["q339", "q340"],
            "level_range": [60, 64],
            "unlock_requirements": {"level": 59}
        },
        {
            "name": "Twilight Temple",
            "description": "Un temple ancien situé exactement à la frontière entre le jour et la nuit, où le seigneur du crépuscule attend les aventuriers.",
            "monsters": ["Twilight Priest", "Balance Guardian"],
            "quests": ["q341", "q342"],
            "level_range": [64, 67],
            "unlock_requirements": {"level": 63, "quest_completed": "q340"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Emperor of Darkness"}
}