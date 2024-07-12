"""
File contains functions to open, read and update config files and json files.
"""

import configparser
import traceback
import json
import os
from os import path

class ConfigAndFileUtils:
    """
    Class contains functions to open, read and update config files and json files.
    """
    def __init__(self):
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, 'config.ini')
        self.config = configparser.ConfigParser()

    def open_config_file(self):
        """
        Open the config.ini file.
        """
        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)
        try:
            with open(self.config_path, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def read_config_file(self):
        """
        Read the config.ini file.
        """
        try:
            self.config.read('config.ini')
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def update_config_file(self):
        """
        Update the config.ini file.
        """
        try:
            with open(self.config_path, 'w', encoding='utf 8') as configfile:
                self.config.write(configfile)
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def open_patchnotes_file(self):
        """
        Open the patchnotes.json file.
        """
        try:
            with open("patchnotes.json", "r", encoding='utf-8') as configfile:
                patchnotes = json.load(configfile)
                return patchnotes
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def open_colors_json_file(self):
        """
        Open the colors.json file.
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            with open(os.path.join(script_dir, '..', 'Themes', 'colors.json'), 'r', encoding='utf-8') as colors: # pylint: disable=line-too-long
                COLORS_DICT = json.load(colors) # pylint: disable=invalid-name
                return COLORS_DICT

        except FileNotFoundError as e:
            traceback.print_exc(e)

    def open_snake_color_file(self):
        """
        Open the snake_colors.json file.
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            with open(os.path.join(script_dir, '..', 'Themes', 'snake_colors.json'), 'r', encoding='utf-8') as colors: # pylint: disable=line-too-long
                SNAKE_COLOR_DICT = json.load(colors) # pylint: disable=invalid-name
                return SNAKE_COLOR_DICT
        except FileNotFoundError as e:
            traceback.print_exc(e)
