#***********************************************
# Snake Challange Choice File
#***********************************************

"""
Module for the Snake Challange Choice screen of the Shadows Snake game.
"""

import customtkinter as ctk

class Challange_Choices(ctk.CTkCanvas):
    """
    Class for the Snake Challange Choice screen of the Shadows Snake game.
    """
    def __init__(self, parent, game_config, logfile, functions, create_button_panel):
        self.parent = parent
        self.game_config = game_config
        self.logfile = logfile
        self.functions = functions
        self.create_button_panel = create_button_panel

        self.width = game_config.GAME_WIDTH
        print(
            f"Game width: {self.width}"
        )
        self.height = game_config.GAME_HEIGHT
        print(
            f"Game height: {self.height}"
        )
        print(game_config.SNAKE_LENGTH)
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, 
                         highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
