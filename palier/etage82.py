# -*- coding: utf-8 -*-

# Informations sur l'étage 82
FLOOR_82_INFO = {
    "name": "Floor 82 - Infernal Forge",
    "description": "Un étage volcanique avec des rivières de lave et des forges titanesques. La ville principale, Infernal Forge, est construite dans le cratère d'un volcan actif, protégée par des barrières magiques.",
    "boss": {
        "name": "Vulcanus the Forge God",
        "level": 97,
        "hp": 11400,
        "attack": 134,
        "defense": 114,
        "exp": 5700,
        "col": 28500,
        "drops": {"Divine Ingot": 1.0, "Godforged Hammer": 0.3},
        "description": "Un titan de feu et de métal qui forge des armes divines. Son corps est partiellement fait de métal en fusion, et il peut créer des explosions volcaniques, invoquer des serviteurs de feu et forger des armes vivantes pendant le combat.",
        "required_level": 92,
        "min_party_size": 10
    },
    "safe_zones": ["Infernal Forge", "Cooling Chamber", "Smith's Haven"],
    "danger_level": 10,
    "recommended_level": 87,
    "biomes": [
        {
            "name": "Magma Fields",
            "description": "Des plaines où la lave coule librement et où le sol peut s'effondrer à tout moment, révélant des geysers de feu et des créatures de magma.",
            "monsters": ["Lava Elemental", "Magma Beast"],
            "quests": ["q499", "q500"],
            "level_range": [87, 90],
            "unlock_requirements": None
        },
        {
            "name": "Living Forges",
            "description": "D'immenses forges où des armes légendaires sont créées, gardées par des constructions de métal vivant et des élémentaires de feu.",
            "monsters": ["Forge Guardian", "Living Armor"],
            "quests": ["q501", "q502"],
            "level_range": [90, 94],
            "unlock_requirements": {"level": 89}
        },
        {
            "name": "Divine Anvil",
            "description": "Le cœur de l'étage, où le Dieu de la Forge travaille sur son enclume colossale, entouré de ses plus puissantes créations et de serviteurs de feu.",
            "monsters": ["Flame Titan", "Molten Construct"],
            "quests": ["q503", "q504"],
            "level_range": [94, 97],
            "unlock_requirements": {"level": 93, "quest_completed": "q502"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Leviathan the Deep Terror"}
}