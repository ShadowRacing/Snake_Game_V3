"""
This module is responsible for creating the button panel of the Shadows Snake game. # pylint: disable=line-too-long
"""

# Importing necessary modules
import customtkinter as ctk

# Importing necessary modules from other folders
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST

class ResetSettingsPanel:
    """
    Class for creating the reset settings panel of the Shadows Snake game.
    """
    def __init__(self, settings_canvas_reset, game_logger, functions):
        # Initializing variables
        self.settings_canvas_reset = settings_canvas_reset
        self.game_logger = game_logger
        self.functions = functions
        self.buttons = []
        self.theme_updater = ThemeUpdater(self.game_logger)

        # Managing the buttons height and width
        self.button_width = GameConstants.SETTINGS_BUTTON_RESET_WIDTH
        self.button_height = GameConstants.SETTINGS_BUTTON_RESET_HEIGHT
        self.corner_radius = GameConstants.SETTINGS_BUTTON_RESET_CORNER_RADIUS
        self.text = GameConstants.SETTINGS_BUTTON_RESET_TEXT

    def show_all_reset_buttons(self):
        """
        Show all reset buttons.
        """
        self.reset_screen_size_button()
        self.reset_theme_button()
        self.reset_contrast_button()
        self.reset_high_score_label_showing_button()
        self.reset_snake_speed_button()
        self.reset_game_size_button()
        self.reset_snake_color_button()
        self.reset_move_up_button()
        self.reset_move_down_button()
        self.reset_move_left_button()
        self.reset_move_right_button()
        self.reset_start_game_button()
        self.reset_pause_game_button()
        self.reset_restart_game_button()
        self.reset_all_settings_button()
        self.reset_all_movements_button()

    def info_general_reset_mini_snake_command(self):
        """
        Function for the info general reset mini snake button command.
        """
        if 'info_general_reset_mini_snake' in self.functions:
            self.functions['info_general_reset_mini_snake']()
        else:
            self.game_logger.log_game_event("No function assigned to 'info_general_reset_mini_snake'")

    def reset_screen_size_command(self):
        """
        Function for the reset screen size button command.
        """
        if 'reset_screen_size' in self.functions:
            self.functions['reset_screen_size']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_screen_size'")

    def reset_theme_command(self):
        """
        Function for the reset theme button command.
        """
        if 'reset_theme' in self.functions:
            self.functions['reset_theme']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_theme'")

    def reset_contrast_command(self):
        """
        Function for the reset contrast button command.
        """
        if 'reset_contrast' in self.functions:
            self.functions['reset_contrast']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_contrast'")

    def reset_high_score_label_showing_command(self):
        """
        Function for the high score label showing button command.
        """
        if 'reset_high_score_label_showing' in self.functions:
            self.functions['reset_high_score_label_showing']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_high_score_label_showing'") # pylint: disable=line-too-long

    def reset_snake_speed_command(self):
        """
        Function for the reset snake speed button command.
        """
        if 'reset_snake_speed' in self.functions:
            self.functions['reset_snake_speed']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_snake_speed'")

    def reset_game_size_command(self):
        """
        Function for the reset game size button command.
        """
        if 'reset_game_size' in self.functions:
            self.functions['reset_game_size']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_game_size'")

    def reset_snake_color_command(self):
        """
        Function for the reset snake color button command.
        """
        if 'reset_snake_color' in self.functions:
            self.functions['reset_snake_color']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_snake_color'")

    def reset_move_up_command(self):
        """
        Function for the reset move up button command.
        """
        if 'reset_move_up' in self.functions:
            self.functions['reset_move_up']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_up'")

    def reset_move_down_command(self):
        """
        Function for the reset move down button command.
        """
        if 'reset_move_down' in self.functions:
            self.functions['reset_move_down']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_down'")

    def reset_move_left_command(self):
        """
        Function for the reset move left button command.
        """
        if 'reset_move_left' in self.functions:
            self.functions['reset_move_left']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_left'")

    def reset_move_right_command(self):
        """
        Function for the reset move right button command.
        """
        if 'reset_move_right' in self.functions:
            self.functions['reset_move_right']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_move_right'")

    def reset_start_game_command(self):
        """
        Function for the reset start button command.
        """
        if 'reset_start_game' in self.functions:
            self.functions['reset_start_game']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_start_game'")

    def reset_pause_game_command(self):
        """
        Function for the reset pause button command.
        """
        if 'reset_pause' in self.functions:
            self.functions['reset_pause']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_pause'")

    def reset_restart_game_command(self):
        """
        Function for the reset restart button command.
        """
        if 'reset_restart' in self.functions:
            self.functions['reset_restart']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_restart'")

    def reset_all_settings_command(self):
        """
        Function for the reset all settings button command.
        """
        if 'reset_all_settings' in self.functions:
            self.functions['reset_all_settings']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_all_settings'")

    def reset_all_movements_command(self):
        """
        Function for the reset all movements button command.
        """
        if 'reset_all_movements' in self.functions:
            self.functions['reset_all_movements']()
        else:
            self.game_logger.log_game_event("No function assigned to 'reset_all_movements'")

    def create_buttons(self, command, x, y):
        """
        Create all buttons.
        """
        reset_buttons = ctk.CTkButton(self.settings_canvas_reset,
                                    width=self.button_width,
                                    height=self.button_height,
                                    corner_radius=self.corner_radius,
                                    text=self.text,
                                    font=FONT_LIST[11],
                                    command=command
                                    )
        reset_buttons.place(in_=self.settings_canvas_reset, x=x, y=y)
        return reset_buttons
    
    def info_general_reset_mini_snake(self):
        """
        Function for creating the info general reset mini snake button.
        """
        button = self.create_buttons(self.info_general_reset_mini_snake_command, 800, 350)
        self.buttons.append(button)

    def reset_screen_size_button(self):
        """
        Function for creating the reset screen size button.
        """
        button = self.create_buttons(self.reset_screen_size_command, 200, 50)
        self.buttons.append(button)

    def reset_theme_button(self):
        """
        Function for creating the reset theme button.
        """
        button = self.create_buttons(self.reset_theme_command, 400, 50)
        self.buttons.append(button)

    def reset_contrast_button(self):
        """
        Function for creating the reset contrast button.
        """
        button = self.create_buttons(self.reset_contrast_command, 600, 50)
        self.buttons.append(button)

    def reset_high_score_label_showing_button(self):
        """
        Function for creating the high score label showing button.
        """
        button = self.create_buttons(self.reset_high_score_label_showing_command, 600, 200)
        self.buttons.append(button)

    def reset_snake_speed_button(self):
        """
        Function for creating the reset snake speed button.
        """
        button = self.create_buttons(self.reset_snake_speed_command, 200, 200)
        self.buttons.append(button)

    def reset_game_size_button(self):
        """
        Function for creating the reset game size button.
        """
        button = self.create_buttons(self.reset_game_size_command, 400, 200)
        self.buttons.append(button)

    def reset_snake_color_button(self):
        """
        Function for creating the reset snake color button.
        """
        button = self.create_buttons(self.reset_snake_color_command, 800, 50)
        self.buttons.append(button)

    def reset_move_up_button(self):
        """
        Function for creating the reset move up button.
        """
        button = self.create_buttons(self.reset_move_up_command, 200, 350)
        self.buttons.append(button)

    def reset_move_down_button(self):
        """
        Function for creating the reset move down button.
        """
        button = self.create_buttons(self.reset_move_down_command, 600, 350)
        self.buttons.append(button)

    def reset_move_left_button(self):
        """
        Function for creating the reset move left button.
        """
        button = self.create_buttons(self.reset_move_left_command, 400, 350)
        self.buttons.append(button)

    def reset_move_right_button(self):
        """
        Function for creating the reset move right button.
        """
        button = self.create_buttons(self.reset_move_right_command, 800, 350)
        self.buttons.append(button)

    def reset_start_game_button(self):
        """
        Function for creating the reset start game button.
        """
        button = self.create_buttons(self.reset_start_game_command, 200, 500)
        self.buttons.append(button)

    def reset_pause_game_button(self):
        """
        Function for creating the reset pause game button.
        """
        button = self.create_buttons(self.reset_pause_game_command, 400, 500)
        self.buttons.append(button)

    def reset_restart_game_button(self):
        """
        Function for creating the reset restart game button.
        """
        button = self.create_buttons(self.reset_restart_game_command, 600, 500)
        self.buttons.append(button)

    def reset_all_settings_button(self):
        """
        Function for creating the reset all settings button.
        """
        button = self.create_buttons(self.reset_all_settings_command, 800, 200)
        self.buttons.append(button)

    def reset_all_movements_button(self):
        """
        Function for creating the reset all movements button.
        """
        button = self.create_buttons(self.reset_all_movements_command, 800, 500)
        self.buttons.append(button)

    def destroy_buttons(self):
        """
        Destroy all buttons.
        """
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()
