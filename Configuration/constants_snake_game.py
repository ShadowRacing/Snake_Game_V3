# *****************************************
# Shadows Snake Constants File
# *****************************************

"""
This module contains the constants used in the Shadows Snake game.
"""

# Import the required modules
import json
import os
import configparser
import traceback

# Get the directory of the current script
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except FileNotFoundError as e:
    traceback.print_exc(e)

# Load colors from JSON file
try:
    with open(os.path.join(script_dir, '..', 'Themes', 'colors.json'), 'r', encoding='utf-8') as colors: # pylint: disable=line-too-long
        COLORS_DICT = json.load(colors)

    with open(os.path.join(script_dir, '..', 'Themes', 'snake_colors.json'), 'r', encoding='utf-8') as colors: # pylint: disable=line-too-long
        SNAKE_COLOR_DICT = json.load(colors)
except FileNotFoundError as e:
    traceback.print_exc(e)

# Load the game settings from the config.ini file
try:
    config = configparser.ConfigParser()
    config.read('config.ini')
except FileNotFoundError as e:
    traceback.print_exc(e)

SCREEN_SIZE_FULLSCREEN = None

# Get the screen size from the config.ini file
try:
    screen_size = config.get('Settings', 'screen_size', fallback='Default')
    if screen_size.lower()== 'default':
        # Get the actual size of the monitor
        width = 1200 # pylint: disable=invalid-name
        height = 800 # pylint: disable=invalid-name
    elif screen_size.lower() == 'fullscreen':
        SCREEN_SIZE_FULLSCREEN = 'fullscreen'
        width = 1200 # pylint: disable=invalid-name
        height = 800 # pylint: disable=invalid-name
    else:
        # Split the screen size into width and height and convert them to integers
        width, height = map(int, screen_size.split('x'))
except ValueError as e:
    traceback.print_exc(e)

# Define other constants
class GameConstants:
    """
    Class for the constants used in the Shadows Snake game.
    """
    CLICK_BUTTON_WIDTH = 150
    CLICK_BUTTON_HEIGHT = 40
    CLICK_BUTTON_CORNER_RADIUS = 6
    OPTION_BUTTON_WIDTH = 175
    OPTION_BUTTON_HEIGHT = 40
    OPTION_BUTTON_CORNER_RADIUS = 6
    GAME_WIDTH = 400
    GAME_HEIGHT = 400
    MIN_HEIGHT = height
    MIN_WIDTH = width
    RESIZING = False
    SETTINGS_LABEL_WIDTH = 175
    SETTINGS_LABEL_HEIGHT = 30
    SETTINGS_LABEL_CORNER_RADIUS = 6
    SETTINGS_BUTTON_RESET_WIDTH = 175
    SETTINGS_BUTTON_RESET_HEIGHT = 40
    SETTINGS_BUTTON_RESET_CORNER_RADIUS = 6
    SETTINGS_BUTTON_RESET_TEXT = "Reset Button"
    GAME_LABEL_WIDTH = 275
    GAME_LABEL_HEIGHT = 30
    GAME_LABEL_CORNER_RADIUS = 6
    ANCHOR = 'w'



# Define the font list
FONT_SIZE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
FONT_LIST = [('consolas', size) for size in FONT_SIZE_LIST]

# *****************************************
# Shadows Snake Constants File
# *****************************************
