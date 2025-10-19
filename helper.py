import movement
import layouts

global maximum_petals
global minimum_petals
maximum_petals = 15  # determined by game code
minimum_petals = 7  # determined by game code


def generate_grid_matrix(grid):
    matrix = {}
    grid_size = get_world_size()
    for area in grid:
        for x in range(grid_size - 1):
            for y in range(grid_size - 1):
                key = build_pos_key()
                crop = area["crop"]
                matrix[key] = {"x": x, "y": y, "crop": crop, "value": None}
    return matrix


def build_pos_key():
    return str(get_pos_x()) + "_" + str(get_pos_y())


# def get_area_from_grid(grid):
#     x = get_pos_x()
#     y = get_pos_y()
#     for area in grid:
#         if area["range"]["start"][0] <= x and area["range"]["end"][0] >= x:
#             if area["range"]["start"][1] <= y and area["range"]["end"][1] >= y:
#                 return area

# global sunflowers_map
# sunflowers_map = {}
# def cell_action(area):
# 	global sunflowers_map
# 	do = can_harvest()
# 	current_crop = get_entity_type()
# 	petals = []

# 	# Check if crop can and should be harvested
# 	# harvest the crop if yes
# 	if do and crop_harvest_info[current_crop]:
# 		harvest()

# 	# Check if any action should be taken on this cell
# 	if not do and not get_ground_type() == Grounds.Soil or not area or "crop" not in area or not area["crop"]:
# 		if not get_entity_type() == Entities.Hedge:
# 			return

# 	# Check if the crop can be planted on current ground
# 	if crop_needs_soil[area["crop"]] and get_ground_type() != Grounds.Soil:
# 		till()

# 	# Check for special planting needs
# 	if area["plant_mode"] == None:
# 		plant(area["crop"])
# 	# Checkboard pattern for trees
# 	elif area["plant_mode"] == "modulo2":
# 		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
# 			plant(area["crop"])
# 		elif get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1:
# 			plant(area["crop"])
# 	# Plant mode that measures the plant (e.g. # of petals for sunflowers)
# 	elif area["plant_mode"] == "measure":
# 		plant(area["crop"])
# 		key = str(get_pos_x()) + "_" + str(get_pos_y())
# 		sunflowers_map[key] = {"x": get_pos_x(), "y": get_pos_y(), "count": measure(), "time": get_time()}
# 	# Plants a Bush and turns it into a maze of size get_world_size()
# 	elif area["plant_mode"] == "maze":
# 		plant(area["crop"])
# 		amount = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
# 		use_item(Items.Weird_Substance, amount)


# def get_crops_from_grid(grid):
#     crops = []
#     for area in grid:
#         if area["crop"] not in crops:
#             crops.append(area["crop"])
#     return crops
