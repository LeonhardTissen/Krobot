def getDateSpecifics(date):
	specifics = ""

	# Add new lines for various events throughout the week
	if date == "Sunday":
		specifics += "\n:tv: The Queen of Sauce"
		specifics += "\n:cactus: Buy Staircases from the Desert Trader"
	elif date == "Wednesday":
		specifics += "\n:tv: The Queen of Sauce Re-run"
	elif date == "Thursday":
		specifics += "\n:cactus: Buy Magic Rock Candy from the Desert Trader"

	return specifics
