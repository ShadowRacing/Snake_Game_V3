# *****************************************
# Shadows Snake Game Snake Endless Game File
# *****************************************

"""
This module contains the Snake_endless class which is responsible for the endless game mode of the Shadows Snake game. # pylint: disable=line-too-long
"""

import time
import configparser
import traceback
import secrets
from os import path
from PIL import Image

import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST, GameConstants
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import EndlessFood
from Logic.snake_logic_snake_game import Snake
from Logic.game_labelpanel import GameLabelsPanel
from Logic.buttonpanel_snake_game import ClickButtonPanel

class SnakeEndless(ctk.CTkCanvas):
    """
    Class for the endless game mode of the Shadows Snake game.
    """
    def __init__(self, parent, game_config, game_logger, functions, create_button_panel):
        # Create the game logger
        self.game_logger = game_logger
        self.game_config = game_config
        self.functions = functions
        self.create_button_panel = create_button_panel
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.config_path_icon = path.join(self.config_dir, "..", 'app_icon.ico')
        self.game_logger.log_game_event(f"Config file read in Endless snake game file: {self.config_path}") # pylint: disable=line-too-long


        # Game configuration
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        self.game_logger.log_game_event(f"Snake length: {self.snake_length}")
        self.game_logger.log_game_event(f"Game width: {self.width}")
        self.game_logger.log_game_event(f"Game height: {self.height}")
        self.game_logger.log_game_event(f"Highlight thickness: {self.highlightthickness}")
        self.game_logger.log_game_event(f"Highlight background: {self.highlightbackground}")
        self.game_logger.log_game_event(f"Initial direction of snake: {self.direction}")

        # Game state
        self.score = 0
        self.special_score = 0
        self.shorten_score = 0
        self.game_over_flag = False
        self.paused = False
        self.has_changed_direction = False
        self.next_special_food_score = 50
        self.next_shorten_food_score = 100
        self.next_food_score = 0

        self.game_logger.log_game_event(f"Initial score: {self.score}")
        self.game_logger.log_game_event(f"Initial special score: {self.special_score}")
        self.game_logger.log_game_event(f"Initial shorten score: {self.shorten_score}")
        self.game_logger.log_game_event(f"Game over flag: {self.game_over_flag}")
        self.game_logger.log_game_event(f"Game paused: {self.paused}")
        self.game_logger.log_game_event(f"Has changed direction: {self.has_changed_direction}")
        self.game_logger.log_game_event(f"Next special food score: {self.next_special_food_score}")
        self.game_logger.log_game_event(f"Next shorten food score: {self.next_shorten_food_score}")
        self.game_logger.log_game_event(f"Next food score: {self.next_food_score}")

        # Time-related variables
        self.start_time = None
        self.paused_time = None
        self.total_paused_time = 0
        self.total_time_played = 0
        self.total_time_paused = 0
        self.last_direction_change_time = 0
        self.pause_duration = 0
        self.high_score_time = 0
        self.current_time = 0
        self.get_time_score = 0
        self.get_snake_length = 0

        self.game_logger.log_game_event("Time-related variables initialized.")
        self.game_logger.log_game_event(f"Start time: {self.start_time}")
        self.game_logger.log_game_event(f"Paused time: {self.paused_time}")
        self.game_logger.log_game_event(f"Total paused time: {self.total_paused_time}")
        self.game_logger.log_game_event(f"Total time played: {self.total_time_played}")
        self.game_logger.log_game_event(f"Total time paused: {self.total_time_paused}")
        self.game_logger.log_game_event(f"Last direction change time: {self.last_direction_change_time}") # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Pause duration: {self.pause_duration}")
        self.game_logger.log_game_event(f"High score time: {self.high_score_time}")
        self.game_logger.log_game_event(f"Current time: {self.current_time}")
        self.game_logger.log_game_event(f"Get time score: {self.get_time_score}")
        self.game_logger.log_game_event(f"Get snake length: {self.get_snake_length}")

        # High scores
        self.high_score = 0
        self.snake_length_high_score = 0
        self.special_score_high_score = 0
        self.shorten_score_high_score = 0

        self.game_logger.log_game_event("High scores initialized")
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Snake length high score: {self.snake_length_high_score}")
        self.game_logger.log_game_event(f"Special score high score: {self.special_score_high_score}") # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Shorten score high score: {self.shorten_score_high_score}") # pylint: disable=line-too-long

        # Other variables
        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.random_number_off_shorten_food = 0
        self.get_special_high_score = 0
        self.get_shorten_high_score = 0

        # Print statements
        self.game_logger.log_game_event(f"Width: {self.width}")
        self.game_logger.log_game_event(f"Height: {self.height}")

        self.snake_canvas_x = GameConstants.GAME_CANVAS_PLACE_X
        self.snake_canvas_y = GameConstants.GAME_CANVAS_PLACE_Y

        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                         highlightbackground=self.highlightbackground)

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,  highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                                          highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=self.snake_canvas_x, y=self.snake_canvas_y)

        # Create the snake and the food
        self.snake = Snake(self.game_logger, self.snake_canvas, game_config)
        self.food = EndlessFood(self.game_logger, self.snake_canvas, game_config)
        self.game_labels_panel_2 = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'snake_endless')
        self.create_button_panel = ClickButtonPanel(parent, self.game_logger, self.functions) # pylint: disable=line-too-long

        self.game_labels_panel_2.endless_create_game_labels()

        # Create the endless snake game labels
        self.state = 'start_game'
        self.config.set('Endless_Snake_Settings', 'state', self.state)
        self.config.set('Settings', 'home_button_state', 'normal')
        self.config.set('Settings', 'endless_reset_high_score_button_state', 'normal')
        self.config.set('Settings', 'endless_reset_high_score_time_button_state', 'normal')
        self.config.set('Settings', 'endless_reset_high_score_snake_length_button_state', 'normal')
        self.config.set('Settings', 'endless_reset_high_score_special_button_state', 'normal')
        self.config.set('Settings', 'endless_reset_high_score_shorten_button_state', 'normal')
        self.write_changes_to_configini()

        try:
            self.create_and_place_image_label(self.snake_canvas,5, 635, self.config_path_icon)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.configfile()

    def configfile(self):
        """
        Read the config file and check if the necessary sections and options exist.
        """

        try:
            self.config.read(self.config_path)
            self.game_logger.log_game_event("Config file read")
        except FileNotFoundError as e:
            traceback.print_exc(e)

        # Check if the config file has the necessary sections and options If not, add them
        try:
            self.config.set('Settings', 'game_mode', 'endless_snake')
            self.game_logger.log_game_event("Game mode set to endless_snake.")
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'score'):
                self.config.set('Endless_Snake_Values','score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'special_score'):
                self.config.set('Endless_Snake_Values','special_score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'special_score_high_score'):
                self.config.set('Endless_Snake_Values','special_score_high_score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'high_score'):
                self.config.set('Endless_Snake_Values','high_score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'time_score'):
                self.config.set('Endless_Snake_Values','time_score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'high_score_time'):
                self.config.set('Endless_Snake_Values','high_score_time', '0')
                self.game_logger.log_game_event("high_score_time added")
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'snake_length'):
                self.config.set('Endless_Snake_Values','snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'snake_length_high_score'):
                self.config.set('Endless_Snake_Values','snake_length_high_score', '0')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Settings', 'state'):
                self.config.set('Endless_Snake_Settings', 'state', 'start_screen')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'next_special_food_score'):
                self.config.set('Endless_Snake_Values', 'next_special_food_score', '50')
                self.write_changes_to_configini()
            else:
                self.config.set('Endless_Snake_Values', 'next_special_food_score', '50')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            if not self.config.has_option('Endless_Snake_Values', 'next_shorten_food_score'):
                self.config.set('Endless_Snake_Values', 'next_shorten_food_score', '100')
                self.write_changes_to_configini()
            else:
                self.config.set('Endless_Snake_Values', 'next_shorten_food_score', '100')
                self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.key_bindings = {
            'move_up': self.config.get('KeyBindings', 'move_up').split(', '),
            'move_down': self.config.get('KeyBindings', 'move_down').split(', '),
            'move_left': self.config.get('KeyBindings', 'move_left').split(', '),
            'move_right': self.config.get('KeyBindings', 'move_right').split(', '),
            'StartGame': self.config.get('KeyBindings', 'StartGame').split(', '),
            'PauseGame': self.config.get('KeyBindings', 'PauseGame').split(', '),
            'RestartGame': self.config.get('KeyBindings', 'RestartGame').split(', ')
        }

        # Start the game loop
        self.start_screen()
        self.bind_and_unbind_keys()

    def create_and_place_image_label(self, canvas, x, y, image_path):
        """
        Create and place a CTkImage and CTkLabel on the specified canvas.
        """
        my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                dark_image=Image.open(image_path),
                                size=(160, 160))

        image_label = ctk.CTkLabel(canvas, image=my_image, text="")
        image_label.place(x=x, y=y)

    def delete_game_labels_(self):
        """
        Delete the game labels.
        """
        self.game_labels_panel_2.endless_delete_labels()

    def update_high_score_labels_(self):
        """
        Update the high score labels.
        """
        self.game_labels_panel_2.endless_update_high_score_labels()

    def start_screen(self):
        """
        Method to display the start screen of the game.
        """
        self.snake_canvas.delete("all")
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Press 'Space' to start", fill="white", tag="start") # pylint: disable=line-too-long
        self.snake_canvas.focus_set()
        self.games_focused()
        self.bind_and_unbind_keys()
        self.game_labels_panel_2.endless_update_game_labels()
        self.game_labels_panel_2.endless_update_high_score_labels()
        self.game_logger.log_game_event("Updated high score labels.")
        self.state = 'start_screen'
        self.config.set('Endless_Snake_Settings', 'state', self.state)
        self.write_changes_to_configini()
        self.game_logger.log_game_event("Set the game state to start_screen. And wrote changes to config.ini.") # pylint: disable=line-too-long

    def start_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Method to start the game.
        """
        self.food.reset_food()
        self.bind_and_unbind_keys()
        self.state = 'playing'
        self.config.set('Endless_Snake_Settings', 'state', 'playing')
        self.config.set('Settings', 'home_button_state', 'disabled')
        self.config.set('Settings', 'endless_reset_high_score_button_state', 'disabled')
        self.config.set('Settings', 'endless_reset_high_score_time_button_state', 'disabled')
        self.config.set('Settings', 'endless_reset_high_score_snake_length_button_state', 'disabled') # pylint: disable=line-too-long
        self.config.set('Settings', 'endless_reset_high_score_special_button_state', 'disabled') # pylint: disable=line-too-long
        self.config.set('Settings', 'endless_reset_high_score_shorten_button_state', 'disabled') # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event("Set buttons states to: disabled")
        self.write_changes_to_configini()
        self.game_logger.log_game_event("Wrote changes to config.ini")
        self.create_button_panel.update_button_state()
        self.game_logger.log_game_event("Updated button states.")
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")

        try:
            self.config.read(self.config_path)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            self.high_score = int(self.config.get('Endless_Snake_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
            self.high_score_time = int(self.config.get('Endless_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
            self.snake_length_high_score = int(self.config.get('Endless_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
            self.special_score_high_score = int(self.config.get('Endless_Snake_Values', 'special_score_high_score', fallback='0')) # pylint: disable=line-too-long
            self.shorten_score_high_score = int(self.config.get('Endless_Snake_Values', 'shorten_score_high_score', fallback='0')) # pylint: disable=line-too-long
            self.game_logger.log_game_event("got high scores from config.ini")
            self.game_labels_panel_2.endless_update_high_score_labels()
            self.game_logger.log_game_event("Updated high score labels.")
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas.delete("all")
        self.game_logger.log_game_event("Deleted all items on the canvas.")

        #Spawn food and look for the snakes coordinates
        snake_coordinates = self.snake.get_coordinates()
        self.game_logger.log_game_event("Got the snake coordinates.")
        self.food.spawn_food(snake_coordinates, len(snake_coordinates))
        self.game_logger.log_game_event("Spawned food.")
        self.game_logger.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)

    def next_turn(self, snake, food):
        """
        Move the snake to the next turn.
        """
        x, y = snake.coordinates[0]

        try:
            self.config.read('config.ini')
            self.score = int(self.config.get('Endless_Snake_Values', 'score', fallback='0'))
            self.next_special_food_score = int(self.config.get('Endless_Snake_Values', 'next_special_food_score', fallback='50')) # pylint: disable=line-too-long
            self.next_shorten_food_score = int(self.config.get('Endless_Snake_Values', 'next_shorten_food_score', fallback='100')) # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

        if self.paused:
            self.snake_canvas.after(self.game_config.SPEED, self.next_turn, snake, food)
            return

        # Calculate total_time_played only when the game is not paused
        if not self.paused:
            self.current_time = time.time()
            self.total_time_played = int(self.current_time - self.start_time - self.total_paused_time) # pylint: disable=line-too-long
            #self.game_logger.log_game_event(self.total_time_played)
            try:
                self.config.set('Endless_Snake_Values', 'time_score', str(self.total_time_played))
                self.write_changes_to_configini()
            except FileNotFoundError as e:
                traceback.print_exc(e)

        food_eaten = False
        for food_id in list(food.food_items.keys()):
            food_item = food.food_items[food_id]
            if x == food_item['x'] and y == food_item['y']:
                food_eaten = True
                del food.food_items[food_id]
                self.snake_canvas.delete(food_item['tag'])

        special_food_eaten = False
        for special_food_id in list(food.special_food_items.keys()):
            special_food_item = food.special_food_items[special_food_id]
            if x == special_food_item['x'] and y == special_food_item['y']:
                special_food_eaten = True
                del food.special_food_items[special_food_id]
                self.snake_canvas.delete(special_food_item['tag'])

        shorten_food_eaten = False
        for shorten_food_id in list(food.shorten_food_items.keys()):
            shorten_food_item = food.shorten_food_items[shorten_food_id]
            if x == shorten_food_item['x'] and y == shorten_food_item['y']:
                shorten_food_eaten = True
                del food.shorten_food_items[shorten_food_id]
                self.snake_canvas.delete(shorten_food_item['tag'])

        if food_eaten:
            self.food.remove_occuppied_coordinates(food_item['x'], food_item['y'])
            self.score += 10 #should be 1
            self.snake_length += 1
            if len(food.food_coordinates) < 2:
                food.spawn_food(snake.get_coordinates(), self.score)
                try:
                    self.config.set('Endless_Snake_Values', 'score', str(self.score))
                    self.config.set('Endless_Snake_Values', 'snake_length', str(self.snake_length))
                    self.write_changes_to_configini()
                except FileNotFoundError as e:
                    traceback.print_exc(e)

        elif special_food_eaten:
            self.food.remove_occuppied_coordinates(special_food_item['x'], special_food_item['y'])
            self.score += 5
            self.special_score += 1
            if len(food.special_food_coordinates) < 1:
                #food.special_spawn_food(snake.get_coordinates())
                try:
                    self.config.set('Endless_Snake_Values', 'score', str(self.score))
                    self.config.set('Endless_Snake_Values', 'snake_length', str(self.snake_length))
                    self.config.set('Endless_Snake_Values', 'special_score', str(self.special_score)) # pylint: disable=line-too-long
                    self.write_changes_to_configini()
                except FileNotFoundError as e:
                    traceback.print_exc(e)

        elif shorten_food_eaten:
            self.food.remove_occuppied_coordinates(shorten_food_item['x'], shorten_food_item['y'])
            self.random_number_off_shorten_food = secrets.randbelow(11)
            self.snake_length -= self.random_number_off_shorten_food
            self.shorten_score += 1

            for _ in range(self.random_number_off_shorten_food):
                del snake.coordinates[-1]
                self.snake_canvas.delete(snake.squares[-1])
                del snake.squares[-1]

            if len(food.shorten_food_coordinates) < 1:
                #food.shorten_spawn_food(snake.get_coordinates())
                try:
                    self.config.set('Endless_Snake_Values', 'snake_length', str(self.snake_length)) # pylint: disable=line-too-long
                    self.config.set('Endless_Snake_Values', 'shorten_score', str(self.shorten_score)) # pylint: disable=line-too-long
                    self.write_changes_to_configini()
                except FileNotFoundError as e:
                    traceback.print_exc(e)

        else:
            del snake.coordinates[-1]
            self.snake_canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if self.score >= self.next_special_food_score:
            self.food.special_spawn_food(self.snake.get_coordinates())
            self.next_special_food_score += 50
            self.config.set('Endless_Snake_Values', 'next_special_food_score', str(self.next_special_food_score)) # pylint: disable=line-too-long
            self.write_changes_to_configini()

        if self.score >= self.next_shorten_food_score:
            self.food.shorten_spawn_food(self.snake.get_coordinates())
            self.next_shorten_food_score += 100
            self.config.set('Endless_Snake_Values', 'next_shorten_food_score', str(self.next_shorten_food_score)) # pylint: disable=line-too-long
            self.write_changes_to_configini()

        if self.score >= self.next_food_score:
            self.food.spawn_food(self.snake.get_coordinates(), self.score)

        if self.direction == "up" or self.direction == "w":
            y -= self.game_config.CELL_SIZE
        elif self.direction == "down" or self.direction == "s":
            y += self.game_config.CELL_SIZE
        elif self.direction == "left" or self.direction == "a":
            x -= self.game_config.CELL_SIZE
        elif self.direction == "right" or self.direction == "d":
            x += self.game_config.CELL_SIZE

        snake.coordinates.insert(0, (x, y))
        square = self.snake_canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, # pylint: disable=line-too-long
                                                    fill=self.game_config.SNAKE_COLOR, outline=self.game_config.SNAKE_OUTLINE) # pylint: disable=line-too-long
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)

        try:
            self.config.set('Endless_Snake_Values', 'time_score', str(self.total_time_played))
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        if self.check_collisions(snake):
            self.game_logger.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = 150 - int(self.game_config.SPEED)
            self.snake_canvas.after(delay, self.next_turn, snake, food)

        self.has_changed_direction = False
        self.game_labels_panel_2.endless_update_game_labels()
        self.game_labels_panel_2.endless_update_high_score_labels()

        self.snake_canvas.update()

    def game_over(self):
        """
        Method to end the game.
        """
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("bound and unbound keys.")
        self.food.reset_food()
        self.game_logger.log_game_event(f"Total play time: {self.total_time_played}")
        try:
            self.config.set('Endless_Snake_Settings', 'state', 'game_over')
            self.config.set('Settings', 'home_button_state', 'normal')
            self.config.set('Settings', 'endless_reset_high_score_button_state', 'normal')
            self.config.set('Settings', 'endless_reset_high_score_time_button_state', 'normal')
            self.config.set('Settings', 'endless_reset_high_score_snake_length_button_state', 'normal') # pylint: disable=line-too-long
            self.config.set('Settings', 'endless_reset_high_score_special_button_state', 'normal') # pylint: disable=line-too-long
            self.config.set('Settings', 'endless_reset_high_score_shorten_button_state', 'normal') # pylint: disable=line-too-long
            self.game_logger.log_game_event("Set buttons states to: normal")
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.create_button_panel.update_button_state()
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.coordinates}")

        self.snake_canvas.delete("all")
        self.game_logger.log_game_event("Deleted all items on the canvas.")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover") # pylint: disable=line-too-long
        # Unbind any previous bindings to avoid conflicts
        self.snake_canvas.unbind('<space>')
        self.game_logger.log_game_event("Unbound space key.")
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")

        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Score: {self.score}")

        try:
            self.config.read('config.ini')
            self.high_score = int(self.config.get('Endless_Snake_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)


        if self.score > self.high_score:
            try:
                self.config.set('Endless_Snake_Values', 'high_score', str(self.score))
            except FileNotFoundError as e:
                traceback.print_exc(e)

        self.get_time_score = int(self.config.get('Endless_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
        if self.total_time_played > self.get_time_score:
            try:
                self.config.set('Endless_Snake_Values', 'high_score_time', str(self.total_time_played)) # pylint: disable=line-too-long
                self.game_logger.log_game_event(f"high_score_time updated to: {self.total_time_played}" ) # pylint: disable=line-too-long
            except FileNotFoundError as e:
                traceback.print_exc(e)

        self.get_snake_length = int(self.config.get('Endless_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
        if self.snake_length > self.get_snake_length:
            try:
                self.config.set('Endless_Snake_Values', 'snake_length_high_score', str(self.snake_length)) # pylint: disable=line-too-long
                self.game_logger.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" ) # pylint: disable=line-too-long
            except FileNotFoundError as e:
                traceback.print_exc(e)

        self.get_special_high_score = int(self.config.get('Endless_Snake_Values', 'special_score_high_score', fallback='0')) # pylint: disable=line-too-long
        self.game_logger.log_game_event(self.get_special_high_score)
        if self.special_score > self.get_special_high_score:
            try:
                self.config.set('Endless_Snake_Values', 'special_score_high_score', str(self.special_score)) # pylint: disable=line-too-long
            except FileNotFoundError as e:
                traceback.print_exc(e)

        self.get_shorten_high_score = int(self.config.get('Endless_Snake_Values', 'shorten_snake_high_score', fallback='0')) # pylint: disable=line-too-long
        if self.shorten_score > self.get_shorten_high_score:
            try:
                self.config.set('Endless_Snake_Values', 'shorten_snake_high_score', str(self.shorten_score)) # pylint: disable=line-too-long
            except FileNotFoundError as e:
                traceback.print_exc(e)

        try:
            self.config.set('Endless_Snake_Values', 'next_special_food_score', '50')
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        try:
            self.config.set('Endless_Snake_Values', 'next_shorten_food_score', '100')
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.write_changes_to_configini()

    def restart_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Method to restart the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("bound and unbound keys.")
        self.game_logger.log_game_event("Game restarted")
        self.game_over_flag = False
        self.snake_canvas.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Create a new Snake object
        self.snake = Snake(self.game_logger, self.snake_canvas, self.game_config)
        self.food = EndlessFood(self.game_logger, self.snake_canvas, self.game_config)
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}") # pylint: disable=line-too-long

        try:
            self.config.read('config.ini')
            self.state = 'start_game'
            self.config.set('Endless_Snake_Values', 'score', '0')
            self.config.set('Endless_Snake_Values', 'snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
            self.config.set('Endless_Snake_Values', 'special_score', '0')
            self.config.set('Endless_Snake_Values', 'shorten_score', '0')
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.score = 0
        self.game_labels_panel_2.endless_update_game_labels()
        self.start_game()

    def pause_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Pause the game.
        """
        if self.state == 'playing':
            self.game_logger.log_game_event("Game paused")
            self.state = 'paused'
            self.config.set('Endless_Snake_Settings', 'state', self.state)
            self.write_changes_to_configini()
            self.create_button_panel.update_button_state()
            self.paused_label()
            self.paused = True
            self.paused_time = time.time()
        elif self.state == 'paused':
            self.game_logger.log_game_event("Game resumed")
            self.state = 'playing'
            self.config.set('Endless_Snake_Settings', 'state', self.state)
            self.write_changes_to_configini()
            self.create_button_panel.update_button_state()
            self.snake_canvas.delete("paused")
            self.paused = False
            self.pause_duration = time.time() - self.paused_time
            self.total_paused_time += self.pause_duration
            self.start_time += self.pause_duration
            self.paused_time = None
        self.bind_and_unbind_keys()

    def paused_label(self):
        """
        Display the paused label.
        """
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Game Paused", fill="white", tag="paused") # pylint: disable=line-too-long

    def change_direction(self, new_direction):
        """
        Change the direction of the snake.
        """
        if not self.has_changed_direction:
            current_time = time.time()
            if current_time - self.last_direction_change_time < 0.01:
                return

            opposite_directions = [('up', 'down'), ('down', 'up'), ('left', 'right'), ('right', 'left'), # pylint: disable=line-too-long
                                ('w', 's'), ('s', 'w'), ('a', 'd'), ('d', 'a')] # pylint: disable=line-too-long

            if any([self.direction == current and new_direction == opposite for current, opposite in opposite_directions]): # pylint: disable=line-too-long
                return

            self.direction = new_direction
            self.last_direction_change_time = current_time
            self.has_changed_direction = True

    def check_collisions(self, snake):
        """
        Check if the snake has collided with the walls or itself.
        """
        x, y = snake.coordinates[0]

        if x < 0 or x >= self.game_config.GAME_WIDTH or y < 0 or y >= self.game_config.GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def games_focused(self, event=None):
        # pylint: disable=unused-argument
        """
        Focus on the game.
        """
        self.snake_canvas.configure(highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.game_logger.log_game_event("Game focused")

    def bind_and_unbind_keys(self):
        """
        Bind and unbind keys for the game.
        """

        # Unbind all events to avoid conflicts
        for key in self.key_bindings.values():
            for k in key:
                k = k.replace("'", "")
                self.snake_canvas.unbind(f'<{k}>')
                print(f"Unbinding {k}")

        if self.state == 'start_game' or self.state == 'start_screen':
            for key in self.key_bindings['StartGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.start_game)

        elif self.state == 'game_over':
            for key in self.key_bindings['RestartGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.restart_game)

        elif self.state == 'playing':
            for key in self.key_bindings['PauseGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.pause_game)
            for key in self.key_bindings['move_up']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('up'))
            for key in self.key_bindings['move_down']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('down'))
            for key in self.key_bindings['move_left']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('left'))
            for key in self.key_bindings['move_right']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('right'))

        elif self.state == 'paused':
            for key in self.key_bindings['PauseGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.pause_game)


    def write_changes_to_configini(self):
        """
        Write the changes to the config.ini file.
        """
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
            self.game_logger.log_game_event("Wrote changes to config.ini")

    def destroy_button_panel(self):
        """
        Method to destroy the button panel.
        """
        self.create_button_panel.destroy_canvas()

# *****************************************
# Shadows Snake Game Snake Endless Game File
# *****************************************
