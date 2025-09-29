# -*- coding: utf-8 -*-

# Informations sur l'étage 80
FLOOR_80_INFO = {
    "name": "Floor 80 - Celestial Spire",
    "description": "Un étage composé d'une immense tour qui s'élève jusqu'aux nuages. La ville principale, Celestial Spire, est construite en spirale autour de cette tour et offre une vue imprenable sur les étages inférieurs d'Aincrad.",
    "boss": {
        "name": "Ascendius the Skyward Judge",
        "level": 95,
        "hp": 11000,
        "attack": 130,
        "defense": 110,
        "exp": 5500,
        "col": 27500,
        "drops": {"Divine Judgment": 1.0, "Ascension Wings": 0.3},
        "description": "Un juge céleste aux six ailes dorées qui pèse les âmes des mortels. Il peut voler à une vitesse incroyable, lancer des rayons de lumière divine et invoquer des gardiens célestes pour l'assister.",
        "required_level": 90,
        "min_party_size": 10
    },
    "safe_zones": ["Celestial Spire", "Sky Sanctuary", "Pilgrim's Rest"],
    "danger_level": 10,
    "recommended_level": 85,
    "biomes": [
        {
            "name": "Lower Ascent",
            "description": "Les premiers niveaux de la tour, où des vents violents et des créatures volantes testent ceux qui souhaitent s'élever vers les sommets.",
            "monsters": ["Wind Elemental", "Sky Hunter"],
            "quests": ["q487", "q488"],
            "level_range": [85, 88],
            "unlock_requirements": None
        },
        {
            "name": "Heavenly Trials",
            "description": "La section médiane de la tour, composée de salles d'épreuves où les aventuriers doivent prouver leur valeur face à des gardiens et des pièges.",
            "monsters": ["Trial Guardian", "Divine Construct"],
            "quests": ["q489", "q490"],
            "level_range": [88, 92],
            "unlock_requirements": {"level": 87}
        },
        {
            "name": "Judgment Hall",
            "description": "Le sommet de la tour, baigné dans une lumière dorée perpétuelle, où le Juge Céleste attend pour déterminer si les aventuriers sont dignes de continuer leur ascension.",
            "monsters": ["Angelic Warrior", "Light Sentinel"],
            "quests": ["q491", "q492"],
            "level_range": [92, 95],
            "unlock_requirements": {"level": 91, "quest_completed": "q490"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Primordius the Elemental Lord"}
}