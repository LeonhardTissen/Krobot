from discord import Client, Intents
import asyncio

from src.getResponse import getResponse
from src.loadSaveData import loadSaveData
from src.loadEnv import TOKEN, CHANNEL_ID

bot = Client(intents=Intents.all())

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))

	channel = bot.get_channel(CHANNEL_ID)

	last_day = -1
	
	while True:
		(seasonId, day, year) = loadSaveData()

		if last_day != day:
			last_day = day
			response = getResponse(seasonId, day, year)
			print(response)
			await channel.send(response)

		await asyncio.sleep(5)

bot.run(TOKEN)
