# *****************************************
# Wims Snake Constants File
# *****************************************

# Import the required modules
import json, os, configparser

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load colors from JSON file
with open(os.path.join(script_dir, '..', 'Themes', 'colors.json'), 'r') as f:
    COLORS_DICT = json.load(f)

with open(os.path.join(script_dir, '..', 'Themes', 'snake_colors.json'), 'r') as f:
    SNAKE_COLOR_DICT = json.load(f)

# Load the game settings from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')



# Get the screen size from the config.ini file
screen_size = config.get('Settings', 'screen_size', fallback='Default')
if screen_size.lower() == 'fullscreen' or screen_size.lower()== 'default':
    # Get the actual size of the monitor
    width = 1200
    height = 800
else:
    # Split the screen size into width and height and convert them to integers
    width, height = map(int, screen_size.split('x'))


# Define other constants
class GameConstants:
    BUTTON_WIDTH = 160
    BUTTON_HEIGHT = 40
    GAME_WIDTH = 400
    GAME_HEIGHT = 400
    MIN_HEIGHT = height
    MIN_WIDTH = width
    RESIZING = False

# Define the font list
FONT_SIZE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
FONT_LIST = [('consolas', size) for size in FONT_SIZE_LIST]

# *****************************************
# Wims Snake Constants File
# *****************************************