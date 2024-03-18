import json

def isNewDay(seasonId, day, year):
	# Check if lastday.json exists
	try:
		with open('lastday.json', 'r') as f:
			last_day = json.load(f)

			# If the day has changed, update lastday.json and return True
			if last_day['seasonId'] != seasonId or last_day['day'] != day or last_day['year'] != year:
				with open('lastday.json', 'w') as f:
					json.dump({'seasonId': seasonId, 'day': day, 'year': year}, f)
				return True
			else:
				return False

	except FileNotFoundError:
		# Create lastday.json if it doesn't exist
		with open('lastday.json', 'w') as f:
			json.dump({'seasonId': seasonId, 'day': day, 'year': year}, f)
		return True

def getCurrentDay():
	# Get current day from lastday.json
	try:
		with open('lastday.json', 'r') as f:
			last_day = json.load(f)
			return (last_day['day'], last_day['seasonId'], last_day['year'])
	except FileNotFoundError:
		return 0
	