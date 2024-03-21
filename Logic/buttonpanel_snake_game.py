# *****************************************
# Wims Snake Button Panel File
# *****************************************


# Importing necessary modules
import customtkinter as ctk, configparser
from os import path

# Importing necessary modules from other folders
from Themes.contrast_updater_snake_game import UpdateContrast
from Themes.theme_updater_snake_game import ThemeUpdater
from Configuration.constants_snake_game import GameConstants, FONT_LIST
from Logic.Screen_size_Changer_snake_game import Screen_size
from Logic.labelpanel_snake_game import SettingsOptionButtonLabels

# Class for creating the button panel
class ClickButtonPanel:
    def __init__(self, parent, logfile):
        # Initializing variables
        self.parent = parent
        self.logfile = logfile
        self.theme_updater = ThemeUpdater(self.logfile)
        self.home_button_ref = None
       
        # Creating a separate canvas for the buttons
        self.button_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightbackground='Black', highlightthickness=5)
        self.button_canvas.pack(side='left', fill='both')

        # Managing the buttons height and width
        self.button_width = GameConstants.BUTTON_WIDTH
        self.button_height = GameConstants.BUTTON_HEIGHT

        # Create a dictionary to store button objects
        self.home_button_ref = None

    # Methods to create specific buttons
    # Each method calls the create_click_button method with specific parameters
    def home_button(self):
        home_button = ctk.CTkButton(self.button_canvas, text="Home", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal",
                                command=self.home_command)
        home_button.grid(in_=self.button_canvas, row=0, column=0, padx=10, pady=10, sticky="w")


    def quit_button(self):
        quit_button = ctk.CTkButton(self.button_canvas, text="Quit", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        quit_button.grid(in_=self.button_canvas, row=20, column=0, padx=10, pady=10, sticky="w")

    def settings_button(self):
        settings_button = ctk.CTkButton(self.button_canvas, text="Settings", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        settings_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w")

    def info_button(self):
        info_button = ctk.CTkButton(self.button_canvas, text="Information", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        info_button.grid(in_=self.button_canvas, row=4, column=0, padx=10, pady=10, sticky="w")

    def patchnotes_button(self):
        patchnotes_button = ctk.CTkButton(self.button_canvas, text="Patchnotes", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        patchnotes_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def classic_snake_button(self):
        classic_snake_button = ctk.CTkButton(self.button_canvas, text="Classic Snake", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        classic_snake_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w")

    def snake_endless_button(self):
        snake_endless_button = ctk.CTkButton(self.button_canvas, text="Endless Snake", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_endless_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def snake_special_button(self):
        snake_special_button = ctk.CTkButton(self.button_canvas, text="Classic Snake", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_special_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w")

    # in-game buttons
    def snake_color_button(self):
        snake_color_button = ctk.CTkButton(self.button_canvas, text="Snake Color", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_color_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w")

    def snake_outline_button(self):
        snake_outline_button = ctk.CTkButton(self.button_canvas, text="Snake Outline", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_outline_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def snake_length_button(self):
        snake_length_button = ctk.CTkButton(self.button_canvas, text="Snake Length", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_length_button.grid(in_=self.button_canvas, row=1, column=0, padx=10, pady=10, sticky="w")

    def reset_high_score_button(self):
        reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Score\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        reset_high_score_button.grid(in_=self.button_canvas, row=2, column=0, padx=10, pady=10, sticky="w")

    def reset_high_score_time_button(self):
        reset_high_score_button = ctk.CTkButton(self.button_canvas, text="Reset Time\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        reset_high_score_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w")

    def reset_high_score_snake_length(self):
        reset_high_score_snake_length_button = ctk.CTkButton(self.button_canvas, text="Reset snakelength\n Highscore", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        reset_high_score_snake_length_button.grid(in_=self.button_canvas, row=3, column=0, padx=10, pady=10, sticky="w")

    # only in the special game mode
    def game_size_button(self):
        game_size_button = ctk.CTkButton(self.button_canvas, text="Game Size", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        game_size_button.grid(in_=self.button_canvas, row=4, column=0, padx=10, pady=10, sticky="w")

    # only in the special game mode
    def snake_speed_button(self):
        snake_speed_button = ctk.CTkButton(self.button_canvas, text="Snake Speed", font=FONT_LIST[11],
                                width=self.button_width, height=self.button_height, state="normal")
        snake_speed_button.grid(in_=self.button_canvas, row=5, column=0, padx=10, pady=10, sticky="w")

    def set_home_button_state(self, state):
        if self.home_button_ref:
            self.home_button_ref.configure(state=state)

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
        self.config.read(self.config_path)

        # Setting up screen size changer
        self.screen_size_config = self.config.get('Settings', 'screen_size', fallback='Default')
        self.screen_size_var = ctk.StringVar()  # Variable to track the selected value
        self.screen_size_var.set(self.screen_size_config)  # Set the default value
        self.screen_size_changer = Screen_size(root, self.logfile, self.screen_size_var, self.config, self.screen_size_config)

        # Setting up theme changer
        self.theme_config = self.config.get('Settings', 'theme', fallback='Default')
        self.theme_var = ctk.StringVar()  # Variable to track the selected value
        self.theme_var.set(self.theme_config)
        self.theme_changer = ThemeUpdater(self.logfile)

        # Setting up contrast updater
        self.contrast_config = self.config.get('Settings', 'contrast', fallback='Default')
        self.contrast_mode = ctk.StringVar()
        self.contrast_mode.set(self.contrast_config)
        self.contrast_updater = UpdateContrast(self.logfile)

    # Method to update the config.ini file
    def updating_config_ini(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

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
        option_button.set(config)

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

        # Handle exceptions appropriately
        except Exception as e:
            print("Error:", e)

class DisabelingButtons:
    def __init__(self, button_panel):
        self.button_panel = button_panel
    
    def disable_buttons(self):
        self.button_panel.set_home_button_state("disabled")
        print("Buttons disabled")
    
    def enable_buttons(self):
        self.button_panel.set_home_button_state("normal")
        print("Buttons enabled")

class ButtonCommands:
    def __init__(self, logfile, functions):
        self.functions = functions
        self.logfile = logfile

    def home_command(self):
        self.functions['return_home']()

    def quit_command(self):
        self.functions['confirm_quit']()

    def settings_command(self):
        self.functions['open_settings']()

    def info_command(self):
        self.functions['open_info']()

    def patchnotes_command(self):
        pass

    def classic_snake_command(self):
        self.functions['classic_snake']()

    def snake_endless_command(self):
        self.functions['snake_endless']()

    def snake_special_command(self):
        self.functions['snake_special']()

    def snake_color_command(self):
        pass

    def snake_outline_command(self):
        pass

    def snake_length_command(self):
        self.functions['reset_snake_length']()

    def reset_high_score_command(self):
        self.functions['reset_high_score']()

    def reset_high_score_time_command(self):
        self.functions['reset_high_score_time']()

    def reset_high_score_snake_length_command(self):
        pass

    def game_size_command(self):
        pass

    def snake_speed_command(self):
        pass

    def destroy_canvas(self):
        self.functions['destroy_canvas']()

# *****************************************
# Wims Snake Button Panel File
# *****************************************