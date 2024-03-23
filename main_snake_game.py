# *****************************************
# Wims Snake Main File
# *****************************************

# Import all the necessary libraries
import customtkinter as ctk
import configparser, traceback, time
from os import path

# Importing thhe necessary modules from other folders
from Logs.gamelogger_snake_game import LogFile
from Configuration.constants_snake_game import GameConstants
from Configuration.gameconfig_snake_game import GameConfig
from Logic.buttonpanel_snake_game import ClickButtonPanel, OptionButtonPanel, ButtonCommands, DisabelingButtons
from Logic.labelpanel_snake_game import NameOffFrameLabelPanel, SettingsOptionButtonLabels, GameLabelsPanel
from Logic.snake_logic_snake_game import Snake
from Logic.food_logic_snake_game import ClassicFood, SpecialFood, EndlessFood
from Games.snake_classic_game import Snake_Classic_Game
from Games.snake_endless_game import Snake_endless
from Games.snake_special_game import Snake_Special
from Themes.theme_updater_snake_game import ThemeUpdater
from Themes.contrast_updater_snake_game import UpdateContrast


# Define the main application class
class SnakeGameApp:
    def __init__ (self, root, game_width, game_height):
        #Initialize the game app values
        self.root = root
        self.logfile = LogFile(root)
        self.logfile.log_game_event("Started the GameApp Class")
        self.game_config = GameConfig(logfile=self.logfile, game_mode = "initial_config")
        self.update_contrast = UpdateContrast(self.logfile)
        self.theme_updater = ThemeUpdater(self.logfile)
        self.game_width = game_width
        self.game_height = game_height
        # self.previous_width = root.winfo_width()
        # self.previous_height = root.winfo_height()
        self.theme_updater.set_initial_theme()

        # Read the config file and load it
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.apply_theme()
        self.update_contrast.apply_contrast(selected_value=None)

        # Write the changes to the config file
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
        
        # Button press variables
        self.button_press_variable_high_score = 0
        self.button_press_variable_high_score_time = 0
        self.button_press_time_limit = float(self.config.get('Settings', 'button_press_time_limit', fallback=0.5))

        # Creating the main canvas for the app
        self.main_canvas = ctk.CTkCanvas(root, highlightbackground='Black', highlightthickness=5)
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
            'reset_button_press_variable': self.reset_button_press_variable,
            'reset_high_score_snake_length': self.reset_snake_length,
            'reset_high_score_time': self.reset_high_score_time,
            'reset_high_score': self.reset_high_score,
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

        self.button_panel = DisabelingButtons(self.create_button_panel)

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
        ctk.set_default_color_theme(theme_path)
    
    def create_home_screen(self):
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_main_menu_label()
        self.create_button_panel.classic_snake_button()
        self.create_button_panel.snake_endless_button()
        self.create_button_panel.snake_special_button()
        self.create_button_panel.info_button()
        self.create_button_panel.settings_button()
        self.create_button_panel.quit_button()
        self.game_labels_panel.delete_labels()
        self.reset_button_press_variable()
    
    def classic_snake(self):
        # Hide the main canvas
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.reset_button_press_variable()

        # Create a new canvas for the classic snake game
        self.game_config.set_configuration("classic_snake")
        self.classic_snake_canvas = Snake_Classic_Game(self.root, 
                                                        self.game_config, 
                                                        self.logfile,
                                                        self.functions,
                                                        self.button_panel
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
        self.create_button_panel.snake_color_button()
        self.create_button_panel.snake_outline_button()
        self.create_button_panel.reset_high_score_button()
        self.create_button_panel.reset_high_score_time_button()
        self.create_button_panel.reset_high_score_snake_length()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_classic_snake_label()
    
    # Start the endless snake game
    def snake_endless(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.reset_button_press_variable()

        self.game_config.set_configuration("snake_endless")
        self.endless_snake_canvas = Snake_endless(self.root, self.game_config)
        self.endless_snake_canvas.pack(expand=True, fill="both")

        # Update the main canvas attribute
        self.main_canvas = self.endless_snake_canvas

        # Update the button panel
        self.create_button_panel = ClickButtonPanel(self.main_canvas,
                                                        self.logfile, 
                                                        self.functions
                                                        )
        
        self.disabeling_buttons = DisabelingButtons(self.button_panel)

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
        self.create_button_panel.snake_color_button()
        self.create_button_panel.snake_outline_button()
        self.create_button_panel.snake_length_button()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_endless_snake_label()
    
    # Start the special snake game
    def snake_special(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.reset_button_press_variable()


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
        self.create_button_panel.snake_color_button()
        self.create_button_panel.snake_outline_button()
        self.create_button_panel.game_size_button()
        self.create_button_panel.snake_length_button()
        self.create_button_panel.snake_speed_button()
        self.create_button_panel.quit_button()
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_special_snake_label()
    
    # Open the information screen
    def open_info(self):
        self.original_main_canvas.pack_forget()

        # Reset the button press variable
        self.reset_button_press_variable()

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
        self.reset_button_press_variable()

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
        
        # Create settings labels, buttons, and options
        self.framelabel_panel.set_create_label_canvas_flag(True)
        self.framelabel_panel.create_settings_label()
        self.create_button_panel.create_home_button()
        self.create_option_button_panel.show_options()
        self.settings_labels.create_screen_options_label()
        self.settings_labels.create_theme_options_label()
        self.settings_labels.create_contrast_options_label()
        self.settings_labels.create_theme_label()
    
    def reset_high_score(self):
        if self.button_press_variable_high_score == 0:
            self.first_button_press_time = time.time()
            self.button_press_variable_high_score += 1
        elif self.button_press_variable_high_score == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            self.config.read(self.config_path)
            self.config.set('Classic_Snake_Values', 'high_score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            self.config.read(self.config_path)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore reset to 0")
            self.button_press_variable_high_score = 0
            self.first_button_press_time = None

    def reset_high_score_time(self):
        if self.button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.button_press_variable_high_score_time += 1
        elif self.button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            self.config.read(self.config_path)
            self.config.set('Classic_Snake_Values', 'high_score_time', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            self.config.read(self.config_path)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.button_press_variable_high_score_time = 0
            self.first_button_press_time = None
    
    def reset_snake_length(self):
        if self.button_press_variable_high_score_time == 0:
            self.first_button_press_time = time.time()
            self.button_press_variable_high_score_time += 1
        elif self.button_press_variable_high_score_time == 1 and time.time() - self.first_button_press_time <= self.button_press_time_limit:
            self.config.read(self.config_path)
            self.config.set('Classic_Snake_Values', 'snake_length_high_score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            self.config.read(self.config_path)
            self.classic_snake_canvas.update_high_score_labels_()
            self.logfile.log_game_event("Highscore time reset to 0")
            self.button_press_variable_high_score_time = 0
            self.first_button_press_time = None
    
    def reset_button_press_variable(self):
        self.button_press_variable_high_score = 0
        self.button_press_variable_high_score_time = 0

    # Destroy the current canvas
    def destroy_canvas(self, canvas, canvas_name):
        try:
            if canvas is not None:
                self.framelabel_panel.set_create_label_canvas_flag(False)
                canvas.destroy()
                return None
            return canvas
        
        except Exception:
            self.logfile.log_game_event(f"Error in destroy_canvas: {canvas_name}")
            traceback.print_exc()
            return canvas

    # Return to the home screen
    def return_home(self):
        if self.main_canvas == self.classic_snake_canvas:
            self.classic_snake_canvas.delete_game_labels()
        time.sleep(0.1)
        # Destroy all game canvases
        self.classic_snake_canvas = self.destroy_canvas(self.classic_snake_canvas, "self.classic_snake_canvas")
        self.endless_snake_canvas = self.destroy_canvas(self.endless_snake_canvas, "self.endless_snake_canvas")
        self.special_snake_canvas = self.destroy_canvas(self.special_snake_canvas, "self.special_snake_canvas")
        self.info_canvas = self.destroy_canvas(self.info_canvas, "self.info_canvas")
        self.settings_canvas = self.destroy_canvas(self.settings_canvas, "self.settings_canvas")
        
        # Show the original main canvas (home screen)
        self.original_main_canvas.pack(expand=True, fill="both")

    # Confirm quitting the game
    def confirm_quit(self):
        self.logfile.on_closing()


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