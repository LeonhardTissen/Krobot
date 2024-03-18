from discord import Client, Intents
import asyncio

from src.getResponse import getResponse
from src.loadSaveData import loadSaveData
from src.loadEnv import TOKEN, CHANNEL_ID
from src.isNewDay import isNewDay

bot = Client(intents=Intents.all())

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

	channel = bot.get_channel(CHANNEL_ID)
	
	# Continuously check for new day
	while True:
		(seasonId, day, year) = loadSaveData()

		# If the day has changed, send a message to the channel with the new response
		if isNewDay(seasonId, day, year):
			response = getResponse(seasonId, day, year)
			print(response)
			await channel.send(response)

		await asyncio.sleep(5)

if __name__ == "__main__":
	bot.run(TOKEN)
