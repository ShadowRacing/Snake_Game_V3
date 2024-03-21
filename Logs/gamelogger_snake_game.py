# ************************************
# Wims Snake Game Logger File
# ************************************

# Importing the necessary modules
import datetime, sys, os


# Class for logging game events
class LogFile:
    def __init__(self, window):
        # Initializing variables
        self.window = window
        self.current_datetime = datetime.datetime.now()

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the log filename
        self.log_filename = os.path.join(script_dir, "main_snake_logfile.txt")
       
        # Open the file in write mode
        self.log_file = open(self.log_filename, 'a')
        self.log_game_event("Started the app")
        
        # Redirect sys.stdout to the log file
        sys.stdout = self.log_file

    # Method to log game events
    def log_game_event(self, event):
        self.current_datetime = datetime.datetime.now()
        formatted_datetime = self.current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{formatted_datetime}] {event}\n"
        self.log_file.write(log_line)

    # This function will be called when the window is closed
    def on_closing(self):
        try:
            self.log_game_event("Closed the app\n\n\n\n")
        finally:
            self.log_file.close()
            self.window.destroy()


# *****************************************
# Wims Snake Game Logger File
# *****************************************