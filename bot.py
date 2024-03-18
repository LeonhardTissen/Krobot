from discord import Client, Intents
import asyncio

from src.getResponse import getResponse
from src.loadSaveData import loadSaveData
from src.loadEnv import TOKEN, CHANNEL_ID
from src.currentDay import isNewDay
from src.commands import execCommand

bot = Client(intents=Intents.all())

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

	channel = bot.get_channel(CHANNEL_ID)
	
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

		await asyncio.sleep(5)

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	args = message.content.split(" ")

	await execCommand(args, message.channel)

if __name__ == "__main__":
	bot.run(TOKEN)
