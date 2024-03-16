from src.getResponse import getResponse
from src.loadSaveData import loadSaveData

(seasonId, day, year) = loadSaveData()
response = getResponse(seasonId, day, year)
print(response)

year = 1
for seasonId in range(0, 4):
	for day in range(1, 29):
		print(getResponse(seasonId, day, year))
