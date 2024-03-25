# *****************************************
# Wims Snake Contrast Updating File
# *****************************************

#Importing the custom tkinter module
import customtkinter as ctk, configparser

#Class for updating the contrast
class UpdateContrast:
    def __init__(self, logfile):
        #Initializing variables
        self.logfile = logfile
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
    
    #Method to apply the contrast
    def apply_contrast(self,  selected_value=None):
        if selected_value is None:
            config = configparser.ConfigParser()
            config.read('config.ini')
            selected_value = config.get('Settings', 'contrast', fallback='Dark')

        self.update_config_contrast(selected_value)
        if selected_value == 'Dark':
            ctk.set_appearance_mode('dark')
            self.logfile.log_game_event(f"Contrast mode set to dark")
        elif selected_value == 'Light':
            ctk.set_appearance_mode('light')
            self.logfile.log_game_event(f"Contrast mode set to light")
        elif selected_value == 'System':
            ctk.set_appearance_mode('system')
            self.logfile.log_game_event(f"Contrast mode set to system")
        else:
            ctk.set_appearance_mode('dark')
            self.logfile.log_game_event(f"Contrast mode set to dark")
    
    #Method to update the config.ini file
    def update_config_contrast(self, selected_value):
        self.config.set('Settings', 'contrast', selected_value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

# *****************************************
# Wims Snake Contrast Updating File
# *****************************************