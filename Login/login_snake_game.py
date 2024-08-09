"""
File: login_example.py
"""

import json
import os
# import shutil
# import configparser
#import traceback
from os import path
from PIL import Image
import customtkinter as ctk

from Logic.config_handler import ConfigHandler

# Function to read user data from file
class LoginAndUserScreen():
    """
    Class to create a login screen with the following features:
    """
    def __init__(self, parent, game_logger, on_login_success_callback=None):
        # Main attributes
        self.parent = parent
        self.game_logger = game_logger
        self.on_login_success_callback = on_login_success_callback
        self.current_user = None

        # Frame attributes
        self.login_frame = None
        self.user_frame = None
        self.header_frame = None

        # Label attributes
        self.header_label = None
        self.login_label = None
        self.username_label = None
        self.password_label = None
        self.result_label = None
        self.snake_game_label = None
        self.instruction_label = None
        self.entry_label = None
        self.confimation_label = None
        self.username_forgot_password_entry_label = None
        self.password_forgot_password_entry_label = None
        self.instruction_label_delete_user = None
        self.username_delete_user_entry_label = None
        self.password_delete_user_entry_label = None

        # Entry attributes
        self.username_entry = None
        self.password_entry = None
        self.username_forgot_password_entry = None
        self.password_forgot_password_entry = None
        self.username_delete_user_entry = None
        self.password_delete_user_entry = None

        # Button attributes
        self.login_button = None
        self.create_button = None
        self.forgot_button = None
        self.delete_button = None
        self.reset_password_button = None
        self.stop_forget_password = None
        self.delete_user_button = None
        self.stop_delete_user = None
        self.yes_button = None
        self.no_button = None
        self.shortcuts_button = None
        self.create_user_button = None
        self.forgot_password_button = None

        # Shortcut related attributes
        self.shortcuts_frame = None
        self.shortcuts_displayed = None

        # Image related attributes
        self.my_image = None
        self.image_label = None

        # File path and configuration
        script_dir = os.path.dirname(__file__)
        self.login_data = os.path.join(script_dir, "users.json")
        self.config_path_icon = path.join(script_dir, '..', 'app_icon.ico')
        self.parent.iconbitmap('app_icon.ico')
        self.config_dir = os.path.dirname(os.path.dirname(__file__))  # pylint: disable=line-too-long
        self.config_handler = ConfigHandler(self.config_dir, self.game_logger)

        # Initialize shortcuts frame
        self.create_shortcuts_frame()

        # Bind shortcuts to the parent window
        # self.parent.bind('<Control-c>', lambda event: self.handle_shortcut('create_user'))
        # self.parent.bind('<Control-f>', lambda event: self.handle_shortcut('forgot_password'))
        # self.parent.bind('<Control-d>', lambda event: self.handle_shortcut('delete_account'))
        # self.parent.bind('<Control-y>', lambda event: self.handle_shortcut('yes'))
        # self.parent.bind('<Control-n>', lambda event: self.handle_shortcut('no'))
        # self.parent.bind('<Control-r>', lambda event: self.handle_shortcut('reset_password'))
        # self.parent.bind('<Control-s>', lambda event: self.handle_shortcut('shortcuts'))
        # self.parent.bind('<Escape>', self.handle_escape)
        # self.parent.bind('<Return>', self.login)

        # self.login_frame.focus_set()

    def create_login_screen(self):
        """
        Function to create the login screen
        """

        # Frame for login and create user
        self.login_frame = ctk.CTkFrame(self.parent,
                                                    height=100,
                                                    width=2000,
                                                    fg_color="grey20")
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.header_frame = ctk.CTkFrame(self.login_frame,
                                                    height=50,
                                                    width=2000,
                                                    fg_color="grey20",
                                                    corner_radius=0 )
        self.header_frame.place(x=0, y=0, relwidth=1, relheight=0.2)

        # Header label
        self.header_label = ctk.CTkLabel(self.header_frame,
                                                    text="Shadow's Snake Game",
                                                    font=("Lexend", 24),
                                                    text_color="white")
        self.header_label.place(x=10, y=10)

        # Buttons for login and create user
        self.login_button = ctk.CTkButton(self.header_frame, text="Login",
                                                    command=self.login,
                                                    fg_color="#7F00FF",
                                                    text_color="white",
                                                    hover_color="#480082")

        self.create_button = ctk.CTkButton(self.header_frame,
                                                    text="Create Account",
                                                    command=self.create_user,
                                                    border_width=1,
                                                    border_color="blue",
                                                    text_color="blue",
                                                    fg_color="white",
                                                    hover_color="#E6E6FA")

        self.shortcuts_button = ctk.CTkButton(self.header_frame,
                                      text="Shortcuts",
                                      command=self.toggle_shortcuts,
                                      fg_color="grey90",
                                      text_color="blue",
                                      hover_color="#E6E6FA")
        self.shortcuts_button.place(x=640, y=10)

        self.login_button.place(x=470, y=10)
        self.create_button.place(x=300, y=10)

        # Frame for username and password
        self.user_frame = ctk.CTkFrame(self.login_frame,
                                                    height=200,
                                                    width=1500,
                                                    fg_color="grey20",
                                                    corner_radius=0,
                                                    border_width=1,
                                                    border_color="grey40")
        self.user_frame.place(x=0, y= 50, relwidth=1, relheight=1)

        self.result_label = ctk.CTkLabel(self.user_frame,
                                                    text="",
                                                    corner_radius=10)
        self.result_label.place(x=10, y=45)

        self.login_label = ctk.CTkLabel(self.user_frame,
                                                    text="Login to play:",
                                                    font=("Lexend", 24),
                                                    fg_color="grey20")
        self.login_label.place(x=10, y=10)

        # Username input
        self.username_label = ctk.CTkLabel(self.user_frame,
                                                    text="Username")

        self.username_entry = ctk.CTkEntry(self.user_frame,
                                                    fg_color="grey40",
                                                    height=30,
                                                    width=250,
                                                    placeholder_text="Enter your username",
                                                    placeholder_text_color="white")
        self.username_label.place(x=13, y=80)
        self.username_entry.place(x=10, y=110)

        # Password input
        self.password_label = ctk.CTkLabel(self.user_frame,
                                                    text="Password")
        self.password_entry = ctk.CTkEntry(self.user_frame,
                                                    show="*",
                                                    fg_color="grey40",
                                                    height=30,
                                                    width=250,
                                                    placeholder_text="Enter your password",
                                                    placeholder_text_color="white")
        self.password_label.place(x=303, y=80)
        self.password_entry.place(x=300, y=110)

        # Buttons for forgot password and delete user
        self.forgot_button = ctk.CTkButton(self.user_frame,
                                                    text="Forgot Password",
                                                    command=self.forgot_password,
                                                    fg_color="grey90",
                                                    text_color="blue",
                                                    hover_color="#E6E6FA")
        self.delete_button = ctk.CTkButton(self.user_frame,
                                                    text="Delete Account",
                                                    command=self.delete_account,
                                                    fg_color="grey90",
                                                    text_color="blue",
                                                    hover_color="#E6E6FA")
        self.forgot_button.place(x=625, y=110)
        self.delete_button.place(x=795, y=110)

        self.create_and_place_image_label(self.user_frame, 150, 5, self.config_path_icon)

        #self.login_frame.bind('<Return>', self.login)
        self.username_entry.bind('<Return>', self.simulate_login_button_click)
        self.password_entry.bind('<Return>', self.simulate_login_button_click)
        self.parent.bind('<Control-c>', lambda event: self.handle_shortcut('create_user'))
        self.parent.bind('<Control-f>', lambda event: self.handle_shortcut('forgot_password'))
        self.parent.bind('<Control-d>', lambda event: self.handle_shortcut('delete_account'))
        self.parent.bind('<Control-y>', lambda event: self.handle_shortcut('yes'))
        self.parent.bind('<Control-n>', lambda event: self.handle_shortcut('no'))
        self.parent.bind('<Control-r>', lambda event: self.handle_shortcut('reset_password'))
        self.parent.bind('<Control-s>', lambda event: self.handle_shortcut('shortcuts'))
        self.parent.bind('<Escape>', self.handle_escape)
        self.parent.bind('<Return>', self.login)

        self.login_frame.focus_set()

        

        self.create_shortcuts_frame()

        # self.logout_button = ctk.CTkButton(self.user_frame, text="Logout", command=self.logout)
        # self.logout_button.pack(pady=10)

    def handle_shortcut(self, action):
        if action == 'create_user' and hasattr(self, 'create_button') and self.create_button.winfo_exists():
            self.create_user()
        elif action == 'forgot_password' and hasattr(self, 'forgot_button') and self.forgot_button.winfo_exists():
            self.forgot_password()
        elif action == 'delete_account' and hasattr(self, 'delete_button') and self.delete_button.winfo_exists():
            self.delete_account()
        elif action == 'yes' and hasattr(self, 'yes_button') and self.yes_button.winfo_exists():
            self.yes_button.invoke()
        elif action == 'no' and hasattr(self, 'no_button') and self.no_button.winfo_exists():
            self.no_button.invoke()
        elif action == 'reset_password' and hasattr(self, 'reset_password_button') and self.reset_password_button.winfo_exists():
            self.reset_password_button.invoke()
        elif action == 'shortcuts':
            self.toggle_shortcuts()



    def create_and_place_image_label(self, canvas, x, y, image_path):
        """
        Create and place a CTkImage and CTkLabel on the specified canvas.
        """
        self.my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                dark_image=Image.open(image_path),
                                size=(40, 40))

        self.image_label = ctk.CTkLabel(canvas, image=self.my_image, text="", corner_radius=6)
        self.image_label.place(x=x, y=y)

    def read_user_data(self):
        """
        Function to read user data from file
        """
        if os.path.exists(self.login_data):
            with open(self.login_data, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    # Function to write user data to file
    def write_user_data(self, username, password):
        """
        Function to write user data to file
        """
        # Assuming self.login_data is the path to the users.json file
        if not os.path.exists(self.login_data):
            data = {username: password}
        else:
            with open(self.login_data, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data[username] = password

        with open(self.login_data, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def handle_escape(self, event): # pylint: disable=unused-argument
        """
        Function to handle the escape key
        """
        if hasattr(self, 'stop_forget_password') and self.stop_forget_password is not None: # pylint: disable=line-too-long
            try:
                if self.stop_forget_password.winfo_exists():
                    self.delete_forgot_password_widgets()
            except TypeError:
                # Widget has been destroyed, but the attribute still exists
                pass
        elif hasattr(self, 'stop_delete_user') and self.stop_delete_user is not None: # pylint: disable=line-too-long
            try:
                if self.stop_delete_user.winfo_exists():
                    self.delete_delete_user_widgets()
            except TypeError:
                # Widget has been destroyed, but the attribute still exists
                pass
        elif hasattr(self, 'no_button') and self.no_button.winfo_exists():
            self.no_button.invoke()

    def create_shortcuts_frame(self):
        """
        create a frame to display the shortcuts for the login screen
        """
        self.shortcuts_frame = ctk.CTkFrame(self.login_frame,
                                            fg_color="grey30",
                                            corner_radius=10,
                                            width=350,
                                            height=200)

        shortcuts_label = ctk.CTkLabel(self.shortcuts_frame,
                                    text="Shortcuts:",
                                    font=("Lexend", 16, "bold"),
                                    text_color="white")
        shortcuts_label.pack(pady=(10, 5))

        shortcuts = [
            "Enter:  Login                              |    Escape:  Cancel",
            "Ctrl+C:  Create Account           |     Ctrl+R: Reset Password",
            "Ctrl+F:  Forgot Password        |    Ctrl+Y: Confirm (Yes)",
            "Ctrl+D:  Delete Account           |     Ctrl+N:  Cancel (No)"
        ]

        for shortcut in shortcuts:
            shortcut_label = ctk.CTkLabel(self.shortcuts_frame,
                                        text=shortcut,
                                        text_color="white")
            shortcut_label.pack(pady=2,padx =5, anchor='w')
        # Initially hide the frame
        self.shortcuts_frame.place_forget()
        self.shortcuts_frame.pack_propagate(False)

    def toggle_shortcuts(self):
        """
        Toggle the shortcuts frame on and off
        """
        if not hasattr(self, 'shortcuts_frame'):
            self.create_shortcuts_frame()

        if self.shortcuts_frame.winfo_viewable():
            self.shortcuts_frame.place_forget()
        else:
            # Position the frame just below the button
            self.shortcuts_frame.place(x=10, y=225)
            self.shortcuts_frame.lift()  # Bring the frame to the front

    # Function to create a new user
    def create_user(self):
        """
        Function to create a new user and their configuration file
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            users = self.read_user_data()
            if username in users:
                self.game_logger.log_game_event("User already exists!")
                self.result_label.configure(text="User already exists!", fg_color="red")
                self.reset_label_text()
            else:
                self.game_logger.log_game_event("User created successfully!")
                self.write_user_data(username, password)
                self.config_handler.create_user_config(username)
                self.result_label.configure(text="User created successfully!", fg_color="green")
                self.reset_label_text()
        else:
            self.game_logger.log_game_event("Please enter a username and password")
            self.result_label.configure(text="Please enter a username and password", fg_color="red")
            self.reset_label_text()

    def handle_yes(self, event=None): # pylint: disable=unused-argument
        if hasattr(self, 'yes_button') and self.yes_button.winfo_exists():
            self.yes_button.invoke()

    def handle_no(self, event=None): # pylint: disable=unused-argument
        if hasattr(self, 'no_button') and self.no_button.winfo_exists():
            self.no_button.invoke()

    def handle_reset_password(self, event): # pylint: disable=unused-argument
        if hasattr(self, 'reset_password_button') and self.reset_password_button.winfo_exists():
            self.reset_password_button.invoke()

    def simulate_login_button_click(self, event): # pylint: disable=unused-argument
        """
        simulate login button click
        """
        self.login_button.invoke()

    # def simulate__forget_cancel_button_click(self, event):
    #     self.stop_forget_password.invoke()

    # def simulate_cancel_delete_button_click(self, event):
    #     self.stop_delete_user.invoke()

    def login(self, event=None): # pylint: disable=unused-argument
        """
        Function to log in an existing user
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            users = self.read_user_data()
            if username in users and users[username] == password:
                self.current_user = username
                self.result_label.configure(text="Login successful!", fg_color="green")
                self.username_entry.unbind('<Return>')
                self.password_entry.unbind('<Return>')
                self.parent.after(2000, lambda: self.switch_to_user_screen(username))
            elif username not in users:
                self.result_label.configure(text="User does not exist", fg_color="red")
                self.reset_label_text()
            elif username in users and users[username] != password:
                self.result_label.configure(text="Incorrect Password", fg_color="red")
                self.reset_label_text()
            else:
                self.result_label.configure(text="Invalid username or password", fg_color="red")
                self.reset_label_text()
        else:
            self.result_label.configure(text="Please enter a username and password", fg_color="red")
            self.reset_label_text()

    def reset_label_text(self):
        """
        Function to reset the text of the result label after 3 seconds
        """
        self.result_label.after(3000, lambda: self.result_label.configure(text="", fg_color="grey20")) # pylint: disable=line-too-long

    def reset_entry_label_text(self):
        """
        Function to reset the text of the entry label after 3 seconds
        """
        self.entry_label.after(3000, lambda: self.entry_label.configure(text="", fg_color="grey20"))

    def enter_user(self, username):
        """
        Function to enter a user
        """
        self.switch_to_user_screen(username)

    def forgot_password(self):
        """
        Function to reset the password of an existing user
        """

        self.forgot_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.create_button.configure(state="disabled")
        self.login_button.configure(state="disabled")
        self.password_entry.configure(state="disabled")
        self.username_entry.configure(state="disabled")

        self.instruction_label = ctk.CTkLabel(self.user_frame,
                                                            text="Enter your username and password to reset your password", # pylint: disable=line-too-long
                                                            text_color="red",
                                                            fg_color="grey20") # pylint: disable=line-too-long
        self.instruction_label.place(x=13, y=400)

        self.entry_label = ctk.CTkLabel(self.user_frame,
                                                            text="",
                                                            fg_color="grey20",
                                                            corner_radius=10) # pylint: disable=line-too-long`
        self.entry_label.place(x=13, y=440)

        self.username_forgot_password_entry = ctk.CTkEntry(self.user_frame,
                                                           fg_color="grey40",
                                                           height=30,
                                                           width=250,
                                                           placeholder_text="Enter your username",
                                                           placeholder_text_color="white") # pylint: disable=line-too-long
        self.username_forgot_password_entry.place(x=10, y=500)

        self.password_forgot_password_entry = ctk.CTkEntry(self.user_frame,
                                                           show="*",
                                                           fg_color="grey40",
                                                           height=30,
                                                           width=250,
                                                           placeholder_text="Enter your password",
                                                           placeholder_text_color="white") # pylint: disable=line-too-long
        self.password_forgot_password_entry.place(x=300, y=500)

        self.username_forgot_password_entry_label = ctk.CTkLabel(self.user_frame, text="Username")
        self.username_forgot_password_entry_label.place(x=13, y=470)

        self.password_forgot_password_entry_label = ctk.CTkLabel(self.user_frame, text="New Password")
        self.password_forgot_password_entry_label.place(x=303, y=470)

        self.reset_password_button = ctk.CTkButton(self.user_frame, text="Reset Password", command=self.forgot_password_callback, fg_color="grey90", text_color="blue", hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.reset_password_button.place(x=625, y=500)

        self.stop_forget_password = ctk.CTkButton(self.user_frame, text="Cancel", command=self.delete_forgot_password_widgets, fg_color="grey90", text_color="blue", hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.stop_forget_password.place(x=795, y=500)

    def forgot_password_callback(self):
        username = self.username_forgot_password_entry.get()
        new_password = self.password_forgot_password_entry.get()
        if username and new_password:
            users = self.read_user_data()
            if username in users:
                if new_password == users[username]:
                    self.entry_label.configure(text="New password cannot be the same as the old password.", fg_color="red")
                    self.reset_entry_label_text()
                else:
                    self.show_reset_password_confirmation(username, new_password)
            else:
                self.entry_label.configure(text="User does not exist", fg_color="red")
                self.reset_entry_label_text()
        else:
            self.entry_label.configure(text="Please enter a username and new password", fg_color="red")
            self.reset_entry_label_text()

    def show_reset_password_confirmation(self, username, new_password):
        self.confimation_label = ctk.CTkLabel(self.user_frame, 
                                            text="Are you sure you want to reset your password?", 
                                            fg_color="grey20")
        self.confimation_label.place(x=13, y=540)

        self.yes_button = ctk.CTkButton(self.user_frame,
                                        text="Yes",
                                        command=lambda: self.confirm_reset_password(username, new_password),
                                        fg_color="grey90",
                                        text_color="green",
                                        hover_color="#E6E6FA")
        self.no_button = ctk.CTkButton(self.user_frame,
                                    text="No",
                                    command=self.delete_reset_password_confirmation,
                                    fg_color="grey90",
                                    text_color="red",
                                    hover_color="#E6E6FA")
        
        self.yes_button.place(x=625, y=540)
        self.no_button.place(x=795, y=540)
    
    def confirm_reset_password(self, username, new_password):
        self.write_user_data(username, new_password)
        self.entry_label.configure(text="Password updated successfully!", fg_color="green")
        self.reset_entry_label_text()
        self.parent.after(2000, self.delete_forgot_password_widgets)
        self.delete_reset_password_confirmation()

    def delete_reset_password_confirmation(self):
        if hasattr(self, 'confimation_label'):
            self.confimation_label.destroy()
        if hasattr(self, 'yes_button'):
            self.yes_button.destroy()
        if hasattr(self, 'no_button'):
            self.no_button.destroy()

    def delete_forgot_password_widgets(self):
        """
        Function to delete the widgets created for the forgot password feature
        """
        if hasattr(self, 'instruction_label'):
            self.instruction_label.destroy()
        if hasattr(self, 'entry_label'):
            self.entry_label.destroy()
        if hasattr(self, 'username_forgot_password_entry'):
            self.username_forgot_password_entry.destroy()
        if hasattr(self, 'password_forgot_password_entry'):
            self.password_forgot_password_entry.destroy()
        if hasattr(self, 'username_forgot_password_entry_label'):
            self.username_forgot_password_entry_label.destroy()
        if hasattr(self, 'password_forgot_password_entry_label'):
            self.password_forgot_password_entry_label.destroy()
        if hasattr(self, 'reset_password_button'):
            self.reset_password_button.destroy()
        if hasattr(self, 'stop_forget_password'):
            self.stop_forget_password.destroy()

        self.forgot_button.configure(state="normal")
        self.delete_button.configure(state="normal")
        self.create_button.configure(state="normal")
        self.login_button.configure(state="normal")
        self.password_entry.configure(state="normal")
        self.username_entry.configure(state="normal")

        
    def switch_to_user_screen(self, username):
        """
        Function to switch to the user screen
        """
        self.result_label.configure(text="Login successful!", fg_color="green")

        if self.on_login_success_callback:
            self.on_login_success_callback(username)
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        self.username_entry.unbind('<Return>')
        self.password_entry.unbind('<Return>')
        self.parent.unbind('<Control-c>')
        self.parent.unbind('<Control-f>')
        self.parent.unbind('<Control-d>')
        self.parent.unbind('<Control-y>')
        self.parent.unbind('<Control-n>')
        self.parent.unbind('<Control-r>')
        self.parent.unbind('<Control-s>')
        self.parent.unbind('<Escape>')
        self.login_frame.destroy()

    def get_user_name(self):
        """
        Function to get the current user name
        """
        return self.current_user

    def logout(self):
        """
        Function to logout the current user
        """

    def delete_account(self):
        """
        Function to delete the account of the current user
        """
        self.delete_delete_user_widgets()  # Clear any existing delete user widgets

        buttons_to_disable = [
            'forgot_button',
            'delete_button',
            'create_button',
            'login_button',
            'password_entry',
            'username_entry'
        ]

        for button in buttons_to_disable:
            if hasattr(self, button):
                getattr(self, button).configure(state="disabled")

        self.instruction_label_delete_user = ctk.CTkLabel(self.user_frame,
                                                        text="Enter your username and password to delete",
                                                        text_color="red",
                                                        fg_color="grey20")
        self.instruction_label_delete_user.place(x=13, y=400)

        self.entry_label = ctk.CTkLabel(self.user_frame, text="",
                                                        fg_color="grey20",
                                        corner_radius=10)
        self.entry_label.place(x=13, y=440)

        self.username_delete_user_entry = ctk.CTkEntry(self.user_frame,
                                                    fg_color="grey40",
                                                    height=30,
                                                    width=250,
                                                    placeholder_text="Enter your username",
                                                    placeholder_text_color="white")

        self.password_delete_user_entry = ctk.CTkEntry(self.user_frame, show="*",
                                                    fg_color="grey40",
                                                    height=30,
                                                    width=250,
                                                    placeholder_text="Enter your password",
                                                    placeholder_text_color="white")
        self.username_delete_user_entry.place(x=10, y=500)
        self.password_delete_user_entry.place(x=300, y=500)

        self.username_delete_user_entry_label = ctk.CTkLabel(self.user_frame,
                                                        text="Username")
        self.username_delete_user_entry_label.place(x=13, y=470)

        self.password_delete_user_entry_label = ctk.CTkLabel(self.user_frame,
                                                        text="Password")
        self.password_delete_user_entry_label.place(x=303, y=470)

        self.delete_user_button = ctk.CTkButton(self.user_frame,
                                                        text="Delete User",
                                                        command=self.delete_user_callback,
                                                        fg_color="grey90",
                                                        text_color="blue",
                                                        hover_color="#E6E6FA")
        self.delete_user_button.place(x=625, y=500)

        self.stop_delete_user = ctk.CTkButton(self.user_frame,
                                                        text="Cancel",
                                                        command=self.delete_delete_user_widgets,
                                                        fg_color="grey90",
                                                        text_color="blue",
                                                        hover_color="#E6E6FA")
        self.stop_delete_user.place(x=795, y=500)

    def delete_delete_user_widgets(self):
        """
        Function to delete the widgets created for the delete user feature
        """
        attributes_to_delete = [
            'instruction_label_delete_user',
            'entry_label',
            'username_delete_user_entry',
            'password_delete_user_entry',
            'username_delete_user_entry_label',
            'password_delete_user_entry_label',
            'delete_user_button',
            'stop_delete_user',
            'confimation_label',
            'yes_button',
            'no_button'
        ]

        for attr in attributes_to_delete:
            if hasattr(self, attr):
                widget = getattr(self, attr)
                if widget is not None and widget.winfo_exists():
                    widget.destroy()
                setattr(self, attr, None)

        buttons_to_enable = [
            'forgot_button',
            'delete_button',
            'create_button',
            'login_button',
            'password_entry',
            'username_entry'
        ]

        for button in buttons_to_enable:
            if hasattr(self, button):
                getattr(self, button).configure(state="normal")

    def delete_user_callback(self):
        """
        Function to delete the account of the current user
        """
        self.confimation_label = ctk.CTkLabel(self.user_frame,
                                                        text="Are you sure you want to delete your account?", # pylint: disable=line-too-long
                                                        fg_color="grey20") # pylint: disable=line-too-long
        self.confimation_label.place(x=13, y=540)
        self.yes_button = ctk.CTkButton(self.user_frame,
                                                        text="Yes",
                                                        command=self.confirm_delete_user,
                                                        fg_color="grey90",
                                                        text_color="green",
                                                        hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.no_button = ctk.CTkButton(self.user_frame,
                                                        text="No",
                                                        command=self.delete_are_you_sure_widgets,
                                                        fg_color="grey90",
                                                        text_color="red",
                                                        hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.yes_button.place(x=625, y=540)
        self.no_button.place(x=795, y=540)

    def confirm_delete_user(self):
        """
        Function to confirm the deletion of the account of the current user
        """
        username = self.username_delete_user_entry.get()
        password = self.password_delete_user_entry.get()
        if username:
            users = self.read_user_data()
            if username in users:
                if password == users[username]:
                    del users[username]
                    with open(self.login_data, 'w', encoding='utf-8') as file:
                        json.dump(users, file, indent=4)
                    self.entry_label.configure(text="User deleted successfully!", fg_color="green")
                    self.reset_entry_label_text()
                    self.parent.after(2000, self.delete_delete_user_widgets)
                else:
                    self.entry_label.configure(text="Incorrect password.", fg_color="red")
                    self.reset_entry_label_text()
            else:
                self.entry_label.configure(text="User does not exist", fg_color="red")
                self.reset_entry_label_text()
        else:
            self.entry_label.configure(text="Please enter a username", fg_color="red")
            self.reset_entry_label_text()
        # Call to remove the confirmation widgets regardless of the outcome
        self.delete_are_you_sure_widgets()

    def delete_are_you_sure_widgets(self):
        """
        Function to delete the widgets created for the are you sure feature
        """
        self.confimation_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()
