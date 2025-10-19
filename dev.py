import world_tools
import movement
import helper

def farm_pumpkin_mode():
	has_dead_pumpkin = True
	for x in range(world_tools.grid_size()):
		for y in range(world_tools.grid_size()):
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	while has_dead_pumpkin:
		dp_found = False
		for x in range(world_tools.grid_size()):
			for y in range(world_tools.grid_size()):
				if not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
					use_item(Items.Fertilizer)
				if get_entity_type() == Entities.Dead_Pumpkin:
					dp_found = True
					plant(Entities.Pumpkin)
				move(North)
			move(East)
		if dp_found == False:
			has_dead_pumpkin = False

			
def handle_sunflower(sunflower_list):
	
	for sunflower in sunflower_list:
		x = sunflower[0]
		y = sunflower[1]
		
	
	
#def farm_mazes():