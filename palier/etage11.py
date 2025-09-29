# -*- coding: utf-8 -*-

# Informations sur l'étage 11
FLOOR_11_INFO = {
    "name": "Floor 11 - Taft",
    "description": "Un étage dominé par de vastes prairies et des collines verdoyantes. La ville principale, Taft, est connue pour ses élevages de bétail et ses produits laitiers.",
    "boss": {
        "name": "Bullbous the Stampede King",
        "level": 47,
        "hp": 2800,
        "attack": 65,
        "defense": 60,
        "exp": 1500,
        "col": 7500,
        "drops": {"Stampede Horn": 1.0, "Trampling Boots": 0.3},
        "description": "Un taureau colossal à six pattes qui peut provoquer des tremblements de terre en frappant le sol. Il mène une harde de taureaux sauvages qui l'assistent au combat.",
        "required_level": 42,
        "min_party_size": 5
    },
    "safe_zones": ["Taft", "Shepherd's Rest", "Green Hill"],
    "danger_level": 5,
    "recommended_level": 40,
    "biomes": [
        {
            "name": "Rolling Meadows",
            "description": "De vastes prairies ondulantes où paissent des troupeaux d'herbivores, parfois menacés par des prédateurs.",
            "monsters": ["Wild Bull", "Prairie Wolf"],
            "quests": ["q121", "q122"],
            "level_range": [40, 43],
            "unlock_requirements": None
        },
        {
            "name": "Shepherd's Hills",
            "description": "Des collines parsemées de fermes et de pâturages, où des bergers élèvent du bétail malgré les créatures hostiles.",
            "monsters": ["Hill Ogre", "Sheep Thief"],
            "quests": ["q123", "q124"],
            "level_range": [43, 45],
            "unlock_requirements": {"level": 42}
        },
        {
            "name": "Thunder Plains",
            "description": "Une plaine où résonnent constamment les sabots du troupeau du boss, créant un bruit semblable au tonnerre.",
            "monsters": ["Thunder Hoof", "Stampede Scout"],
            "quests": ["q125", "q126"],
            "level_range": [45, 47],
            "unlock_requirements": {"level": 44, "quest_completed": "q124"}
        }
    ],
    "unlock_requirements": {"boss_defeated": "Kagachi the Samurai Lord"}
}