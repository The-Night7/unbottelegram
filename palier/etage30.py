# -*- coding: utf-8 -*-

# Informations sur l'étage 30
FLOOR_30_INFO = {
    "name": "Floor 30 - Stormfront",
    "description": "Un étage balayé par des tempêtes électriques perpétuelles. La ville principale, Stormfront, est protégée par un dôme de paratonnerre qui canalise la foudre pour alimenter la ville en énergie.",
    "boss": {
        "name": "Fulguris the Storm Emperor",
        "level": 60,
        "hp": 4000,
        "attack": 75,
        "defense": 70,
        "exp": 2000,
        "col": 10500,
        "drops": {"Lightning Crystal": 1.0, "Thunderbolt Spear": 0.3},
        "description": "Un titan entouré d'éclairs perpétuels qui peut contrôler la foudre et le tonnerre. Son corps est partiellement composé d'énergie pure et il peut se déplacer à la vitesse de l'éclair.",
        "required_level": 55,
        "min_party_size": 7
    },
    "safe_zones": ["Stormfront", "Lightning Shelter", "Thunder Peak"],
    "danger_level": 7,
    "recommended_level": 50,
    "biomes": [
        {
            "name": "Electric Plains",
            "description": "Des plaines où la foudre frappe constamment, créant des formations de verre fulgurite et attirant des créatures d'énergie pure.",
            "monsters": ["Lightning Elemental", "Charged Beast"],
            "quests": ["q223", "q224"],
            "level_range": [50, 53],
            "unlock_requirements": None
        },
        {
            "name": "Thundercloud Forest",
            "description": "Une forêt où les arbres métalliques attirent la foudre et où des nuages d'orage flottent entre les branches.",
            "monsters": ["Storm Harpy", "Thunder Treant"],
            "quests": ["q225", "q226"],
            "level_range": [53, 57],
            "unlock_requirements": {"level": 52}
        },
        {
            "name": "Emperor's Spire",
            "description": "Une tour qui s'élève jusqu'aux nuages, constamment frappée par la foudre et servant de trône au boss.",
            "monsters": ["Lightning Guardian", "Storm Knight"],
            "quests": ["q227", "q228"],
            "level_range": [57, 60],
            "unlock_requirements": {"level": 56, "quest_completed": "q226"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Umbra the Shadow Lord"}
}