"""
This module contains the class for creating the game labels for the game.
"""


import configparser
import traceback
from os import path
import customtkinter as ctk
from Configuration.constants_snake_game import FONT_LIST, GameConstants

from Logic.leveling_system import LevelingSystem

class GameLabelsPanel:
    """
    Class for creating the labels for the game.
    """
    def __init__(self, snake_canvas, game_logger, game_config):
        self.snake_canvas = snake_canvas
        self.game_logger = game_logger
        self.game_config = game_config
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT

        self.high_score_label_needed = None
        self.score_label_needed = None

        self.classic_score_label = None
        self.classic_high_score_label = None
        self.classic_time_label = None
        self.classic_high_score_time_label = None
        self.classic_high_scores_label = None
        self.classic_snake_length_label = None
        self.classic_high_score_snake_length_label = None

        self.endless_score_label = None
        self.endless_high_score_label = None
        self.endless_time_label = None
        self.endless_high_score_time_label = None
        self.endless_high_scores_label = None
        self.endless_snake_length_label = None
        self.endless_high_score_snake_length_label = None
        self.endless_special_score_label = None
        self.endless_special_high_score_label = None
        self.endless_shorten_score_label = None
        self.endless_shorten_high_score_label = None

        self.leveling_score_label = None
        self.leveling_high_score_label = None
        self.leveling_time_label = None
        self.leveling_high_score_time_label = None
        self.leveling_high_scores_label = None
        self.leveling_snake_length_label = None
        self.leveling_high_score_snake_length_label = None
        self.leveling_xp_score_label = None
        self.leveling_xp_high_score_label = None
        self.leveling_level_score_label = None
        self.leveling_level_high_score_label = None

        self.challange_score_label = None
        self.challange_high_score_label = None

        self.classic_score_label_ = None
        self.classic_high_score_label_ = None
        self.classic_time_label_ = None
        self.classic_high_score_time_label_ = None
        self.classic_high_scores_label_ = None
        self.classic_snake_length_label_ = None
        self.classic_high_score_snake_length_label_ = None

        self.endless_score_label_ = None
        self.endless_high_score_label_ = None
        self.endless_time_label_ = None
        self.endless_high_score_time_label_ = None
        self.endless_high_scores_label_ = None
        self.endless_snake_length_label_ = None
        self.endless_high_score_snake_length_label_ = None
        self.endless_special_score_label_ = None
        self.endless_special_high_score_label_ = None
        self.endless_shorten_score_label_ = None
        self.endless_shorten_high_score_label_ = None

        self.leveling_score_label_ = None
        self.leveling_high_score_label_ = None
        self.leveling_time_label_ = None
        self.leveling_high_score_time_label_ = None
        self.leveling_high_scores_label_ = None
        self.leveling_snake_length_label_ = None
        self.leveling_high_score_snake_length_label_ = None
        self.leveling_xp_score_label_ = None
        self.leveling_xp_high_score_label_ = None
        self.leveling_level_score_label_ = None
        self.leveling_level_high_score_label_ = None

        self.challange_score_label_ = None
        self.challange_high_score_label_ = None

        self.classic_score_label_flag = False
        self.classic_time_label_flag = False
        self.classic_high_score_label_flag = False
        self.classic_high_score_time_label_flag = False

        self.endless_score_label_flag = False
        self.endless_time_label_flag = False
        self.endless_high_score_label_flag = False
        self.endless_high_score_time_label_flag = False
        self.endless_special_score_label_flag = False
        self.endless_shorten_score_label_flag = False

        self.leveling_score_label_flag = False
        self.leveling_time_label_flag = False
        self.leveling_high_score_label_flag = False
        self.leveling_high_score_time_label_flag = False

        self.challange_score_label_flag = False
        self.challange_high_score_label_flag = False

        self.width = GameConstants.GAME_LABEL_WIDTH
        self.height = GameConstants.GAME_LABEL_HEIGHT
        self.corner_radius = GameConstants.GAME_LABEL_CORNER_RADIUS
        self.anchor = GameConstants.ANCHOR

        self.leveling_system = LevelingSystem()

        try:
            self.config_dir = path.dirname(__file__)
            self.config_path = path.join(self.config_dir, '..', 'config.ini')
            self.config = configparser.RawConfigParser()
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        #Get the score from the config file
        try:
            self.classic_score_label_ = 0
            self.config.set('Classic_Snake_Values', 'score', '0')
            self.classic_time_label_ = 0
            self.config.set('Classic_Snake_Values', 'time_score', '0')
            self.classic_snake_length_label_ = 0
            self.config.set('Classic_Snake_Values', 'snake_length', '0')
            self.endless_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'score', '0')
            self.endless_time_label_ = 0
            self.config.set('Endless_Snake_Values', 'time_score', '0')
            self.endless_snake_length_label_ = 0
            self.config.set('Endless_Snake_Values', 'snake_length', '0')
            self.endless_special_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'special_score', '0')
            self.endless_shorten_score_label_ = 0
            self.config.set('Endless_Snake_Values', 'shorten_score', '0')
            self.leveling_score_label_ = 0
            self.config.set('Leveling_Snake_Values', 'score', '0')
            self.leveling_time_label_ = 0
            self.config.set('Leveling_Snake_Values', 'time_score', '0')
            self.leveling_snake_length_label_ = 0
            self.config.set('Leveling_Snake_Values', 'snake_length', '0')
            self.challange_score_label_ = 0
            self.config.set('food_time_attack_Values', 'score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def config_file_read_write(self):
        """
        Read and write the config file for the game.
        """
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..', 'config.ini')
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)

    def classic_create_game_labels(self):
        """
        Create the game labels for the classic snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        self.classic_create_score_label()
        self.classic_create_time_label()
        self.classic_create_snake_length_label()
        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.classic_create_high_score_label()
            self.classic_create_high_score_time_label()
            self.classic_create_high_scores_label()
            self.classic_create_high_score_snake_length_label()

    def classic_update_high_score_labels(self):
        """
        Update the high score labels for the classic snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.classic_update_high_score_label()
            self.classic_update_high_score_time_label()
            self.classic_update_high_score_snake_length_label()

    def classic_update_game_labels(self):
        """
        Update the game labels for the classic snake game.
        """
        self.classic_update_score_label()
        self.classic_update_time_label()
        self.classic_update_snake_length_label()

    def classic_create_score_label(self):
        """
        Create the score label for the classic snake game.
        """
        self.classic_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score:{self.classic_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_score_label.place(x=200, y=50)

    def classic_update_score_label(self):
        """
        Update the score label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_score_label_ = self.config.get('Classic_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.classic_score_label.configure(text=f"Score: {self.classic_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_label(self):
        """
        Create the high score label for the classic snake game.
        """
        self.classic_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score: {self.classic_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_high_score_label.place(x=200, y=550)

    def classic_update_high_score_label(self):
        """
        Update the high score label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_high_score_label_ = self.config.get('Classic_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.classic_high_score_label.configure(text=f"Score: {self.classic_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_time_label(self):
        """
        Create the time label for the classic snake game.
        """
        self.classic_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Time: {self.classic_score_label_} Seconds",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_time_label.place(x=200, y=100)

    def classic_update_time_label(self):
        """
        Update the time label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_time_label_ = self.config.get('Classic_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.classic_time_label.configure(text=f"Time: {self.classic_time_label_} Seconds")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_time_label(self):
        """
        Create the high score time label for the classic snake game.
        """
        self.classic_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score Time: {self.classic_score_label_} Seconds", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_high_score_time_label.place(x=200, y=600)

    def classic_update_high_score_time_label(self):
        """
        Update the high score time label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_high_score_time_label_ = self.config.get('Classic_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_high_score_time_label.configure(text=f"Score Time: {self.classic_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_snake_length_label(self):
        """
        Create the snake length label for the classic snake game.
        """
        self.classic_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_snake_length_label.place(x=200, y=150)

    def classic_update_snake_length_label(self):
        """
        Update the snake length label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_snake_length_label.configure(text=f"Snake Length: {self.classic_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the classic snake game.
        """
        self.classic_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_high_score_snake_length_label.place(x=200, y=650)

    def classic_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the classic snake game.
        """
        try:
            self.config_file_read_write()
            self.classic_high_score_snake_length_label_ = self.config.get('Classic_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.classic_high_score_snake_length_label.configure(text=f"Snake Length: {self.classic_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def classic_create_high_scores_label(self):
        """
        Create the high scores label for the classic snake game.
        """
        self.classic_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="High Scores:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.classic_high_scores_label.place(x=200, y=500)

    def classic_reset_labels(self):
        """
        Reset the labels for the classic snake game.
        """
        self.classic_score_label.configure(text='0')
        self.classic_time_label.configure(text='0')

    def classic_delete_labels(self):
        """
        Delete the labels for the classic snake game.
        """
        try:
            if self.classic_score_label is not None:
                self.classic_score_label.destroy()
            if self.classic_time_label is not None:
                self.classic_time_label.destroy()
            if self.classic_high_score_label is not None:
                self.classic_high_score_label.destroy()
            if self.classic_high_score_time_label is not None:
                self.classic_high_score_time_label.destroy()
            if self.classic_high_scores_label is not None:
                self.classic_high_scores_label.destroy()
            if self.classic_snake_length_label is not None:
                self.classic_snake_length_label.destroy()
            if self.classic_high_score_snake_length_label is not None:
                self.classic_high_score_snake_length_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)


    def endless_create_game_labels(self):
        """
        Create the game labels for the endless snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long
        self.endless_create_score_label()
        self.endless_create_time_label()
        self.endless_create_snake_length_label()
        self.endless_create_special_score_label()
        self.endless_create_shorten_score_label()

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.endless_create_high_score_label()
            self.endless_create_high_score_time_label()
            self.endless_create_high_scores_label()
            self.endless_create_high_score_snake_length_label()
            self.endless_create_special_high_score_label()
            self.endless_create_shorten_high_score_label()

    def endless_update_high_score_labels(self):
        """
        Update the high score labels for the endless snake game.
        """

        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long
        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default': # pylint: disable=line-too-long
            self.endless_update_high_score_label()
            self.endless_update_high_score_time_label()
            self.endless_update_high_score_snake_length_label()
            self.endless_update_special_high_score_label()
            self.endless_update_shorten_high_score_label()

    def endless_update_game_labels(self):
        """
        Update the game labels for the endless snake game.
        """
        self.endless_update_score_label()
        self.endless_update_time_label()
        self.endless_update_snake_length_label()
        self.endless_update_special_score_label()
        self.endless_update_shorten_score_label()

    def endless_create_high_scores_label(self):
        """
        Create the high scores label for the endless snake game.
        """
        self.endless_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="High Scores:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_high_scores_label.place(x=200, y=400)

    def endless_create_score_label(self):
        """
        Create the score label for the endless snake game.
        """
        self.endless_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score:{self.endless_score_label_}",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_score_label.place(x=200, y=50)

    def endless_update_score_label(self):
        """
        Update the score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_score_label_ = self.config.get('Endless_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.endless_score_label.configure(text=f"Score: {self.endless_score_label_} ")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_label(self):
        """
        Create the high score label for the endless snake game.
        """
        self.endless_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score: {self.endless_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_high_score_label.place(x=200, y=450)

    def endless_update_high_score_label(self):
        """
        Update the high score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_high_score_label_ = self.config.get('Endless_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_high_score_label.configure(text=f"Score: {self.endless_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_time_label(self):
        """
        Create the time label for the endless snake game.
        """
        self.endless_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Time: {self.endless_time_label_} Seconds",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_time_label.place(x=200, y=100)

    def endless_update_time_label(self):
        """
        Update the time label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_time_label_ = self.config.get('Endless_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.endless_time_label.configure(text=f"Time: {self.endless_time_label_} Seconds")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_time_label(self):
        """
        Create the high score time label for the endless snake game.
        """
        self.endless_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score Time: {self.endless_time_label_} Seconds", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_high_score_time_label.place(x=200, y=500)

    def endless_update_high_score_time_label(self):
        """
        Update the high score time label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_high_score_time_label_ = self.config.get('Endless_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_high_score_time_label.configure(text=f"Score Time: {self.endless_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_snake_length_label(self):
        """
        Create the snake length label for the endless snake game.
        """
        self.endless_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_snake_length_label.place(x=200, y=150)

    def endless_update_snake_length_label(self):
        """
        Update the snake length label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_snake_length_label_ = self.config.get('Endless_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_snake_length_label.configure(text=f"Snake Length: {self.endless_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the endless snake game.
        """
        self.endless_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_high_score_snake_length_label.place(x=200, y=550)

    def endless_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_high_score_snake_length_label_ = self.config.get('Endless_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.endless_high_score_snake_length_label.configure(text=f"Snake Length: {self.endless_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_special_score_label(self):
        """
        Create the special score label for the endless snake game.
        """
        self.endless_special_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Special Score:{self.endless_special_score_label} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_special_score_label.place(x=200, y=200)

    def endless_update_special_score_label(self):
        """
        Update the special score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_special_score_label_ = self.config.get('Endless_Snake_Values', 'special_score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.endless_special_score_label.configure(text=f"Special Score: {self.endless_special_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_special_high_score_label(self):
        """
        Create the special high score label for the endless snake game.
        """
        self.endless_special_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Special Score: {self.endless_special_high_score_label} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor )
        self.endless_special_high_score_label.place(x=200, y=600)

    def endless_update_special_high_score_label(self):
        """
        Update the special high score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_special_high_score_label_ = self.config.get('Endless_Snake_Values', 'special_score_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_special_high_score_label.configure(text=f"Special Score: {self.endless_special_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_shorten_score_label(self):
        """
        Create the shorten score label for the endless snake game.
        """
        self.endless_shorten_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Shorten Score: {self.endless_shorten_score_label} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_shorten_score_label.place(x=200, y=250)

    def endless_update_shorten_score_label(self):
        """
        Update the shorten score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_shorten_score_label_ = self.config.get('Endless_Snake_Values', 'shorten_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_shorten_score_label.configure(text=f"Shorten Score: {self.endless_shorten_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_create_shorten_high_score_label(self):
        """
        Create the shorten high score label for the endless snake game.
        """
        self.endless_shorten_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Shorten Score: {self.endless_shorten_high_score_label} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.endless_shorten_high_score_label.place(x=200, y=650)

    def endless_update_shorten_high_score_label(self):
        """
        Update the shorten high score label for the endless snake game.
        """
        try:
            self.config_file_read_write()
            self.endless_shorten_high_score_label_ = self.config.get('Endless_Snake_Values', 'shorten_snake_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.endless_shorten_high_score_label.configure(text=f"Shorten Score: {self.endless_shorten_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def endless_reset_labels(self):
        """
        Reset the labels for the endless snake game.
        """
        self.endless_score_label.configure(text='0')
        self.endless_time_label.configure(text='0')

    def endless_delete_labels(self):
        """
        Delete the labels for the endless snake game.
        """
        try:
            if self.endless_score_label is not None:
                self.endless_score_label.destroy()
            if self.endless_time_label is not None:
                self.endless_time_label.destroy()
            if self.endless_high_score_label is not None:
                self.endless_high_score_label.destroy()
            if self.endless_high_score_time_label is not None:
                self.endless_high_score_time_label.destroy()
            if self.endless_high_scores_label is not None:
                self.endless_high_scores_label.destroy()
            if self.endless_snake_length_label is not None:
                self.endless_snake_length_label.destroy()
            if self.endless_high_score_snake_length_label is not None:
                self.endless_high_score_snake_length_label.destroy()
            if self.endless_special_score_label is not None:
                self.endless_special_score_label.destroy()
            if self.endless_special_high_score_label is not None:
                self.endless_special_high_score_label.destroy()
            if self.endless_shorten_score_label is not None:
                self.endless_shorten_score_label.destroy()
            if self.endless_shorten_high_score_label is not None:
                self.endless_shorten_high_score_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)

    def leveling_create_game_labels(self):
        """
        Create the game labels for the leveling snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        self.leveling_create_score_label()
        self.leveling_create_time_label()
        self.leveling_create_snake_length_label()
        self.leveling_create_xp_label()
        self.leveling_create_level_label()

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.leveling_create_high_score_label()
            self.leveling_create_high_score_time_label()
            self.leveling_create_high_scores_label()
            self.leveling_create_high_score_snake_length_label()
            self.leveling_create_xp_high_score_label()
            self.leveling_create_level_high_score_label()

    def leveling_update_high_score_labels(self):
        """
        Update the high score labels for the leveling snake game.
        """
        self.config.read(self.config_path)
        self.high_score_label_needed = self.config.get('Settings', 'label_needed_high_score', fallback='Default') # pylint: disable=line-too-long

        if self.high_score_label_needed == 'True' or self.high_score_label_needed == 'Default':
            self.leveling_update_high_score_label()
            self.leveling_update_high_score_time_label()
            self.leveling_update_high_score_snake_length_label()
            self.leveling_update_xp_high_score_label()
            self.leveling_update_level_high_score_label()

    def leveling_create_high_scores_label(self):
        """
        Create the high scores label for the leveling snake game.
        """
        self.leveling_high_scores_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="High Scores:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_high_scores_label.place(x=200, y=300)

    def leveling_update_game_labels(self):
        """
        Update the game labels for the leveling snake game.
        """
        self.leveling_update_score_label()
        self.leveling_update_time_label()
        self.leveling_update_snake_length_label()
        self.leveling_update_xp_label()
        self.leveling_update_level_label()

    def leveling_create_score_label(self):
        """
        Create the score label for the leveling snake game.
        """
        self.leveling_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score:{self.leveling_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_score_label.place(x=200, y=50)

    def leveling_update_score_label(self):
        """
        Update the score label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_score_label_ = self.config.get('Leveling_Snake_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the score label on the screen
            self.leveling_score_label.configure(text=f"Score: {self.leveling_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_label(self):
        """
        Create the high score label for the leveling snake game.
        """
        self.leveling_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score: {self.leveling_score_label_} ", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_high_score_label.place(x=200, y=350)

    def leveling_update_high_score_label(self):
        """
        Update the high score label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_high_score_label_ = self.config.get('Leveling_Snake_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score label on the screen
            self.leveling_high_score_label.configure(text=f"Score: {self.leveling_high_score_label_} ") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_time_label(self):
        """
        Create the time label for the leveling snake game.
        """
        self.leveling_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Time: {self.leveling_score_label_} Seconds",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_time_label.place(x=200, y=100)

    def leveling_update_time_label(self):
        """
        Update the time label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_time_label_ = self.config.get('Leveling_Snake_Values', 'time_score', fallback='0') # pylint: disable=line-too-long
            #update the time label on the screen
            self.leveling_time_label.configure(text=f"Time: {self.leveling_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_time_label(self):
        """
        Create the high score time label for the leveling snake game.
        """
        self.leveling_high_score_time_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score Time: {self.leveling_score_label_} Seconds", # pylint: disable=line-too-long
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_high_score_time_label.place(x=200, y=400)

    def leveling_update_high_score_time_label(self):
        """
        Update the high score time label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_high_score_time_label_ = self.config.get('Leveling_Snake_Values', 'high_score_time', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_high_score_time_label.configure(text=f"Score Time: {self.leveling_high_score_time_label_} Seconds") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_snake_length_label(self):
        """
        Create the snake length label for the leveling snake game.
        """
        self.leveling_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_snake_length_label.place(x=200, y=150)

    def leveling_update_snake_length_label(self):
        """
        Update the snake length label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_snake_length_label_ = self.config.get('Leveling_Snake_Values', 'snake_length', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_snake_length_label.configure(text=f"Snake Length: {self.leveling_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_high_score_snake_length_label(self):
        """
        Create the high score snake length label for the leveling snake game.
        """
        self.leveling_high_score_snake_length_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Snake Length:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_high_score_snake_length_label.place(x=200, y=450)

    def leveling_update_high_score_snake_length_label(self):
        """
        Update the high score snake length label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_high_score_snake_length_label_ = self.config.get('Leveling_Snake_Values', 'snake_length_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_high_score_snake_length_label.configure(text=f"Snake Length: {self.leveling_high_score_snake_length_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_xp_label(self):
        """
        Create the xp label for the leveling snake game.
        """
        self.leveling_xp_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="XP hello:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_xp_score_label.place(x=500, y=10)

    def leveling_update_xp_label(self):
        """
        Update the xp label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_xp_score_label_ = self.config.get('Leveling_Snake_Values', 'xp', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_xp_score_label.configure(text=f"XP Hello: {self.leveling_xp_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_xp_high_score_label(self):
        """
        Create the xp high score label for the leveling snake game.
        """
        self.leveling_xp_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="XP:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_xp_high_score_label.place(x=200, y=500)

    def leveling_update_xp_high_score_label(self):
        """
        Update the xp high score label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_xp_high_score_label_ = self.config.get('Leveling_Snake_Values', 'xp_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_xp_high_score_label.configure(text=f"XP: {self.leveling_xp_high_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_level_label(self):
        """
        Create the level label for the leveling snake game.
        """
        self.leveling_level_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Level:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_level_score_label.place(x=800, y=10)

    def leveling_update_level_label(self):
        """
        Update the level label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_level_score_label_ = self.config.get('Leveling_Snake_Values', 'level', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_level_score_label.configure(text=f"Level: {self.leveling_level_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_create_level_high_score_label(self):
        """
        Create the level high score label for the leveling snake game.
        """
        self.leveling_level_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text="Level:",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.leveling_level_high_score_label.place(x=200, y=550)

    def leveling_update_level_high_score_label(self):
        """
        Update the level high score label for the leveling snake game.
        """
        try:
            self.config_file_read_write()
            self.leveling_level_high_score_label_ = self.config.get('Leveling_Snake_Values', 'level_high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.leveling_level_high_score_label.configure(text=f"level: {self.leveling_level_high_score_label_}") # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def leveling_reset_labels(self):
        """
        Reset the labels for the leveling snake game.
        """
        self.leveling_score_label.configure(text='0')
        self.leveling_time_label.configure(text='0')

    def leveling_delete_labels(self):
        """
        Delete the labels for the leveling snake game.
        """
        try:
            if self.leveling_score_label is not None:
                self.leveling_score_label.destroy()
            if self.leveling_time_label is not None:
                self.leveling_time_label.destroy()
            if self.leveling_high_score_label is not None:
                self.leveling_high_score_label.destroy()
            if self.leveling_high_score_time_label is not None:
                self.leveling_high_score_time_label.destroy()
            if self.leveling_high_scores_label is not None:
                self.leveling_high_scores_label.destroy()
            if self.leveling_snake_length_label is not None:
                self.leveling_snake_length_label.destroy()
            if self.leveling_high_score_snake_length_label is not None:
                self.leveling_high_score_snake_length_label.destroy()
            if self.leveling_xp_score_label is not None:
                self.leveling_xp_score_label.destroy()
            if self.leveling_xp_high_score_label is not None:
                self.leveling_xp_high_score_label.destroy()
            if self.leveling_level_score_label is not None:
                self.leveling_level_score_label.destroy()
            if self.leveling_level_high_score_label is not None:
                self.leveling_level_high_score_label.destroy()
        except ValueError as e:
            traceback.print_exc(e)

    def challange_create_game_labels(self):
        """
        Create the game labels for the challange snake game.
        """
        self.config.read(self.config_path)
        self.score_label_needed = self.config.get('Settings', 'label_needed_score', fallback='Default') # pylint: disable=line-too-long
        self.challange_create_score_label()

        if self.score_label_needed == 'True' or self.score_label_needed == 'Default':
            self.challange_create_high_score_label()

    def challange_update_game_labels(self):
        """
        Update the game labels for the challange snake game.
        """
        self.challange_update_score_label()

    def challange_update_high_score_labels(self):
        """
        Update the high score labels for the challange snake game.
        """
        self.config.read(self.config_path)
        self.score_label_needed = self.config.get('Settings', 'label_needed_score', fallback='Default') # pylint: disable=line-too-long

        if self.score_label_needed == 'True' or self.score_label_needed == 'Default':
            self.challange_update_high_score_label()

    def challange_create_score_label(self):
        """
        Create the score label for the challange snake game.
        """
        self.challange_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score:{self.challange_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.challange_score_label.place(x=200, y=500)  # adjust the position as needed

    def challange_update_score_label(self):
        """
        Update the score label for the challange snake game.
        """
        try:
            self.config_file_read_write()
            self.challange_score_label_ = self.config.get('food_time_attack_Values', 'score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.challange_score_label.configure(text=f"Score: {self.challange_score_label_}")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def challange_create_high_score_label(self):
        """
        Create the high score label for the challange snake game.
        """
        self.challange_high_score_label = ctk.CTkLabel(self.snake_canvas,
                                            width=self.width,
                                            height=self.height,
                                            corner_radius=self.corner_radius,
                                            text=f"Score:{self.challange_score_label_} ",
                                            font=FONT_LIST[11],
                                            bg_color='grey20',
                                            anchor=self.anchor)
        self.challange_high_score_label.place(x=200, y=550)

    def challange_update_high_score_label(self):
        """
        Update the high score label for the challange snake game.
        """
        try:
            self.config_file_read_write()
            self.challange_high_score_label_ = self.config.get('food_time_attack_Values', 'high_score', fallback='0') # pylint: disable=line-too-long
            #update the high score time label on the screen
            self.challange_high_score_label.configure(text=f"level: {self.challange_score_label_}")
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def challange_reset_labels(self):
        """
        Reset the labels for the challange snake game.
        """
        self.challange_score_label.configure(text='0')

    def challange_delete_labels__(self):
        """
        Delete the labels for the challange snake game.
        """
        try:
            if self.challange_score_label is not None:
                self.challange_score_label.destroy()
                self.game_logger.log_game_event('Deleted score challange')
            if self.challange_high_score_label is not None:
                self.challange_high_score_label.destroy()
                self.game_logger.log_game_event('Deleted high score challange')
            self.game_logger.log_game_event('Deleted Labels challange')
        except ValueError as e:
            traceback.print_exc(e)
