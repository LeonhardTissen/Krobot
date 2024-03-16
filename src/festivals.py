from .seasonNames import seasonNames

def getFestival(day, seasonId):
	festival = ""
	season = seasonNames[seasonId]
	if season == "Spring":
		if day == 13:
			festival = "Egg Festival"
		elif day == 24:
			festival = "Flower Dance"
	elif season == "Summer":
		if day == 11:
			festival = "Luau"
		elif day == 28:
			festival = "Dance of the Moonlight Jellies"
	elif season == "Fall":
		if day == 16:
			festival = "Stardew Valley Fair"
		elif day == 27:
			festival = "Spirit's Eve"
	elif season == "Winter":
		if day == 8:
			festival = "Festival of Ice"
		elif day >= 15 and day <= 17:
			festival = "Night Market"
		elif day == 25:
			festival = "Feast of the Winter Star"

	if festival != "":
		return f"\n({festival})"
		
	return ""
