# -*- coding: utf-8 -*-

# Informations sur l'étage 97
FLOOR_97_INFO = {
    "name": "Floor 97 - Pandemonium",
    "description": "Un étage chaotique où les lois de la physique semblent brisées, avec des paysages impossibles et des structures qui défient la logique. La ville principale, Pandemonium, est le seul îlot de stabilité dans ce chaos.",
    "boss": {
        "name": "Chaos the Reality Breaker",
        "level": 102,
        "hp": 13400,
        "attack": 144,
        "defense": 134,
        "exp": 6700,
        "col": 33500,
        "drops": {"Reality Shard": 1.0, "Chaos Blade": 0.3},
        "description": "Une entité qui incarne le chaos primordial et qui peut altérer la réalité à volonté. Il peut transformer l'environnement, changer les lois physiques localement et créer des illusions parfaites qui peuvent causer de vrais dégâts.",
        "required_level": 97,
        "min_party_size": 10
    },
    "safe_zones": ["Pandemonium", "Reality Anchor", "Order Sanctuary"],
    "danger_level": 10,
    "recommended_level": 92,
    "biomes": [
        {
            "name": "Twisted Lands",
            "description": "Des terres où la géométrie est impossible, avec des escaliers qui montent en descendant et des chemins qui reviennent à leur point de départ malgré une trajectoire rectiligne.",
            "monsters": ["Reality Warper", "Impossible Beast"],
            "quests": ["q583", "q584"],
            "level_range": [92, 95],
            "unlock_requirements": None
        },
        {
            "name": "Madness Realm",
            "description": "Une zone où la folie règne, où les pensées des aventuriers prennent forme et où leurs peurs les plus profondes se matérialisent pour les attaquer.",
            "monsters": ["Nightmare Manifestation", "Mind Flayer"],
            "quests": ["q585", "q586"],
            "level_range": [95, 99],
            "unlock_requirements": {"level": 94}
        },
        {
            "name": "Void of Creation",
            "description": "L'épicentre du chaos, où la réalité est constamment détruite et recréée, et où le Briseur de Réalité forge de nouvelles lois physiques selon ses caprices.",
            "monsters": ["Chaos Guardian", "Primordial Entity"],
            "quests": ["q587", "q588"],
            "level_range": [99, 102],
            "unlock_requirements": {"level": 98, "quest_completed": "q586"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Eternus the Time Keeper"}
}