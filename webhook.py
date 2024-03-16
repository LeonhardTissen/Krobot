from discord_webhook import DiscordWebhook
import asyncio

from src.getResponse import getResponse
from src.loadSaveData import loadSaveData
from src.loadEnv import WEBHOOK_URL
	
# Continuously check for new day
async def main():
	last_day = -1

	while True:
		(seasonId, day, year) = loadSaveData()

		# If the day has changed, send a message to the channel with the new response
		if last_day != day:
			last_day = day
			response = getResponse(seasonId, day, year)
			print(response)
			webhook = DiscordWebhook(url=WEBHOOK_URL, content=response)
			webhookResponse = webhook.execute()
			print(webhookResponse)

		await asyncio.sleep(5)

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	loop.close()
