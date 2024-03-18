from discord import Client, Intents, Streaming
import asyncio

from src.getResponse import getResponse
from src.loadSaveData import loadSaveData
from src.loadEnv import TOKEN, CHANNEL_ID
from src.currentDay import isNewDay
from src.commands import execCommand
from src.seasonNames import seasonNames

bot = Client(intents=Intents.all())

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

	channel = bot.get_channel(CHANNEL_ID)

	currentStatus = None
	
	# Continuously check for new day
	while True:
		(seasonId, day, year) = loadSaveData()
		# Testing:
		# (seasonId, day, year) = (3, 1, 6)

		# If the day has changed, send a message to the channel with the new response
		if isNewDay(seasonId, day, year):
			response = getResponse(seasonId, day, year)
			print(response)
			await channel.send(response)

		# Set status to current day
		status = f"{seasonNames[seasonId]} {day}, Year {year}"
		
		if currentStatus != status:
			currentStatus = status
			await bot.change_presence(activity=Streaming(name=status, url="https://twitch.tv/WarzeDev"))

		await asyncio.sleep(5)

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	args = message.content.split(" ")

	await execCommand(args, message)

if __name__ == "__main__":
	bot.run(TOKEN)
