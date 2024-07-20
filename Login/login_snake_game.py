"""
File: login_example.py
"""

import json
import os
import traceback
from os import path
from PIL import Image
import customtkinter as ctk

# Function to read user data from file
class LoginAndUserScreen():
    """
    Class to create a login screen with the following features:
    """
    def __init__(self, parent, on_login_success_callback=None):
        self.parent = parent
        self.on_login_success_callback = on_login_success_callback
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

        script_dir = os.path.dirname(__file__)
        self.login_data = os.path.join(script_dir, "users.json")

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config_path_icon = path.join(self.config_dir, '..', 'app_icon.ico')
        self.parent.iconbitmap('app_icon.ico')
        self.my_image = None
        self.image_label = None

    def create_login_screen(self):
        """
        Function to create the login screen
        """
        self.login_frame = ctk.CTkFrame(self.parent, fg_color="grey20", border_color="purple")
        self.login_frame.pack(fill="both", expand=True)

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login to play:", font=("Helvetica", 40), fg_color="grey20") # pylint: disable=line-too-long
        self.login_label.pack(pady=10)

        # self.snake_game_label = ctk.CTkLabel(self.login_frame, text="Wim's Snake Game", font=("Helvetica", 40), fg_color="grey10") # pylint: disable=line-too-long
        # self.snake_game_label.pack(pady=10)

        self.username_label = ctk.CTkLabel(self.login_frame, text="Username", font=("Helvetica", 18), fg_color="grey20")
        self.username_label.pack(pady=10)

        self.username_entry = ctk.CTkComboBox(self.login_frame, command=self.update_usernames_combobox) # pylint: disable=line-too-long
        self.username_entry.pack(pady=10)
        self.username_entry.set("")
        self.update_usernames_combobox()

        self.password_label = ctk.CTkLabel(self.login_frame, text="Password", font=("Helvetica", 18), fg_color="grey20")
        self.password_label.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login, fg_color="#3B8ED0")
        self.login_button.pack(pady=10)

        self.create_user_button = ctk.CTkButton(self.login_frame, text="Create User", command=self.create_user, fg_color="#3B8ED0") # pylint: disable=line-too-long
        self.create_user_button.pack(pady=10)

        self.forgot_password_button = ctk.CTkButton(self.login_frame, text="Forgot Password", command=self.forgot_password, fg_color="#3B8ED0") # pylint: disable=line-too-long
        self.forgot_password_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.login_frame, text="", corner_radius=10)
        self.result_label.pack(pady=10)

        self.create_and_place_image_label(self.login_frame, 5, 635, self.config_path_icon)

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

        self.update_usernames_combobox()

    # Function to update the ComboBox with usernames
    def update_usernames_combobox(self):
        """
        Function to update the ComboBox with usernames
        """
        users = self.read_user_data()
        usernames = list(users.keys())
        print(users)
        try:
            self.username_entry.configure(values=usernames)
        except AttributeError:
            traceback.print_exc()
        print(usernames)

    # Function to create a new user
    def create_user(self):
        """
        Function to create a new user
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            users = self.read_user_data()
            if username in users:
                self.result_label.configure(text="User already exists!", fg_color="red")
                self.reset_label_text()
            else:
                self.write_user_data(username, password)
                self.result_label.configure(text="User created successfully!", fg_color="green")
                self.reset_label_text()
        else:
            self.result_label.configure(text="Please enter a username and password", fg_color="red")
            self.reset_label_text()

    # Function to log in an existing user
    def login(self):
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
                # Delay switching to the next screen by 2000 milliseconds (2 seconds)
                self.result_label.after(1000, self.switch_to_user_screen())
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
        self.result_label.after(3000, lambda: self.result_label.configure(text="", fg_color="black")) # pylint: disable=line-too-long

    def enter_user(self):
        """
        Function to enter a user
        """
        self.switch_to_user_screen()

    def forgot_password(self):
        """
        Function to reset the password of an existing user
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username:
            users = self.read_user_data()
            if username in users:
                dialog = ctk.CTkInputDialog(title="Reset Password", text="Enter your new password:") # pylint: disable=line-too-long
                new_password = dialog.get_input()  # This waits for the user to input a new password # pylint: disable=line-too-long
                if new_password and new_password != password:  # Check if the user entered a new password # pylint: disable=line-too-long
                    self.write_user_data(username, new_password)  # Save the updated users dictionary back to the JSON file # pylint: disable=line-too-long
                    self.result_label.configure(text="Password updated successfully!", fg_color="green") # pylint: disable=line-too-long
                    self.reset_label_text()
                elif new_password == users[username]:  # Check if the new password is the same as the old password # pylint: disable=line-too-long
                    self.result_label.configure(text="New password cannot be the same as the old password.", fg_color="red") # pylint: disable=line-too-long
                    self.reset_label_text()
                else:
                    self.result_label.configure(text="Password update cancelled.", fg_color="red") # pylint: disable=line-too-long
                    self.reset_label_text()
            else:
                self.result_label.configure(text="User does not exist", fg_color="red")
                self.reset_label_text()
        else:
            self.result_label.configure(text="Please enter a username", fg_color="red")
            self.reset_label_text()

    def switch_to_user_screen(self):
        """
        Function to switch to the user screen
        """
        if self.on_login_success_callback:
            self.on_login_success_callback()
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        self.login_frame.destroy()

    def get_user_name(self):
        """
        Function to get the current user name
        """
        return self.current_user
