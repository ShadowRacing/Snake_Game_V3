# ************************************
# Shadows Snake Screen Size File
# ************************************

"""
This module contains the Screen_size class which is responsible for changing the screen size of the Shadows Snake game. # pylint: disable=line-too-long
"""

class ScreenSize:
    """
    Class for changing the screen size of the Shadows Snake game."""
    def __init__(self, root, logfile, screen_size_var, config, screen_size):
        """
        Initialize the Screen_size class.
        """
        self.logfile = logfile
        self.root = root
        self.screen_size_var = screen_size_var
        self.config = config
        self.screen_size = screen_size
        self.width = 1200
        self.height = 800

    def change_screen_size(self, selected_value):
        """
        Change the screen size based on the selected value.
        """
        self.screen_size = selected_value
        self.root.attributes('-fullscreen', False)
        screen_sizes = {
            "Fullscreen": self.set_fullscreen_size,
            "Default": lambda: self.set_custom_size(1200, 800),
            "1600x900": lambda: self.set_custom_size(1600, 900),
            "1800x1080": lambda: self.set_custom_size(1800, 1080),
            "1800x1200": lambda: self.set_custom_size(1800, 1200),
            "1920x1080": lambda: self.set_custom_size(1920, 1080),
            "1920x1200": lambda: self.set_custom_size(1920, 1200),
            "2560x1440": lambda: self.set_custom_size(2560, 1440)
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
        """
        Set the screen size for fullscreen mode.
        """
        self.root.attributes('-fullscreen', True)

    # The set_custom_size method sets a custom screen size.
    def set_custom_size(self, width, height):
        """
        Set a custom screen size.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        if width > screen_width or height > screen_height:
            self.logfile.log_game_event(f"Invalid screen size: {width}x{height}, setting to the maximum screen height and width") # pylint: disable=line-too-long
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
        """
        Center the screen.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def update_config(self, selected_value):
        """
        Update the screen size in the configuration file and write the changes to the file. # pylint: disable=line-too-long
        """
        self.config.set('Settings', 'screen_size', selected_value)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.logfile.log_game_event("Updated the config.ini Writing updates")


# ************************************
# Shadows Snake Screen Size File
# ************************************
