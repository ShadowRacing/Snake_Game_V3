# *****************************************
# Wims Snake Button Panel File
# *****************************************


# Importing necessary modules
import customtkinter as ctk, configparser, time, traceback
from os import path

# Importing necessary modules from other folders
from Themes.contrast_updater_snake_game import UpdateContrast
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST, COLORS_DICT
from Logic.Screen_size_Changer_snake_game import Screen_size
from Logic.labelpanel_snake_game import SettingsOptionButtonLabels

class ButtonCommands:
    def __init__(self, logfile, functions):
        self.functions = functions
        self.logfile = logfile

    def home_command(self):
        if 'return_home' in self.functions:
            self.functions['return_home']()
        else:
            self.logfile.log_game_event("No function assigned to 'home'")

    def quit_command(self):
        if 'confirm_quit' in self.functions:
            self.functions['confirm_quit']()
        else:
            self.logfile.log_game_event("No function assigned to 'confirm_quit'")

    def settings_command(self):
        if 'open_settings' in self.functions:
            self.functions['open_settings']()
        else:
            self.logfile.log_game_event("No function assigned to 'open_settings'")

    def info_command(self):
        if 'open_info' in self.functions:
            self.functions['open_info']()
        else:
            self.logfile.log_game_event("No function assigned to 'info'")

    def patchnotes_command(self):
        if 'patchnotes' in self.functions:
            self.functions['patchnotes']()
        else:
            self.logfile.log_game_event("No function assigned to 'patchnotes'")

    def classic_snake_command(self):
        if 'classic_snake' in self.functions:
            self.functions['classic_snake']()
        else:
            self.logfile.log_game_event("No function assigned to 'classic_snake'")

    def snake_endless_command(self):
        if 'snake_endless' in self.functions:
            self.functions['snake_endless']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_endless'")

    def snake_leveling_command(self):
        if 'snake_leveling' in self.functions:
            self.functions['snake_leveling']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_leveling'")
    
    def multiplayer_snake_command(self):
        if 'snake_multiplayer' in self.functions:
            self.functions['snake_multiplayer']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_multiplayer'")

    def snake_color_command(self):
        if 'snake_color' in self.functions:
            self.functions['snake_color']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_color'")

    def snake_outline_command(self):
        if 'snake_outline' in self.functions:
            self.functions['snake_outline']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_outline'")

    def snake_length_command(self):
        if 'snake_length' in self.functions:
            self.functions['snake_length']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_length'")

    def classic_reset_high_score_command(self):
        if 'classic_reset_high_score' in self.functions:
            self.functions['classic_reset_high_score']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score'")

    def classic_reset_high_score_time_command(self):
        if 'classic_reset_high_score_time' in self.functions:
            self.functions['classic_reset_high_score_time']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score_time'")

    def classic_reset_high_score_snake_length_command(self):
        if 'classic_reset_high_score_snake_length' in self.functions:
            self.functions['classic_reset_high_score_snake_length']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score_snake_length'")

    def endless_reset_high_score_command(self):
        if 'endless_reset_high_score' in self.functions:
            self.functions['endless_reset_high_score']()
        else:
            self.logfile.log_game_event("No function assigned to 'endless_reset_high_score'")
    
    def endless_reset_high_score_time_command(self):
        if 'endless_reset_high_score_time' in self.functions:
            self.functions['endless_reset_high_score_time']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score_time'")
    
    def endless_reset_high_score_snake_length_command(self):
        if 'endless_reset_high_score_snake_length' in self.functions:
            self.functions['endless_reset_high_score_snake_length']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score_snake_length'")

    def endless_reset_high_special_score_command(self):
        if 'endless_reset_high_score_special_score' in self.functions:
            self.functions['endless_reset_high_score_special_score']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_special_score'")
    
    def endless_reset_high_score_shorten_snake_command(self):
        if 'endless_reset_high_score_shorten_snake' in self.functions:
            self.functions['endless_reset_high_score_shorten_snake']()
        else:
            self.logfile.log_game_event("No function assigned to 'reset_high_score_shorten_snake'")

    def game_size_command(self):
        if 'game_size' in self.functions:
            self.functions['game_size']()
        else:
            self.logfile.log_game_event("No function assigned to 'game_size'")

    def snake_speed_command(self):
        if 'snake_speed' in self.functions:
            self.functions['snake_speed']()
        else:
            self.logfile.log_game_event("No function assigned to 'snake_speed'")

    def destroy_canvas(self):
        if 'destroy_canvas' in self.functions:
            self.functions['destroy_canvas']()
        else:
            self.logfile.log_game_event("No function assigned to 'destroy_canvas'")

