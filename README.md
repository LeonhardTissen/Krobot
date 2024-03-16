# Stardew Valley Reminder Bot

![Krobot](img/krobotbannerlarge.png)

A script that sends reminders to a Discord channel for the game Stardew Valley.

It shows various events such as birthdays and festivals.

The script can be run as a bot or alternatively as a webhook.

## Installation

Install required packages
```bash
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in the required fields
```bash
cp .env.example .env
```

In order to load the save file, you will need to fill in the `SAVE_FILE` field. Instructions on finding your save file can be found [here](https://stardewcommunitywiki.com/Saves#Find_your_save_files).

If you are running the webhook, you will need to fill in the `WEBHOOK_URL` field.

If you are running the bot, you will need to fill in the `DISCORD_TOKEN` and `CHANNEL_ID` fields.

## Testing

See all possible responses
```bash
python3 testall.py
```

See response for the current save file
```bash
python3 testsave.py
```

## Usage

Run the bot
```bash
python3 bot.py
```

Or use the webhook
```bash
python3 webhook.py
```
