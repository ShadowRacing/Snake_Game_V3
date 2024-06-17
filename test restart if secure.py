import tkinter as tk
import subprocess
import sys

class App:
    def __init__(self, master):
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        restart_button = tk.Button(self.master, text="Restart", command=self.restart)
        restart_button.pack()

    def validate_argv(self, argv):
        # Validate arguments: ensure they are strings and safe
        for arg in argv:
            if not isinstance(arg, str):
                raise ValueError("All arguments must be strings")
            if any(char in arg for char in [';', '&', '|', '$', '`']):
                raise ValueError("Argument contains unsafe characters")
        return argv

    def restart(self):
        try:
            validated_args = self.validate_argv(sys.argv)
            # Restart the script with validated arguments
            subprocess.Popen([sys.executable] + validated_args, close_fds=True)
            # Close the Tkinter window
            self.master.destroy()
        except Exception as e:
            print(f"Error restarting the application: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


