# -*- coding: utf-8 -*-

# Informations sur l'étage 98
FLOOR_98_INFO = {
    "name": "Floor 98 - Divine Sanctuary",
    "description": "Un étage céleste baigné dans une lumière dorée, avec des temples majestueux et des jardins paradisiaques. La ville principale, Divine Sanctuary, est construite autour d'un temple colossal dédié aux dieux.",
    "boss": {
        "name": "Seraphim the Archangel",
        "level": 103,
        "hp": 13600,
        "attack": 146,
        "defense": 136,
        "exp": 6800,
        "col": 34000,
        "drops": {"Divine Feather": 1.0, "Seraph's Sword": 0.3},
        "description": "Un archange à six ailes dorées qui représente la justice divine. Il manie une épée de lumière pure qui peut trancher n'importe quelle matière et peut invoquer des rayons de jugement qui infligent des dégâts massifs.",
        "required_level": 98,
        "min_party_size": 10
    },
    "safe_zones": ["Divine Sanctuary", "Pilgrim's Rest", "Holy Gardens"],
    "danger_level": 10,
    "recommended_level": 93,
    "biomes": [
        {
            "name": "Sacred Gardens",
            "description": "Des jardins parfaits où poussent des plantes aux propriétés miraculeuses, gardés par des créatures célestes qui testent la pureté des intentions des aventuriers.",
            "monsters": ["Garden Guardian", "Divine Beast"],
            "quests": ["q589", "q590"],
            "level_range": [93, 96],
            "unlock_requirements": None
        },
        {
            "name": "Halls of Judgment",
            "description": "Des temples où les âmes sont pesées et jugées, remplis d'épreuves morales et de défis spirituels que les aventuriers doivent surmonter.",
            "monsters": ["Divine Judge", "Soul Examiner"],
            "quests": ["q591", "q592"],
            "level_range": [96, 100],
            "unlock_requirements": {"level": 95}
        },
        {
            "name": "Celestial Throne",
            "description": "Le sanctuaire le plus sacré de l'étage, où l'Archange siège sur un trône de lumière pure, entouré de ses plus fidèles serviteurs.",
            "monsters": ["Angelic Warrior", "Celestial Guardian"],
            "quests": ["q593", "q594"],
            "level_range": [100, 103],
            "unlock_requirements": {"level": 99, "quest_completed": "q592"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Chaos the Reality Breaker"}
}