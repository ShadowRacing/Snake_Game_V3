"""
This module is responsible for creating the button panel of the Shadows Snake game. # pylint: disable=line-too-long
"""

# Importing necessary modules
import time
import configparser
import traceback
from os import path
from PIL import Image
import customtkinter as ctk

# Importing necessary modules from other folders
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST
from Logic.button_commands_snake_game import ButtonCommands


# Class for creating the button panel
class ClickButtonPanel:
    """
    Class for creating the button panel of the Shadows Snake game.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClickButtonPanel, cls).__new__(cls)
        return cls._instance

    def __init__(self, parent, game_logger, functions, home_button=None):
        # Check if we've already initialized the instance
        if getattr(self, '_initialized', False):
            return
        # Initializing variables
        self.parent = parent
        self.game_logger = game_logger
        self.functions = functions
        self.home_button = home_button
        self.theme_updater = ThemeUpdater(self.game_logger)

        # Managing the buttons height and width
        self.button_width = GameConstants.CLICK_BUTTON_WIDTH
        self.button_height = GameConstants.CLICK_BUTTON_HEIGHT
        self.corner_radius = GameConstants.CLICK_BUTTON_CORNER_RADIUS

        self.button_commands = ButtonCommands(self.game_logger, self.functions)

        # Creating a separate canvas for the buttons
        self.button_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        self.button_canvas.pack(side='left', fill='both')

        # Creating counter for home button clicks
        self.home_button_clicks = 0
        self.first_click_time = 0

        self.config = configparser.ConfigParser()
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.state_game = None
        self.home_button_state = 'normal'
        self.classic_reset_high_score_button_state = 'normal'
        self.classic_reset_high_score_time_button_state = 'normal'
        self.classic_reset_high_score_snake_length_button_state = 'normal'

        self.endless_reset_high_score_button_state = None
        self.endless_reset_high_score_time_button_state = None
        self.endless_reset_high_score_snake_length_button_state = None
        self.endless_reset_high_score_special_button_state = None
        self.endless_reset_high_score_shorten_button_state = None

        self.leveling_reset_high_score_button_state = None
        self.leveling_reset_high_score_time_button_state = None
        self.leveling_reset_high_score_snake_length_button_state = None
        self.leveling_reset_high_score_special_button_state = None
        self.leveling_reset_high_score_shorten_button_state = None
        self.leveling_reset_high_score_xp_button_state = None
        self.leveling_reset_high_score_level_button_state = None

        self.challange_reset_high_score_button_state = None
        self.challange_reset_high_score_time_button_state = None
        self.challange_reset_high_score_snake_length_button_state = None
        self._initialized = True

        self.game_mode = None
        self.classic_state_game = None
        self.endless_state_game = None
        self.leveling_state_game = None
        self.challange_state_game = None

        self.classic_reset_high_score_button = None
        self.classic_reset_high_score_time_button = None
        self.classic_reset_high_score_snake_length_button = None

        self.endless_reset_high_score_button = None
        self.endless_reset_high_score_time_button = None
        self.endless_reset_high_score_snake_length_button = None
        self.endless_reset_high_score_special_score_button = None
        self.endless_reset_high_score_shorten_score_button = None

        self.leveling_reset_high_score_button = None
        self.leveling_reset_high_score_time_button = None
        self.leveling_reset_high_score_snake_length_button = None
        self.leveling_reset_high_score_special_score_button = None
        self.leveling_reset_high_score_shorten_score_button = None
        self.leveling_reset_high_score_xp_button = None
        self.leveling_reset_high_score_level_button = None

        self.challange_high_score_button_state = None
        self.challange_high_score_time_button_state = None
        self.challange_high_score_snake_length_button_state = None

        self.settings = 'Settings'
        self.game_mode_value  = 'game_mode'
        self.classic_snake_settings = 'Classic_Snake_Settings'
        self.endless_snake_settings = 'Endless_Snake_Settings'
        self.leveling_snake_settings = 'Leveling_Snake_Settings'
        self.challange_snake_settings = 'Challange_Snake_Settings'
        self.state = 'state'
        self.playing = 'playing'

        # Read the config file and load it
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config_path_icon = path.join(self.config_dir, '..', 'app_icon.ico')

        self.create_and_place_image_label(self.button_canvas, 5, 635, self.config_path_icon)

    def create_and_place_image_label(self, canvas, x, y, image_path):
        """
        Create and place a CTkImage and CTkLabel on the specified canvas.
        """
        my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                dark_image=Image.open(image_path),
                                size=(160, 160))

        image_label = ctk.CTkLabel(canvas, image=my_image, text="")
        image_label.place(x=x, y=y)

    def switch_canvas(self):
        """
        Function for switching the canvas.
        """
        # Set _initialized to False
        self._initialized = False

    def write_changes_to_configini(self):
        """
        Write the changes to the config.ini file.
        """
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def destroy_canvas(self):
        """
        Function for destroying the button canvas.
        """
        self.button_canvas.destroy()

    # Methods to create specific buttons
    # Each method calls the create_click_button method with specific parameters
    def create_home_button(self):
        """
        Function for creating the home button.
        """
        self.home_button_state = self.config.get('Settings', 'home_button_state')

        self.home_button = ctk.CTkButton(self.button_canvas, text="Main Menu", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, corner_radius=self.corner_radius ,state=self.home_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.home_command)
        self.home_button.grid(in_=self.button_canvas, row=0, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def set_config_value(self, section, key, value):
        """
        Function for setting the value in the config.ini file.
        """
        self.config.set(section, key, value)
        self.write_changes_to_configini()

    def update_button_state(self):
        """
        Function for updating the button states.
        """
        # Read the new state from the config.ini file
        time.sleep(0.1)
        self.config.read(self.config_path)
        self.game_mode = self.config.get('Settings', 'game_mode')
        self.classic_state_game = self.config.get('Classic_Snake_Settings', 'state', fallback='playing') # pylint: disable=line-too-long
        self.endless_state_game = self.config.get('Endless_Snake_Settings', 'state', fallback='playing') # pylint: disable=line-too-long
        self.leveling_state_game = self.config.get('Leveling_Snake_Settings', 'state', fallback='playing') # pylint: disable=line-too-long
        self.challange_state_game = self.config.get('Challange_Snake_Settings', 'state', fallback='playing') # pylint: disable=line-too-long

        if self.game_mode  == 'classic_snake':
            if self.classic_state_game == 'playing':
                self.home_button_state = 'disabled'
                self.classic_reset_high_score_button_state = 'disabled'
                self.classic_reset_high_score_time_button_state = 'disabled'
                self.classic_reset_high_score_snake_length_button_state = 'disabled'
            elif self.classic_state_game == 'paused':
                self.classic_reset_high_score_button_state = 'normal'
                self.classic_reset_high_score_time_button_state = 'normal'
                self.classic_reset_high_score_snake_length_button_state = 'normal'
            else:
                # Handle unexpected state or fallback to a default
                self.home_button_state = 'normal'
                self.classic_reset_high_score_button_state = 'normal'
                self.classic_reset_high_score_time_button_state = 'normal'
                self.classic_reset_high_score_snake_length_button_state = 'normal'

            self.set_config_value(self.settings, 'home_button_state', self.home_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'classic_reset_high_score_button_state', self.classic_reset_high_score_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'classic_reset_high_score_time_button_state', self.classic_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'classic_reset_high_score_snake_length_button_state', self.classic_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long

            # Update the state of the home button
            self.home_button.configure(state=self.home_button_state)
            self.classic_reset_high_score_button.configure(state=self.classic_reset_high_score_button_state) # pylint: disable=line-too-long
            self.classic_reset_high_score_time_button.configure(state=self.classic_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.classic_reset_high_score_snake_length_button.configure(state=self.classic_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long


        if self.game_mode == 'endless_snake':
            if self.endless_state_game == 'playing':
                self.home_button_state = 'disabled'
                self.endless_reset_high_score_button_state = 'disabled'
                self.endless_reset_high_score_time_button_state = 'disabled'
                self.endless_reset_high_score_snake_length_button_state = 'disabled'
                self.endless_reset_high_score_special_button_state = 'disabled'
                self.endless_reset_high_score_shorten_button_state = 'disabled'
            elif self.endless_state_game == 'paused':
                self.endless_reset_high_score_button_state = 'normal'
                self.endless_reset_high_score_time_button_state = 'normal'
                self.endless_reset_high_score_snake_length_button_state = 'normal'
                self.endless_reset_high_score_special_button_state = 'normal'
                self.endless_reset_high_score_shorten_button_state = 'normal'
            else:
                # Handle unexpected state or fallback to a default
                self.home_button_state = 'normal'
                self.endless_reset_high_score_button_state = 'normal'
                self.endless_reset_high_score_time_button_state = 'normal'
                self.endless_reset_high_score_snake_length_button_state = 'normal'
                self.endless_reset_high_score_special_button_state = 'normal'
                self.endless_reset_high_score_shorten_button_state = 'normal'


            self.set_config_value(self.settings, 'home_button_state', self.home_button_state)
            self.set_config_value(self.settings, 'endless_reset_high_score_button_state', self.endless_reset_high_score_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'endless_reset_high_score_time_button_state', self.endless_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'endless_reset_high_score_snake_length_button_state', self.endless_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'endless_reset_high_score_special_score_button_state', self.endless_reset_high_score_special_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'endless_reset_high_score_shorten_score_button_state', self.endless_reset_high_score_shorten_button_state) # pylint: disable=line-too-long

            # Update the state of the home button
            self.home_button.configure(state=self.home_button_state)
            self.endless_reset_high_score_button.configure(state=self.endless_reset_high_score_button_state) # pylint: disable=line-too-long
            self.endless_reset_high_score_time_button.configure(state=self.endless_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.endless_reset_high_score_snake_length_button.configure(state=self.endless_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long
            self.endless_reset_high_score_special_score_button.configure(state=self.endless_reset_high_score_special_button_state) # pylint: disable=line-too-long
            self.endless_reset_high_score_shorten_score_button.configure(state=self.endless_reset_high_score_shorten_button_state) # pylint: disable=line-too-long

        if self.game_mode == 'leveling_snake':
            if self.leveling_state_game == 'playing':
                self.home_button_state = 'disabled'
                self.leveling_reset_high_score_button_state = 'disabled'
                self.leveling_reset_high_score_time_button_state = 'disabled'
                self.leveling_reset_high_score_snake_length_button_state = 'disabled'
                self.leveling_reset_high_score_special_button_state = 'disabled'
                self.leveling_reset_high_score_shorten_button_state = 'disabled'
                self.leveling_reset_high_score_xp_button_state = 'disabled'
                self.leveling_reset_high_score_level_button_state = 'disabled'
            elif self.leveling_state_game == 'paused':
                self.leveling_reset_high_score_button_state = 'normal'
                self.leveling_reset_high_score_time_button_state = 'normal'
                self.leveling_reset_high_score_snake_length_button_state = 'normal'
                self.leveling_reset_high_score_special_button_state = 'normal'
                self.leveling_reset_high_score_shorten_button_state = 'normal'
                self.leveling_reset_high_score_xp_button_state = 'normal'
                self.leveling_reset_high_score_level_button_state = 'normal'
            else:
                # Handle unexpected state or fallback to a default
                self.home_button_state = 'normal'
                self.leveling_reset_high_score_button_state = 'normal'
                self.leveling_reset_high_score_time_button_state = 'normal'
                self.leveling_reset_high_score_snake_length_button_state = 'normal'
                self.leveling_reset_high_score_special_button_state = 'normal'
                self.leveling_reset_high_score_shorten_button_state = 'normal'
                self.leveling_reset_high_score_xp_button_state = 'normal'
                self.leveling_reset_high_score_level_button_state = 'normal'

            self.set_config_value(self.settings, 'home_button_state', self.home_button_state)
            self.set_config_value(self.settings, 'leveling_reset_high_score_button_state', self.leveling_reset_high_score_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_time_button_state', self.leveling_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_snake_length_button_state', self.leveling_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_special_button_state', self.leveling_reset_high_score_special_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_shorten_button_state', self.leveling_reset_high_score_shorten_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_xp_button_state', self.leveling_reset_high_score_xp_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'leveling_reset_high_score_level_button_state', self.leveling_reset_high_score_level_button_state) # pylint: disable=line-too-long

            # Update the state of the home button
            self.home_button.configure(state=self.home_button_state)
            self.leveling_reset_high_score_button.configure(state=self.leveling_reset_high_score_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_time_button.configure(state=self.leveling_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_snake_length_button.configure(state=self.leveling_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_special_score_button.configure(state=self.leveling_reset_high_score_special_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_shorten_score_button.configure(state=self.leveling_reset_high_score_shorten_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_xp_button.configure(state=self.leveling_reset_high_score_xp_button_state) # pylint: disable=line-too-long
            self.leveling_reset_high_score_level_button.configure(state=self.leveling_reset_high_score_level_button_state) # pylint: disable=line-too-long

        if self.game_mode == 'challange_snake':
            if self.challange_state_game == 'playing':
                self.home_button_state = 'disabled'
                self.challange_reset_high_score_button_state = 'disabled'
                self.challange_reset_high_score_time_button_state = 'disabled'
                self.challange_reset_high_score_snake_length_button_state = 'disabled'
            elif self.challange_state_game == 'paused':
                self.challange_reset_high_score_button_state = 'normal'
                self.challange_reset_high_score_time_button_state = 'normal'
                self.challange_reset_high_score_snake_length_button_state = 'normal'
            else:
                # Handle unexpected state or fallback to a default
                self.home_button_state = 'normal'
                self.challange_reset_high_score_button_state = 'normal'
                self.challange_reset_high_score_time_button_state = 'normal'
                self.challange_reset_high_score_snake_length_button_state = 'normal'

            self.set_config_value(self.settings, 'home_button_state', self.home_button_state)
            self.set_config_value(self.settings, 'challange_reset_high_score_button_state', self.challange_reset_high_score_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'challange_reset_high_score_time_button_state', self.challange_reset_high_score_time_button_state) # pylint: disable=line-too-long
            self.set_config_value(self.settings, 'challange_reset_high_score_snake_length_button_state', self.challange_reset_high_score_snake_length_button_state) # pylint: disable=line-too-long


    def create_restart_app_button(self):
        """
        Function for creating the restart app button.
        """
        restart_app_button = ctk.CTkButton(self.button_canvas, text="Restart App", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, corner_radius=self.corner_radius, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.restart_app_command)
        restart_app_button.grid(in_=self.button_canvas, row=99, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_quit_button(self):
        """
        Function for creating the quit button.
        """
        quit_button = ctk.CTkButton(self.button_canvas, text="Quit", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.quit_command)
        quit_button.grid(in_=self.button_canvas, row=100, column=0, padx=10, pady=10, sticky="w")

    def create_settings_button(self):
        """
        Function for creating the settings button.
        """
        settings_button = ctk.CTkButton(self.button_canvas, text="Settings", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_command)
        settings_button.grid(in_=self.button_canvas, row=9, column=0, padx=10, pady=10, sticky="w")

    def create_settings_values_button(self):
        """
        Function for creating the settings values button.
        """
        settings_values_button = ctk.CTkButton(self.button_canvas, text="Values\nSettings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_values_command)
        settings_values_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_info_home_button(self):
        """
        Function for creating the home button.
        """
        info_home_button = ctk.CTkButton(self.button_canvas, text="Home info", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_home_command)
        info_home_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def create_info_button(self):
        """
        Function for creating the information button.
        """
        info_button = ctk.CTkButton(self.button_canvas, text="Information", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_command)
        info_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w")

    def create_info_general_button(self):
        """
        Function for creating the general info button.
        """
        info_general_button = ctk.CTkButton(self.button_canvas, text="General", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_general_command)
        info_general_button.grid(in_=self.button_canvas, row=16, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_info_classic_game_mode_button(self):
        """
        Function for creating the classic game mode info button.
        """
        info_classic_game_mode_button = ctk.CTkButton(self.button_canvas, text="Classic", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_classic_game_mode_command)
        info_classic_game_mode_button.grid(in_=self.button_canvas, row=17, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_info_endless_game_mode_button(self):
        """
        Function for creating the endless game mode info button.
        """
        info_endless_game_mode_button = ctk.CTkButton(self.button_canvas, text="Endless", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_endless_game_mode_command)
        info_endless_game_mode_button.grid(in_=self.button_canvas, row=18, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_info_leveling_game_mode_button(self):
        """
        Function for creating the leveling game mode info button.
        """
        info_leveling_game_mode_button = ctk.CTkButton(self.button_canvas, text="Leveling", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_leveling_game_mode_command)
        info_leveling_game_mode_button.grid(in_=self.button_canvas, row=19, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_info_challange_game_mode_button(self):
        """
        Function for creating the challange game mode info button.
        """
        info_challange_game_mode_button = ctk.CTkButton(self.button_canvas, text="Challange", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_challange_game_mode_command)
        info_challange_game_mode_button.grid(in_=self.button_canvas, row=20, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_patchnotes_button(self):
        """
        Function for creating the patchnotes button.
        """
        patchnotes_button = ctk.CTkButton(self.button_canvas, text="Patchnotes", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", #Should ne normal # pylint: disable=line-too-long
                                command=self.button_commands.patchnotes_command)
        patchnotes_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_reset_settings_button(self):
        """
        Function for creating the reset settings button.
        """
        reset_settings_button = ctk.CTkButton(self.button_canvas, text="Reset\nSettings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.reset_settings_command)
        reset_settings_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_classic_snake_button(self):
        """
        Function for creating the classic snake button.
        """
        classic_snake_button = ctk.CTkButton(self.button_canvas, text="Classic", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.classic_snake_command)
        classic_snake_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_snake_endless_button(self):
        """
        Function for creating the endless snake button.
        """
        snake_endless_button = ctk.CTkButton(self.button_canvas, text="Endless", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_endless_command)
        snake_endless_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_snake_leveling_button(self):
        """
        Function for creating the leveling snake button.
        """
        snake_leveling_button = ctk.CTkButton(self.button_canvas, text="Leveling", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",  #Should ne normal # pylint: disable=line-too-long
                                command=self.button_commands.snake_leveling_command)
        snake_leveling_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_challange_choice_button(self):
        """
        Function for creating the challange choices button.
        """
        challange_choice_button = ctk.CTkButton(self.button_canvas, text="Challanges", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.challange_choices_command)
        challange_choice_button.grid(in_=self.button_canvas, row=4, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_challange_settings_button(self):
        """
        Function for creating the challange settings button.
        """
        challange_settings_button = ctk.CTkButton(self.button_canvas, text="Challange Settings", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.challange_settings_command)
        challange_settings_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_food_time_attack_button(self):
        """
        Function for creating the Food Time Attack button.
        """
        food_time_attack_button = ctk.CTkButton(self.button_canvas, text="Challange", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.food_time_attack_command)
        food_time_attack_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_snake_color_button(self):
        """
        Function for creating the snake color button.
        """
        snake_color_button = ctk.CTkButton(self.button_canvas, text="Snake Color", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_color_command)
        snake_color_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_snake_outline_button(self):
        """
        Function for creating the snake outline button.
        """
        snake_outline_button = ctk.CTkButton(self.button_canvas, text="Snake Outline", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_outline_command)
        snake_outline_button.grid(in_=self.button_canvas, row=7, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_classic_snake_length_button(self):
        """
        Function for creating the snake length button.
        """
        classic_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal", # pylint: disable=line-too-long
                                command=self.button_commands.snake_length_command)
        classic_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_classic_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """

        self.classic_reset_high_score_button_state = self.config.get('Settings', 'classic_reset_high_score_button_state') # pylint: disable=line-too-long

        self.classic_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.classic_reset_high_score_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_command) # pylint: disable=line-too-long
        self.classic_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_classic_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """

        self.classic_reset_high_score_time_button_state = self.config.get('Settings', 'classic_reset_high_score_time_button_state') # pylint: disable=line-too-long

        self.classic_reset_high_score_time_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.classic_reset_high_score_time_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_time_command) # pylint: disable=line-too-long
        self.classic_reset_high_score_time_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_classic_reset_high_score_snake_length(self):
        """
        Function for creating the reset high score snake length button.
        """

        self.classic_reset_high_score_snake_length_button_state = self.config.get('Settings', 'classic_reset_high_score_snake_length_button_state') # pylint: disable=line-too-long

        self.classic_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.classic_reset_high_score_snake_length_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.classic_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        self.classic_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_snake_length_button(self):
        """
        Function for creating the snake length button.
        """
        endless_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state='normal', # pylint: disable=line-too-long
                                command=self.button_commands.snake_length_command) # pylint: disable=line-too-long
        endless_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """
        self.endless_reset_high_score_button_state = self.config.get('Settings', 'endless_reset_high_score_button_state') # pylint: disable=line-too-long

        self.endless_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.endless_reset_high_score_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_command) # pylint: disable=line-too-long
        self.endless_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """
        self.endless_reset_high_score_time_button_state = self.config.get('Settings', 'endless_reset_high_score_time_button_state') # pylint: disable=line-too-long

        self.endless_reset_high_score_time_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.endless_reset_high_score_time_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_time_command) # pylint: disable=line-too-long
        self.endless_reset_high_score_time_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_reset_high_score_snake_length(self):
        """
        Function for creating the reset high score snake length button.
        """
        self.endless_reset_high_score_snake_length_button_state = self.config.get('Settings', 'endless_reset_high_score_snake_length_button_state') # pylint: disable=line-too-long

        self.endless_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.endless_reset_high_score_snake_length_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        self.endless_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_reset_high_score_special_score_button(self):
        """
        Function for creating the reset high score special score button.
        """
        self.endless_reset_high_score_special_button_state = self.config.get('Settings', 'endless_reset_high_score_special_button_state') # pylint: disable=line-too-long
        self.endless_reset_high_score_special_score_button = ctk.CTkButton(self.button_canvas, text="Reset Special\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.endless_reset_high_score_special_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_special_score_command) # pylint: disable=line-too-long
        self.endless_reset_high_score_special_score_button.grid(in_=self.button_canvas, row=13, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_endless_reset_high_score_shorten_snake_button(self):
        """
        Function for creating the reset high score shorten snake button.
        """
        self.endless_reset_high_score_shorten_button_state = self.config.get('Settings', 'endless_reset_high_score_shorten_button_state') # pylint: disable=line-too-long

        self.endless_reset_high_score_shorten_score_button = ctk.CTkButton(self.button_canvas, text="Reset Shorten\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.endless_reset_high_score_shorten_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.endless_reset_high_score_shorten_snake_command) # pylint: disable=line-too-long
        self.endless_reset_high_score_shorten_score_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_button(self):
        """
        Function for creating the reset high score button.
        """
        self.leveling_reset_high_score_button_state = self.config.get('Settings', 'leveling_reset_high_score_button_state') # pylint: disable=line-too-long

        self.leveling_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_command)
        self.leveling_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_time_button(self):
        """
        Function for creating the reset high score time button.
        """
        self.leveling_reset_high_score_time_button_state = self.config.get('Settings', 'leveling_reset_high_score_time_button_state') # pylint: disable=line-too-long
        self.leveling_reset_high_score_time_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_time_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_time_command)
        self.leveling_reset_high_score_time_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_snake_length_button(self):
        """
        Function for creating the reset high score snake length button.
        """
        self.leveling_reset_high_score_snake_length_button_state = self.config.get('Settings', 'leveling_reset_high_score_special_button_state') # pylint: disable=line-too-long

        self.leveling_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_snake_length_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_snake_length_command) # pylint: disable=line-too-long
        self.leveling_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_special_score_button(self):
        """
        Function for creating the reset high score special score button.
        """
        self.leveling_reset_high_score_special_button_state = self.config.get('Settings', 'leveling_reset_high_score_special_button_state') # pylint: disable=line-too-long

        self.leveling_reset_high_score_special_score_button = ctk.CTkButton(self.button_canvas, text="Reset Special\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_special_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_special_score_command) # pylint: disable=line-too-long
        self.leveling_reset_high_score_special_score_button.grid(in_=self.button_canvas, row=13, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_shorten_snake_button(self):
        """
        Function for creating the reset high score shorten snake button.
        """
        self.leveling_reset_high_score_shorten_button_state = self.config.get('Settings', 'leveling_reset_high_score_shorten_button_state') # pylint: disable=line-too-long

        self.leveling_reset_high_score_shorten_score_button = ctk.CTkButton(self.button_canvas, text="Reset Shorten\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_shorten_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_shorten_snake_command) # pylint: disable=line-too-long
        self.leveling_reset_high_score_shorten_score_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_scores_xp_button(self):
        """
        Function for creating the reset high scores xp button.
        """
        self.leveling_reset_high_score_xp_button_state = self.config.get('Settings', 'leveling_reset_high_score_xp_button_state') # pylint: disable=line-too-long
        self.leveling_reset_high_score_xp_button = ctk.CTkButton(self.button_canvas, text="Reset XP\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_xp_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_scores_xp_command)
        self.leveling_reset_high_score_xp_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    def create_leveling_reset_high_score_level_button(self):
        """
        Function for creating the reset high score level button.
        """
        self.leveling_reset_high_score_level_button_state = self.config.get('Settings', 'leveling_reset_high_score_level_button_state') # pylint: disable=line-too-long

        self.leveling_reset_high_score_level_button = ctk.CTkButton(self.button_canvas, text="Reset Level\n Highscore", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state=self.leveling_reset_high_score_level_button_state, # pylint: disable=line-too-long
                                command=self.button_commands.leveling_reset_high_score_level_command) # pylint: disable=line-too-long
        self.leveling_reset_high_score_level_button.grid(in_=self.button_canvas, row=16, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    # only in the special game mode
    def create_game_size_button(self):
        """
        Function for creating the game size button.
        """
        game_size_button = ctk.CTkButton(self.button_canvas, text="Game Size", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.game_size_command)
        game_size_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long

    # only in the special game mode
    def create_snake_speed_button(self):
        """
        Function for creating the snake speed button.
        """
        snake_speed_button = ctk.CTkButton(self.button_canvas, text="Snake Speed", font=FONT_LIST[11], # pylint: disable=line-too-long
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_speed_command)
        snake_speed_button.grid(in_=self.button_canvas, row=9, column=0, padx=10, pady=10, sticky="w") # pylint: disable=line-too-long
