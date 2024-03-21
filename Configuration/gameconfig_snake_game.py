# *****************************************
# Wims Snake Game Config File
# *****************************************

# Class for the game configuration
class GameConfig:
    def __init__(self, logfile, game_mode):
        # Initializing variables
        self.logfile = logfile
        self.TIME_PLAYED = 0
        
        # Set the game configuration
        try:
            self.set_configuration(game_mode)
        except ValueError as e:
            self.logfile.log_game_event(f"Error setting configuration: {e}")

    # Method to set the game configuration
    def set_configuration(self, game_mode):
        try:
            if game_mode == "initial_config":
                self.GAME_WIDTH = 300
                self.GAME_HEIGHT = 300
                self.SPEED = 10
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 3
                self.SNAKE_COLOR = 'White'
                self.SNAKE_OUTLINE = 'Black'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Blue'
                self.BACKGROUND_COLOR = 'Blue'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: initial config")

            elif game_mode == "classic_snake":
                self.GAME_WIDTH = 500
                self.GAME_HEIGHT = 500
                self.SPEED = 10
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 5
                self.SNAKE_COLOR = 'Green'
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: classic_snake")

            elif game_mode == "snake_endless":
                self.GAME_WIDTH = 400
                self.GAME_HEIGHT = 400
                self.SPEED = 20
                self.CELL_SIZE = 20
                self.SNAKE_LENGTH = 5
                self.SNAKE_COLOR = 'Green'
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Red'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: snake_endless")

            elif game_mode == "snake_special":
                self.GAME_WIDTH = 400
                self.GAME_HEIGHT = 400
                self.SPEED = 40
                self.CELL_SIZE = 10
                self.SNAKE_LENGTH = 2
                self.SNAKE_COLOR = 'Red'
                self.SNAKE_OUTLINE = 'White'
                self.FOOD_COLOR = 'Green'
                self.SPECIAL_FOOD_COLOR = 'Purple'
                self.BACKGROUND_COLOR = 'Black'
                self.HIGHLIGHTTHICKNESS = 5
                self.HIGHLIGHTBACKGROUND = 'Black'
                self.DIRECTIONOFFSNAKE = "down"
                self.logfile.log_game_event("Game mode: snake_special")
        except KeyError as e:
           self.logfile.log_game_event(f"Error: Color '{e.args[0]}' not found in COLORS_DICT.")

# *****************************************
# Wims Snake Game Config File
# *****************************************