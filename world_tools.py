import movement

grid_size = get_world_size()


#### Finds all pumpkin patches (areas, whatever) in a list of areas and writes them to a new list
def find_pumpkin_patches(grid):
    pumpkin_patches = []
    for area in grid:
        if area["crop"] == Entities.Pumpkin:
            pumpkin_patches.append(area)
    return pumpkin_patches


### Finds all sunflower coordinates and writes them to a new list


def find_sunflowers(grid):
    all_sunflowers = []
    for area in grid:
        start_x = area["range"]["start"][0]
        start_y = area["range"]["start"][1]
        end_x = area["range"]["end"][0]
        end_y = area["range"]["end"][1]

        if area["crop"] == Entities.Sunflower:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    all_sunflowers.append([x, y])
    return all_sunflowers


def reset_field_soil():
    movement.go_to_default_pos()
    for x in range(grid_size()):
        for y in range(grid_size()):
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            if get_pos_x() == get_world_size() - 1:
                move(North)
            move(East)
