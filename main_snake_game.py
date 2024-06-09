"""
The main file for the Shadows Snake game.
"""

# Import all the necessary libraries
import traceback
import time
import configparser
import json
#from tkinter import TclError
from os import path
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Logs.gamelogger_snake_game import GameLogger , ErrorgameLogger
from Configuration.constants_snake_game import GameConstants, SCREEN_SIZE_FULLSCREEN, FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.buttonpanel_snake_game import ClickButtonPanel, ButtonCommands # pylint: disable=line-too-long
from Logic.buttonpanelreset_snake_game import ResetSettingsPanel
from Logic.optionmenubuttonpanel import OptionButtonPanel
from Logic.labelpanel_snake_game import NameOffFrameLabelPanel, SettingsOptionButtonLabels # pylint: disable=line-too-long
from Logic.game_labelpanel import GameLabelsPanel
from Logic.config_ini_initials import ConfigIni
from Logic.snake_challange_choice import ChallangeChoices
from Logic.snake_challange_settings import ChallangeSettings
from Logic.resetconfigvalues import ResetConfigValues
from Logic.little_snake_game import MiniSnakeGame
from Games.snake_classic_game import SnakeClassicGame
from Games.snake_endless_game import SnakeEndless
from Games.snake_leveling_game import SnakeLeveling
from Games.snake_challange_games import FoodTimeAttack
from Themes.theme_updater_snake_game import ThemeUpdater
from Themes.contrast_updater_snake_game import UpdateContrast


