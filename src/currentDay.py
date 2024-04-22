import json

lastDayFile = 'lastday.json'

def isNewDay(seasonId, day, year):
	# Check if file exists
	try:
		with open(lastDayFile, 'r') as f:
			last_day = json.load(f)

			# If the day has changed, update file and return True
			if last_day['seasonId'] != seasonId or last_day['day'] != day or last_day['year'] != year:
				with open(lastDayFile, 'w') as f:
					json.dump({'seasonId': seasonId, 'day': day, 'year': year}, f, indent=4)
				return True
			else:
				return False

	except FileNotFoundError:
		# Create file if it doesn't exist
		with open(lastDayFile, 'w') as f:
			json.dump({'seasonId': seasonId, 'day': day, 'year': year}, f, indent=4)
		return True

def getCurrentDay():
	# Get current day from file
	try:
		with open(lastDayFile, 'r') as f:
			last_day = json.load(f)
			return (last_day['day'], last_day['seasonId'], last_day['year'])
	except FileNotFoundError:
		return 0
	