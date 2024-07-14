"""
File: login_example.py
"""

import json
import os
import customtkinter as ctk

# Define the file where user data will be stored
USER_DATA_FILE = 'users.json'

# Function to read user data from file
class LoginAndUserScreen():
    """
    Class to create a login screen with the following features:
    """
    def __init__(self, parent):
        self.parent = parent
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

    def create_login_screen(self):
        """
        Function to create the login screen
        """
        self.login_frame = ctk.CTkFrame(self.parent, fg_color="black")
        self.login_frame.pack(fill="both", expand=True)

        self.username_label = ctk.CTkLabel(self.login_frame, text="Username")
        self.username_label.pack(pady=10)
        self.username_entry = ctk.CTkComboBox(self.login_frame, command=self.update_usernames_combobox) # pylint: disable=line-too-long
        self.username_entry.pack(pady=10)
        self.username_entry.set("")

        self.password_label = ctk.CTkLabel(self.login_frame, text="Password")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.create_user_button = ctk.CTkButton(self.login_frame, text="Create User", command=self.create_user) # pylint: disable=line-too-long
        self.create_user_button.pack(pady=10)

        self.forgot_password_button = ctk.CTkButton(self.login_frame, text="Forgot Password", command=self.forgot_password) # pylint: disable=line-too-long
        self.forgot_password_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.login_frame, text="", corner_radius=10)
        self.result_label.pack(pady=10)

        # self.logout_button = ctk.CTkButton(self.user_frame, text="Logout", command=self.logout)
        # self.logout_button.pack(pady=10)

    def read_user_data(self):
        """
        Function to read user data from file
        """
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    # Function to write user data to file
    def write_user_data(self, data):
        """
        Function to write user data to file
        """
        with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        self.update_usernames_combobox()

    # Function to update the ComboBox with usernames
    def update_usernames_combobox(self):
        """
        Function to update the ComboBox with usernames
        """
        users = self.read_user_data()
        usernames = list(users.keys())
        self.username_entry.configure(values=usernames)

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
                users[username] = password
                self.write_user_data(users)
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
                self.result_label.configure(text="Login successful!", fg_color="green")
                # Delay switching to the next screen by 2000 milliseconds (2 seconds)
                self.result_label.after(1000, lambda: self.switch_to_user_screen(username))
            elif username not in users:
                self.result_label.configure(text="User does not exist", fg_color="red")
            elif username in users and users[username] != password:
                self.result_label.configure(text="Incorrect Password", fg_color="red")
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

    def enter_user(self, username):
        """
        Function to enter a user
        """
        self.switch_to_user_screen(username)

    def forgot_password(self):
        """
        Function to reset the password of an existing user
        """
        username = self.username_entry.get()
        if username:
            users = self.read_user_data()
            if username in users:
                dialog = ctk.CTkInputDialog(title="Reset Password", text="Enter your new password:") # pylint: disable=line-too-long
                new_password = dialog.get_input()  # This waits for the user to input a new password # pylint: disable=line-too-long
                if new_password and new_password != users[username]:  # Check if the user entered a new password # pylint: disable=line-too-long
                    users[username] = new_password  # Update the password in the users dictionary
                    self.write_user_data(users)  # Save the updated users dictionary back to the JSON file # pylint: disable=line-too-long
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
