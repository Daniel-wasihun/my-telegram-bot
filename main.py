# main.py
from telegram.ext import Application, CommandHandler
import asyncio
import logging
import os
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update, context):
    """Sends a welcome message when the /start command is issued."""
    user = update.effective_user
    logger.info("User %s started the bot.", user.id)
    await update.message.reply_html(
        f"Hello, Welcome to Daniel Wasihun Bot, {user.mention_html()}! 👋",
        # reply_markup=ForceReply(selective=True),
    )

def main():
    """Starts the bot."""
    # Get the bot token from the environment variable 'TELEGRAM_BOT_TOKEN'
    # load_dotenv() above ensures this variable is now available
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')

    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set in .env file or system.")
        raise ValueError("Telegram bot token not found. Please set the TELEGRAM_BOT_TOKEN in your .env file.")

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot started polling...")
    application.run_polling()
    logger.info("Bot stopped.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error("An error occurred: %s", e)

