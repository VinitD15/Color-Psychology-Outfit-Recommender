## Festival Reminder Bot

This is a small Python project I made to remind me about upcoming festivals.
I can add any festival with its date, see all saved festivals, delete any festival, and the bot also tells me if a festival is today or coming soon.

# About the Project
The idea of this project is simple:
Sometimes we forget festival dates, so this bot helps by showing reminders.
I used Python basics like dates, dictionaries, lists, loops, and file handling.
The bot also saves everything in a JSON file so the data doesn’t get lost.

# Features

-- Add a festival with its date and an optional note
-- View all festivals in a neat table
-- Delete any festival
-- Reminder when a festival is today
-- Reminder for festivals coming in the next 7 days
-- Data gets saved automatically in festivals.json
-- Optional: Desktop notifications if plyer is installed

# Tools and Libraries I Used

-- Language: Python 3
-- Editor: VS Code

# Main Libraries
-- Datetime → to work with dates
-- json → to save and load festival data
-- OS → to clear screen

# Optional
-- prettytable → to show tables nicely
-- plyer → for popup reminders


# Data Storage
-- All the festivals are stored in a file called festivals.json.
-- This file is created automatically and keeps the data even after closing the program.

# Concepts Used

-- Dictionaries and lists
-- Functions
-- Date comparison
-- Loops
-- If-else
-- JSON file handling

## How to Run

1. Download the project folder
2. Open it in VS Code
3. Check Python is installed:
   python --version
4. Install extra libraries:
   pip install prettytable plyer
5. Run the program:
   python festival_bot.py

![Festival Reminder Bot Menu](image_alt)




