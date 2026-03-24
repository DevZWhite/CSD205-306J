def plant_pumpkin():
	for x in range(8):
		for y in range(8):

			# Remove dead pumpkins first
			if get_entity_type() == Entities.Dead_Pumpkin:
				clear_entity()

			# Harvest live crops
			if can_harvest():
				harvest()

			# Prepare soil
			if get_ground_type() != Grounds.Soil:
				till()

			# Plant new pumpkins
			if get_entity_type() is None and num_items(Items.Carrot) >= 500:
				plant(Entities.Pumpkin)

			move(North)

		move(East)

	retToOrigin()
	