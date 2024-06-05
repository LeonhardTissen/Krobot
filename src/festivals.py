from .seasonNames import seasonNames

festivalList = {
	"Spring": {
		13: ":egg: Egg Festival",
		15: ":cactus: Desert Festival",
		16: ":cactus: Desert Festival",
		17: ":cactus: Desert Festival",
		24: ":tulip: Flower Dance"
	},
	"Summer": {
		11: ":palm_tree: Luau",
		20: ":fish: Trout Derby",
		21: ":fish: Trout Derby",
		28: ":jellyfish: Dance of the Moonlight Jellies"
	},
	"Fall": {
		16: ":flags: Stardew Valley Fair",
		27: ":jack_o_lantern: Spirit's Eve"
	},
	"Winter": {
		8: ":ice_cube: Festival of Ice",
		12: ":squid: SquidFest",
		13: ":squid: SquidFest",
		15: ":ring_buoy: Night Market",
		16: ":ring_buoy: Night Market",
		17: ":ring_buoy: Night Market",
		25: ":glowing_star: Feast of the Winter Star"
	}
}

def getFestival(day, seasonId):
	season = seasonNames[seasonId]
	festivalsInSeason = festivalList[season]
	if day in festivalsInSeason:
		return festivalsInSeason[day]
	
	return ""
