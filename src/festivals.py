from .seasonNames import seasonNames

def getFestival(day, seasonId):
	festival = ""
	season = seasonNames[seasonId]
	if season == "Spring":
		if day == 13:
			festival = ":egg: Egg Festival"
		elif day >= 15 and day <= 17:
			festival = ":cactus: Desert Festival"
		elif day == 24:
			festival = ":tulip: Flower Dance"
	elif season == "Summer":
		if day == 11:
			festival = ":palm_tree: Luau"
		elif day >= 20 and day <= 21:
			festival = ":fish: Trout Derby"
		elif day == 28:
			festival = ":jellyfish: Dance of the Moonlight Jellies"
	elif season == "Fall":
		if day == 16:
			festival = ":flags: Stardew Valley Fair"
		elif day == 27:
			festival = ":jack_o_lantern: Spirit's Eve"
	elif season == "Winter":
		if day == 8:
			festival = ":ice_cube: Festival of Ice"
		elif day >= 12 and day <= 13:
			festival = ":squid: SquidFest"
		elif day >= 15 and day <= 17:
			festival = ":ring_buoy: Night Market"
		elif day == 25:
			festival = ":glowing_star: Feast of the Winter Star"

	if festival != "":
		return f"\n({festival})"
	
	# If no festival, return empty string
	return ""
