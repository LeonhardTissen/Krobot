from src.getResponse import getResponse
from src.loadSaveData import loadSaveData

# Get response from actual save data
(seasonId, day, year) = loadSaveData()
response = getResponse(seasonId, day, year)
print(response)

# Get response from all possible days, years, and seasons
for year in range(1, 3):
	for seasonId in range(0, 4):
		for day in range(1, 29):
			print(getResponse(seasonId, day, year))
