# -*- coding: utf-8 -*-

# Informations sur l'étage 23
FLOOR_23_INFO = {
    "name": "Floor 23 - Ronbaru",
    "description": "Un étage dominé par des collines verdoyantes et des vallées fertiles. La ville principale, Ronbaru, est connue pour ses champs en terrasse et ses rizières.",
    "boss": {
        "name": "Harvester the Plant Lord",
        "level": 47,
        "hp": 2700,
        "attack": 62,
        "defense": 55,
        "exp": 1300,
        "col": 6500,
        "drops": {"Fertile Seed": 1.0, "Harvest Scythe": 0.3},
        "description": "Un être mi-homme mi-plante qui contrôle la végétation environnante. Il peut faire pousser des plantes carnivores et utiliser des lianes pour immobiliser ses adversaires.",
        "required_level": 42,
        "min_party_size": 5
    },
    "safe_zones": ["Ronbaru", "Farmer's Rest", "Terraced Village"],
    "danger_level": 5,
    "recommended_level": 37,
    "biomes": [
        {
            "name": "Fertile Valley",
            "description": "Une vallée luxuriante où poussent des cultures diverses et où vivent des créatures herbivores pacifiques, parfois menacées par des prédateurs.",
            "monsters": ["Crop Guardian", "Valley Predator"],
            "quests": ["q187", "q188"],
            "level_range": [37, 40],
            "unlock_requirements": None
        },
        {
            "name": "Rice Terraces",
            "description": "Des champs en terrasse inondés où poussent du riz et où des créatures amphibies ont élu domicile.",
            "monsters": ["Terrace Lurker", "Rice Field Sprite"],
            "quests": ["q189", "q190"],
            "level_range": [40, 44],
            "unlock_requirements": {"level": 39}
        },
        {
            "name": "Ancient Grove",
            "description": "Un bosquet d'arbres millénaires au centre de l'étage, où le boss a établi son domaine et fait pousser des plantes monstrueuses.",
            "monsters": ["Sentient Vine", "Carnivorous Flower"],
            "quests": ["q191", "q192"],
            "level_range": [44, 47],
            "unlock_requirements": {"level": 43, "quest_completed": "q190"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Storm Griffin"}
}