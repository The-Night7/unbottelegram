# -*- coding: utf-8 -*-

# Informations sur l'étage 37
FLOOR_37_INFO = {
    "name": "Floor 37 - Floria",
    "description": "Un étage couvert de jardins luxuriants et de serres gigantesques. La ville principale, Floria, est construite au milieu d'un jardin botanique aux plantes rares et exotiques.",
    "boss": {
        "name": "Viridis the Garden Keeper",
        "level": 73,
        "hp": 5400,
        "attack": 89,
        "defense": 84,
        "exp": 2700,
        "col": 14000,
        "drops": {"Perfect Seed": 1.0, "Thornvine Whip": 0.3},
        "description": "Un être mi-homme mi-plante qui veille sur les jardins sacrés. Il peut contrôler toutes les plantes environnantes, libérer des pollens empoisonnés et régénérer ses blessures grâce à la photosynthèse.",
        "required_level": 68,
        "min_party_size": 7
    },
    "safe_zones": ["Floria", "Botanist's Haven", "Greenhouse Village"],
    "danger_level": 8,
    "recommended_level": 64,
    "biomes": [
        {
            "name": "Cultivated Gardens",
            "description": "Des jardins soigneusement entretenus où poussent des plantes aux propriétés magiques et où travaillent des jardiniers automates.",
            "monsters": ["Garden Golem", "Animated Shrub"],
            "quests": ["q265", "q266"],
            "level_range": [64, 67],
            "unlock_requirements": None
        },
        {
            "name": "Exotic Greenhouse",
            "description": "D'immenses serres où sont cultivées des plantes d'autres mondes, certaines carnivores et d'autres aux effets étranges.",
            "monsters": ["Carnivorous Plant", "Spore Cloud"],
            "quests": ["q267", "q268"],
            "level_range": [67, 70],
            "unlock_requirements": {"level": 66}
        },
        {
            "name": "Sacred Grove",
            "description": "Le jardin secret au centre de l'étage, où le Gardien cultive les plantes les plus rares et les plus dangereuses d'Aincrad.",
            "monsters": ["Ancient Treant", "Flower Guardian"],
            "quests": ["q269", "q270"],
            "level_range": [70, 73],
            "unlock_requirements": {"level": 69, "quest_completed": "q268"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Chronos the Timekeeper"}
}