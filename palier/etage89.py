# -*- coding: utf-8 -*-

# Informations sur l'étage 89
FLOOR_89_INFO = {
    "name": "Floor 89 - Shadowrealm",
    "description": "Un étage plongé dans une obscurité perpétuelle, où la lumière est rare et précieuse. La ville principale, Shadowrealm, est éclairée par des cristaux luminescents et entourée d'une barrière qui repousse les ténèbres.",
    "boss": {
        "name": "Umbra the Shadow Sovereign",
        "level": 104,
        "hp": 12800,
        "attack": 148,
        "defense": 128,
        "exp": 6400,
        "col": 32000,
        "drops": {"Shadow Essence": 1.0, "Void Blade": 0.3},
        "description": "Le souverain absolu des ombres, dont le corps semble fait de ténèbres pures. Il peut se fondre dans l'obscurité, créer des clones d'ombre et absorber la lumière pour renforcer ses pouvoirs.",
        "required_level": 99,
        "min_party_size": 10
    },
    "safe_zones": ["Shadowrealm", "Light Haven", "Beacon Keep"],
    "danger_level": 10,
    "recommended_level": 94,
    "biomes": [
        {
            "name": "Twilight Forest",
            "description": "Une forêt où les arbres absorbent la lumière, créant une pénombre perpétuelle où se cachent des prédateurs qui chassent dans l'obscurité.",
            "monsters": ["Shadow Stalker", "Twilight Beast"],
            "quests": ["q541", "q542"],
            "level_range": [94, 97],
            "unlock_requirements": None
        },
        {
            "name": "Void Chasms",
            "description": "Des gouffres si profonds que la lumière n'y pénètre jamais, habités par des créatures qui n'ont jamais connu la clarté et qui fuient toute source lumineuse.",
            "monsters": ["Void Dweller", "Abyssal Horror"],
            "quests": ["q543", "q544"],
            "level_range": [97, 101],
            "unlock_requirements": {"level": 96}
        },
        {
            "name": "Shadow Throne",
            "description": "Le domaine personnel du Souverain des Ombres, où les ténèbres sont si épaisses qu'elles semblent tangibles et où même la lumière magique est rapidement étouffée.",
            "monsters": ["Shadow Knight", "Darkness Elemental"],
            "quests": ["q545", "q546"],
            "level_range": [101, 104],
            "unlock_requirements": {"level": 100, "quest_completed": "q544"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Draconius the Dragon Emperor"}
}