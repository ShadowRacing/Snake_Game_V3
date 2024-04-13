# *****************************************
# Shadows Snake Food Logic File
# *****************************************

#Importing the required modules
import uuid, random, time, traceback, configparser

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import GameConstants

#Class for the food logic
class ClassicFood:
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
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event("Food ID:")
                self.game_logger.log_game_event(food_id)
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(self.food_items)
        except Exception as e:
            traceback.print_exc(e)

    #Creating the food oval
    def create_food_oval(self, x, y, fill_color, tag):
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag)


    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        try: 
            while True:
                x = random.randint(0, (GameConstants.GAME_WIDTH / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                y = random.randint(0, (GameConstants.GAME_HEIGHT / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates)
                if not collision:
                    break
            return x, y
        except Exception as e:
            traceback.print_exc(e)

class EndlessFood:
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
        self.game_config = game_config
        self.occupied_coordinates = set()
        try:
            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
            self.score = int(self.config.get('Endless_Snake_Values', 'score', fallback='0'))
        except Exception as e:
            traceback.print_exc(e)

    def add_occuppied_coordinates(self, x, y):
        self.occupied_coordinates.add((x, y))
        print(self.occupied_coordinates)

    def remove_occuppied_coordinates(self, x, y):
        self.occupied_coordinates.remove((x, y))
    
    def is_occupied(self, x, y):
        return (x, y) in self.occupied_coordinates

    #Food logic
    def spawn_food(self, snake_coordinates, score):
        num_food_items = min(score // 50 + 1, 10)
        self.game_logger.log_game_event("Number off food items: ")
        self.game_logger.log_game_event(num_food_items)

        try:
            while len(self.food_items) < num_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event("Food ID:")
                self.game_logger.log_game_event(food_id)
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(self.food_items)
        except Exception as e:
            traceback.print_exc(e)
    
    #Special food logic
    def special_spawn_food(self, snake_coordinates):
        num_special_food_items = 1
        try:
            while len(self.special_food_items) < num_special_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                special_food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(special_food_id)
                tag = "specialfood" + special_food_id
                special_oval_id = self.create_food_oval(x, y, self.game_config.SPECIAL_FOOD_COLOR, tag)
                self.special_food_items[special_food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': special_oval_id}
                self.game_logger.log_game_event("Special Food ID:")
                self.game_logger.log_game_event(special_food_id)
        except Exception as e:
            traceback.print_exc(e)

    def shorten_spawn_food(self, snake_coordinates):
        num_shorten_food_items = 1
        try:
            while len(self.shorten_food_items) < num_shorten_food_items:
                x, y = self.generate_random_coordinates(snake_coordinates)
                self.add_occuppied_coordinates(x, y)
                shorten_food_id = str(uuid.uuid4())
                self.game_logger.log_game_event(shorten_food_id)
                tag = "shortenfood" + shorten_food_id
                shorten_oval_id = self.create_food_oval(x, y, self.game_config.SHORTEN_FOOD_COLOR, tag)
                self.shorten_food_items[shorten_food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': shorten_oval_id}
                self.game_logger.log_game_event("Shorten Food ID:")
                self.game_logger.log_game_event(shorten_food_id)
        except Exception as e:
            traceback.print_exc(e)

    #Creating the food oval
    def create_food_oval(self, x, y, fill_color, tag):
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag)

    def reset_food(self):
        self.food_items.clear()
        self.special_food_items.clear()
        self.shorten_food_items.clear()
        self.occupied_coordinates.clear()

    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        try:    
            while True:
                x = random.randint(0, (GameConstants.GAME_WIDTH / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                y = random.randint(0, (GameConstants.GAME_HEIGHT / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates)
                if not collision and not self.is_occupied(x, y):
                    break
            return x, y
        except Exception as e:
            traceback.print_exc(e)
    
class LevelingFood:
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
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event("Food ID:")
                self.game_logger.log_game_event(food_id)
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(self.food_items)
        except Exception as e:
            traceback.print_exc(e)

    #Creating the food oval
    def create_food_oval(self, x, y, fill_color, tag):
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag)


    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        try: 
            while True:
                x = random.randint(0, (GameConstants.GAME_WIDTH / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                y = random.randint(0, (GameConstants.GAME_HEIGHT / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates)
                if not collision:
                    break
            return x, y
        except Exception as e:
            traceback.print_exc(e)

class ChallangeFood:
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
        try:
            if len(self.food_items) == 0:  # Check if no food items are currently on the screen
                x, y = self.generate_random_coordinates(snake_coordinates)
                food_id = str(uuid.uuid4())
                self.game_logger.log_game_event("Food ID:")
                self.game_logger.log_game_event(food_id)
                tag = "food" + food_id
                oval_id = self.create_food_oval(x, y, self.game_config.FOOD_COLOR, tag)
                self.food_items[food_id] = {'x': x, 'y': y, 'tag': tag, 'oval_id': oval_id}
                self.game_logger.log_game_event(self.food_items)
        except Exception as e:
            traceback.print_exc(e)

    #Creating the food oval
    def create_food_oval(self, x, y, fill_color, tag):
        return self.canvas.create_oval(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=fill_color, tag=tag)


    #Creating random coordinates for the food to spawn, and also chechking where the snake is.
    def generate_random_coordinates(self, snake_coordinates):
        try: 
            while True:
                x = random.randint(0, (GameConstants.GAME_WIDTH / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                y = random.randint(0, (GameConstants.GAME_HEIGHT / self.game_config.CELL_SIZE) - 1) * self.game_config.CELL_SIZE
                collision = any(x == segment[0] and y == segment[1] for segment in snake_coordinates)
                if not collision:
                    break
            return x, y
        except Exception as e:
            traceback.print_exc(e)


# *****************************************
# Shadows Snake Food Logic File
# *****************************************