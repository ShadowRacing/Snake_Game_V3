# *****************************************
# Wims Snake Main File
# *****************************************

# Import all the necessary libraries
import customtkinter as ctk
import configparser, traceback, time
from os import path

# Importing thhe necessary modules from other folders
from Logs.gamelogger_snake_game import LogFile , ErrorLogFile
from Configuration.constants_snake_game import GameConstants, SCREEN_SIZE_FULLSCREEN
from Configuration.gameconfig_snake_game import GameConfig
from Logic.buttonpanel_snake_game import ClickButtonPanel, OptionButtonPanel, ButtonCommands
from Logic.labelpanel_snake_game import NameOffFrameLabelPanel, SettingsOptionButtonLabels, GameLabelsPanel
from Logic.snake_logic_snake_game import Snake
from Logic.food_logic_snake_game import ClassicFood, LevelingFood, EndlessFood
from Logic.config_ini_Initials import ConfigIni
from Games.snake_classic_game import Snake_Classic_Game
from Games.snake_endless_game import Snake_endless
from Games.snake_leveling_game import Snake_Leveling
from Games.multiplayer import MultiPlayer
from Themes.theme_updater_snake_game import ThemeUpdater
from Themes.contrast_updater_snake_game import UpdateContrast

# Define the main application class
class SnakeGameApp:
    def __init__ (self, root, game_width, game_height):
        #Initialize the game app values
        self.config_ini = ConfigIni()
        self.config_ini.set_config()
        time.sleep(1)
        self.root = root
        self.logfile = LogFile(root)
        self.error_logfile = ErrorLogFile()
        self.logfile.log_game_event("Started the GameApp Class")
        self.game_config = GameConfig(logfile=self.logfile, game_mode = "initial_config")
        self.update_contrast = UpdateContrast(self.logfile)
        self.theme_updater = ThemeUpdater(self.logfile)
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
        except Exception as e:
            traceback.print_exc(e)

        self.apply_theme()
        self.update_contrast.apply_contrast(selected_value=None)

        # Write the changes to the config file
        try:
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            traceback.print_exc(e)

        # Button press variables
        self.button_press_variable = 0
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0
        self.multiplayer_button_press_variable_high_score = 0
        self.multiplayer_button_press_variable_high_score_time = 0
        self.button_press_time_limit = float(self.config.get('Settings', 'button_press_time_limit', fallback=0.5))

        # Creating the main canvas for the app
        self.main_canvas = ctk.CTkCanvas(root, highlightbackground='Black', highlightthickness=5, bg='Grey20')
        self.main_canvas.pack(expand=True, fill="both")
        self.original_main_canvas = self.main_canvas

        # All the game canvases
        self.classic_snake_canvas = None
        self.endless_snake_canvas = None
        self.leveling_snake_canvas = None
        self.multiplayer_snake_canvas = None
        self.info_canvas = None
        self.settings_canvas = None

        # The current game canvas
        #self.current_classic_snake_canvas = None

        # Create the snake and food objects
        self.snake = Snake(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
        self.classicfood = ClassicFood(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
        self.leveling_food = LevelingFood(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
        self.endless_food = EndlessFood(self.logfile, canvas=self.main_canvas, game_config=self.game_config)

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
            'open_settings': self.open_settings,
            'open_info': self.open_info,
            'snake_multiplayer': self.snake_multiplayer,
            'snake_leveling': self.snake_leveling,
            'snake_endless': self.snake_endless,
            'classic_snake': self.classic_snake,
        }

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.logfile, self.functions)

        # And then create the ButtonCommands instance
        self.button_commands = ButtonCommands(self.logfile, self.functions)

        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.logfile,  self.game_config, self.open_info,
                                      self.open_settings)

        self.game_labels_panel = GameLabelsPanel(self.main_canvas,self.logfile,  self.game_config)

        self.settings_labels = SettingsOptionButtonLabels(self.logfile, self.main_canvas)

        self.settings_labels.update_initial_game_size()

        # Create the home screen
        self.create_home_screen()
        self.logfile.log_game_event("start_screen method called")

    # Apply theme from the configuration
    def apply_theme(self):
        theme_name = self.config.get('Settings', 'theme', fallback='Default')
        theme_dir = path.dirname(__file__)
        theme_path = path.join(theme_dir, 'themes', f"{theme_name}.json")
        try:
            ctk.set_default_color_theme(theme_path)
        except Exception as e:
            traceback.print_exc(e)

    def create_home_screen(self):
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_main_menu_label()
        self.create_button_panel.classic_snake_button()
        self.create_button_panel.snake_endless_button()
        self.create_button_panel.snake_leveling_button()
        self.create_button_panel.multiplayer_snake_button()
        self.create_button_panel.info_button()
        self.create_button_panel.settings_button()
        self.create_button_panel.quit_button()
        self.game_labels_panel.classic_delete_labels()
        self.classic_reset_button_press_variable()
        self.endless_reset_button_press_variable()
        self.leveling_reset_button_press_variable()
        self.multiplayer_reset_button_press_variable()

    def classic_snake(self):
       self.start_game("classic_snake")

    # Start the endless snake game
    def snake_endless(self):
        self.start_game("snake_endless")

    # Start the leveling snake game
    def snake_leveling(self):
        self.start_game("snake_leveling")

    def snake_multiplayer(self):
        self.start_game("snake_multiplayer")

    def start_game(self, game_type):
        # Hide the main canvas
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.general_reset_button_press_variable()

        # Set the configuration based on the game type
        self.game_config.set_configuration(game_type)

        # Create a new canvas for the specified game type
        if game_type == "classic_snake":
            self.classic_snake_canvas = Snake_Classic_Game(self.root, self.game_config, self.logfile, self.functions, self.create_button_panel)
        elif game_type == "snake_endless":
            self.endless_snake_canvas = Snake_endless(self.root, self.game_config, self.logfile, self.functions, self.create_button_panel)
        elif game_type == "snake_leveling":
            self.leveling_snake_canvas = Snake_Leveling(self.root, self.game_config, self.logfile, self.functions, self.create_button_panel)
        elif game_type == "snake_multiplayer":
            self.multiplayer_snake_canvas = MultiPlayer(self.root, self.game_config, self.logfile, self.functions, self.create_button_panel)
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
        elif game_type == "snake_multiplayer":
            self.multiplayer_snake_canvas.pack(expand=True, fill="both")
            self.main_canvas = self.multiplayer_snake_canvas

        # Initializing the button panel and label panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas, self.logfile, self.functions)
        self.button_commands = ButtonCommands(self.logfile, self.functions)
        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas, self.logfile, self.game_config, self.open_info, self.open_settings)
        self.game_labels_panel = GameLabelsPanel(self.main_canvas, self.logfile, self.game_config)
        self.settings_labels = SettingsOptionButtonLabels(self.logfile, self.main_canvas)
        self.settings_labels.update_initial_game_size()

        # Create the home screen
        self.create_home_screen()
        self.logfile.log_game_event("start_screen method called")

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        #self.create_button_panel.reset_high_score_buttons(game_type)
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)




    # Open the information screen
    def open_info(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.general_reset_button_press_variable()

        self.info_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        self.info_canvas.pack(expand=True, fill="both")

        self.main_canvas = self.info_canvas

        # Update the button panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas,
                                                    self.logfile,
                                                    self.functions
                                                    )

        # Update the frame label panel
        self.framelabel_panel = NameOffFrameLabelPanel( self.main_canvas,
                                                        self.logfile,
                                                        self.game_config,
                                                        self.open_info,
                                                        self.open_settings
                                                        )

        # Update the game labels panel
        self.game_labels_panel = GameLabelsPanel(self.main_canvas,
                                                        self.logfile,
                                                        self.game_config
                                                        )

        # Create information labels and buttons
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_info_label()
        self.create_button_panel.create_home_button()
        self.create_button_panel.patchnotes_button()
    
    # Open the settings screen
    def open_settings(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.general_reset_button_press_variable()

        self.settings_canvas = ctk.CTkCanvas(self.root, bg='Grey20', highlightbackground='Black', highlightthickness=5)
        self.settings_canvas.pack(expand=True, fill="both")

        # Update the main canvas attribute
        self.main_canvas = self.settings_canvas

        self.create_button_panel = ClickButtonPanel(self.main_canvas,
                                                        self.logfile,
                                                        self.functions
                                                        )

        self.create_option_button_panel = OptionButtonPanel(
            self.root,
            self.settings_canvas,
            self.logfile
        )

        # Update the frame label panel
        self.framelabel_panel = NameOffFrameLabelPanel( self.main_canvas,
                                                        self.logfile,
                                                        self.game_config,
                                                        self.open_info,
                                                        self.open_settings
                                                        )
        
        # Update the game labels panel
        self.game_labels_panel = GameLabelsPanel(self.main_canvas,
                                                        self.logfile,
                                                        self.game_config
                                                        )

        # Create the settings labels
        self.settings_labels = SettingsOptionButtonLabels(
            self.logfile,
            self.settings_canvas
        )

        self.get_color_from_config()
        self.draw_snake_with_color(self.snake_color)

        # Create settings labels, buttons, and options
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_settings_label()
        self.create_button_panel.create_home_button()
        self.create_option_button_panel.show_options()
        self.settings_labels.create_settings_labels()
        self.settings_labels.create_theme_label()
        self.settings_labels.create_game_size_label()



    def get_color_from_config(self):
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

    def classic_reset_high_score(self):
        if self.classic_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score += 1
        elif self.classic_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score', '0')
            except Exception as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore reset to 0")
            self.classic_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def classic_reset_high_score_time(self):
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            except Exception as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None
    
    def classic_reset_snake_length(self):
        if self.classic_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.classic_button_press_variable_high_score_time += 1
        elif self.classic_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            except Exception as e:
                traceback.print_exc(e)
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.classic_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def classic_reset_button_press_variable(self):
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0

    def endless_reset_high_score(self):
        if self.endless_button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score += 1
        elif self.endless_button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore reset to 0")
            self.endless_button_press_variable_high_score = 0
            self.first_button_press_time = None

    def endless_reset_high_score_time(self):
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_high_score_snake_length(self):
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None
    
    def endless_reset_high_score_special_score(self):
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore special reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None
    
    def endless_reset_high_score_shorten_snake(self):
        if self.endless_button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.endless_button_press_variable_high_score_time += 1
        elif self.endless_button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except Exception as e:
                traceback.print_exc(e)
            try:
                self.config.read(self.config_path)
            except Exception as e:
                traceback.print_exc(e)
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore shorten snake reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_button_press_variable(self):
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0

    def leveling_reset_button_press_variable(self):
        self.leveling_button_press_variable_high_score = 0
        self.leveling_button_press_variable_high_score_time = 0
    
    def multiplayer_reset_button_press_variable(self):
        self.multiplayer_button_press_variable_high_score = 0
        self.multiplayer_button_press_variable_high_score_time = 0

    def general_reset_button_press_variable(self):
        self.button_press_variable = 0

    # Destroy the current canvas
    def destroy_canvas(self, canvas, canvas_name):
        try:
            if canvas is not None:
                self.framelabel_panel.set_create_label_canvas_flag(False)
                canvas.destroy()
                return None
            return canvas
        
        except Exception as e:
            traceback.print_exc(e)
            return canvas

    # Return to the home screen
    def return_home(self):
        try:
            if self.main_canvas == self.classic_snake_canvas:
                self.classic_snake_canvas.delete_game_labels()
            if self.main_canvas == self.endless_snake_canvas:
                self.endless_snake_canvas.delete_game_labels_()
            if self.main_canvas == self.leveling_snake_canvas:
                self.leveling_snake_canvas.delete_game_labels__()
            if self.main_canvas == self.multiplayer_snake_canvas:
              self.multiplayer_snake_canvas.delete_game_labels___()
            time.sleep(0.1)
            # Destroy all game canvases
            self.classic_snake_canvas = self.destroy_canvas(self.classic_snake_canvas, "self.classic_snake_canvas")
            self.endless_snake_canvas = self.destroy_canvas(self.endless_snake_canvas, "self.endless_snake_canvas")
            self.leveling_snake_canvas = self.destroy_canvas(self.leveling_snake_canvas, "self.leveling_snake_canvas")
            self.multiplayer_snake_canvas = self.destroy_canvas(self.multiplayer_snake_canvas, "self.multiplayer_snake_canvas")
            self.info_canvas = self.destroy_canvas(self.info_canvas, "self.info_canvas")
            self.settings_canvas = self.destroy_canvas(self.settings_canvas, "self.settings_canvas")

            self.classic_snake_canvas = self.destroy_canvas(self.main_canvas, "self.main_canvas")
            
            # Show the original main canvas (home screen)
            self.original_main_canvas.pack(expand=True, fill="both")
        except Exception as e:
            traceback.print_exc(e)

    # Confirm quitting the game
    def confirm_quit(self):
        try:
            self.logfile.on_closing()
            self.error_logfile.on_closing()
        except Exception as e:
            traceback.print_exc(e)


# Main function
if __name__ == "__main__":
    root = ctk.CTk()
    app = SnakeGameApp(root, GameConstants.MIN_WIDTH, GameConstants.MIN_HEIGHT)
    root.title("Wims Snake Game")
    root.geometry(f"{GameConstants.MIN_WIDTH}x{GameConstants.MIN_HEIGHT}")
    if SCREEN_SIZE_FULLSCREEN == 'fullscreen':
        root.attributes('-fullscreen', True)
    root.resizable(False, False)

    # Center the window on the screen
    def center_window():
        root.update_idletasks()
        window_width, window_height = root.winfo_width(), root.winfo_height()
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.after(10, center_window)
    root.mainloop()

# *****************************************
# Wims Snake Main File
# *****************************************