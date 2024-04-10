# *****************************************
# Shadows Snake Constants File
# *****************************************

# Import the required modules
import json, os, configparser, traceback

# Get the directory of the current script
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except:
    traceback.print_exc()

# Load colors from JSON file
try:
    with open(os.path.join(script_dir, '..', 'Themes', 'colors.json'), 'r') as f:
        COLORS_DICT = json.load(f)

    with open(os.path.join(script_dir, '..', 'Themes', 'snake_colors.json'), 'r') as f:
        SNAKE_COLOR_DICT = json.load(f)
except:
    traceback.print_exc()

# Load the game settings from the config.ini file
try:
    config = configparser.ConfigParser()
    config.read('config.ini')
except:
    traceback.print_exc()

SCREEN_SIZE_FULLSCREEN = None

# Get the screen size from the config.ini file
try:
    screen_size = config.get('Settings', 'screen_size', fallback='Default')
    if screen_size.lower()== 'default':
        # Get the actual size of the monitor
        width = 1200
        height = 800
    elif screen_size.lower() == 'fullscreen':
        SCREEN_SIZE_FULLSCREEN = 'fullscreen'
        width = 1200
        height = 800
    else:
        # Split the screen size into width and height and convert them to integers
        width, height = map(int, screen_size.split('x'))
except:
    traceback.print_exc()   

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
# Shadows Snake Constants File
# *****************************************