dateSpecifics = {
	"Sunday": [
		":tv: The Queen of Sauce",
		":cactus: Staircases from the Desert Trader for 1 Jade",
		":gift: The gift limit has been reset",
		":pig2: Traveling Cart in the Cindersap Forest",
	],
	"Monday": [
		":clipboard: New Special Orders available",
		":coconut: Coconuts at the Oasis for 400g",
	],
	"Tuesday": [
		":hammer: Robin's shop is closed",
		":women_wrestling: If it's not raining, Robin and Marnie close their shops to attend exercise class",
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
		":pig2: Traveling Cart in the Cindersap Forest",
	],
}

def getDateSpecifics(date):
	specifics = ""

	# Add new lines for various events throughout the week
	if date in dateSpecifics:
		for event in dateSpecifics[date]:
			specifics += "\n" + event

	return specifics
