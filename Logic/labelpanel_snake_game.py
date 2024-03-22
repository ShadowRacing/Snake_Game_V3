import customtkinter as ctk
import configparser, time
from os import path
from Configuration.constants_snake_game import FONT_LIST

class NameOffFrameLabelPanel:
    def __init__(self, parent, logfile, info_callback, settings_callback, game_config):
        self.parent = parent
        self.logfile = logfile
        
        self.game_config = game_config
        self.create_label_canvas_flag = False
        self.info_callback = info_callback
        self.settings_callback = settings_callback
        self.label_canvas = None
        self.label_texts = {
            "main_menu": "Main Menu",
            "classic_snake": "Classic Snake",
            "endless_snake": "Endless Snake",
            "special_snake": "Special Snake",
            "info": "Game Information",
            "settings": "Settings"
        }
    
    def create_label_with_border(self, text):
        label_border = ctk.CTkFrame(self.label_canvas, border_color='Grey10', border_width=5)
        label = ctk.CTkLabel(label_border, text=text, font=FONT_LIST[20])
        label.pack(fill="both", expand=True, padx=1, pady=1)
        label_border.pack(side="bottom", padx=10, pady=10, fill="x")
        return label

    def create_label_canvas(self, label_type):
        if self.create_label_canvas_flag:
            self.label_canvas = ctk.CTkCanvas(self.parent, bg='Grey10', highlightthickness=5, highlightbackground='Black')
            self.label_canvas.pack(side='bottom', fill='both')
            self.create_label_canvas_flag = False

        if label_type in self.label_texts:
            self.create_label_with_border(self.label_texts[label_type])

    def create_main_menu_label(self):
        self.create_label_canvas("main_menu")

    def create_classic_snake_label(self):
        self.create_label_canvas("classic_snake")

    def create_endless_snake_label(self):
        self.create_label_canvas("endless_snake")

    def create_special_snake_label(self):
        self.create_label_canvas("special_snake")

    def create_info_label(self):
        self.create_label_canvas("info")

    def create_settings_label(self):
        self.create_label_canvas("settings")

    def set_create_label_canvas_flag(self, value=True):
        self.create_label_canvas_flag = value

