from .addToJson import addReminderToJson
from .currentDay import getCurrentDay
from .seasonNames import seasonNames
from .reminders import getReminders

dayMultipliers = {
	"day": 1,
	"week": 7,
	"month": 28,
}

minimumDays = 1
maximumDays = 112
async def execCommandInNDays(args, message):
	addedNumber = int(args[1])
	addedType = args[2]
	reminder = " ".join(args[3:])
	# Remove s if it's plural
	if addedType[:-1] == "s":
		addedType = addedType[:-1]

	if addedType not in dayMultipliers:
		await message.channel.send("Please enter a valid time type (`days`, `weeks`, `months`)")
		return
	
	addedDays = addedNumber * dayMultipliers[addedType]

	if addedDays < minimumDays or addedDays > maximumDays:
		await message.channel.send(f"Please enter a valid number of days (1-{maximumDays})")
		return

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

async def execCommand(args, message):
	# Example: in 3 days Ancient fruit will be ready
	command = args[0]
	if command == "in":
		await execCommandInNDays(args, message)
	elif command == "reminders":
		await message.channel.send(getReminders())
