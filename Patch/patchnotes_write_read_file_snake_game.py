# *****************************************
# Shadows Snake Patchnotes File
# *****************************************

"""
Module for managing the patchnotes of the Shadows Snake game.
"""

# Import the json module
import json
import traceback

# Define the patchnotes list
patchnotes = [
    {
        "version": "0.2.6",
        "changes": [
            "Bug fixes:",
            "game size sets contrast to default",
            "game size sets theme to default",
            "theme sets game size to default",
            "theme sets contrast to default",
            "contrast sets game size to default",
            "contrast sets theme to default"
        ]
    },
    {
        "version": "0.2.5",
        "changes": [
            "New features:",
            "Added the ability to reset kebindings",
            "added the ability to reset all the settings to default",
            "Redone the game settings screen again, now with a better layout",
            "Bug fixes:",
            "Fixed that the screen for the keybindings was not working correctly",
            "When patchnotes is open and you go back home you cannot open the Patchnotes anymore",
            "reset frame satays when you have opent it when going home",
            "Buttons stayed for the settings reset buttons frame"
        ]
    },
    {
        "version": "0.2.4",
        "changes": [
            "New features:",
            "Added the ability to change the key bindings",
            "Redone the game settings screen",
            "Bug fixes:",
            "Fixed that the screen for the keybindings was not working correctly",
        ]
    },
    {
        "version": "0.2.3",
        "changes": [
            "Rewrote the bindingskeys Preparing for the next update:",
        ]
    },
    {
        "version": "0.2.2",
        "changes": [
            "New features:",
            "Better error handling",
            "Better logging",
            "Bug fixes:",
            "No label when changing themes",
            "No label when changing game size",
            "Endless game mode doesn't work",
        ]
    },
    {
        "version": "0.2.1",
        "changes": [
            "New features:",
            "Added error handling",
            "Bug fixes:",
            "No reset buttons on the classic snake",
            "No label on the classic snake",
            "No reset buttons on the endless snake",
            "No label on the endless snake",
            "No reset buttons on the leveling snake",
            "No label on the leveling snake",
            "Reset definition doesn't work Classic snake",
            "Reset definition doesn't work Endless snake",
            "Reset definition doesn't work leveling snake",
            "Canvas isn't being destroyed when going to home classic snake",
            "Canvas isn't being destroyed when going to home endless snake",
            "Canvas isn't being destroyed when going to home leveling snake",
            "Cannot update highscores classic snake",
            "Cannot update highscores endless snake",
            "Cannot update highscores leveling snake",
            "Home screen called multiple times",
            "No reset buttons for the highscores classic snake",
            "No reset buttons for the highscores endless snake",
            "No reset buttons for the highscores leveling snake"
        ]
    },
    {
        "version": "0.2.0",
        "changes": [
            "New features:",
            "Restructerd the Main file code"
        ]
    },
    {
        "version": "0.1.6",
        "changes": [
            "Bug fixes:",
            "Fixed that the theme and game_size restart labels were cancelling eachother out",
            "Fixed that the level system was not working correctly",
            "Fixed that the level is not saved with the highscores",
            "Hopefully fixed that the levels are not being reset properly",
            "Fixed that fullscreen was not working correctly",
            "Fixed that when starting you were starting with xp=1 instead off xp=0"
        ]
    },
    {
        "version": "0.1.5",
        "changes": [
            "New features:",
            "Added leveling game mode",
            "Added themes to the game",
            "Added a new food type: Special food",
            "Added a new food type: Shorten food",
            ""
            "Bug fixes:",
            "Fixed that when you press all the buttons the snake dies instantly",
            "The labels for the highscores are now updating correctly",
            "Fixed that the shorten food highscore was not updating correctly",
            "Fixed that the Special highscore was not updating correctly",
            "Fixed that all the food types cannot overlap eachother"
        ]
    },
    {
        "version": "0.1.4",
        "changes": [
            "New features:",
            "Added config.ini to keep track off the settings and scores",
            "Bug fixes:",
            "Labels not updating when they have been reset",
            "Fixed that the game timer was still running when paused",
        ]
    },
    {
        "version": "0.1.3",
        "changes": [
            "New features:",
            "Added Labels to the game",
            "Bug fixes:",
            "The default screen width and height don't center the app",
            "Reset highscores not exctually resetting the highscores",
            "Fixed the speed bug in the code"
        ]
    },
    {
        "version": "0.1.2",
        "changes": [
            "New features:",
            "Added Highscores to the game",
            "Bug fixes:",
            "Fixed the bugs regarding the gamelogger",
            "Fixed screen size bug",
            "Fixed information screen not working properly",
            "Fixed that the restart label in the settings screen was not working",
            "Fixed no labels on the canvasses"
        ]
    },
    {
        "version": "0.1.1",
        "changes": [
            "New features:",
            "Added a new game mode: Endless mode",
            "Added a new game mode: Leveling mode",
            "Added a game logger to log the game",
            "Bug fixes:",
            "When going back to normal size from fullscreen, the game size is now correctly resized",
            "With no size in config.ini the game doesn't crash anymore"
        ]
    },
    {
        "version": "0.1",
        "changes": [
            "Initial release",
            "Bug fixes:",
            "Fix a bug regarding remembering the game size",
            "No fullscreen when setting to fullscreen mode",
            "Improved performance"
        ]
    }
]
# Save the patchnotes to a JSON file
FILENAME = "patchnotes.json"
try:
    with open(FILENAME, "w", encoding='utf-8') as file:
        json.dump(patchnotes, file)
except FileNotFoundError as e:
    traceback.print_exc(e)

# Read the patchnotes from the JSON file
try:
    with open(FILENAME, "r", encoding='utf-8') as file:
        patchnotes = json.load(file)
except FileNotFoundError as e:
    traceback.print_exc(e)

# Print the patchnotes


# *****************************************
# Shadows Snake Patchnotes File
# *****************************************
