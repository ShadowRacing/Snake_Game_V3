# ************************************
# Wims Snake Game Logger File
# ************************************

# Importing the necessary modules
import datetime
import sys
import os

class LogFile:
    def __init__(self, window):
        # Initializing variables
        self.window = window
        self.current_datetime = datetime.datetime.now()

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the log filename
        self.log_filename = os.path.join(script_dir, "main_snake_logfile.txt")

        # Open the file in append mode
        self.log_file = open(self.log_filename, 'a')
        self.log_game_event("Started the app")

        # Redirect sys.stdout to the log file
        sys.stdout = self.log_file

    def log_game_event(self, event):
        #Method to log game events
        self.current_datetime = datetime.datetime.now()
        formatted_datetime = self.current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{formatted_datetime}] {event}\n"
        self.log_file.write(log_line)

    def on_closing(self):
        #This function will be called when the window is closed
        try:
            self.log_game_event("Closed the app\n\n\n\n")
        finally:
            self.log_file.close()
            self.window.destroy()

class ErrorLogFile:
    def __init__(self):
        # Initializing variables
        self.current_datetime = datetime.datetime.now()
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the log filename
        self.error_log_filename = os.path.join(script_dir, "error_snake_logfile.txt")

        # Open the file in append mode
        self.error_log_filename = open(self.error_log_filename, 'a')
        self.log_error("\n\n")
        self.log_error("Started the Error Log File")

        # Redirect sys.stderr to the log file
        sys.stderr = self.error_log_filename

    def log_error(self, error):
        #Method to log errors
        self.current_datetime = datetime.datetime.now()
        formatted_datetime = self.current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{formatted_datetime}] {error}\n"
        self.error_log_filename.write(log_line)

    def on_closing(self):
        #This function will be called when the window is closed
        try:
            self.log_error("No errors occurred")
            self.log_error("Closed the Error Log File\n\n\n\n") 
        finally:
            self.error_log_filename.close()


# *****************************************
# Wims Snake Game Logger File
# *****************************************