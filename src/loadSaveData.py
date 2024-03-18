import xmltodict

from .loadEnv import SAVE_LOCATION

def loadSaveData():
	with open(SAVE_LOCATION, 'r') as file:
		# Parse the save XML data to a dictionary and extract day, season and year
		data = file.read()
		parsedData = xmltodict.parse(data)

		playerData = parsedData['SaveGame']['player']

		seasonId = int(playerData['seasonForSaveGame'])

		year = int(playerData['yearForSaveGame'])

		day = int(playerData['dayOfMonthForSaveGame'])

		# Account for rare case where game thinks the day is 29
		if day > 28:
			day = 1
			seasonId += 1
			if seasonId > 3:
				seasonId = 0
				year += 1

		return (seasonId, day, year)
