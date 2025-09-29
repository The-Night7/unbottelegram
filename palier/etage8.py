# -*- coding: utf-8 -*-

# Informations sur l'étage 8
FLOOR_8_INFO = {
    "name": "Floor 8 - Elven Glade",
    "description": "Un étage verdoyant dominé par une immense forêt elfique aux arbres millénaires. La ville principale, Elven Glade, est construite dans les branches des arbres les plus grands.",
    "boss": {
        "name": "Zelgius the Corrupted Archdruid",
        "level": 46,
        "hp": 2400,
        "attack": 60,
        "defense": 55,
        "exp": 1300,
        "col": 6500,
        "drops": {"Nature's Essence": 1.0, "Staff of the Wild": 0.3},
        "description": "Un ancien archidruide elfe corrompu par des forces obscures. Il peut contrôler les plantes et les animaux de la forêt et se transformer en différentes créatures.",
        "required_level": 41,
        "min_party_size": 5
    },
    "safe_zones": ["Elven Glade", "Treehaven", "Moonlight Clearing"],
    "danger_level": 5,
    "recommended_level": 36,
    "biomes": [
        {
            "name": "Sacred Grove",
            "description": "Un bosquet d'arbres anciens imprégnés de magie elfique, où des créatures féeriques et des gardiens sylvestres protègent les lieux.",
            "monsters": ["Forest Guardian", "Luminous Sprite"],
            "quests": ["q109", "q110"],
            "level_range": [36, 39],
            "unlock_requirements": None
        },
        {
            "name": "Dark Thicket",
            "description": "Une partie de la forêt où les arbres sont si denses que la lumière du soleil ne pénètre jamais, habitée par des créatures corrompues.",
            "monsters": ["Shadow Panther", "Corrupted Treant"],
            "quests": ["q111", "q112"],
            "level_range": [39, 42],
            "unlock_requirements": {"level": 38}
        },
        {
            "name": "Ancient Heart",
            "description": "Le cœur de la forêt où se trouve l'arbre-mère et le sanctuaire corrompu du boss.",
            "monsters": ["Blighted Elf", "Twisted Dryad"],
            "quests": ["q113", "q114"],
            "level_range": [42, 46],
            "unlock_requirements": {"level": 41, "quest_completed": "q112"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Frostclaw the Winter Beast"}
}