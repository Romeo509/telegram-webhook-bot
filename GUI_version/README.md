# Telegram Bot Webhook Generator

## Overview
The **Telegram Bot Webhook Generator** is a Python-based graphical user interface (GUI) application designed to simplify the creation of Telegram bots that can launch web apps. This tool allows users to generate Python scripts for Telegram bots with a simple user interface, offering two output options: a raw Python script or an executable file. 

This project utilizes the `customtkinter` library for modern GUI design and the `python-telegram-bot` library for interacting with the Telegram Bot API.

## Features
- **User-friendly Interface**: Create bots easily with a straightforward GUI.
- **Bot Token Input**: Enter your Telegram bot token to authenticate.
- **Web App URL Input**: Specify the URL of the web application you want to link.
- **Output Options**: Generate either a raw Python script or a standalone executable.
- **Custom Background**: Aesthetic design with a customizable background image.

## Requirements
Before running the application, ensure you have the following installed:

- Python 3.12 or later
- Required Python packages:
  - `customtkinter`
  - `Pillow`
  - `python-telegram-bot`
  - `PyInstaller` (for compiling to EXE)

### Installation
To install the required packages, use pip:

```bash
pip install customtkinter Pillow python-telegram-bot pyinstaller
