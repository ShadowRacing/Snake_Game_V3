"""
File: login_example.py
"""

import json
import os
import shutil
import configparser
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
        self.parent = parent
        self.on_login_success_callback = on_login_success_callback
        self.game_logger = game_logger
        # Create the login frame
        self.login_frame = None
        self.user_frame = None
        self.username_label = None
        self.username_entry = None
        self.password_label = None
        self.password_entry = None
        self.login_button = None
        self.create_user_button = None
        self.forgot_password_button = None
        self.result_label = None
        self.current_user = None
        self.login_label = None
        self.snake_game_label = None
        self.username_forgot_password_entry = None
        self.password_forgot_password_entry = None
        self.username_forgot_password_entry_label = None
        self.password_forgot_password_entry_label = None
        self.reset_password_button = None
        self.stop_forget_password = None
        self.instruction_label = None
        self.entry_label = None
        self.username_delete_user_entry = None
        self.password_delete_user_entry = None
        self.username_delete_user_entry_label = None
        self.password_delete_user_entry_label = None
        self.delete_user_button = None
        self.stop_delete_user = None
        self.instruction_label_delete_user = None
        self.confimation_label = None
        self.yes_button = None
        self.no_button = None
        self.stop_forget_password = None
        self.stop_delete_user = None
        self.header_frame = None
        self.header_label = None
        self.login_button = None
        self.create_button = None
        self.forgot_button = None
        self.delete_button = None

        script_dir = os.path.dirname(__file__)
        self.login_data = os.path.join(script_dir, "users.json")
        self.config_path_icon = path.join(script_dir, '..', 'app_icon.ico')
        self.parent.iconbitmap('app_icon.ico')
        # self.config_dir = path.dirname(__file__)
        # self.config_path = path.join(self.config_dir, 'config.ini')
        self.config_dir = os.path.dirname(os.path.dirname(__file__))  # Assumes Login file is in Login folder
        self.config_handler = ConfigHandler(self.config_dir, self.game_logger)

        self.my_image = None
        self.image_label = None

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

        self.create_and_place_image_label(self.login_frame, 5, 635, self.config_path_icon)

        #self.login_frame.bind('<Return>', self.login)
        self.username_entry.bind('<Return>', self.simulate_login_button_click)
        self.password_entry.bind('<Return>', self.simulate_login_button_click)
        self.login_frame.focus_set()

        # self.logout_button = ctk.CTkButton(self.user_frame, text="Logout", command=self.logout)
        # self.logout_button.pack(pady=10)

    def create_and_place_image_label(self, canvas, x, y, image_path):
        """
        Create and place a CTkImage and CTkLabel on the specified canvas.
        """
        self.my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                dark_image=Image.open(image_path),
                                size=(160, 160))

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


    def simulate_login_button_click(self, event):
        self.login_button.invoke()

    def login(self, event=None):
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
                                                            text="Enter your username and password to reset your password",
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

        self.password_forgot_password_entry_label = ctk.CTkLabel(self.user_frame, text="Password")
        self.password_forgot_password_entry_label.place(x=303, y=470)

        self.reset_password_button = ctk.CTkButton(self.user_frame, text="Reset Password", command=self.forgot_password_callback, fg_color="grey90", text_color="blue", hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.reset_password_button.place(x=625, y=500)

        self.stop_forget_password = ctk.CTkButton(self.user_frame, text="Cancel", command=self.delete_forgot_password_widgets, fg_color="grey90", text_color="blue", hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.stop_forget_password.place(x=795, y=500)

    def forgot_password_callback(self):
        """
        Function to reset the password of an existing user
        """
        username = self.username_forgot_password_entry.get()
        password = self.password_forgot_password_entry.get()
        if username:
            users = self.read_user_data()
            new_password = password
            if username in users:
                if new_password == users[username]:
                    self.entry_label.configure(text="New password cannot be the same as the old password.", fg_color="red") # pylint: disable=line-too-long
                    self.reset_entry_label_text()
                elif new_password and new_password != users[username]:# pylint: disable=line-too-long
                    self.write_user_data(username, new_password)
                    self.entry_label.configure(text="Password updated successfully!", fg_color="green") # pylint: disable=line-too-long
                    self.reset_entry_label_text()
                    self.parent.after(2000, self.delete_forgot_password_widgets)
                else:
                    self.entry_label.configure(text="Password update cancelled.", fg_color="red")
                    self.reset_entry_label_text()
            else:
                self.entry_label.configure(text="User does not exist", fg_color="red")
                self.reset_entry_label_text()
        else:
            self.entry_label.configure(text="Please enter a username", fg_color="red")
            self.reset_entry_label_text()

    def delete_forgot_password_widgets(self):
        """
        Function to delete the widgets created for the forgot password feature
        """
        self.instruction_label.destroy()
        self.entry_label.destroy()
        self.username_forgot_password_entry.destroy()
        self.password_forgot_password_entry.destroy()
        self.username_forgot_password_entry_label.destroy()
        self.password_forgot_password_entry_label.destroy()
        self.reset_password_button.destroy()
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

        self.forgot_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.create_button.configure(state="disabled")
        self.login_button.configure(state="disabled")
        self.password_entry.configure(state="disabled")
        self.username_entry.configure(state="disabled")

        self.instruction_label_delete_user = ctk.CTkLabel(self.user_frame,
                                                        text="Enter your username and password to delete", # pylint: disable=line-too-long
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
                                                        hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.delete_user_button.place(x=625, y=500)

        self.stop_delete_user = ctk.CTkButton(self.user_frame,
                                                        text="Cancel",
                                                        command=self.delete_delete_user_widgets,
                                                        fg_color="grey90",
                                                        text_color="blue",
                                                        hover_color="#E6E6FA") # pylint: disable=line-too-long
        self.stop_delete_user.place(x=795, y=500)

    def delete_delete_user_widgets(self):
        """
        Function to delete the widgets created for the delete user feature
        """
        self.instruction_label_delete_user.destroy()
        self.entry_label.destroy()
        self.username_delete_user_entry.destroy()
        self.password_delete_user_entry.destroy()
        self.username_delete_user_entry_label.destroy()
        self.password_delete_user_entry_label.destroy()
        self.delete_user_button.destroy()
        self.stop_delete_user.destroy()
        self.forgot_button.configure(state="normal")
        self.delete_button.configure(state="normal")
        self.create_button.configure(state="normal")
        self.login_button.configure(state="normal")
        self.password_entry.configure(state="normal")
        self.username_entry.configure(state="normal")

    def delete_user_callback(self):
        """
        Function to delete the account of the current user
        """
        self.confimation_label = ctk.CTkLabel(self.user_frame, 
                                                        text="Are you sure you want to delete your account?", 
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
