# *****************************************
# Shadows Snake Game Snake Classic Game File
# *****************************************

"""
This module is responsible for the classic snake game mode of the Shadows Snake game.
"""

import time
import configparser
import traceback
import json
from os import path
from PIL import Image
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST, GameConstants
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import ClassicFood
from Logic.snake_logic_snake_game import Snake
from Logic.game_labelpanel import GameLabelsPanel
from Logic.buttonpanel_snake_game import ClickButtonPanel

class SnakeClassicGame(ctk.CTkCanvas):
    """
    Class for the classic snake game mode of the Shadows Snake game.
    """
    def __init__(self, parent, game_config, game_logger, functions, create_button_panel, config_handler):
        # Create the game logger
        self.game_logger = game_logger
        self.game_config = game_config
        self.functions = functions
        self.create_button_panel = create_button_panel

        self.config_handler = config_handler
        self.config, self.config_path = self.config_handler.load_config()

        self.config_dir = path.dirname(path.dirname(__file__))  # Go up one directory
        self.config, self.config_path = self.config_handler.load_config()
        self.config_path_icon = path.join(self.config_dir, 'app_icon.ico')
        self.game_logger.log_game_event(f"Config file read in Classic snake game file: {self.config_path}") # pylint: disable=line-too-long

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
        self.game_over_flag = False
        self.paused = False
        self.has_changed_direction = False

        self.game_logger.log_game_event(f"Initial score: {self.score}")
        self.game_logger.log_game_event(f"Game over flag: {self.game_over_flag}")
        self.game_logger.log_game_event(f"Game paused: {self.paused}")
        self.game_logger.log_game_event(f"Has changed direction: {self.has_changed_direction}")

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

        self.game_logger.log_game_event("High scores initialized")
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Snake length high score: {self.snake_length_high_score}")

        self.snake_canvas_x = GameConstants.GAME_CANVAS_PLACE_X
        self.snake_canvas_y = GameConstants.GAME_CANVAS_PLACE_Y

        # Canvas for the snake and food
        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                         highlightbackground=self.highlightbackground)

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,  highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                                             highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=self.snake_canvas_x, y=self.snake_canvas_y) # pylint: disable=line-too-long

        # Create the snake and the food
        self.snake = Snake(self.game_logger, self.snake_canvas, game_config)
        self.food = ClassicFood(self.game_logger, self.snake_canvas, game_config)
        self.game_labels_panel = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'classic_snake')
        self.create_button_panel = ClickButtonPanel(parent, self.game_logger, self.functions, self.config, self.config_path) # pylint: disable=line-too-long


        # Create the classic snake game labels
        self.game_labels_panel.classic_create_game_labels()

        # Game states being set to default values
        self.state = 'start_game'
        self.config['Classic_Snake_Settings'] = {'state': self.state}
        self.config['Settings']['home_button_state'] = 'normal'
        self.config['Settings']['classic_reset_high_score_button_state'] = 'normal'
        self.config['Settings']['classic_reset_high_score_time_button_state'] = 'normal'
        self.config['Settings']['classic_reset_high_score_snake_length_button_state'] = 'normal'
        self.write_changes_to_config()

        # call the configfile method
        self.configfile()

    def configfile(self):
        """
        Method to read the config file and set the game mode to classic_snake.
        """
        try:
            self.config, _ = self.config_handler.load_config()
            self.game_logger.log_game_event("Config file read")
        except FileNotFoundError as e:
            self.game_logger.log_game_event(f"Error reading config file: {str(e)}")
            traceback.print_exc()

        # Set game mode to classic_snake
        self.config['Settings']['game_mode'] = 'classic_snake'
        self.game_logger.log_game_event("Game mode set to classic_snake.")
        self.config_handler.save_config(self.config, self.config_path)

        # Initialize Classic_Snake_Values if not present
        if 'Classic_Snake_Values' not in self.config:
            self.config['Classic_Snake_Values'] = {
                'score': 0,
                'high_score': 0,
                'time_score': 0,
                'high_score_time': 0,
                'snake_length': self.game_config.SNAKE_LENGTH,
                'snake_length_high_score': 0
            }
            self.config_handler.save_config(self.config, self.config_path)

        # Initialize Classic_Snake_Settings if not present
        if 'Classic_Snake_Settings' not in self.config:
            self.config['Classic_Snake_Settings'] = {'state': 'start_screen'}
            self.config_handler.save_config(self.config, self.config_path)

        # Key bindings
        self.key_bindings = self.config.get('KeyBindings', {})
        if not self.key_bindings:
            # Set default key bindings if not present in config
            self.key_bindings = {
                "move_up": "w",
                "move_down": "s",
                "move_left": "a",
                "move_right": "d",
                "startgame": "space",
                "pausegame": "Escape",
                "restartgame": "r"
            }
            self.config['KeyBindings'] = self.key_bindings
            self.config_handler.save_config(self.config, self.config_path)

        # Start the game loop
        self.start_screen()
        self.bind_and_unbind_keys()

        try:
            self.create_and_place_image_label(self.snake_canvas, 500, 635, self.config_path_icon)
        except FileNotFoundError as e:
            self.game_logger.log_game_event(f"Error loading icon image: {str(e)}")
            traceback.print_exc()

    def create_and_place_image_label(self, canvas, x, y, image_path):
        """
        Create and place a CTkImage and CTkLabel on the specified canvas.
        """
        my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                dark_image=Image.open(image_path),
                                size=(160, 160))

        image_label = ctk.CTkLabel(canvas, image=my_image, text="")
        image_label.place(x=x, y=y)

    def delete_game_labels(self):
        """
        Method to delete the game labels.
        """
        self.game_labels_panel.classic_delete_labels()

    def update_high_score_labels_(self):
        """
        Method to update the high score labels.
        """
        self.game_labels_panel.classic_update_high_score_labels()

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
        self.game_labels_panel.classic_update_game_labels()
        self.game_labels_panel.classic_update_high_score_labels()
        self.game_logger.log_game_event("Updated high score labels.")
        self.state = 'start_screen'
        self.config['Classic_Snake_Settings']['state'] = self.state
        self.write_changes_to_config()
        self.game_logger.log_game_event("Set the game state to start_screen. And wrote changes to config.ini.") # pylint: disable=line-too-long

    def start_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Method to start the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Unbound and bound keys.")
        self.state = 'playing'
        self.config['Classic_Snake_Settings']['state'] = self.state
        self.config['Settings']['home_button_state'] = 'disabled'
        self.config['Settings']['classic_reset_high_score_button_state'] = 'disabled'
        self.config['Settings']['classic_reset_high_score_time_button_state'] = 'disabled'
        self.config['Settings']['classic_reset_high_score_snake_length_button_state'] = 'disabled'
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event("Set buttons states to: disabled")
        self.write_changes_to_config()
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
            self.high_score = int(self.config['Classic_Snake_Values'].get('high_score', 0))
            self.high_score_time = int(self.config['Classic_Snake_Values'].get('high_score_time', 0))
            self.snake_length_high_score = int(self.config['Classic_Snake_Values'].get('snake_length_high_score', 0))
            self.game_logger.log_game_event("got high scores from config.ini")
            self.game_labels_panel.classic_update_high_score_labels()
            self.game_logger.log_game_event("Updated high score labels.")
        except FileNotFoundError as e:
            self.game_logger.log_game_event(f"Error accessing config values: {str(e)}")
            traceback.print_exc()

        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas.delete("all")
        self.game_logger.log_game_event("Deleted all items on the canvas.")

        #Spawn food and look for the snakes coordinates
        snake_coordinates = self.snake.get_coordinates()
        self.game_logger.log_game_event("Got the snake coordinates.")
        self.food.spawn_food(snake_coordinates)
        self.game_logger.log_game_event("Spawned food.")
        self.game_logger.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)

    def next_turn(self, snake, food):
        """
        Method to execute the next turn of the game.
        """

        x, y = snake.coordinates[0]

        try:
            self.config.read(self.config_path)
            self.score = int(self.config['Classic_Snake_Values'].get('score', 0))
        except KeyError as e:
            self.game_logger.log_game_event(f"Error accessing score from config: {str(e)}")
            traceback.print_exc()

        if self.paused:
            self.snake_canvas.after(self.game_config.SPEED, self.next_turn, snake, food)
            return

        # Calculate total_time_played only when the game is not paused
        if not self.paused:
            self.current_time = time.time()
            self.total_time_played = int(self.current_time - self.start_time - self.total_paused_time)
            try:
                self.config['Classic_Snake_Values']['time_score'] = str(self.total_time_played)
                self.write_changes_to_config()
            except KeyError as e:
                self.game_logger.log_game_event(f"Error updating time score in config: {str(e)}")
                traceback.print_exc()

        food_eaten = False
        for food_id in list(food.food_items.keys()):
            food_item = food.food_items[food_id]
            if x == food_item['x'] and y == food_item['y']:
                food_eaten = True
                del food.food_items[food_id]
                self.snake_canvas.delete(food_item['tag'])
                self.game_logger.log_game_event("Food eaten and deleted from list.")

        if food_eaten:
            self.score += 1
            self.snake_length += 1
            if len(food.food_coordinates) < 2:
                food.spawn_food(snake.get_coordinates())
                self.config['Classic_Snake_Values']['score'] = str(self.score)
                self.config['Classic_Snake_Values']['snake_length'] = str(self.snake_length) # pylint: disable=line-too-long
                self.write_changes_to_config()

        else:
            del snake.coordinates[-1]
            self.snake_canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if self.direction == "up" or self.direction == "w":
            y -= self.game_config.CELL_SIZE
        elif self.direction == "down" or self.direction == "s":
            y += self.game_config.CELL_SIZE
        elif self.direction == "left" or self.direction == "a":
            x -= self.game_config.CELL_SIZE
        elif self.direction == "right" or self.direction == "d":
            x += self.game_config.CELL_SIZE

        snake.coordinates.insert(0, (x, y))
        square = self.snake_canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y +
                                                    self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, outline=self.game_config.SNAKE_OUTLINE) # pylint: disable=line-too-long
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)
        try:
            #self.config.set('Classic_Snake_Values', 'time_score', str(self.total_time_played))
            self.config['Classic_Snake_Values']['time_score'] = str(self.score)
            self.game_logger.log_game_event("Set time score in config.ini to total time played")
            self.write_changes_to_config()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        if self.check_collisions(snake):
            self.game_logger.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = 150 - int(self.game_config.SPEED)
            self.snake_canvas.after(delay, self.next_turn, snake, food)

        self.has_changed_direction = False
        self.game_labels_panel.classic_update_game_labels()
        self.game_labels_panel.classic_update_high_score_labels()
        #self.game_logger.log_game_event("Updated game labels.")

        self.snake_canvas.update()

    def game_over(self):
        """
        Method to end the game.
        """
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("bound and unbound keys.")
        try:
            self.config['Classic_Snake_Settings']['state'] = self.state
            self.config['Settings']['home_button_state'] = 'normal'
            self.config['Settings']['classic_reset_high_score_button_state'] = 'normal'
            self.config['Settings']['classic_reset_high_score_time_button_state'] = 'normal'
            self.config['Settings']['classic_reset_high_score_snake_length_button_state'] = 'normal'# pylint: disable=line-too-long
            self.game_logger.log_game_event("Set buttons states to: normal.")
            self.write_changes_to_config()
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

        self.snake_canvas.unbind('<space>')
        self.game_logger.log_game_event("Unbound space key.")
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")

        self.config.read(self.config_path)
        self.high_score = int(self.config['Classic_Snake_Values'].get('high_score', 0))
        self.game_logger.log_game_event("Got the high score from config.ini")
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Score: {self.score}")

        if self.score > self.high_score:
            self.config['Classic_Snake_Values']['high_score'] = str(self.score)
            self.game_logger.log_game_event("Set high score in config.ini")

        self.get_time_score = int(self.config['Classic_Snake_Values'].get('high_score_time', 0)) # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Got time score: {self.get_time_score}")

        if self.total_time_played > self.get_time_score:
            self.config['Classic_Snake_Values']['high_score_time'] = str(self.total_time_played) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"high_score_time updated to: {self.total_time_played}" ) # pylint: disable=line-too-long

        self.get_snake_length = int(self.config['Classic_Snake_Values'].get('snake_length_high_score', 0)) # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"Got snake length high score: {self.get_snake_length}")

        if self.snake_length > self.get_snake_length:
            self.config['Classic_Snake_Values']['snake_length_high_score'] = str(self.snake_length) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" ) # pylint: disable=line-too-long

        self.write_changes_to_config()

    def restart_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Method to restart the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")
        self.game_logger.log_game_event("Game restarted")
        self.game_over_flag = False
        self.snake_canvas.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Create a new Snake object
        self.snake = Snake(self.game_logger, self.snake_canvas, self.game_config)
        self.food = ClassicFood(self.game_logger, self.snake_canvas, self.game_config)
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}") # pylint: disable=line-too-long

        self.config.read(self.config_path)
        self.state = 'start_game'
        self.config['Classic_Snake_Values']['score'] = '0'
        self.config['Classic_Snake_Values']['snake_length'] = str(self.game_config.SNAKE_LENGTH)
        self.config['Classic_Snake_Settings']['state'] = self.state
        self.game_logger.log_game_event("Set the values and settings in config.ini.")
        self.write_changes_to_config()

        self.score = 0
        self.game_labels_panel.classic_update_game_labels()
        self.game_logger.log_game_event("Updated game labels.")

        self.start_game()

    def pause_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Method to pause the game.
        """
        if self.state == 'playing':
            self.game_logger.log_game_event("Game paused")
            self.state = 'paused'
            self.config['Classic_Snake_Settings']['state'] = self.state
            self.write_changes_to_config()
            self.create_button_panel.update_button_state()
            self.paused_label()
            self.game_logger.log_game_event("Paused label displayed")
            self.paused = True
            self.paused_time = time.time()
        elif self.state == 'paused':
            self.game_logger.log_game_event("Game resumed")
            self.state = 'playing'
            self.config['Classic_Snake_Settings']['state'] = self.state
            self.write_changes_to_config()
            self.create_button_panel.update_button_state()
            self.snake_canvas.delete("pause")
            self.game_logger.log_game_event("Paused label deleted")
            self.paused = False
            self.pause_duration = time.time() - self.paused_time
            self.total_paused_time += self.pause_duration
            self.start_time += self.pause_duration
            self.paused_time = None
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")

    def paused_label(self):
        """
        Method to display the paused label on the game screen.
        """
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Game Paused", fill="white", tag="pause")

    def change_direction(self, new_direction):
        """
        Method to change the direction of the snake.
        """
        if not self.has_changed_direction:
            current_time = time.time()
            if current_time - self.last_direction_change_time < 0.01:
                return

            opposite_directions = [('up', 'down'), ('down', 'up'), ('left', 'right'), ('right', 'left'), # pylint: disable=line-too-long
                                ('w', 's'), ('s', 'w'), ('a', 'd'), ('d', 'a')]

            if any([self.direction == current and new_direction == opposite for current, opposite in opposite_directions]): # pylint: disable=line-too-long
                return

            self.direction = new_direction
            self.last_direction_change_time = current_time
            self.has_changed_direction = True

    def check_collisions(self, snake):
        """
        Method to check for collisions in the game.
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
        Method to focus on the game.
        """
        self.snake_canvas.configure(highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.game_logger.log_game_event("Game focused")

    def bind_and_unbind_keys(self):
        """
        Method to bind and unbind keys based on the game state.
        """
        # Unbind all events to avoid conflicts
        for key in self.key_bindings.values():
            self.snake_canvas.unbind(f'<{key}>')

        if self.state == 'start_game' or self.state == 'start_screen':
            start_key = self.key_bindings.get('startgame')
            if start_key:
                self.snake_canvas.bind(f'<{start_key}>', self.start_game)

        elif self.state == 'game_over':
            restart_key = self.key_bindings.get('restartgame')
            if restart_key:
                self.snake_canvas.bind(f'<{restart_key}>', self.restart_game)

        elif self.state == 'playing':
            pause_key = self.key_bindings.get('pausegame')
            if pause_key:
                self.snake_canvas.bind(f'<{pause_key}>', self.pause_game)
            
            move_up = self.key_bindings.get('move_up')
            if move_up:
                self.snake_canvas.bind(f'<{move_up}>', lambda event: self.change_direction('up'))
            
            move_down = self.key_bindings.get('move_down')
            if move_down:
                self.snake_canvas.bind(f'<{move_down}>', lambda event: self.change_direction('down'))
            
            move_left = self.key_bindings.get('move_left')
            if move_left:
                self.snake_canvas.bind(f'<{move_left}>', lambda event: self.change_direction('left'))
            
            move_right = self.key_bindings.get('move_right')
            if move_right:
                self.snake_canvas.bind(f'<{move_right}>', lambda event: self.change_direction('right'))

        elif self.state == 'paused':
            pause_key = self.key_bindings.get('pausegame')
            if pause_key:
                self.snake_canvas.bind(f'<{pause_key}>', self.pause_game)

    def write_changes_to_config(self):
        """
        Write the changes to the config file using the config handler.
        """
        self.config_handler.save_config(self.config, self.config_path)
        self.game_logger.log_game_event("Wrote changes to config file")

    def destroy_button_panel(self):
        """
        Method to destroy the button panel.
        """
        self.create_button_panel.destroy_canvas()

# *****************************************
# Shadows Snake Game Snake Classic Game File
# *****************************************
