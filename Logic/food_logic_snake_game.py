# *****************************************
# Shadows Snake Food Logic File
# *****************************************

"""
This module contains the food logic for the Shadows Snake game.
"""

#Importing the required modules
import uuid
import time
import traceback
import configparser
import secrets

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import GameConstants

class ClassicFood:
    """
    Class for the food logic of the Shadows Snake game.
    """
    def __init__(self, game_logger, canvas, game_config):
        #Initializing variables
        self.time = time.time()
        self.game_logger = game_logger
        self.canvas = canvas
        self.food_items = {}
        self.food_coordinates = {}
        self.game_config = game_config


    #Food logic
    def spawn_food(self, snake_coordinates):
        """
        Spawn food on the game canvas.
        """
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(f"Food ID: {food_id}")
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(f"Food items: {self.food_items}")
        except ValueError as e:
            traceback.print_exc(e)

    def create_food_oval(self, x, y, fill_color, tag):
        """
        Create a food oval on the game canvas.
        """
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag) # pylint: disable=line-too-long

    def generate_random_coordinates(self, snake_coordinates):
        """
        Generate random coordinates for the food to spawn on the game canvas.
        """
        try:
            while True:
                x = secrets.randbelow((GameConstants.GAME_WIDTH // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                y = secrets.randbelow((GameConstants.GAME_HEIGHT // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates) # pylint: disable=line-too-long
                if not collision:
                    break
            return x, y
        except ValueError as e:
            traceback.print_exc(e)

class EndlessFood:
    """
    Class for the food logic of the Shadows Snake game.
    """
    def __init__(self, game_logger, canvas, game_config):
        #Initializing variables
        self.time = time.time()
        self.game_logger = game_logger
        self.canvas = canvas
        self.food_items = {}
        self.special_food_items = {}
        self.shorten_food_items = {}
        self.food_coordinates = {}
        self.special_food_coordinates = {}
        self.shorten_food_coordinates = {}
        self.num_food_items = 0
        self.game_config = game_config
        self.occupied_coordinates = set()
        try:
            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
            self.score = int(self.config.get('Endless_Snake_Values', 'score', fallback='0'))
        except FileNotFoundError as e:
            traceback.print_exc(e)

    def add_occuppied_coordinates(self, x, y):
        """
        Add occupied coordinates to the set.
        """
        self.occupied_coordinates.add((x, y))
        self.game_logger.log_game_event(f"Occupied coordinates for food: {self.occupied_coordinates}")

    def remove_occuppied_coordinates(self, x, y):
        """
        Removes occupied coordinates from the set.
        """
        self.occupied_coordinates.remove((x, y))

    def is_occupied(self, x, y):
        """
        Check if the coordinates are occupied.
        """
        return (x, y) in self.occupied_coordinates

    def spawn_food(self, snake_coordinates, score):
        """
        Spawn food on the game canvas.
        """
        self.num_food_items = min(score // 50 + 1, 10)

        try:
            while len(self.food_items) < self.num_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(f"Food ID: {food_id}")
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(f"Food items: {self.food_items}")
                self.game_logger.log_game_event(f"Number off food items: {self.num_food_items}")
        except ValueError as e:
            traceback.print_exc(e)

    def special_spawn_food(self, snake_coordinates):
        """
        Spawn special food on the game canvas.
        """
        num_special_food_items = 1
        try:
            while len(self.special_food_items) < num_special_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                special_food_id = str(uuid.uuid4())
                tag = "specialfood" + special_food_id
                special_oval_id = self.create_food_oval(x, y, self.game_config.SPECIAL_FOOD_COLOR, tag) # pylint: disable=line-too-long
                self.special_food_items[special_food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': special_oval_id} # pylint: disable=line-too-long
                self.game_logger.log_game_event(f"Special Food ID: {special_food_id}")
        except ValueError as e:
            traceback.print_exc(e)

    def shorten_spawn_food(self, snake_coordinates):
        """
        Spawn shorten food on the game canvas.
        """
        num_shorten_food_items = 1
        try:
            while len(self.shorten_food_items) < num_shorten_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                shorten_food_id = str(uuid.uuid4())
                tag = "shortenfood" + shorten_food_id
                shorten_oval_id = self.create_food_oval(x, y, self.game_config.SHORTEN_FOOD_COLOR, tag) # pylint: disable=line-too-long
                self.shorten_food_items[shorten_food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': shorten_oval_id} # pylint: disable=line-too-long
                self.game_logger.log_game_event(f"Shorten Food ID: {shorten_food_id}")
        except ValueError as e:
            traceback.print_exc(e)

    def create_food_oval(self, x, y, fill_color, tag):
        """
        Create a food oval on the game canvas.
        """
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag) # pylint: disable=line-too-long

    def reset_food(self):
        """
        Reset the food items.
        """
        self.food_items.clear()
        self.special_food_items.clear()
        self.shorten_food_items.clear()
        self.occupied_coordinates.clear()

    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        """
        Generate random coordinates for the food to spawn on the game canvas.
        """
        try:
            while True:
                x = secrets.randbelow((GameConstants.GAME_WIDTH // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                y = secrets.randbelow((GameConstants.GAME_HEIGHT // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates) # pylint: disable=line-too-long
                if not collision and not self.is_occupied(x, y):
                    break
            return x, y
        except ValueError as e:
            traceback.print_exc(e)


class LevelingFood:
    """
    Class for the food logic of the Shadows Snake game.
    """
    def __init__(self, game_logger, canvas, game_config):
        #Initializing variables
        self.time = time.time()
        self.game_logger = game_logger
        self.canvas = canvas
        self.food_items = {}
        self.food_coordinates = {}
        self.game_config = game_config

    def spawn_food(self, snake_coordinates):
        """
        Spawn food on the game canvas.
        """
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(f"Food ID: {food_id}")
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(f"Food items: {self.food_items}")
        except ValueError as e:
            traceback.print_exc(e)

    #Creating the food oval
    def create_food_oval(self, x, y, fill_color, tag):
        """
        Create a food oval on the game canvas.
        """
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag) # pylint: disable=line-too-long

    def generate_random_coordinates(self, snake_coordinates):
        """
        Generate random coordinates for the food to spawn on the game canvas.
        """
        try:
            while True:
                x = secrets.randbelow((GameConstants.GAME_WIDTH // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                y = secrets.randbelow((GameConstants.GAME_HEIGHT // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates) # pylint: disable=line-too-long
                if not collision:
                    break
            return x, y
        except ValueError as e:
            traceback.print_exc(e)

class ChallangeFood:
    """
    Class for the food logic of the Shadows Snake game.
    """
    def __init__(self, game_logger, canvas, game_config):
        #Initializing variables
        self.time = time.time()
        self.game_logger = game_logger
        self.canvas = canvas
        self.food_items = {}
        self.food_coordinates = {}
        self.game_config = game_config

    def spawn_food(self, snake_coordinates):
        """
        Spawn food on the game canvas.
        """
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(f"Food ID: {food_id}")
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(f"Food items: {self.food_items}")
        except ValueError as e:
            traceback.print_exc(e)

    def create_food_oval(self, x, y, fill_color, tag):
        """
        Create a food oval on the game canvas.
        """
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag) # pylint: disable=line-too-long

    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        """
        Generate random coordinates for the food to spawn on the game canvas.
        """
        try:
            while True:
                x = secrets.randbelow((GameConstants.GAME_WIDTH // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                y = secrets.randbelow((GameConstants.GAME_HEIGHT // self.game_config.CELL_SIZE)) * self.game_config.CELL_SIZE # pylint: disable=line-too-long
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates) # pylint: disable=line-too-long
                if not collision:
                    break
            return x, y
        except ValueError as e:
            traceback.print_exc(e)


# *****************************************
# Shadows Snake Food Logic File
# *****************************************
