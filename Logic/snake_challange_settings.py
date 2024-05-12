#********************************************************
# Challange Settings File
#********************************************************

"""
Module for the Snake Challange Settings screen of the Shadows Snake game.
"""

import customtkinter as ctk


class Challange_Settings(ctk.CTkCanvas):
    """
    Class for the Snake Challange Settings screen of the Shadows Snake game.
    """
    def __init__(self, parent, game_config, game_logger, functions, create_button_panel):
        self.parent = parent
        self.game_config = game_config
        self.game_logger = game_logger
        self.functions = functions
        self.create_button_panel = create_button_panel

        self.width = game_config.GAME_WIDTH
        self.game_logger.log_game_event(
            f"Game width: {self.width}"
        )
        self.height = game_config.GAME_HEIGHT
        self.game_logger.log_game_event(
            f"Game height: {self.height}"
        )
        self.game_logger.log_game_event(game_config.SNAKE_LENGTH)
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground)

#********************************************************
# Challange Settings File
#********************************************************
