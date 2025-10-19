balanced = [
    {"range": {"start": [0, 0], "end": [9, 9]}, "crop": Entities.Tree, "plant_mode": "modulo2"},
    {"range": {"start": [0, 10], "end": [9, 19]}, "crop": Entities.Pumpkin, "plant_mode": None},
    {"range": {"start": [0, 20], "end": [21, 31]}, "crop": Entities.Sunflower, "plant_mode": None},
    {"range": {"start": [10, 0], "end": [19, 9]}, "crop": Entities.Carrot, "plant_mode": None},
    {"range": {"start": [10, 10], "end": [19, 14]}, "crop": Entities.Cactus, "plant_mode": None},
    {"range": {"start": [10, 0], "end": [19, 9]}, "crop": Entities.Carrot, "plant_mode": None},
    {"range": {"start": [20, 0], "end": [21, 19]}, "crop": Entities.Sunflower, "plant_mode": "measure"},
    {"range": {"start": [21, 0], "end": [31, 31]}, "crop": Entities.Cactus, "plant_mode": None},
]

pumpkin = []

sunflower = [{"range": {"start": [0, 0], "end": [31, 31]}, "crop": Entities.Sunflower, "plant_mode": "measure"}]

bush = [{"range": {"start": [0, 0], "end": [31, 31]}, "crop": Entities.Bush, "plant_mode": None}]

maze = [{"range": {"start": [0, 0], "end": [0, 0]}, "crop": Entities.Bush, "plant_mode": "maze"}]
