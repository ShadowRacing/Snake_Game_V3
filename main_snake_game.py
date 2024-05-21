# *****************************************
# Shadows Snake Main File
# *****************************************

"""
The main file for the Shadows Snake game.
"""

# Import all the necessary libraries
import traceback
import time
import configparser
import json
from os import path
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Logs.gamelogger_snake_game import GameLogger , ErrorgameLogger
from Configuration.constants_snake_game import GameConstants, SCREEN_SIZE_FULLSCREEN, FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.buttonpanel_snake_game import ClickButtonPanel, OptionButtonPanel, ButtonCommands, ResetSettingsPanel # pylint: disable=line-too-long
from Logic.labelpanel_snake_game import NameOffFrameLabelPanel, SettingsOptionButtonLabels, GameLabelsPanel # pylint: disable=line-too-long
from Logic.config_ini_initials import ConfigIni
from Logic.snake_challange_choice import ChallangeChoices
from Logic.snake_challange_settings import ChallangeSettings
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
        self.text_version = "Version: 0.2.3"
        self.text_developer = "Developer: Shadow"
        self.font_50 = ("Helvetica", 50)
        self.font_30 = ("Helvetica", 30)

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
        self.settings_canvas = None
        self.reset_label = None
        self.reset_settings_frame = None
        self.reset_settings_frame_1 = None

        self.patchnotes_displayed = False
        self.reset_settings_displayed = False
        self.scrollable_frame = self.scrollable_frame = ctk.CTkScrollableFrame(self.info_canvas, width=850, height=600, fg_color='Grey10') # pylint: disable=line-too-long
        self.patchnotes_label = None

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
            'open_info': self.open_info,
            'snake_leveling': self.snake_leveling,
            'snake_endless': self.snake_endless,
            'classic_snake': self.classic_snake,
            'food_time_attack': self.food_time_attack,
            'challange_choices': self.challange_choices,
            'challange_settings': self.challange_settings,
            'patchnotes': self.patchnotes,
            'reset_settings': self.reset_settings,
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
        }

        self.create_option_button_panel = None
        self.first_button_press_time = None

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long

        # And then create the ButtonCommands instance
        self.button_commands = ButtonCommands(self.game_logger, self.functions)

        self.reset_commands = ResetSettingsPanel(self.reset_settings_frame,self.game_logger, self.button_commands,  self.functions) # pylint: disable=line-too-long

        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.game_logger,
                                                        self.game_config, self.open_info,
                                                        self.open_settings)

        self.game_labels_panel = GameLabelsPanel(self.main_canvas,self.game_logger,  self.game_config) # pylint: disable=line-too-long

        self.settings_labels = SettingsOptionButtonLabels(self.game_logger, self.main_canvas)

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

    # Open the settings screen
    def open_settings(self):
        """
        Open the settings screen.
        """
        self.start_game("settings")

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

        # Create a new canvas for the specified game type
        if game_type == "classic_snake":
            self.classic_snake_canvas = SnakeClassicGame(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "snake_endless":
            self.endless_snake_canvas = SnakeEndless(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "snake_leveling":
            self.leveling_snake_canvas = SnakeLeveling(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "food_time_attack":
            self.food_time_attack_canvas = FoodTimeAttack(self.root, self.game_config, self.game_logger, self.functions, self.create_button_panel) # pylint: disable=line-too-long
        elif game_type == "info":
            self.info_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
        elif game_type == "settings":
            self.settings_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5) # pylint: disable=line-too-long
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
            self.info_canvas.update_idletasks()  # update canvas before getting its dimensions
            canvas_width = self.info_canvas.winfo_width() // 2 + 80
            canvas_height = self.info_canvas.winfo_height() // 2 - 50
            self.info_canvas.create_text(canvas_width, canvas_height - 50, text=self.text_name, font=self.font_50, fill="white", tags="text") # pylint: disable=line-too-long
            self.info_canvas.create_text(canvas_width, canvas_height, text=self.text_version, font=self.font_30, fill="white", tags="text") # pylint: disable=line-too-long
            self.info_canvas.create_text(canvas_width, canvas_height + 50, text=self.text_developer, font=self.font_30, fill="white", tags="text") # pylint: disable=line-too-long
        elif game_type == "settings":
            self.settings_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.settings_canvas
        elif game_type == "challange_choices":
            self.challange_choice_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.challange_choice_canvas
        elif game_type == "challange_settings":
            self.challange_settings_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.challange_settings_canvas

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.game_logger, self.functions) # pylint: disable=line-too-long
        self.create_option_button_panel = OptionButtonPanel(self.root, self.main_canvas, self.game_logger) # pylint: disable=line-too-long
        self.button_commands = ButtonCommands(self.game_logger, self.functions)
        self.reset_commands = ResetSettingsPanel(self.reset_settings_frame,self.game_logger, self.button_commands,  self.functions) # pylint: disable=line-too-long
        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.game_logger, self.game_config, self.open_info, self.open_settings) # pylint: disable=line-too-long
        self.game_labels_panel = GameLabelsPanel(self.main_canvas, self.game_logger, self.game_config) # pylint: disable=line-too-long
        self.settings_labels = SettingsOptionButtonLabels(self.game_logger, self.main_canvas)
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
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_info_label()
            self.create_button_panel.patchnotes_button()

        elif game_type == "settings":
            self.get_color_from_config()
            self.draw_snake_with_color(self.snake_color)
            self.framelabel_panel.set_create_label_canvas_flag(True)
            self.framelabel_panel.create_settings_label()
            self.create_option_button_panel.show_options()
            self.create_button_panel.reset_settings_button()
            self.settings_labels.create_settings_labels()
            self.settings_labels.create_theme_label()
            self.settings_labels.create_game_size_label()

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        #self.create_button_panel.reset_high_score_buttons(game_type)
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
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            #800, 50
            x1, y1, x2, y2 = 830, 125, 855, 100
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            x1, y1, x2, y2 = 860, 125, 885, 100
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            x1, y1, x2, y2 = 890, 125, 915, 100
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            x1, y1, x2, y2 = 920, 125, 945, 100
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            x1, y1, x2, y2 = 950, 125, 975, 100
            self.settings_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

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

    def reset_settings(self):
        """
        Reset the specified setting to the default value.
        """

        if hasattr(self, 'reset_settings_displayed'):
            self.reset_settings_displayed = False
            self.scrollable_frame.place_forget()

        if not hasattr(self, 'reset_settings_displayed'):
            self.reset_settings_displayed = False

        if not self.reset_settings_displayed:
            self.reset_label = ctk.CTkLabel(self.settings_canvas,
                                        height = 50,
                                        width = 873,
                                        corner_radius = 6,
                                        text="Reset Settings",
                                        font=FONT_LIST[15])
            self.reset_label.place(x=250, y=10)

            self.reset_settings_frame = ctk.CTkFrame(self.settings_canvas,
                                        width=850,
                                        height=600,
                                        fg_color='Grey10') # pylint: disable=line-too-long
            self.reset_settings_frame.place(x=250, y=75)
            self.reset_commands.reset_screen_size_button()
            self.reset_commands.reset_theme_button()
            self.reset_commands.reset_contrast_button()
            self.reset_commands.reset_high_score_label_showing_button()
            self.reset_commands.reset_snake_speed_button()
            self.reset_commands.reset_game_size_button()
            self.reset_commands.reset_snake_color_button()
            self.reset_commands.reset_move_up_button()
            self.reset_commands.reset_move_down_button()
            self.reset_commands.reset_move_left_button()
            self.reset_commands.reset_move_right_button()
            self.reset_commands.reset_pause_game_button()
            self.reset_commands.reset_start_game_button()
            self.reset_commands.reset_restart_game_button()
            self.reset_commands.reset_all_settings_button()
            self.reset_commands.reset_all_movements_button()

            self.reset_settings_displayed = True
            print("before being set true")
            print(self.reset_settings_displayed)

        else:
            self.reset_commands.destroy_buttons_on_reset_frame_settings()
            self.reset_settings_frame.destroy()
            self.reset_settings_displayed = False
            self.reset_label.destroy()

    def reset_screen_size(self):
        """
        Reset the screen size to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'screen_size', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Screen size reset to Default")

    def reset_theme(self):
        """
        Reset the theme to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'theme', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Theme reset to Default")

    def reset_contrast(self):
        """
        Reset the contrast to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'contrast', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Contrast reset to Default")

    def reset_high_score_showing(self):
        """
        Reset the high score label showing to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'high_score_label_showing', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("High score label showing reset to True")

    def reset_snake_speed(self):
        """
        Reset the snake speed to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'snake_speed', '50')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Snake speed reset to 5")

    def reset_game_size(self):
        """
        Reset the game size to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'game_size', '600x600')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Game size reset to 600x600")

    def reset_snake_color(self):
        """
        Reset the snake color to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'snake_color', 'Default')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Snake color reset to Default")

    def reset_move_up(self):
        """
        Reset the move up key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'move_up', 'w')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move up key reset to w")

    def reset_move_down(self):
        """
        Reset the move down key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'move_down', 's')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move down key reset to s")

    def reset_move_left(self):
        """
        Reset the move left key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'move_left', 'a')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move left key reset to a")

    def reset_move_right(self):
        """
        Reset the move right key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'move_right', 'd')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Move right key reset to d")

    def reset_pause(self):
        """
        Reset the pause key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'pause', 'Escape')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Pause key reset to Escape")

    def reset_start_game(self):
        """
        Reset the start game key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'start_game', 'space')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Start game key reset to space")

    def reset_restart(self):
        """
        Reset the restart key to the default value.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'restart', 'r')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("Restart key reset to r")

    def reset_all_settings(self):
        """
        Reset all the settings to the default values.
        """
        self.config.read(self.config_path)
        self.config.set('Settings', 'screen_size', 'Default')
        self.config.set('Settings', 'theme', 'Default')
        self.config.set('Settings', 'contrast', 'Default')
        self.config.set('Settings', 'high_score_label_showing', 'Default')
        self.config.set('Settings', 'snake_speed', '50')
        self.config.set('Settings', 'game_size', 'Default')
        self.config.set('Settings', 'snake_color', 'Default')
        self.config.set('KeyBindings', 'move_up', 'w')
        self.config.set('KeyBindings', 'move_down', 's')
        self.config.set('KeyBindings', 'move_left', 'a')
        self.config.set('KeyBindings', 'move_right', 'd')
        self.config.set('KeyBindings', 'pause', 'Escape')
        self.config.set('KeyBindings', 'start_game', 'sapce')
        self.config.set('KeyBindings', 'restart', 'r')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("All settings reset to default")

    def reset_all_movements(self):
        """
        Reset all the movements to the default values.
        """
        self.config.read(self.config_path)
        self.config.set('KeyBindings', 'move_up', 'w')
        self.config.set('KeyBindings', 'move_down', 's')
        self.config.set('KeyBindings', 'move_left', 'a')
        self.config.set('KeyBindings', 'move_right', 'd')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event("All movements reset to default")

    def classic_reset_high_score(self):
        """
        Reset the high score for the classic snake game.
        """
        if self.classic_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score += 1
        elif self.classic_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore reset to 0")
            self.classic_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def classic_reset_high_score_time(self):
        """
        Reset the high score time for the classic snake game.
        """
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def classic_reset_snake_length(self):
        """
        Reset the high score snake length for the classic snake game.
        """
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def classic_reset_button_press_variable(self):
        """
        Reset the button press variable for the classic snake game.
        """
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0

    def endless_reset_high_score(self):
        """
        Reset the high score for the endless snake game.
        """
        if self.endless_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score += 1
        elif self.endless_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore reset to 0")
            self.endless_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def endless_reset_high_score_time(self):
        """
        Reset the high score time for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_special_score(self):
        """
        Reset the high score special score for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore special reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the endless snake game.
        """
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore shorten snake reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_button_press_variable(self):
        """
        Reset the button press variable for the endless snake game.
        """
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0

    def leveling_reset_high_score(self):
        """
        Reset the high score for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score += 1
        elif self.leveling_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore reset to 0")
            self.leveling_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_time(self):
        """
        Reset the high score time for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_snake_length(self):
        """
        Reset the high score snake length for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore time reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_special_score(self):
        """
        Reset the high score special score for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore special reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_shorten_snake(self):
        """
        Reset the high score shorten snake for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore shorten snake reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_scores_xp(self):
        """
        Reset the high score xp for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'xp_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore xp reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_high_score_level(self):
        """
        Reset the high score level for the leveling snake game.
        """
        if self.leveling_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.leveling_button_press_variable_high_score_time += 1
        elif self.leveling_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit: # pylint: disable=line-too-long
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.set('Leveling_Snake_Values', 'level_high_score', '0')
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except FileNotFoundError as e:
                traceback.print_exc(e)
            self.leveling_snake_canvas.update_high_score_labels_()
            self.game_logger.log_game_event("Highscore level reset to 0")
            self.leveling_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def leveling_reset_button_press_variable(self):
        """
        Reset the button press variable for the leveling snake game.
        """
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0

    def general_reset_button_press_variable(self):
        """
        Reset the button press variable for the game.
        """
        self.button_press_variable = 0

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
            self.settings_canvas = self.destroy_canvas(self.settings_canvas)

            # Reset the patchnotes_displayed variable
            if hasattr(self.button_commands, 'patchnotes_displayed'):
                self.scrollable_frame.place_forget()
                self.patchnotes_displayed = False

            
            # if self.patchnotes_displayed is True:
            #     self.patchnotes_displayed = False

            # Reset the reset_settings_displayed variable
            if hasattr(self, 'reset_settings_displayed'):
                self.reset_commands.destroy_buttons_on_reset_frame_settings()
                self.reset_settings_displayed = False
            
            # if self.reset_settings_displayed is True:
            #     self.reset_settings_displayed = False

            # Show the original main canvas (home screen)
            self.original_main_canvas.pack(expand=True, fill="both")
        except ValueError as e:
            traceback.print_exc(e)

    # Confirm quitting the game
    def confirm_quit(self):
        """
        Confirm quitting the game.
        """
        try:
            self.game_logger.on_closing()
            self.error_game_logger.on_closing()
        except FileNotFoundError as e:
            traceback.print_exc(e)


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

# *****************************************
# Shadows Snake Main File
# *****************************************
