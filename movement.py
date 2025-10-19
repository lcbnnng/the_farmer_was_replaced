import world_tools
import helper

grid_size = get_world_size()


def go_to_pos(x, y, grid_size):
    current_x = get_pos_x()
    current_y = get_pos_y()
    cutoff_point = grid_size / 2
    while current_x != x or current_y != y:
        if current_x != x:
            dist_east = (x - current_x + grid_size) % grid_size
            dist_west = (current_x - x + grid_size) % grid_size

            if dist_east <= dist_west:
                move(East)
            else:
                move(West)

        elif current_y != y:
            dist_north = (y - current_y + grid_size) % grid_size
            dist_south = (current_y - y + grid_size) % grid_size

            if dist_north <= dist_south:
                move(North)
            else:
                move(South)

        current_x = get_pos_x()
        current_y = get_pos_y()
    return


def go_to_default_pos():
    go_to_pos(0, 0, grid_size)


def mover(farming_mode, grid):

    area = helper.get_area_from_grid(grid)

    if farming_mode == "balanced":

        helper.cell_action(area)
        if get_pos_x() == get_world_size() - 1:
            move(North)
            move(East)
        else:
            move(East)
    elif farming_mode == "sunflower":
        helper.cell_action(area)
        if get_pos_x() == get_world_size() - 1:
            move(North)
            move(East)
        else:
            move(East)
    elif farming_mode == "bush":
        helper.cell_action(area)
        if get_pos_x() == get_world_size() - 1:
            move(North)
            move(East)
        else:
            move(East)
    elif farming_mode == "maze":
        if get_pos_x == 0 and get_pos_y() == 0:
            helper.cell_action(area)
        if get_pos_x() == get_world_size() - 1:
            move(North)
            move(East)
        else:
            move(East)