class SettingsOptionButtonLabels:
    def __init__(self, logfile, settings_canvas):
        self.logfile = logfile
        self.settings_canvas = settings_canvas

    def create_screen_options_label(self):
        self.screen_label = ctk.CTkLabel(self.settings_canvas, 
                                        width=160,
                                        height=30,
                                        corner_radius=6,
                                        text="Screen size", 
                                        font=FONT_LIST[11],
                                        anchor='w')
        self.screen_label.place(x=200, y=10)
        
    def create_theme_options_label(self):
        self.theme_label = ctk.CTkLabel(self.settings_canvas, 
                                        width=160,
                                        height=30,
                                        corner_radius=6,
                                        text="Theme options", 
                                        font=FONT_LIST[11],
                                        anchor='w')
        self.theme_label.place(x=400, y=10)

    def create_contrast_options_label(self):
        self.contrast_label = ctk.CTkLabel(self.settings_canvas, 
                                           width=160,
                                           height=30,
                                           corner_radius=6,
                                           text="Dark or Light", 
                                           font=FONT_LIST[11],
                                           anchor='w'
                                           )
        self.contrast_label.place(x=600, y=10)

    def create_theme_label(self):
        config_dir = path.dirname(__file__)
        config_path = path.join(config_dir, '..','config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)

        current_theme = config.get('Settings', 'theme')
        initial_theme = config.get('Settings', 'initial_theme')

        # Check if the 'label_needed' option exists, if not, add it
        if not config.has_option('Settings', 'label_needed'):
            config.set('Settings', 'label_needed', 'False')

        if current_theme != initial_theme:
            if hasattr(self, 'restart_game_label'):
                self.restart_game_label.destroy()
            self.restart_game_label = ctk.CTkLabel(self.settings_canvas, text="You need to restart to apply the theme", font=FONT_LIST[11])
            self.restart_game_label.place(x=400, y=100)
            config.set('Settings', 'label_needed', 'True')
        else:
            if hasattr(self, 'restart_game_label'):
                self.restart_game_label.destroy()
                del self.restart_game_label
            config.set('Settings', 'label_needed', 'False')

        # Write the changes to the config file
        with open(config_path, 'w') as configfile:
            config.write(configfile)

    def set_create_label_canvas_flag(self, value=True):
        self.create_label_canvas_flag = value

class GameLabelsPanel:
    def __init__(self, logfile, snake_canvas, game_config):
        self.lofile = logfile
        self.snake_canvas = snake_canvas
        self.game_config = game_config
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT

        self.score_label_flag = False
        self.time_label_flag = False
        self.high_score_label_flag = False
        self.high_score_time_label_flag = True

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)

        #Get the score from the config file
        self.score_label_ = self.config.get('Classic_Snake_Values', 'score', fallback='0')

    def create_game_labels(self):
        self.create_score_label()
        self.create_high_score_label()
        self.create_time_label()
        self.create_high_score_time_label()
        self.create_high_scores_label()
        self.create_snake_length_label()
        self.create_high_score_snake_length_label()
    
    def update_high_score_labels(self):
        self.update_high_score_label()
        self.update_high_score_time_label()
        self.update_high_score_snake_length_label()
    
    def update_game_labels(self):
        self.update_score_label()
        self.update_time_label()
        self.update_snake_length_label()


    def create_score_label(self):
        self.score_label = ctk.CTkLabel(self.snake_canvas, 
                                            height=30,
                                            width=275,
                                            corner_radius=10,
                                            text=f"Score:{self.score_label_} Food eaten", 
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor='w'
                                            )
        self.score_label.place(x=200, y=50)
    
    def update_score_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.score_label_ = self.config.get('Classic_Snake_Values', 'score', fallback='0')
        #update the score label on the screen
        self.score_label.configure(text=f"Score: {self.score_label_} Food eaten")
    
    def create_high_score_label(self):
        self.high_score_label = ctk.CTkLabel(self.snake_canvas,
                                             height=30,
                                             width=275,
                                             corner_radius=10, 
                                             text=f"Score: {self.score_label_} Food eaten", 
                                             font=FONT_LIST[11],
                                             bg_color='grey20',
                                             anchor='w'
                                             )
        self.high_score_label.place(x=200, y=550)
    
    def update_high_score_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.high_score_label_ = self.config.get('Classic_Snake_Values', 'high_score', fallback='0')
        #update the high score label on the screen
        self.high_score_label.configure(text=f"Score: {self.high_score_label_} Food eaten")

    def create_time_label(self):
        self.time_label = ctk.CTkLabel(self.snake_canvas, 
                                        height=30,
                                        width=275,
                                        corner_radius=10,
                                        text=f"Time: {self.score_label_} Seconds", 
                                        font=FONT_LIST[11],
                                        bg_color='grey20',
                                        anchor='w'
                                        )
        self.time_label.place(x=200, y=100)

    def update_time_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.time_label_ = self.config.get('Classic_Snake_Values', 'time_score', fallback='0')
        #update the time label on the screen
        self.time_label.configure(text=f"Time: {self.time_label_} Seconds")

    def create_high_score_time_label(self):
        self.high_score_time_label = ctk.CTkLabel(self.snake_canvas, 
                                                    height=30,
                                                    width=275,
                                                    corner_radius=10,
                                                    text=f"Score Time: {self.score_label_} Seconds", 
                                                    font=FONT_LIST[11],
                                                    bg_color='grey20',
                                                    anchor='w'
                                                    )
        self.high_score_time_label.place(x=200, y=600)

    def update_high_score_time_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.high_score_time_label_ = self.config.get('Classic_Snake_Values', 'high_score_time', fallback='0')
        #update the high score time label on the screen
        self.high_score_time_label.configure(text=f"Score Time: {self.high_score_time_label_} Seconds")

    def create_snake_length_label(self):
        self.snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                                height=30,
                                                width=275, 
                                                corner_radius=10,
                                                text="Snake Length:", 
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.snake_length_label.place(x=200, y=150)
    
    def update_snake_length_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length', fallback='0')
        #update the high score time label on the screen
        self.snake_length_label.configure(text=f"Snake Length: {self.snake_length_label_}")

    def create_high_score_snake_length_label(self):
        self.high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas, 
                                                            height=30,
                                                            width=275,
                                                            corner_radius=10,
                                                            text="Snake Length:", 
                                                            font=FONT_LIST[11],
                                                            bg_color='grey20',
                                                            anchor='w'
                                                            )
        self.high_score_snake_length_label.place(x=200, y=650)
    
    def update_high_score_snake_length_label(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)
        self.high_score_snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length_high_score', fallback='0')
        #update the high score time label on the screen
        self.high_score_snake_length_label.configure(text=f"Snake Length: {self.high_score_snake_length_label_}")

    def create_high_scores_label(self):
        self.high_scores_label = ctk.CTkLabel(self.snake_canvas, 
                                                height=30,
                                                width=275,
                                                corner_radius=10,
                                                text="High Scores:", 
                                                font=FONT_LIST[11],
                                                bg_color='grey20',
                                                anchor='w'
                                                )
        self.high_scores_label.place(x=200, y=500)

    def reset_labels(self):
        self.score_label.configure(text='0')
        self.time_label.configure(text='0')

    
    def delete_labels(self):
        try:
            print("delete_labels method called")
            self.score_label.destroy()
            self.time_label.destroy()
            self.high_score_label.destroy()
            self.high_score_time_label.destroy()
            self.high_scores_label.destroy()
            self.snake_length_label.destroy()
            self.high_score_snake_length_label.destroy()
        except Exception as e:
            print(f"Error occurred: {e}")

