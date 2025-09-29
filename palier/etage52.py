# -*- coding: utf-8 -*-

# Informations sur l'étage 52
FLOOR_52_INFO = {
    "name": "Floor 52 - Ferrum",
    "description": "Un étage industriel dominé par d'immenses forges et des usines mécaniques. La ville principale, Ferrum, est construite autour d'une gigantesque fonderie centrale.",
    "boss": {
        "name": "Mechanicus the Clockwork Titan",
        "level": 69,
        "hp": 5400,
        "attack": 84,
        "defense": 74,
        "exp": 2700,
        "col": 11500,
        "drops": {"Perfect Gear": 1.0, "Mechanical Arm": 0.3},
        "description": "Un titan mécanique composé d'innombrables engrenages et pistons. Il peut se transformer pour adopter différentes configurations de combat et réparer ses dommages en absorbant le métal environnant.",
        "required_level": 64,
        "min_party_size": 6
    },
    "safe_zones": ["Ferrum", "Engineer's Quarter", "Steam Haven"],
    "danger_level": 7,
    "recommended_level": 59,
    "biomes": [
        {
            "name": "Factory District",
            "description": "Un dédale d'usines et d'ateliers où des machines autonomes fabriquent sans cesse des pièces mécaniques et où rôdent des constructions hostiles.",
            "monsters": ["Clockwork Soldier", "Steam Golem"],
            "quests": ["q343", "q344"],
            "level_range": [59, 62],
            "unlock_requirements": None
        },
        {
            "name": "Molten Foundry",
            "description": "D'immenses fonderies où le métal en fusion coule dans des moules gigantesques, gardées par des élémentaires de feu et des constructions résistantes à la chaleur.",
            "monsters": ["Molten Guardian", "Forge Elemental"],
            "quests": ["q345", "q346"],
            "level_range": [62, 66],
            "unlock_requirements": {"level": 61}
        },
        {
            "name": "Clockwork Spire",
            "description": "Une tour mécanique au centre de l'étage, remplie d'engrenages géants et de mécanismes complexes, où le titan mécanique supervise sa production.",
            "monsters": ["Gear Knight", "Mechanical Beast"],
            "quests": ["q347", "q348"],
            "level_range": [66, 69],
            "unlock_requirements": {"level": 65, "quest_completed": "q346"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Dualius the Twilight Lord"}
}