import customtkinter as ctk, traceback

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('400x300')
        ctk.set_default_color_theme('dark-blue')

        # radio button
        self.selected_theme = ctk.StringVar()
        self.theme_frame = ctk.CTkFrame(self)
        self.theme_frame.pack()

        self.create_theme_label()

        try:
            self.theme_size = ctk.CTkOptionMenu(
                self.theme_frame,
                width= 200,
                height= 100,
                hover=False,
                corner_radius=8,
                values=["default", "black", "blue", "dark-blue", "green", "grey", "orange", "pink", "purple", "red", "white", "yellow"],
                command= self.change_theme
            )
            self.theme_size.place(x=100, y=50)

        except Exception:
            traceback.print_exc()

    def create_theme_label(self):
        self.theme_label = ctk.CTkButton(self.theme_frame, 
                                        text="Theme options", 
                                        font=("Arial", 11))
        self.theme_label.place(x=100, y=200)
        self.theme_frame.pack()

    def change_theme(self, theme):
        ctk.set_default_color_theme(theme)
        self.theme_label.destroy()  # Destroy the existing label
        self.create_theme_label()  # Create a new label with the new theme

if __name__ == "__main__":
    app = App()
    app.mainloop()