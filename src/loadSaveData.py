import xmltodict

from .loadEnv import SAVE_LOCATION

def loadSaveData():
	with open(SAVE_LOCATION, 'r') as file:
		data = file.read()
		parsedData = xmltodict.parse(data)

		playerData = parsedData['SaveGame']['player']

		seasonId = int(playerData['seasonForSaveGame'])

		year = playerData['yearForSaveGame']

		day = int(playerData['dayOfMonthForSaveGame'])

		return (seasonId, day, year)
