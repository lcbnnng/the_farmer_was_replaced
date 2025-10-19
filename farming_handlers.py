import helper
import movement


def plant_sunflower():
    key = helper.build_pos_key()
    plant(Entities.Sunflower)
    amount = measure()
    return {"key": key, "amount": amount}


def handle_sunflower(sunflowers_map):
    global maximum_petals
    global minimum_petals
    max_petals = maximum_petals
    min_petals = minimum_petals
    sorted_sunflowers_map = []
    for i in range(max_petals, min_petals - 1, -1):
        for key in sunflowers_map:
            if sunflowers_map[key]["count"] == i:
                sorted_sunflowers_map.append(sunflowers_map[key])

    for flower in sorted_sunflowers_map:
        pos_x = flower["x"]
        pos_y = flower["y"]
        movement.go_to_pos(pos_x, pos_y, get_world_size())
        if can_harvest():
            harvest()
    movement.go_to_default_pos()


def handle_cactus():
    pass


def handle_pumpkin(pumpkin_patches):
    for patch in pumpkin_patches:
        start_x = patch["range"]["start"][0]
        start_y = patch["range"]["start"][1]
        end_x = patch["range"]["end"][0]
        end_y = patch["range"]["end"][1]
        has_dead_pumpkin = True

        while has_dead_pumpkin:
            dead_pumpkin_found = False
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    movement.go_to_pos(x, y, get_world_size())

                    if get_entity_type() == Entities.Dead_Pumpkin:
                        dead_pumpkin_found = True
                        if get_ground_type() != Grounds.Soil:
                            till()
                        plant(Entities.Pumpkin)
            if not dead_pumpkin_found and get_pos_x() == end_x and get_pos_y() == end_y:
                has_dead_pumpkin = False
        if get_entity_type() == Entities.Pumpkin:
            harvest()
        movement.go_to_default_pos()


def handle_maze():
    treasure_x, treasure_y = measure()
    while get_pos_x() != treasure_x and get_pos_y() != treasure_y:
        if can_move(East):
            move(East)
        elif can_move(North):
            move(North)
        elif can_move(West):
            move(West)
        else:
            move(South)
    if get_entity_type() == Entities.Treasure:
        harvest()
        if can_move(East):
            move(East)
        elif can_move(North):
            move(North)
        elif can_move(West):
            move(West)
        else:
            move(South)
    harvest()
    movement.go_to_default_pos()
