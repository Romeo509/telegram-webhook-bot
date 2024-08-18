from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Open Link", url="https://your-web-hosting.com/your-page")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below:', reply_markup=reply_markup)

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command handler for /start command
    application.add_handler(CommandHandler('start', start))

    # Run the bot until you send a signal to stop
    application.run_polling()

if __name__ == '__main__':
    main()
