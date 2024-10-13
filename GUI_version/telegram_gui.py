import customtkinter as ctk
import os

# Function to generate the bot script
def generate_script():
    bot_token = token_entry.get()
    web_url = url_entry.get()
    script_type = "raw" if raw_var.get() else "exe"

    # Define the bot script content
    script_content = f"""from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, CallbackContext

TELEGRAM_TOKEN = '{bot_token}'

async def start(update: Update, context: CallbackContext) -> None:
    web_app_url = "{web_url}"
    keyboard = [[InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=web_app_url))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the Web App:', reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

if __name__ == '__main__':
    main()
"""

    # Save the script
    output_file = "telegram_bot_script.py"
    with open(output_file, "w") as file:
        file.write(script_content)

    if script_type == "exe":
        # Use PyInstaller to create the EXE file
        os.system("pyinstaller --onefile --noconsole telegram_bot_script.py")
        status_label.configure(text="EXE generated: dist/telegram_bot_script.exe")
    else:
        status_label.configure(text="Script generated: telegram_bot_script.py")

# Create the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Telegram Webhook Generator")
app.geometry("450x350")
app.configure(bg="#1c1c1c")

container_frame = ctk.CTkFrame(app, fg_color="#ffffff", corner_radius=15)
container_frame.pack(padx=20, pady=20, fill="both", expand=True)

app.attributes("-alpha", 0.95)
container_frame.configure(fg_color=("#2a2a2a", "#3e3e3e"))

# Inside the container
token_label = ctk.CTkLabel(container_frame, text="Bot Token:", text_color="#ffffff")
token_label.pack(pady=10)
token_entry = ctk.CTkEntry(container_frame, width=300)
token_entry.pack()

url_label = ctk.CTkLabel(container_frame, text="Web URL:", text_color="#ffffff")
url_label.pack(pady=10)
url_entry = ctk.CTkEntry(container_frame, width=300)
url_entry.pack()

# Checkboxes for file type (Raw Python script or EXE)
raw_var = ctk.BooleanVar(value=True)
exe_var = ctk.BooleanVar(value=False)

raw_checkbox = ctk.CTkCheckBox(container_frame, text="Generate Raw Python Script", variable=raw_var, text_color="#ffffff")
raw_checkbox.pack(pady=5)

exe_checkbox = ctk.CTkCheckBox(container_frame, text="Generate EXE File", variable=exe_var, text_color="#ffffff")
exe_checkbox.pack(pady=5)

# Button to generate the script
generate_button = ctk.CTkButton(container_frame, text="Generate", command=generate_script, fg_color="#0078d7", text_color="#ffffff")
generate_button.pack(pady=20)

# Status label to show messages
status_label = ctk.CTkLabel(container_frame, text="", text_color="#ffffff")
status_label.pack(pady=10)

# Run the application
app.mainloop()
