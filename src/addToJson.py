import json

remindersFile = 'reminders.json'

def addReminderToJson(reminder):
	try:
		# Open file
		with open(remindersFile, 'r') as f:
			reminderJson = json.load(f)
			reminderJson['reminders'].append(reminder)

			# Write to file
			with open(remindersFile, 'w') as f:
				json.dump(reminderJson, f, indent=4)
	
	except FileNotFoundError:
		# Create file if it doesn't exist

		with open(remindersFile, 'w') as f:
			json.dump({'reminders': [reminder]}, f, indent=4)
