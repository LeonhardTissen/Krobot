import os
import xmltodict
from dotenv import load_dotenv

load_dotenv()

saveLocation = os.getenv('SAVE_LOCATION')

def loadSaveData():
	with open(saveLocation, 'r') as file:
		data = file.read()
		parsedData = xmltodict.parse(data)

		playerData = parsedData['SaveGame']['player']

		seasonId = int(playerData['seasonForSaveGame'])

		year = playerData['yearForSaveGame']

		day = int(playerData['dayOfMonthForSaveGame'])

		return (seasonId, day, year)
