# Stardew Valley Reminder Bot

![Krobot](img/krobotbannerlarge.png)

A script that sends reminders to a Discord channel for the game Stardew Valley.

It shows various events such as birthdays and festivals.

## Installation

Install required packages
```bash
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in the required fields
```bash
cp .env.example .env
```

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

Or use a webhook
```bash
python3 webhook.py
```
