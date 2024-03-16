from src.getResponse import getResponse

# Get response from all possible days, years, and seasons
for year in range(1, 3):
	for seasonId in range(0, 4):
		for day in range(1, 29):
			print(getResponse(seasonId, day, year))
