import json

def addReminderToJson(reminder):
	try:
		# Open reminders.json file
		with open('reminders.json', 'r') as f:
			reminderJson = json.load(f)
			reminderJson['reminders'].append(reminder)

			# Write to reminders.json
			with open('reminders.json', 'w') as f:
				json.dump(reminderJson, f, indent=4)
	
	except FileNotFoundError:
		# Create reminders.json if it doesn't exist

		with open('reminders.json', 'w') as f:
			json.dump({'reminders': [reminder]}, f, indent=4)
