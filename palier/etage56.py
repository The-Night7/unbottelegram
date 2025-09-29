# -*- coding: utf-8 -*-

# Informations sur l'étage 56
FLOOR_56_INFO = {
    "name": "Floor 56 - Pani",
    "description": "Un étage composé d'îles tropicales et de lagons aux eaux cristallines. La ville principale, Pani, est construite sur l'île centrale et est connue pour ses marchés colorés et ses festivals.",
    "boss": {
        "name": "Oceanus the Tidal Lord",
        "level": 76,
        "hp": 6200,
        "attack": 91,
        "defense": 86,
        "exp": 3100,
        "col": 13000,
        "drops": {"Tidal Pearl": 1.0, "Tsunami Trident": 0.3},
        "description": "Un seigneur des mers à l'apparence mi-humaine mi-poisson. Il peut contrôler les eaux, créer des raz-de-marée et invoquer des créatures marines pour l'assister.",
        "required_level": 71,
        "min_party_size": 7
    },
    "safe_zones": ["Pani", "Coral Harbor", "Fisherman's Village"],
    "danger_level": 8,
    "recommended_level": 66,
    "biomes": [
        {
            "name": "Tropical Shores",
            "description": "Des plages de sable blanc bordées de palmiers, où vivent des crabes géants et d'autres créatures côtières.",
            "monsters": ["Giant Crab", "Beach Predator"],
            "quests": ["q361", "q362"],
            "level_range": [66, 69],
            "unlock_requirements": None
        },
        {
            "name": "Coral Reefs",
            "description": "Des récifs coralliens multicolores sous la surface de l'eau, habités par des poissons exotiques et des créatures marines dangereuses.",
            "monsters": ["Reef Guardian", "Electric Eel"],
            "quests": ["q363", "q364"],
            "level_range": [69, 73],
            "unlock_requirements": {"level": 68}
        },
        {
            "name": "Abyssal Temple",
            "description": "Un temple englouti au fond de l'océan, où le seigneur des marées a établi son domaine et attend les aventuriers.",
            "monsters": ["Deep One", "Temple Guardian"],
            "quests": ["q365", "q366"],
            "level_range": [73, 76],
            "unlock_requirements": {"level": 72, "quest_completed": "q364"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "The Adamantine Sentinel"}
}