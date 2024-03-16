# Load xml and convert to json
import xmltodict, json

saveLocation = "/home/warze/.config/StardewValley/Saves/Warze_367185259/Warze_367185259"

seasonNames = {
	0: "Spring",
	1: "Summer",
	2: "Fall",
	3: "Winter"
}

dates = {
	1: "Monday",
	2: "Tuesday",
	3: "Wednesday",
	4: "Thursday",
	5: "Friday",
	6: "Saturday",
	0: "Sunday"
}

def getFestival(day, seasonId):
	festival = ""
	season = seasonNames[seasonId]
	if season == "Spring":
		if day == 13:
			festival = "Egg Festival"
		elif day == 24:
			festival = "Flower Dance"
	elif season == "Summer":
		if day == 11:
			festival = "Luau"
		elif day == 28:
			festival = "Dance of the Moonlight Jellies"
	elif season == "Fall":
		if day == 16:
			festival = "Stardew Valley Fair"
		elif day == 27:
			festival = "Spirit's Eve"
	elif season == "Winter":
		if day == 8:
			festival = "Festival of Ice"
		elif day >= 15 and day <= 17:
			festival = "Night Market"
		elif day == 25:
			festival = "Feast of the Winter Star"

	if festival != "":
		return f"\n({festival})"
		
	return ""


def getBirthday(day, seasonId):
	birthday = ""

	season = seasonNames[seasonId]
	if season == "Spring":
		if day == 4:
			birthday = "Kent"
		elif day == 7:
			birthday = "Lewis"
		elif day == 10:
			birthday = "Vincent"
		elif day == 14:
			birthday = "Haley"
		elif day == 18:
			birthday = "Pam"
		elif day == 20:
			birthday = "Shane"
		elif day == 26:
			birthday = "Pierre"
		elif day == 27:
			birthday = "Emily"
		
	elif season == "Summer":
		if day == 4:
			birthday = "Jas"
		elif day == 8:
			birthday = "Gus"
		elif day == 10:
			birthday = "Maru"
		elif day == 13:
			birthday = "Alex"
		elif day == 17:
			birthday = "Sam"
		elif day == 19:
			birthday = "Demetrius"
		elif day == 22:
			birthday = "Dwarf"
		elif day == 24:
			birthday = "Willy"
		elif day == 26:
			birthday = "Leo"
	
	elif season == "Fall":
		if day == 2:
			birthday = "Penny"
		elif day == 5:
			birthday = "Elliott"
		elif day == 11:
			birthday = "Jodi"
		elif day == 13:
			birthday = "Abigail"
		elif day == 15:
			birthday = "Sandy"
		elif day == 18:
			birthday = "Marnie"
		elif day == 21:
			birthday = "Robin"
		elif day == 24:
			birthday = "George"
	
	elif season == "Winter":
		if day == 1:
			birthday = "Krobus"
		elif day == 3:
			birthday = "Linus"
		elif day == 7:
			birthday = "Caroline"
		elif day == 10:
			birthday = "Sebastian"
		elif day == 14:
			birthday = "Harvey"
		elif day == 17:
			birthday = "Wizard"
		elif day == 20:
			birthday = "Evelyn"
		elif day == 23:
			birthday = "Leah"
		elif day == 26:
			birthday = "Clint"
		

	if birthday != "":
		return f"\n([{birthday}](https://stardewcommunitywiki.com/{birthday})'s Birthday :birthday:)"

	return ""


def getDateSpecifics(date):
	specifics = ""

	if date == "Sunday":
		specifics += "\n:tv: The Queen of Sauce"
		specifics += "\n:cactus: Buy Staircases from the Desert Trader"
	elif date == "Wednesday":
		specifics += "\n:tv: The Queen of Sauce Re-run"
	elif date == "Thursday":
		specifics += "\n:cactus: Buy Magic Rock Candy from the Desert Trader"

	return specifics


	

def saveAsJson(parsedData):
	# Save the json data to a file with indentations
	data = json.dumps(parsedData, indent=4)
	with open('save.json', 'w') as file:
		file.write(data)
		file.close()

def getResponse(seasonId, day, year):
	date = dates[day % 7]
	seasonName = seasonNames[seasonId]

	festival = getFestival(day, seasonId)
	birthday = getBirthday(day, seasonId)
	dateSpecifics = getDateSpecifics(date)

	return f"""Day {day} of {seasonName}, Year {year}, {date}{festival}{birthday}{dateSpecifics}"""

def getSaveData():
	with open(saveLocation, 'r') as file:
		data = file.read()
		parsedData = xmltodict.parse(data)

		playerData = parsedData['SaveGame']['player']

		seasonId = int(playerData['seasonForSaveGame'])

		year = playerData['yearForSaveGame']

		day = int(playerData['dayOfMonthForSaveGame'])

		return (seasonId, day, year)



		

import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

	channel = bot.get_channel(int(os.getenv('CHANNEL_ID')))

	last_day = -1
	
	while True:
		(seasonId, day, year) = getSaveData()

		if last_day != day:
			last_day = day
			response = getResponse(seasonId, day, year)
			print(response)
			await channel.send(response)

		await asyncio.sleep(5)

bot.run(TOKEN)
