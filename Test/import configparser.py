import configparser


import customtkinter as CTk, configparser
from Screen_size_Changer_snake_game import Screen_size



class MyApplication(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.screen_size_1 = Screen_size(self, None, None, None, None)  # Pass the required arguments to the Screen_size constructor
        #self.geometry("400x300")
        self.title("Frame Switching Example")

        

        # Load the configuration from the config.ini file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        # Get the selected value from the configuration
        selected_value = self.config.get('Settings', 'screen_size', fallback='Default')
        
        with open("config.ini", "w") as configfile:
            self.config.write(configfile)

        # Create the frames
        self.frame1 = CTk.CTkFrame(self)
        self.frame2 = CTk.CTkFrame(self)
        
        # Create the buttons
        self.button1 = CTk.CTkButton(self.frame1, text="Switch to Frame 2", command=self.switch_to_frame2)
        self.button2 = CTk.CTkButton(self.frame2, text="Switch to Frame 1", command=self.switch_to_frame1)
        
        # Create the dropdown button
        self.theme_options = CTk.CTkOptionMenu(self.frame2, 
                                                    width= 100,
                                                    height= 50,
                                                    fg_color="green",
                                                    dropdown_fg_color="green",
                                                    button_color="orange",
                                                    font=("Arial", 12),
                                                    text_color="black",
                                                    dropdown_text_color="black",
                                                    hover=False,
                                                    corner_radius=8,
                                                    values=["Fullscreen", "Windowed", "Default", "1280x800", "1600x900", "1800x1200", "1920x1080", "1920x1200", "2560x1440", "2560x1600", "3480x2160"],
                                                    command=lambda: self.screen_size_1.change_screen_size
                                                    ) # Fixed line
        self.theme_options.set(selected_value)  # Set the selected value  # Set the selected value
        self.theme_options.place(x=200, y=50)


        # Add the buttons and dropdown to the frames
        self.button1.pack()
        self.theme_options.pack()
        self.button2.pack()
        
        

        # Show the initial frame
        self.show_frame1()
        
    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack()
        
    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack()
        
    def switch_to_frame1(self):
        self.show_frame1()
        
    def switch_to_frame2(self):
        self.show_frame2()

if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()