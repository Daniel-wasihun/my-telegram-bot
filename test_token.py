# test_token.py
import asyncio
from telegram import Bot

async def test_bot():
    bot = Bot(token='BOT_TOKEN')
    try:
        me = await bot.get_me()
        print(f"Bot is working: {me}")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(test_bot())
