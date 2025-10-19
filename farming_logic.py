import farming_handlers
import helper
import layouts

crop_information = {
    Entities.Grass: {"harvest_handler": None, "soil": False, "always_harvest": True, "plant_mode": None},
    Entities.Bush: {"harvest_handler": None, "soil": False, "always_harvest": True, "plant_mode": None},
    Entities.Tree: {"harvest_handler": None, "soil": False, "always_harvest": True, "plant_mode": "modulo2"},
    Entities.Cactus: {
        "harvest_handler": farming_handlers.handle_cactus,
        "soil": False,
        "always_harvest": False,
        "plant_mode": None,
    },
    Entities.Carrot: {"harvest_handler": None, "soil": True, "always_harvest": True, "plant_mode": None},
    Entities.Pumpkin: {
        "harvest_handler": farming_handlers.handle_pumpkin,
        "soil": True,
        "always_harvest": False,
        "plant_mode": None,
    },
    Entities.Sunflower: {
        "harvest_handler": farming_handlers.handle_sunflower,
        "soil": True,
        "always_harvest": False,
        "plant_mode": "measure",
    },
    Entities.Dead_Pumpkin: {"harvest_handler": None, "soil": False, "always_harvest": False, "plant_mode": None},
    Entities.Treasure: {"harvest_handler": None, "soil": False, "always_harvest": True, "plant_mode": None},
    Entities.Hedge: {"harvest_handler": None, "soil": False, "always_harvest": True, "plant_mode": None},
}

farming_mode_grid = {
    "balanced": layouts.balanced,
    "pumpkin": layouts.pumpkin,
    "bush": layouts.bush,
    "sunflower": layouts.sunflower,
    "maze": layouts.maze,
    # "tree": layouts.tree,
}


def get_grid_from_farming_mode(mode):
    return farming_mode_grid[mode]


def get_max_petals():
    max_petals = 15
    return max_petals


def get_min_petals():
    min_petals = 7
    return min_petals


def get_crop_info(crop):
    return crop_information[crop]


def get_crop_harvest_handler(crop):
    return crop_information[crop]["harvest_handler"]


def get_crop_ground_type(crop):
    if crop_information[crop]["soil"]:
        return Grounds.Soil
    else:
        return Grounds.Grassland


def get_crop_always_harvest(crop):
    return crop_information[crop]["always_harvest"]


def get_crop_plant_mode(crop):
    return crop_information[crop]["plant_mode"]


def cell_action(matrix):
    current_x = get_pos_x()
    current_y = get_pos_y()
    key = helper.build_pos_key()
    crop = matrix[key]

    if can_harvest() and crop_information[get_entity_type()]["always_harvest"]:
        harvest()

    # If grass needs to grow here and the ground is not equal to grassland, till the ground and return
    if not crop["crop"] and get_ground_type() != Grounds.Grassland:
        till()
        return
    # If the desired crop is already on the cell return
    elif crop["crop"] == get_entity_type():
        return

    if not get_crop_plant_mode(crop["crop"]):
        plant(crop["crop"])
        return
    else:
        pass
