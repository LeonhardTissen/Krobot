dateSpecifics = {
	"Sunday": [
		":tv: The Queen of Sauce",
		":cactus: Staircases from the Desert Trader for 1 Jade",
		":gift: The gift limit has been reset",
	],
	"Monday": [
		":clipboard: New Special Orders available",
	],
	"Wednesday": [
		":tv: The Queen of Sauce Re-run",
	],
	"Thursday": [
		":candy: Magic Rock Candy from the Desert Trader for 3 Prismatic Shards",
		":arrow_up: Deluxe Speed-Gro from the Oasis for 80g",
	],
	"Friday": [
		":pick: Clint's Blacksmith shop is closed",
	],
}

def getDateSpecifics(date):
	specifics = ""

	# Add new lines for various events throughout the week
	if date in dateSpecifics:
		for event in dateSpecifics[date]:
			specifics += "\n" + event

	return specifics
