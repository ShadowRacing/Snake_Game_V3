# *****************************************
# Wims Snake Main File
# *****************************************

# Import all the necessary libraries
import customtkinter as ctk
import configparser, traceback, time
from os import path

# Importing thhe necessary modules from other folders
from Logs.gamelogger_snake_game import LogFile , ErrorLogFile
from Configuration.constants_snake_game import GameConstants
from Configuration.gameconfig_snake_game import GameConfig
from Logic.buttonpanel_snake_game import ClickButtonPanel, OptionButtonPanel, ButtonCommands
from Logic.labelpanel_snake_game import NameOffFrameLabelPanel, SettingsOptionButtonLabels, GameLabelsPanel
from Logic.snake_logic_snake_game import Snake
from Logic.food_logic_snake_game import ClassicFood, SpecialFood, EndlessFood
from Logic.config_ini_Initials import ConfigIni
from Games.snake_classic_game import Snake_Classic_Game
from Games.snake_endless_game import Snake_endless
from Games.snake_special_game import Snake_Special
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
        # self.previous_width = root.winfo_width()
        # self.previous_height = root.winfo_height()
        self.theme_updater.set_initial_theme()

        # Read the config file and load it
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.config_path)
        except:
            traceback.print_exc()
        
        self.apply_theme()
        self.update_contrast.apply_contrast(selected_value=None)

        # Write the changes to the config file
        try:
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()
        
        # Button press variables
        self.button_press_variable = 0
        self.classic_button_press_variable_high_score = 0
        self.classic_button_press_variable_high_score_time = 0
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0
        self.button_press_time_limit = float(self.config.get('Settings', 'button_press_time_limit', fallback=0.5))

        # Creating the main canvas for the app
        self.main_canvas = ctk.CTkCanvas(root, highlightbackground='Black', highlightthickness=5, bg='Grey20')
        self.main_canvas.pack(expand=True, fill="both")
        self.original_main_canvas = self.main_canvas

        # All the game canvases
        self.classic_snake_canvas = None
        self.endless_snake_canvas = None
        self.special_snake_canvas = None
        self.info_canvas = None
        self.settings_canvas = None

        # The current game canvas
        #self.current_classic_snake_canvas = None

        # Create the snake and food objects
        self.snake = Snake(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
        self.classicfood = ClassicFood(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
        self.special_food = SpecialFood(self.logfile, canvas=self.main_canvas, game_config=self.game_config)
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
            'snake_special': self.snake_special,
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
        except:
            traceback.print_exc()
    
    def create_home_screen(self):
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_main_menu_label()
        self.create_button_panel.classic_snake_button()
        self.create_button_panel.snake_endless_button()
        self.create_button_panel.snake_special_button()
        self.create_button_panel.info_button()
        self.create_button_panel.settings_button()
        self.create_button_panel.quit_button()
        self.game_labels_panel.classic_delete_labels()
        self.classic_reset_button_press_variable()
        self.endless_reset_button_press_variable()
    
    def classic_snake(self):
        # Hide the main canvas
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.classic_reset_button_press_variable()

        # Create a new canvas for the classic snake game
        self.game_config.set_configuration("classic_snake")
        self.classic_snake_canvas = Snake_Classic_Game(self.root, 
                                                        self.game_config, 
                                                        self.logfile,
                                                        self.functions,
                                                        self.create_button_panel
                                                        )
        self.classic_snake_canvas.pack(expand=True, fill="both")

        # Update the main canvas attribute
        self.main_canvas = self.classic_snake_canvas

        #Update the button panel
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

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        self.create_button_panel.classic_reset_high_score_button()
        self.create_button_panel.classic_reset_high_score_time_button()
        self.create_button_panel.classic_reset_high_score_snake_length()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_classic_snake_label()
    
    # Start the endless snake game
    def snake_endless(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.classic_reset_button_press_variable()

        self.game_config.set_configuration("snake_endless")
        self.endless_snake_canvas = Snake_endless(self.root, 
                                                        self.game_config, 
                                                        self.logfile,
                                                        self.functions,
                                                        self.create_button_panel
                                                        )
        self.endless_snake_canvas.pack(expand=True, fill="both")

        # Update the main canvas attribute
        self.main_canvas = self.endless_snake_canvas

        #Update the button panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas,
                                                        self.logfile, 
                                                        self.functions
                                                        )

        # Update the frame label panel
        self.framelabel_panel = NameOffFrameLabelPanel(self.main_canvas,
                                                        self.logfile, 
                                                        self.game_config, 
                                                        self.open_info, 
                                                        self.open_settings
                                                        )
        
        # Update the game labels panel
        self.game_labels_panel_2 = GameLabelsPanel(self.main_canvas, 
                                                        self.logfile, 
                                                        self.game_config
                                                        )

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        self.create_button_panel.endless_reset_high_score_button()
        self.create_button_panel.endless_reset_high_score_time_button()
        self.create_button_panel.endless_reset_high_score_snake_length()
        self.create_button_panel.endless_reset_high_score_special_score_button()
        self.create_button_panel.endless_reset_high_score_shorten_snake_button()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_endless_snake_label()
    
    # Start the special snake game
    def snake_special(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.endless_reset_button_press_variable()


        self.game_config.set_configuration("snake_special")
        self.special_snake_canvas = Snake_Special(self.root, 
                                                  self.game_config
                                                  )
        self.special_snake_canvas.pack(expand=True, fill="both")

        # Update the main canvas attribute
        self.main_canvas = self.special_snake_canvas

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

        # Pack buttons and labels
        self.create_button_panel.create_home_button()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_special_snake_label()
    
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

        # Create settings labels, buttons, and options
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_settings_label()
        self.create_button_panel.create_home_button()
        self.create_option_button_panel.show_options()
        self.settings_labels.create_screen_options_label()
        self.settings_labels.create_theme_options_label()
        self.settings_labels.create_contrast_options_label()
        self.settings_labels.create_theme_label()
        self.settings_labels.create_high_score_label()
        self.settings_labels.snake_color_options_label()

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
            except:
                traceback.print_exc()
            try:
                self.config.set('Classic_Snake_Values', 'high_score', '0')
            except:
                traceback.print_exc()
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            except:
                traceback.print_exc()
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except: 
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except :
                traceback.print_exc()
            try:
                self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            except:
                traceback.print_exc()
            try:
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except: 
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Endless_Snake_Values', 'high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Endless_Snake_Values', 'high_score_time', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Endless_Snake_Values', 'special_score_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
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
            except:
                traceback.print_exc()
            try:
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', '0')
                with open('config.ini', 'w') as configfile:
                    self.config.write(configfile)
            except:
                traceback.print_exc()
            try:
                self.config.read(self.config_path)
            except:
                traceback.print_exc()
            self.endless_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore shorten snake reset to 0")
            self.endless_button_press_variable_high_score_time = 0
            self.first_button_press_time = None

    def endless_reset_button_press_variable(self):
        self.endless_button_press_variable_high_score = 0
        self.endless_button_press_variable_high_score_time = 0

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
        
        except:
            traceback.print_exc()
            return canvas

    # Return to the home screen
    def return_home(self):
        try:
            if self.main_canvas == self.classic_snake_canvas:
                self.classic_snake_canvas.delete_game_labels()
            if self.main_canvas == self.endless_snake_canvas:
                self.endless_snake_canvas.delete_game_labels_()
            time.sleep(0.1)
            # Destroy all game canvases
            self.classic_snake_canvas = self.destroy_canvas(self.classic_snake_canvas, "self.classic_snake_canvas")
            self.endless_snake_canvas = self.destroy_canvas(self.endless_snake_canvas, "self.endless_snake_canvas")
            self.special_snake_canvas = self.destroy_canvas(self.special_snake_canvas, "self.special_snake_canvas")
            self.info_canvas = self.destroy_canvas(self.info_canvas, "self.info_canvas")
            self.settings_canvas = self.destroy_canvas(self.settings_canvas, "self.settings_canvas")
            
            # Show the original main canvas (home screen)
            self.original_main_canvas.pack(expand=True, fill="both")
        except:
            traceback.print_exc()

    # Confirm quitting the game
    def confirm_quit(self):
        try:
            self.logfile.on_closing()
            self.error_logfile.on_closing()
        except:
            traceback.print_exc()

# Main function
if __name__ == "__main__":
    root = ctk.CTk()
    app = SnakeGameApp(root, GameConstants.MIN_WIDTH, GameConstants.MIN_HEIGHT)
    root.title("Wims Snake Game")
    root.geometry(f"{GameConstants.MIN_WIDTH}x{GameConstants.MIN_HEIGHT}")
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