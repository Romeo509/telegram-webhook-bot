import customtkinter as ctk
from PIL import Image, ImageTk  # Importing Image and ImageTk for image handling
import os
import sys

# Function to generate the bot script
def generate_script():
    bot_token = token_entry.get()
    web_url = url_entry.get()
    
    if not bot_token or not web_url:
        status_label.configure(text="Please provide both Bot Token and Web URL", text_color="red")
        return

    script_type = "raw" if raw_var.get() else "exe"

    # Define the bot script content
    script_content = f"""from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
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
        os.system("pyinstaller --onefile --add-data 'telegram_bot_script.py;.' telegram_bot_script.py")
        status_label.configure(text=f"EXE generated: dist/telegram_bot_script.exe", text_color="green")
    else:
        status_label.configure(text=f"Script generated: {output_file}", text_color="green")
    
    # Clear input fields after submission (optional)
    token_entry.delete(0, 'end')
    url_entry.delete(0, 'end')
    raw_var.set(True)  # Reset the checkbox to default

# Create the main window
ctk.set_appearance_mode("dark")  # Set to dark theme
ctk.set_default_color_theme("blue")  # Theme color

app = ctk.CTk()  # Initialize the main window
app.title("Telegram Webhook Generator")
app.geometry("450x350")
app.configure(bg="#1c1c1c")  # Dark background resembling a hacker theme

# Determine if the application is running in a frozen state (as an EXE)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Path for frozen applications
else:
    base_path = os.path.dirname(os.path.abspath(__file__))  # Path for scripts

# Load background image
background_image_path = os.path.join(base_path, "images", "image.png")  # Specify the path to your image
background_image = Image.open(background_image_path)
background_image = background_image.resize((450, 350), Image.LANCZOS)  # Resize to fit the window
bg_image = ImageTk.PhotoImage(background_image)

# Create a "translucent glass-like" container in the center
container_frame = ctk.CTkFrame(app, corner_radius=15)  # No fg_color here for transparency effect
container_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Create a Label for the background image
bg_label = ctk.CTkLabel(container_frame, image=bg_image)  # Use a label to display the image
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Fill the container

# Set transparency by modifying the alpha value (translucency)
app.attributes("-alpha", 0.95)  # Slight transparency for the entire window (simulates glass effect)
container_frame.configure(fg_color=("#2a2a2a", "#3e3e3e"))  # Slight gradient-like colors for container

# Inside the container
token_label = ctk.CTkLabel(container_frame, text="Bot Token:", text_color="#ffffff")  # White text
token_label.pack(pady=10)
token_entry = ctk.CTkEntry(container_frame, width=300)
token_entry.pack()

url_label = ctk.CTkLabel(container_frame, text="Web URL:", text_color="#ffffff")  # White text
url_label.pack(pady=10)
url_entry = ctk.CTkEntry(container_frame, width=300)
url_entry.pack()

# Checkboxes for file type (Raw Python script or EXE)
raw_var = ctk.BooleanVar(value=True)
exe_var = ctk.BooleanVar(value=False)

def toggle_checkboxes():
    if raw_var.get():
        exe_var.set(False)
    else:
        raw_var.set(True)

raw_checkbox = ctk.CTkCheckBox(container_frame, text="Generate Raw Python Script", variable=raw_var, text_color="#ffffff", command=toggle_checkboxes)
raw_checkbox.pack(pady=5)

exe_checkbox = ctk.CTkCheckBox(container_frame, text="Generate EXE File", variable=exe_var, text_color="#ffffff", command=toggle_checkboxes)
exe_checkbox.pack(pady=5)

# Button to generate the script
generate_button = ctk.CTkButton(container_frame, text="Generate", command=generate_script, fg_color="#0078d7", text_color="#ffffff")  # Telegram blue
generate_button.pack(pady=20)

# Status label to show messages
status_label = ctk.CTkLabel(container_frame, text="", text_color="#ffffff")  # White text
status_label.pack(pady=10)

# Run the application
app.mainloop()
