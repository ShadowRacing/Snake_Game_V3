# ************************************
# Wims Snake Screen Size File
# ************************************

class Screen_size:
    # The constructor initializes the logger, the root window, the screen size variable, the configuration parser, and the screen size.
    def __init__(self, root, logfile, screen_size_var, config, screen_size):
        self.logfile = logfile
        self.root = root
        self.screen_size_var = screen_size_var
        self.config = config
        self.screen_size = screen_size

    # The change_screen_size method changes the screen size based on the selected value.
    

    def change_screen_size(self, selected_value):
        self.screen_size = selected_value
        self.root.attributes('-fullscreen', False)
        screen_sizes = {
            "Fullscreen": self.set_fullscreen_size,
            "Default": lambda: self.set_custom_size(1200, 800),
            "600x800": lambda: self.set_custom_size(600, 800),
            "1600x900": lambda: self.set_custom_size(1600, 900),
            "1800x1080": lambda: self.set_custom_size(1800, 1080),
            "1800x1200": lambda: self.set_custom_size(1800, 1200),
            "1920x1080": lambda: self.set_custom_size(1920, 1080),
            "1920x1200": lambda: self.set_custom_size(1920, 1200),
            "2560x1440": lambda: self.set_custom_size(2560, 1440),
            "3480x2160": lambda: self.set_custom_size(3480, 2160),
        }

        if selected_value in screen_sizes:
            screen_sizes[selected_value]()
            self.screen_size_var.set(selected_value)
            self.logfile.log_game_event(f"Changing screen size to {selected_value}")
            self.update_config(selected_value)
        else:
            self.logfile.log_game_event(f"Invalid screen size: {selected_value}")


    # The set_fullscreen_size method sets the screen size for fullscreen mode.
    def set_fullscreen_size(self):
        self.root.attributes('-fullscreen', True)

    # The set_custom_size method sets a custom screen size.
    def set_custom_size(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        if width > screen_width or height > screen_height:
            self.logfile.log_game_event(f"Invalid screen size: {width}x{height}, setting to the maximum screen height and width")
            width = screen_width
            height = screen_height
        
        self.width = width
        self.height = height
        new_geometry = f"{width}x{height}"
        self.logfile.log_game_event(f"Setting custom size: {new_geometry}")
        self.root.geometry(new_geometry)
        self.center_the_screen()

    # The center_the_screen method centers the screen.
    def center_the_screen(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

    # The update_config method updates the screen size in the configuration file and writes the changes to the file.
    def update_config(self, selected_value):
        self.config.set('Settings', 'screen_size', selected_value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.logfile.log_game_event(f"Updated the config.ini")
# ************************************
# Wims Snake Screen Size File
# ************************************