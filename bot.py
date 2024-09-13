from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_TOKEN = 'your tokken'

async def start(update: Update, context: CallbackContext) -> None:
    # Define the Web App link you want to open inside Telegram as a modal
    web_app_url = "https://www.youtube.com"

    # Creates a button that opens the Web App in Telegram
    keyboard = [[InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=web_app_url))]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the Web App:', reply_markup=reply_markup)

def main() -> None:
    # Creates the Application and passes it to your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Adds command handler for /start command
    application.add_handler(CommandHandler('start', start))

    # Runs the bot until you send a signal to stop
    application.run_polling()

if __name__ == '__main__':
    main()