# Class for creating the button panel
class ClickButtonPanel:
    def __init__(self, parent, logfile, functions, home_button=None):
        # Initializing variables
        self.parent = parent
        self.logfile = logfile
        self.functions = functions
        self.home_button = home_button
        self.theme_updater = ThemeUpdater(self.logfile)
       
       
        # Managing the buttons height and width
        self.button_width = GameConstants.BUTTON_WIDTH
        self.button_height = GameConstants.BUTTON_HEIGHT

        self.button_commands = ButtonCommands(self.logfile, self.functions)
        
        # Creating a separate canvas for the buttons
        self.button_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightbackground='Black', highlightthickness=5)
        self.button_canvas.pack(side='left', fill='both')

        # Creating counter for home button clicks
        self.home_button_clicks = 0

    # Methods to create specific buttons    
    # Each method calls the create_click_button method with specific parameters
    def create_home_button(self):
        self.home_button = ctk.CTkButton(self.button_canvas, text="Home", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.home_button_command)
        self.home_button.grid(in_=self.button_canvas, row=0, column=0, padx=10, pady=10, sticky="w")

    def home_button_command(self):
        # If it's the first click, record the current time
        if self.home_button_clicks == 0:
            self.first_click_time = time.time()
        # If it's the second click, check if it's within the time limit
        elif self.home_button_clicks == 1:
            if time.time() - self.first_click_time > 2:  # 2 seconds
                # If it's not within the time limit, reset the counter
                self.home_button_clicks = 0
                return
        self.home_button_clicks += 1
        if self.home_button_clicks >= 2:
            self.button_commands.home_command()
            
    def quit_button(self):
        quit_button = ctk.CTkButton(self.button_canvas, text="Quit", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.quit_command)
        quit_button.grid(in_=self.button_canvas, row=20, column=0, padx=10, pady=10, sticky="w")

    def settings_button(self):
        settings_button = ctk.CTkButton(self.button_canvas, text="Settings", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.settings_command)
        settings_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w")

    def info_button(self):
        info_button = ctk.CTkButton(self.button_canvas, text="Information", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.info_command)
        info_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w")

    def patchnotes_button(self):
        patchnotes_button = ctk.CTkButton(self.button_canvas, text="Patchnotes", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="disabled", #Should ne normal
                                command=self.button_commands.patchnotes_command)
        patchnotes_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w")

    def classic_snake_button(self):
        classic_snake_button = ctk.CTkButton(self.button_canvas, text="Classic", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.classic_snake_command)
        classic_snake_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w")

    def snake_endless_button(self):
        snake_endless_button = ctk.CTkButton(self.button_canvas, text="Endless", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_endless_command)
        snake_endless_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def snake_leveling_button(self):
        snake_leveling_button = ctk.CTkButton(self.button_canvas, text="Leveling", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",#Should ne normal
                                command=self.button_commands.snake_leveling_command)
        snake_leveling_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w")

    def multiplayer_snake_button(self):
        multiplayer_snake_button = ctk.CTkButton(self.button_canvas, text="Multiplayer", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.multiplayer_snake_command)
        multiplayer_snake_button.grid(in_=self.button_canvas, row=4, column=0, padx=10, pady=10, sticky="w")

    def snake_color_button(self):
        snake_color_button = ctk.CTkButton(self.button_canvas, text="Snake Color", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_color_command)
        snake_color_button.grid(in_=self.button_canvas, row=6, column=0, padx=10, pady=10, sticky="w")

    def snake_outline_button(self):
        snake_outline_button = ctk.CTkButton(self.button_canvas, text="Snake Outline", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_outline_command)
        snake_outline_button.grid(in_=self.button_canvas, row=7, column=0, padx=10, pady=10, sticky="w")

    def classic_snake_length_button(self):
        classic_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_length_command)
        classic_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w")

    def classic_reset_high_score_button(self):
        classic_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.classic_reset_high_score_command)
        classic_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w")

    def classic_reset_high_score_time_button(self):
        classic_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.classic_reset_high_score_time_command)
        classic_reset_high_score_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w")

    def classic_reset_high_score_snake_length(self):
        classic_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.classic_reset_high_score_snake_length_command)
        classic_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w")

    def endless_snake_length_button(self):
        endless_snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_length_command)
        endless_snake_length_button.grid(in_=self.button_canvas, row=8, column=0, padx=10, pady=10, sticky="w")

    def endless_reset_high_score_button(self):
        endless_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_score_command)
        endless_reset_high_score_button.grid(in_=self.button_canvas, row=10, column=0, padx=10, pady=10, sticky="w")

    def endless_reset_high_score_time_button(self):
        endless_reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_score_time_command)
        endless_reset_high_score_button.grid(in_=self.button_canvas, row=11, column=0, padx=10, pady=10, sticky="w")

    def endless_reset_high_score_snake_length(self):
        endless_reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset length\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_score_snake_length_command)
        endless_reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=12, column=0, padx=10, pady=10, sticky="w")

    def endless_reset_high_score_special_score_button(self):
        endless_reset_high_score_special_score_button = ctk.CTkButton(self.button_canvas, text="Reset Special\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_special_score_command)
        endless_reset_high_score_special_score_button.grid(in_=self.button_canvas, row=13, column=0, padx=10, pady=10, sticky="w")

    def endless_reset_high_score_shorten_snake_button(self):
        endless_reset_high_score_shorten_snake_button = ctk.CTkButton(self.button_canvas, text="Reset Shorten\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.endless_reset_high_score_shorten_snake_command)
        endless_reset_high_score_shorten_snake_button.grid(in_=self.button_canvas, row=14, column=0, padx=10, pady=10, sticky="w")

    # only in the special game mode
    def game_size_button(self):
        game_size_button = ctk.CTkButton(self.button_canvas, text="Game Size", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.game_size_command)
        game_size_button.grid(in_=self.button_canvas, row=15, column=0, padx=10, pady=10, sticky="w")

    # only in the special game mode
    def snake_speed_button(self):
        snake_speed_button = ctk.CTkButton(self.button_canvas, text="Snake Speed", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.button_commands.snake_speed_command)
        snake_speed_button.grid(in_=self.button_canvas, row=9, column=0, padx=10, pady=10, sticky="w")

# Class for creating the option button panel
class OptionButtonPanel:
    def __init__(self, root, settings_canvas, logfile):
        # Initializing variables
        self.settings_canvas = settings_canvas
        self.logfile = logfile
        self.label_panel = SettingsOptionButtonLabels(logfile, self.settings_canvas)
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.RawConfigParser()


        try:
            self.config.read(self.config_path)
        except:
            traceback.print_exc()

        # Setting up screen size changer
        try:
            self.screen_size_config = self.config.get('Settings', 'screen_size', fallback='Default')
            self.screen_size_var = ctk.StringVar()  # Variable to track the selected value
            self.screen_size_var.set(self.screen_size_config)  # Set the default value
            self.screen_size_changer = Screen_size(root, self.logfile, self.screen_size_var, self.config, self.screen_size_config)
        except:
            traceback.print_exc()

        # Setting up theme changer
        try:
            self.theme_config = self.config.get('Settings', 'theme', fallback='Default')
            self.theme_var = ctk.StringVar()  # Variable to track the selected value
            self.theme_var.set(self.theme_config)
            self.theme_changer = ThemeUpdater(self.logfile)
        except:
            traceback.print_exc()

        # Setting up contrast updater
        try:
            self.contrast_config = self.config.get('Settings', 'contrast', fallback='Default')
            self.contrast_mode = ctk.StringVar()
            self.contrast_mode.set(self.contrast_config)
            self.contrast_updater = UpdateContrast(self.logfile)
        except:
            traceback.print_exc()

        try: 
            self.high_score_label_showing_config = self.config.get('Settings', 'label_needed_high_score', fallback='Default')
            self.high_score_var = ctk.StringVar()
            self.high_score_var.set(self.high_score_label_showing_config)
        except:
            traceback.print_exc()

    # Method to update the config.ini file
    def updating_config_ini(self):
        try:
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
        except:
            traceback.print_exc()

    # Callback methods for handling changes in screen size, theme, and contrast
    def screen_size_callback(self, selected_value):
        # Handle screen size change
        #self.config.set('Settings', 'screen_size', selected_value)
        self.updating_config_ini()
        self.screen_size_changer.change_screen_size(selected_value)

    def theme_callback(self, selected_value):
        # Handle theme change
        #self.config.set('Settings', 'theme', selected_value)
        self.updating_config_ini()
        self.theme_changer.update_config_theme(selected_value)
        self.label_panel.create_theme_label()

    def contrast_callback(self, selected_value):
        # Handle contrast change
        #self.config.set('Settings', 'contrast', selected_value)
        self.updating_config_ini()
        self.contrast_updater.apply_contrast(selected_value)

    def snake_color_callback(self, selected_value):
        # Handle snake color change
        try:
            self.config.set('Settings', 'snake_color', selected_value)
        except:
            traceback.print_exc()
        self.updating_config_ini()
        self.snake_color_rgb = COLORS_DICT.get(selected_value)
        
    def high_score_label_showing_callback(self, selected_value):
        try:
            self.config.set('Settings', 'label_needed_high_score', selected_value)
        except:
            traceback.print_exc()
        self.updating_config_ini()

    def snake_speed_callback(self, selected_value):
        try:
            self.config.set('Settings', 'snake_speed', selected_value)
        except:
            traceback.print_exc()
        self.updating_config_ini()
    
    def game_size_callback(self, selected_value):
        try:
            self.config.set('Settings', 'game_size', selected_value)
            print("Game size changed")
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
            self.label_panel.create_game_size_label()
            print("Game size changed2")
        except:
            traceback.print_exc()
        

    # Method to create an option button
    def create_option_button(self, command, values, config, x, y):
        option_button = ctk.CTkOptionMenu(self.settings_canvas,
                                          width=GameConstants.BUTTON_WIDTH,
                                          height=GameConstants.BUTTON_HEIGHT,
                                          font=FONT_LIST[11],
                                          corner_radius=8,
                                          values=values,
                                          command=command)
        option_button.place(x=x, y=y)
        try:
            option_button.set(config)
        except:
            traceback.print_exc()

    # Method to show the options
    def show_options(self):
        try:
            # Creating the option buttons for screen size, theme, and contrast
            # Screen Size Option
            self.screen_size_config = self.config.get('Settings', 'screen_size', fallback='Default')
            self.create_option_button(self.screen_size_callback,
                                      ["Fullscreen", "Default","600x800", "1600x900", "1800x1080",
                                       "1800x1200", "1920x1080", "1920x1200", "2560x1440"],
                                      self.screen_size_config, 200, 50)

            # Theme Option
            self.theme_config = self.config.get('Settings', 'theme', fallback='Default')
            self.create_option_button(self.theme_callback,
                                      ["Default", "Black", "Blue", "Dark-Blue", "Green", "Grey", "Orange",
                                       "Pink", "Purple", "Red", "White", "Yellow"],
                                      self.theme_config, 400, 50)

            # Contrast Option
            self.contrast_config = self.config.get('Settings', 'contrast', fallback='Dark')
            self.create_option_button(self.contrast_callback, ["Default", "Dark", "Light", "System"],
                                      self.contrast_config, 600, 50)

            # Creating the option buttons for snake color
            self.snake_color_config = self.config.get('Settings', 'snake_color', fallback='Green')
            self.create_option_button(self.snake_color_callback,
                                      ["Default", "Red", "Blue", "Green", "Yellow", "Black", "White", "Grey", "Olive", "Purple", "Orange", "Silver", "Gold", "OrangeRed", "MidnightPurple"],
                                      self.snake_color_config, 800, 50)
            
            self.high_score_label_showing_config = self.config.get('Settings', 'label_needed_high_score', fallback='False')
            self.create_option_button(self.high_score_label_showing_callback,
                                      ["Default", "True", "False"],
                                      self.high_score_label_showing_config, 1000, 50)

            self.snake_speed_config = self.config.get('Settings', 'snake_speed', fallback='20')
            self.create_option_button(self.snake_speed_callback,
                                      ["2","4","6","8","10", "20", "30", "40", "50", "60", "70", "80", "90", "100"],
                                      self.snake_speed_config, 200, 200)

            self.game_size_config = self.config.get('Settings', 'game_size', fallback='Default')
            self.create_option_button(self.game_size_callback,
                                      ["100x100", "200x200", "300x300", "400x400", "500x500", 
                                       "600x600", "700x700", "800x800","900x900", "1000x1000"],
                                      self.game_size_config, 400, 200)
          

        # Handle exceptions appropriately
        except:
            traceback.print_exc()

# *****************************************
# Wims Snake Button Panel File
# *****************************************