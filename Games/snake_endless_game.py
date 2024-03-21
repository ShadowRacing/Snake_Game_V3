# *****************************************
# Wims Snake Game Snake Endless Game File
# *****************************************

import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import COLORS_DICT

class Snake_endless(ctk.CTkCanvas):
    def __init__(self, parent, game_config):
        width = game_config.GAME_WIDTH
        height = game_config.GAME_HEIGHT
        highlightthickness = game_config.HIGHLIGHTTHICKNESS
        highlightbackground = game_config.HIGHLIGHTBACKGROUND
        super().__init__(parent, bg='Grey20', width=width, height=height, highlightthickness=highlightthickness, highlightbackground=highlightbackground)
        self.game_config = game_config
        self.draw_square()

    def draw_square(self):
        # Get the coordinates for the square from the game_config or set them as needed
        x1, y1, x2, y2 = 400, 400, 350, 350
        self.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")

# *****************************************
# Wims Snake Game Snake Endless Game File
# *****************************************