from .addToJson import addReminderToJson
from .currentDay import getCurrentDay
from .seasonNames import seasonNames
from .reminders import getReminders

async def execCommand(args, message):
	# Example: in 3 days Ancient fruit will be ready
	command = args[0]
	if command == "in":
		addedType = args[2]
		addedNumber = args[1]

		if addedType == "days" or addedType == "day":
			addedDays = int(addedNumber)
		elif addedType == "weeks" or addedType == "week":
			addedDays = int(addedNumber) * 7
		elif addedType == "months" or addedType == "month":
			addedDays = int(addedNumber) * 28
		else:
			await message.channel.send("Please enter a valid time type (`days`, `weeks`, `months`)")
			return

		maximumDays = 112

		if addedDays < 1 or addedDays > maximumDays:
			await message.channel.send(f"Please enter a valid number of days (1-{maximumDays})")
			return

		reminder = " ".join(args[3:])

		(day, seasonId, year) = getCurrentDay()

		newDay = int(day) + addedDays

		while newDay > 28:
			newDay = newDay - 28
			seasonId += 1
			if seasonId > 3:
				seasonId = 0
				year += 1

		addReminderToJson({
			"day": newDay,
			"seasonId": seasonId,
			"year": year,
			"reminder": reminder,
			"initiator": message.author.id
		})

		await message.channel.send(f"Reminder set for {seasonNames[seasonId]} {newDay}, Year {year}: {reminder}")
	elif command == "reminders":
		await message.channel.send(getReminders())
