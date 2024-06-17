import tkinter as tk
import subprocess
import sys
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.restart_button = tk.Button(self)
        self.restart_button["text"] = "Restart Script"
        self.restart_button["command"] = self.restart_script
        self.restart_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def restart_script(self):
        try:
            # Validate sys.argv (for example, check for valid filenames or options)
            validated_args = self.validate_argv(sys.argv)
            # Restart the script with validated arguments
            subprocess.Popen([sys.executable] + validated_args)
            # Close the Tkinter window
            self.master.destroy()
        except Exception as e:
            print(f"Error restarting the script: {e}")

    def validate_argv(self, argv):
        # Implement validation logic, e.g., ensuring only certain arguments are allowed
        # This is just an example, adapt it to your specific needs
        for arg in argv:
            if not arg.isalnum() and not os.path.isfile(arg):
                raise ValueError(f"Invalid argument: {arg}")
        return argv

    def some_condition_to_restart(self):
        # Placeholder for actual condition
        return True

root = tk.Tk()
app = Application(master=root)
app.mainloop()