# Define the main application class
class SnakeGameApp:
    """
    The main class for the Shadows Snake game.
    """
    def __init__ (self, root, game_width, game_height): # pylint: disable=redefined-outer-name
        #Initialize the game app values
        self.config_ini = ConfigIni()
        self.config_ini.set_config()
        time.sleep(1)
        self.root = root
        self.game_logger = GameLogger(root)
        self.error_game_logger = ErrorgameLogger()
        self.game_logger.log_game_event("Started the GameApp Class")
        self.game_config = GameConfig(game_logger=self.game_logger, game_mode = "initial_config")
        self.update_contrast = UpdateContrast(self.game_logger)
        self.theme_updater = ThemeUpdater(self.game_logger)
        self.game_width = game_width
        self.game_height = game_height
        self.snake_color = None
        self.theme_updater.set_initial_theme()

        # Read the config file and load it
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.apply_theme()
        self.update_contrast.apply_contrast(selected_value=None)

        # Write the changes to the config file
        try:
            with open(self.config_path, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Button press variables
        self.button_press_variable = 0
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0
        self.button_press_time_limit = float(self.config.get('Settings', 'button_press_time_limit', fallback=0.5)) # pylint: disable=line-too-long


        self.text_name = "Shadow's Snake Game"
        self.text_version = "Version: 0.2.8"
        self.text_developer = "Developer: Shadow"
        self.font_50 = ("Helvetica", 50)
        self.font_30 = ("Helvetica", 30)
        self.font_20 = ("Helvetica", 20)

        self.snake = [(0, 0)]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
        self.current_direction_index = 0
        # self.food = self.spawn_food()
        self.cell_size = 20  # Set the size of a cell in the game board
        self.running = True
        self.mini_snake_game_canvas = ctk.CTkCanvas(self.root, width=60, height=60)  # Create a canvas for the game board
        


        # Creating the main canvas for the app
        self.main_canvas = ctk.CTkCanvas(root, highlightbackground='Black', highlightthickness=5, bg='Grey20') # pylint: disable=line-too-long
        self.main_canvas.pack(expand=True, fill="both")
        self.original_main_canvas = self.main_canvas

        # All the game canvases
        self.classic_snake_canvas = None
        self.endless_snake_canvas = None
        self.leveling_snake_canvas = None
        self.food_time_attack_canvas = None
        self.challange_choice_canvas = None
        self.challange_settings_canvas = None
        self.info_canvas = None
        self.info_general_canvas = None
        self.info_classic_canvas = None
        self.info_endless_canvas = None
        self.info_leveling_canvas = None
        self.info_challange_canvas = None
        self.settings_canvas = None
        self.settings_canvas_values = None
        self.settings_canvas_reset = None
        self.reset_label = None
        self.reset_settings_frame = None
        self.reset_settings_frame_1 = None

        self.patchnotes_displayed = False
        self.info_general_displayed = False
        self.info_classic_displayed = False
        self.info_endless_displayed = False
        self.info_leveling_displayed = False
        self.info_challange_displayed = False
        self.reset_settings_displayed = False
        self.scrollable_frame = self.scrollable_frame = ctk.CTkScrollableFrame(self.info_canvas, width=850, height=600, fg_color='Grey10') # pylint: disable=line-too-long
        self.patchnotes_label = None
        self.info_general_label = None
        self.info_classic_label = None
        self.info_endless_label = None
        self.info_leveling_label = None
        self.info_challange_label = None

        #create the functions dictionary
        self.functions = {
            'return_home': self.return_home,
            'confirm_quit': self.confirm_quit,
            'destroy_canvas': self.destroy_canvas,
            'classic_reset_button_press_variable': self.classic_reset_button_press_variable,
            'classic_reset_high_score_snake_length': self.classic_reset_snake_length,
            'classic_reset_high_score_time': self.classic_reset_high_score_time,
            'classic_reset_high_score': self.classic_reset_high_score,
            'endless_reset_high_score': self.endless_reset_high_score,
            'endless_reset_high_score_time': self.endless_reset_high_score_time,
            'endless_reset_high_score_snake_length': self.endless_reset_high_score_snake_length,
            'endless_reset_high_score_special_score': self.endless_reset_high_score_special_score,
            'endless_reset_high_score_shorten_snake' : self.endless_reset_high_score_shorten_snake,
            'leveling_reset_high_score': self.leveling_reset_high_score,
            'leveling_reset_high_score_time': self.leveling_reset_high_score_time,
            'leveling_reset_high_score_snake_length': self.leveling_reset_high_score_snake_length,
            'leveling_reset_high_score_special_score': self.leveling_reset_high_score_special_score,
            'leveling_reset_high_score_shorten_snake': self.leveling_reset_high_score_shorten_snake,
            'leveling_reset_high_scores_xp': self.leveling_reset_high_scores_xp,
            'leveling_reset_high_score_level': self.leveling_reset_high_score_level,
            'open_settings': self.open_settings,
            'settings_values': self.settings_values,
            'reset_settings': self.reset_settings,
            'open_info': self.open_info,
            'snake_leveling': self.snake_leveling,
            'snake_endless': self.snake_endless,
            'classic_snake': self.classic_snake,
            'food_time_attack': self.food_time_attack,
            'challange_choices': self.challange_choices,
            'challange_settings': self.challange_settings,
            'patchnotes': self.patchnotes,
            'reset_screen_size': self.reset_screen_size,
            'reset_theme': self.reset_theme,
            'reset_contrast': self.reset_contrast,
            'reset_high_score_label_showing': self.reset_high_score_showing,
            'reset_snake_speed': self.reset_snake_speed,
            'reset_game_size': self.reset_game_size,
            'reset_snake_color': self.reset_snake_color,
            'reset_move_up': self.reset_move_up,
            'reset_move_down': self.reset_move_down,
            'reset_move_left': self.reset_move_left,
            'reset_move_right': self.reset_move_right,
            'reset_pause': self.reset_pause,
            'reset_start_game': self.reset_start_game,
            'reset_restart': self.reset_restart,
            'reset_all_settings': self.reset_all_settings,
            'reset_all_movements': self.reset_all_movements,
            'return_info_home': self.info_home,
            'info_general': self.info_general,
            'info_general_reset_mini_snake': self.info_general_reset_mini_snake,
            'info_classic_game_mode': self.info_classic,
            'info_endless_game_mode': self.info_endless,
            'info_leveling_game_mode': self.info_leveling,
            'info_challange_game_mode': self.info_challange,
        }

        self.create_option_button_panel = None
        self.first_button_press_time = None

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long

        self.create_reset_button_panel = ResetSettingsPanel(self.challange_settings_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long

        # And then create the ButtonCommands instance
        self.button_commands = ButtonCommands(self.game_logger, self.functions)

        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.game_logger,
                                                        self.game_config, self.open_info,
                                                        self.open_settings)

        self.game_labels_panel = GameLabelsPanel(self.main_canvas,self.game_logger,  self.game_config) # pylint: disable=line-too-long

        self.settings_labels = SettingsOptionButtonLabels(self.game_logger, self.main_canvas)

        self.reset_config_values = ResetConfigValues(self.game_logger, self.classic_snake_canvas, self.endless_snake_canvas, self.leveling_snake_canvas) # pylint: disable=line-too-long

        self.mini_snake_game = MiniSnakeGame(self.main_canvas, 20, self.game_logger) # pylint: disable=line-too-long

        self.settings_labels.update_initial_game_size()

        # Create the home screen
        self.create_home_screen()
        self.game_logger.log_game_event("Home_screen method called")
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_quit)

    # Apply theme from the configuration
    def apply_theme(self):
        """
        Apply the theme from the configuration file.
        """
        theme_name = self.config.get('Settings', 'theme', fallback='Default')
        theme_dir = path.dirname(__file__)
        theme_path = path.join(theme_dir, 'themes', f"{theme_name}.json")
        try:
            ctk.set_default_color_theme(theme_path)
            self.game_logger.log_game_event(f"Theme applied: {theme_name}")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def create_home_screen(self):
        """
        Create the home screen of the game.
        """
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_main_menu_label()
        self.create_button_panel.classic_snake_button()
        self.create_button_panel.snake_endless_button()
        self.create_button_panel.snake_leveling_button()
        self.create_button_panel.challange_choice_button()
        self.create_button_panel.info_button()
        self.create_button_panel.settings_button()
        self.create_button_panel.quit_button()
        self.game_labels_panel.classic_delete_labels()
        self.classic_reset_button_press_variable()
        self.endless_reset_button_press_variable()
        self.leveling_reset_button_press_variable()
        self.main_canvas.bind("<Configure>", self.update_text_position)

    def update_text_position(self, event=None):# pylint: disable=unused-argument
        """
        Update the position of the text on the canvas.
        """
        canvas_width = self.main_canvas.winfo_width() // 2 + 80
        canvas_height = self.main_canvas.winfo_height() // 2 - 50
        self.main_canvas.delete("text")
        self.main_canvas.create_text(canvas_width, canvas_height - 50, text=self.text_name, font=self.font_50, fill="white", tags="text") # pylint: disable=line-too-long
        self.main_canvas.create_text(canvas_width, canvas_height, text=self.text_version, font=self.font_30, fill="white", tags="text") # pylint: disable=line-too-long
        self.main_canvas.create_text(canvas_width, canvas_height + 50, text=self.text_developer, font=self.font_30, fill="white", tags="text") # pylint: disable=line-too-long

    def classic_snake(self):
        """
        Start the classic snake game.
        """
        self.start_game("classic_snake")

    # Start the endless snake game
    def snake_endless(self):
        """
        Start the endless snake game.
        """
        self.start_game("snake_endless")

    # Start the leveling snake game
    def snake_leveling(self):
        """
        Start the leveling snake game.
        """
        self.start_game("snake_leveling")

    def food_time_attack(self):
        """
        Start the food time attack game.
        """
        self.start_game("food_time_attack")

    def challange_choices(self):
        """
        Start the challange choices screen.
        """
        self.start_game("challange_choices")

    def challange_settings(self):
        """
        Start the challange settings screen.
        """
        self.start_game("challange_settings")

    def open_info(self):
        """
        Open the info screen.
        """
        self.start_game("info")

    def info_home(self):
        """
        Return to the home screen from the info screen.
        """
        self.start_game("info")

    def info_general(self):
        """
        Display the general information.
        """
        self.start_game("info_general")
        self.mini_snake_game_canvas = ctk.CTkCanvas(self.root, width=150, height=150) # pylint: disable=line-too-long
        self.mini_snake_game_canvas.place(x=200, y=100)
        self.mini_snake_game = MiniSnakeGame(self.mini_snake_game_canvas, self.cell_size, self.game_logger)

        # Call the update method to start the game
        self.mini_snake_game.update()

    def info_general_reset_mini_snake(self):
        """
        Reset the mini snake game.
        """
        self.mini_snake_game.reset_game()

    def info_classic(self):
        """
        Display the classic game mode information.
        """
        self.start_game("info_classic_game_mode")

    def info_endless(self):
        """
        Display the endless game mode information.
        """
        self.start_game("info_endless_game_mode")

    def info_leveling(self):
        """
        Display the leveling game mode information.
        """
        self.start_game("info_leveling_game_mode")

    def info_challange(self):
        """
        Display the challange game mode information.
        """
        self.start_game("info_challange_game_mode")

    # Open the settings screen
    def open_settings(self):
        """
        Open the settings screen.
        """
        self.start_game("settings")

    def settings_values(self):
        """
        Open the settings values screen.
        """
        self.start_game("settings_values")

    def reset_settings(self):
        """
        Open the reset settings screen.
        """
        self.start_game("reset_settings")

    def start_game(self, game_type):
        """
        Start the game based on the game type.
        """
        # Hide the main canvas
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.general_reset_button_press_variable()

        # Set the configuration based on the game type
        self.game_config.set_configuration(game_type)

        if hasattr(self, 'create_reset_button_panel'):  # Check if reset buttons panel exists
            self.create_reset_button_panel.destroy_buttons()

        # Create a new canvas for the specified game type
        if game_type == "classic_snake":
            self.classic_snake_canvas = SnakeClassicGame(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
            self.classic_snake_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.classic_snake_canvas
        elif game_type == "snake_endless":
            self.endless_snake_canvas = SnakeEndless(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "snake_leveling":
            self.leveling_snake_canvas = SnakeLeveling(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "food_time_attack":
            self.food_time_attack_canvas = FoodTimeAttack(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "info":
            self.info_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "info_general":
            self.info_general_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        elif game_type == "info_classic_game_mode":
            self.info_classic_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "info_endless_game_mode":
            self.info_endless_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        elif game_type == "info_leveling_game_mode":
            self.info_leveling_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        elif game_type == "info_challange_game_mode":
            self.info_challange_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        elif game_type == "settings":
            self.settings_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "settings_values":
            self.settings_canvas_values = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "reset_settings":
            self.settings_canvas_reset = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "challange_choices":
            self.challange_choice_canvas = ChallangeChoices(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "challange_settings":
            self.challange_settings_canvas = ChallangeSettings(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        else:
            return

        # Pack the canvas
        if game_type == "classic_snake":
            self.classic_snake_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.classic_snake_canvas
        elif game_type == "snake_endless":
            self.endless_snake_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.endless_snake_canvas
        elif game_type == "snake_leveling":
            self.leveling_snake_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.leveling_snake_canvas
        elif game_type == "food_time_attack":
            self.food_time_attack_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.food_time_attack_canvas
        elif game_type == "info":
            self.info_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_canvas
        elif game_type == "info_general":
            self.info_general_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_general_canvas
        elif game_type == "info_classic_game_mode":
            self.info_classic_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_classic_canvas
        elif game_type == "info_endless_game_mode":
            self.info_endless_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_endless_canvas
        elif game_type == "info_leveling_game_mode":
            self.info_leveling_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_leveling_canvas
        elif game_type == "info_challange_game_mode":
            self.info_challange_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.info_challange_canvas
        elif game_type == "settings":
            self.settings_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.settings_canvas
            self.settings_canvas.update_idletasks()  # update canvas before getting its dimensions
            canvas_width = self.settings_canvas.winfo_width() // 2 + 80
            canvas_height = self.settings_canvas.winfo_height() // 2 - 50
            self.settings_canvas.create_text(canvas_width, canvas_height, text="Here you can reset or change your settings", font=self.font_20, fill="white", tags="text") # pylint: disable=line-too-long
            self.settings_canvas.create_text(canvas_width, canvas_height + 50, text="Values settings is for changes the settings like the theme or contrast", font=self.font_20, fill="white", tags="text") # pylint: disable=line-too-long
            self.settings_canvas.create_text(canvas_width, canvas_height + 100, text="Reset settings is for resetting the settings", font=self.font_20, fill="white", tags="text") # pylint: disable=line-too-long
        elif game_type == "settings_values":
            self.settings_canvas_values.pack(expand=True, fill="both")
            self.main_canvas = self.settings_canvas_values
        elif game_type == "reset_settings":
            self.settings_canvas_reset.pack(expand=True, fill="both")
            self.main_canvas = self.settings_canvas_reset
        elif game_type == "challange_choices":
            self.challange_choice_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.challange_choice_canvas
        elif game_type == "challange_settings":
            self.challange_settings_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.challange_settings_canvas

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long
        self.create_option_button_panel = OptionButtonPanel(self.root, self.main_canvas, self.game_logger) # pylint: disable=line-too-long
        self.create_reset_button_panel = ResetSettingsPanel(self.challange_settings_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long
        self.button_commands = ButtonCommands(self.game_logger, self.functions)
        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.game_logger, self.game_config, self.open_info, self.open_settings) # pylint: disable=line-too-long
        self.game_labels_panel = GameLabelsPanel(self.main_canvas, self.game_logger, self.game_config) # pylint: disable=line-too-long
        self.settings_labels = SettingsOptionButtonLabels(self.game_logger, self.main_canvas)
        self.mini_snake_game = MiniSnakeGame(self.main_canvas, 20, self.game_logger)
        self.settings_labels.update_initial_game_size()

        if game_type == "classic_snake":
            self.create_button_panel.classic_reset_high_score_button()
            self.create_button_panel.classic_reset_high_score_time_button()
            self.create_button_panel.classic_reset_high_score_snake_length()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_classic_snake_label()

        elif game_type == "snake_endless":
            self.create_button_panel.endless_reset_high_score_button()
            self.create_button_panel.endless_reset_high_score_time_button()
            self.create_button_panel.endless_reset_high_score_snake_length()
            self.create_button_panel.endless_reset_high_score_special_score_button()
            self.create_button_panel.endless_reset_high_score_shorten_snake_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_endless_snake_label()

        elif game_type == "snake_leveling":
            self.create_button_panel.leveling_reset_high_score_button()
            self.create_button_panel.leveling_reset_high_score_time_button()
            self.create_button_panel.leveling_reset_high_score_snake_length_button()
            self.create_button_panel.leveling_reset_high_score_special_score_button()
            self.create_button_panel.leveling_reset_high_score_shorten_snake_button()
            self.create_button_panel.leveling_reset_high_scores_xp_button()
            self.create_button_panel.leveling_reset_high_score_level_button()

            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_leveling_snake_label()

        elif game_type == "challange_choices":
            self.create_button_panel.challange_settings_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_challange_choices_label()

        elif game_type == "challange_settings":
            self.challange_choice_canvas = self.destroy_canvas(self.challange_choice_canvas)
            self.create_button_panel.food_time_attack_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_challange_settings_label()

        elif game_type == "food_time_attack":
            self.challange_settings_canvas = self.destroy_canvas(self.challange_settings_canvas)
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_food_time_attack_label()

        elif game_type == "info":
            if self.info_general_canvas is not None and self.info_general_canvas.winfo_exists():
                self.info_general_canvas = self.destroy_canvas(self.info_general_canvas)
            elif self.info_classic_canvas is not None and self.info_classic_canvas.winfo_exists():
                self.info_classic_canvas = self.destroy_canvas(self.info_classic_canvas)
            elif self.info_endless_canvas is not None and self.info_endless_canvas.winfo_exists():
                self.info_endless_canvas = self.destroy_canvas(self.info_endless_canvas)
            elif self.info_leveling_canvas is not None and self.info_leveling_canvas.winfo_exists():
                self.info_leveling_canvas = self.destroy_canvas(self.info_leveling_canvas)
            elif self.info_challange_canvas is not None and self.info_challange_canvas.winfo_exists():
                self.info_challange_canvas = self.destroy_canvas(self.info_challange_canvas)
            else:
                pass
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_label()
            self.create_button_panel.patchnotes_button()
            self.create_button_panel.info_general_button()
            self.create_button_panel.info_classic_game_mode_button()
            self.create_button_panel.info_endless_game_mode_button()
            self.create_button_panel.info_leveling_game_mode_button()
            self.create_button_panel.info_challange_game_mode_button()
            #self.patchnotes_displayed = False

        elif game_type == "info_general":
            if self.info_canvas is not None and self.info_canvas.winfo_exists():
                self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.create_button_panel.info_home_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_general_label()
            self.create_reset_button_panel.info_general_reset_mini_snake()
        
        elif game_type == "info_classic_game_mode":
            if self.info_canvas is not None and self.info_canvas.winfo_exists():
                self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.create_button_panel.info_home_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_classic_label()
        
        elif game_type == "info_endless_game_mode":
            if self.info_canvas is not None and self.info_canvas.winfo_exists():
                self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.create_button_panel.info_home_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_endless_label()
        
        elif game_type == "info_leveling_game_mode":
            if self.info_canvas is not None and self.info_canvas.winfo_exists():
                self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.create_button_panel.info_home_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_leveling_label()
        
        elif game_type == "info_challange_game_mode":
            if self.info_canvas is not None and self.info_canvas.winfo_exists():
                self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.create_button_panel.info_home_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_challange_label()

        elif game_type == "settings":
            self.create_button_panel.reset_settings_button()
            self.create_button_panel.settings_values_button()
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_settings_label()

        elif game_type == "settings_values":
            if self.settings_canvas is not None and self.settings_canvas.winfo_exists():
                self.settings_canvas = self.destroy_canvas(self.settings_canvas)
            if self.settings_canvas_reset is not None and self.settings_canvas_reset.winfo_exists():
                self.settings_canvas_reset = self.destroy_canvas(self.settings_canvas_reset)
            self.get_color_from_config()
            self.draw_snake_with_color(self.snake_color)
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_settings_values_label()
            self.create_option_button_panel.show_options()
            self.create_button_panel.reset_settings_button()
            self.settings_labels.create_settings_labels()
            self.settings_labels.create_theme_label()
            self.settings_labels.create_game_size_label()

        elif game_type == "reset_settings":
            if self.settings_canvas is not None and self.settings_canvas.winfo_exists():
                self.settings_canvas = self.destroy_canvas(self.settings_canvas)
            if self.settings_canvas_values is not None and self.settings_canvas_values.winfo_exists(): # pylint: disable=line-too-long
                self.settings_canvas_values = self.destroy_canvas(self.settings_canvas_values)
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.create_button_panel.settings_values_button()
            self.settings_labels.create_settings_reset_labels()
            self.framelabel_panel.create_settings_reset_label()
            self.create_reset_button_panel.show_all_reset_buttons()

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)

    def get_color_from_config(self):
        """
        Get the snake color from the config file.
        """
        self.config.read(self.config_path)
        new_snake_color = self.config.get('Settings', 'snake_color', fallback='Default')
        if new_snake_color.lower() == 'default':
            new_snake_color = '#00FF00'
        if new_snake_color.lower() == 'midnightpurple':
            new_snake_color = "#210F28"
        if new_snake_color != self.snake_color:
            self.snake_color = new_snake_color
            self.draw_snake_with_color(self.snake_color)
        self.root.after(50, self.get_color_from_config)

    def draw_snake_with_color(self, color):
        """
        Draw the snake with the specified color.
        """
        if not None:
            x1, y1, x2, y2 = 825, 125, 800, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long
            #800, 50
            x1, y1, x2, y2 = 830, 125, 855, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long

            x1, y1, x2, y2 = 860, 125, 885, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long

            x1, y1, x2, y2 = 890, 125, 915, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long

            x1, y1, x2, y2 = 920, 125, 945, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long

            x1, y1, x2, y2 = 950, 125, 975, 100
            self.settings_canvas_values.create_rectangle(x1, y1, x2, y2, fill=color, outline="black") # pylint: disable=line-too-long

    def patchnotes(self):
        """
        Display the patchnotes.
        """

        if hasattr(self, 'patchnotes_displayed') and self.info_canvas is True:
            self.scrollable_frame.place(x=250, y=75)

        if not hasattr(self, 'patchnotes_displayed'):
            self.patchnotes_displayed = False

        if not self.patchnotes_displayed:
            # Create a scrollable frame and load the patchnotes into it
            self.patchnotes_label = ctk.CTkLabel(self.info_canvas,
                                        height = 50,
                                        width = 873,
                                        corner_radius = 6,
                                        text="Patchnotes", font=FONT_LIST[15]) # pylint: disable=line-too-long
            self.patchnotes_label.place(x=250, y=10)
            self.scrollable_frame = ctk.CTkScrollableFrame(self.info_canvas, width=850, height=600, fg_color='Grey10') # pylint: disable=line-too-long
            with open("patchnotes.json", "r", encoding='utf-8') as file:
                patchnotes = json.load(file)
                for note in patchnotes:
                    version_label = ctk.CTkLabel(self.scrollable_frame,
                                        height = 30,
                                        width = 750,
                                        corner_radius = 0,
                                        text="Version: " + note['version'], # pylint: disable=line-too-long
                                        font=FONT_LIST[11])
                    version_label.pack()
                    for change in note['changes']:
                        change_label = ctk.CTkLabel(self.scrollable_frame,
                                        height = 30,
                                        width = 750,
                                        corner_radius = 0,
                                        text=change,
                                        font=FONT_LIST[10])
                        change_label.pack()
                    empty_space_label = ctk.CTkLabel(self.scrollable_frame, text="", fg_color='Grey10') # pylint: disable=line-too-long
                    empty_space_label.pack()
            self.scrollable_frame.place(x=250, y=75)
            self.patchnotes_displayed = True
        else:
            if self.scrollable_frame is not None:
                self.scrollable_frame.place_forget()
                self.patchnotes_label.place_forget()
                self.patchnotes_displayed = False

    def reset_screen_size(self):
        """
        Reset the screen size to the default value.
        """
        self.reset_config_values.reset_screen_size()

    def reset_theme(self):
        """
        Reset the theme to the default value.
        """
        self.reset_config_values.reset_theme()

    def reset_contrast(self):
        """
        Reset the contrast to the default value.
        """
        self.reset_config_values.reset_contrast()

    def reset_high_score_showing(self):
        """
        Reset the high score label showing to the default value.
        """
        self.reset_config_values.reset_high_score_showing()
    def reset_snake_speed(self):
        """
        Reset the snake speed to the default value.
        """
        self.reset_config_values.reset_snake_speed()
    def reset_game_size(self):
        """
        Reset the game size to the default value.
        """
        self.reset_config_values.reset_game_size()

    def reset_snake_color(self):
        """
        Reset the snake color to the default value.
        """
        self.reset_config_values.reset_snake_color()

    def reset_move_up(self):
        """
        Reset the move up key to the default value.
        """
        self.reset_config_values.reset_move_up()

    def reset_move_down(self):
        """
        Reset the move down key to the default value.
        """
        self.reset_config_values.reset_move_down()

    def reset_move_left(self):
        """
        Reset the move left key to the default value.
        """
        self.reset_config_values.reset_move_left()

    def reset_move_right(self):
        """
        Reset the move right key to the default value.
        """
        self.reset_config_values.reset_move_right()

    def reset_pause(self):
        """
        Reset the pause key to the default value.
        """
        self.reset_config_values.reset_pause()

    def reset_start_game(self):
        """
        Reset the start game key to the default value.
        """
        self.reset_config_values.reset_start_game()

    def reset_restart(self):
        """
        Reset the restart key to the default value.
        """
        self.reset_config_values.reset_restart()

    def reset_all_settings(self):
        """
        Reset all the settings to the default values.
        """
        self.reset_config_values.reset_all_settings()

    def reset_all_movements(self):
        """
        Reset all the movements to the default values.
        """
        self.reset_config_values.reset_all_movements()

    def classic_reset_high_score(self):
        """
        Reset the high score for the classic snake game.
        """
        self.reset_config_values.classic_reset_high_score()
        self.classic_snake_canvas.update_high_score_labels_()

    def classic_reset_high_score_time(self):
        """
        Reset the high score time for the classic snake game.
        """
        self.reset_config_values.classic_reset_high_score_time()
        self.classic_snake_canvas.update_high_score_labels_()

    def classic_reset_snake_length(self):
        """
        Reset the high score snake length for the classic snake game.
        """
        self.reset_config_values.classic_reset_snake_length()
        self.classic_snake_canvas.update_high_score_labels_()

    def classic_reset_button_press_variable(self):
        """
        Reset the button press variable for the classic snake game.
        """
        self.reset_config_values.classic_reset_button_press_variable()

    def endless_reset_high_score(self):
        """
        Reset the high score for the endless snake game.
        """
        self.reset_config_values.endless_reset_high_score()
        self.endless_snake_canvas.update_high_score_labels_()

    def endless_reset_high_score_time(self):
        """
        Reset the high score time for the endless snake game.
        """
        self.reset_config_values.endless_reset_high_score_time()
        self.endless_snake_canvas.update_high_score_labels_()

    def endless_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the endless snake game.
        """
        self.reset_config_values.endless_reset_high_score_snake_length()
        self.endless_snake_canvas.update_high_score_labels_()

    def endless_reset_high_score_special_score(self):
        """
        Reset the high score special score for the endless snake game.
        """
        self.reset_config_values.endless_reset_high_score_special_score()
        self.endless_snake_canvas.update_high_score_labels_()

    def endless_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the endless snake game.
        """
        self.reset_config_values.endless_reset_high_score_shorten_snake()
        self.endless_snake_canvas.update_high_score_labels_()

    def endless_reset_button_press_variable(self):
        """
        Reset the button press variable for the endless snake game.
        """
        self.reset_config_values.endless_reset_button_press_variable()

    def leveling_reset_high_score(self):
        """
        Reset the high score for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_score_time(self):
        """
        Reset the high score time for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score_time()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score_snake_length()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_score_special_score(self):
        """
        Reset the high score special score for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score_special_score()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score_shorten_snake()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_scores_xp(self):
        """
        Reset the high score xp for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_scores_xp()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_high_score_level(self):
        """
        Reset the high score level for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_high_score_level()
        self.leveling_snake_canvas.update_high_score_labels_()

    def leveling_reset_button_press_variable(self):
        """
        Reset the button press variable for the leveling snake game.
        """
        self.reset_config_values.leveling_reset_button_press_variable()

    def general_reset_button_press_variable(self):
        """
        Reset the button press variable for the game.
        """
        self.reset_config_values.general_reset_button_press_variable()

    # Destroy the current canvas
    def destroy_canvas(self, canvas):
        """
        Destroy the canvas.
        """
        try:
            if canvas is not None:
                self.framelabel_panel.set_create_label_canvas_flag(False)
                canvas.destroy()
                return None
            return canvas

        except ValueError as e:
            traceback.print_exc(e)
            return canvas

    # Return to the home screen
    def return_home(self):
        """
        Return to the home screen.
        """
        try:
             # Reset the patchnotes_displayed variable
            if not hasattr(self.button_commands, 'patchnotes_displayed'):
                if self.scrollable_frame is not None and self.scrollable_frame.winfo_exists():
                    self.scrollable_frame.place_forget()
                self.patchnotes_displayed = False

            if hasattr(self, 'button_commands'):
                # print('button_commands exists')
                self.create_reset_button_panel.destroy_buttons()

            if self.main_canvas == self.classic_snake_canvas:
                self.classic_snake_canvas.delete_game_labels()
            if self.main_canvas == self.endless_snake_canvas:
                self.endless_snake_canvas.delete_game_labels_()
            if self.main_canvas == self.leveling_snake_canvas:
                self.leveling_snake_canvas.delete_game_labels__()
            if self.main_canvas == self.food_time_attack_canvas:
                self.food_time_attack_canvas.delete_game_labels___()

            time.sleep(0.1)
            # Destroy all game canvases
            self.classic_snake_canvas = self.destroy_canvas(self.classic_snake_canvas)
            self.endless_snake_canvas = self.destroy_canvas(self.endless_snake_canvas)
            self.leveling_snake_canvas = self.destroy_canvas(self.leveling_snake_canvas)
            self.food_time_attack_canvas = self.destroy_canvas(self.food_time_attack_canvas)
            self.challange_choice_canvas = self.destroy_canvas(self.challange_choice_canvas)
            self.challange_settings_canvas = self.destroy_canvas(self.challange_settings_canvas)
            self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.info_general_canvas = self.destroy_canvas(self.info_general_canvas)
            self.info_classic_canvas = self.destroy_canvas(self.info_classic_canvas)
            self.info_endless_canvas = self.destroy_canvas(self.info_endless_canvas)
            self.info_leveling_canvas = self.destroy_canvas(self.info_leveling_canvas)
            self.info_challange_canvas = self.destroy_canvas(self.info_challange_canvas)
            self.settings_canvas = self.destroy_canvas(self.settings_canvas)
            self.settings_canvas_reset = self.destroy_canvas(self.settings_canvas_reset)
            self.settings_canvas_values = self.destroy_canvas(self.settings_canvas_values)
            self.mini_snake_game_canvas = self.destroy_canvas(self.mini_snake_game_canvas)

            # Show the original main canvas (home screen)
            self.original_main_canvas.pack(expand=True, fill="both")
        except ValueError as e:
            traceback.print_exc(e)

    def close_mini_snake(self):
        if self.mini_snake_game is not None:
            self.mini_snake_game.running = False
            self.mini_snake_game_canvas.destroy()
            self.mini_snake_game_canvas = None
            self.mini_snake_game = None

    # Confirm quitting the game
    def confirm_quit(self):
        """
        Confirm quitting the game.
        """
        try:
            
            self.close_mini_snake()
            if self.mini_snake_game_canvas is not None:
                self.mini_snake_game_canvas.destroy()
                self.mini_snake_game_canvas = None
            # Assuming game_logger and error_game_logger are defined somewhere in your class
            self.game_logger.on_closing()
            self.error_game_logger.on_closing()
        except FileNotFoundError as e:
            traceback.print_exc(e)
        except AttributeError:
            # Handle the case where game_logger or error_game_logger might not be defined
            pass

# Main function
if __name__ == "__main__":
    root = ctk.CTk()
    app = SnakeGameApp(root, GameConstants.MIN_WIDTH, GameConstants.MIN_HEIGHT)
    root.title("Shadows Snake Game")
    root.geometry(f"{GameConstants.MIN_WIDTH}x{GameConstants.MIN_HEIGHT}")
    if SCREEN_SIZE_FULLSCREEN == 'fullscreen':
        root.attributes('-fullscreen', True)
    root.resizable(False, False)

    def center_window():
        """
        Center the window on the screen.
        """
        root.update_idletasks()
        window_width, window_height = root.winfo_width(), root.winfo_height()
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.after(10, center_window)
    root.mainloop()

# End of main_snake_game.py
