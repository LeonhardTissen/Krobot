from src.getResponse import getResponse
from src.loadSaveData import loadSaveData

# Get response from actual save data
(seasonId, day, year) = loadSaveData()
response = getResponse(seasonId, day, year)
print(response)
