# *****************************************
# Shadows Snake Game Snake Leveling Game File
# *****************************************

"""
This module contains the Snake_Leveling class which is responsible for the game logic of the leveling snake game. # pylint: disable=line-too-long
"""

import time
import configparser
import traceback
from os import path
from PIL import Image
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST, GameConstants
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import LevelingFood
from Logic.snake_logic_snake_game import Snake
from Logic.game_labelpanel import GameLabelsPanel
from Logic.leveling_system import LevelingSystem
from Logic.buttonpanel_snake_game import ClickButtonPanel

class SnakeLeveling(ctk.CTkCanvas):
    """
    Class for the game logic of the leveling snake game.
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
        self.game_logger.log_game_event(f"Config file read in Leveling snake game file: {self.config_path}") # pylint: disable=line-too-long

        # Game configuration
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Game state
        self.score = 0
        self.xp = 0
        self.level = 0
        self.game_over_flag = False
        self.paused = False
        self.has_changed_direction = False
        self.next_special_food_score = 50
        self.next_shorten_food_score = 100

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

        # High scores
        self.high_score = 0
        self.snake_length_high_score = 0
        self.xp_high_score = 0
        self.level_high_score = 0

        # XP and leveling
        self.initial_xp_needed = 0
        self.levels_to_increase_xp = 0
        self.xp_increase_amount = 0
        self.current_xp_threshold = 0

        # Other variables
        self.get_time_score = 0
        self.get_snake_length = 0

        self.snake_canvas_x = GameConstants.GAME_CANVAS_PLACE_X
        self.snake_canvas_y = GameConstants.GAME_CANVAS_PLACE_Y

        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                         highlightbackground=self.highlightbackground)
        self.game_config = game_config

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,  highlightthickness=self.highlightthickness, # pylint: disable=line-too-long
                                          highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=self.snake_canvas_x, y=self.snake_canvas_y)

        self.snake = Snake(self.game_logger, self.snake_canvas, game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas, game_config)
        self.game_labels_panel_3 = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'snake_leveling')
        self.create_button_panel_3 = ClickButtonPanel(parent, self.game_logger, self.functions) # pylint: disable=line-too-long
        self.leveling_system = LevelingSystem()
        self.game_labels_panel_3.leveling_create_game_labels()

        self.state = 'start_game'
        self.config.set('Leveling_Snake_Settings', 'state', self.state)
        self.config.set('Settings', 'home_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_time_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_snake_length_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_special_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_shorten_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_xp_button_state', 'normal')
        self.config.set('Settings', 'leveling_reset_high_score_level_button_state', 'normal')
        self.write_changes_to_configini()

        try:
            self.create_and_place_image_label(self.snake_canvas,5, 635, self.config_path_icon)
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.configfile()

    def configfile(self):
        """
        Read the config file and set the initial values for the game.
        """
        try:
            self.config.read(self.config_path)
            self.game_logger.log_game_event("Config file read")
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.initial_xp_needed = int(self.config.get('Leveling_Snake_Values', 'initial_xp_needed', fallback='100')) # pylint: disable=line-too-long
        self.levels_to_increase_xp = int(self.config.get('Leveling_Snake_Values', 'levels_to_increase_xp', fallback='5')) # pylint: disable=line-too-long
        self.xp_increase_amount = int(self.config.get('Leveling_Snake_Values', 'xp_increase_amount', fallback='10')) # pylint: disable=line-too-long

        try:
            self.config.set('Settings', 'game_mode', 'leveling_snake')
        except NotImplementedError as e:
            traceback.print_exc(e)

        if not self.config.has_option('Leveling_Snake_Values', 'score'):
            self.config.set('Leveling_Snake_Values','score', '0')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'high_score'):
            self.config.set('Leveling_Snake_Values','high_score', '0')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'time_score'):
            self.config.set('Leveling_Snake_Values','time_score', '0')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'high_score_time'):
            self.config.set('Leveling_Snake_Values','high_score_time', '0')
            self.game_logger.log_game_event("high_score_time added")
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'snake_length'):
            self.config.set('Leveling_Snake_Values','snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'snake_length_high_score'):
            self.config.set('Leveling_Snake_Values','snake_length_high_score', '0')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Settings', 'state'):
            self.config.set('Leveling_Snake_Settings', 'state', 'start_screen')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'xp'):
            self.config.set('Leveling_Snake_Values','xp', '0')
            self.write_changes_to_configini()

        if not self.config.has_option('Leveling_Snake_Values', 'level'):
            self.config.set('Leveling_Snake_Values','level', '1')
            self.write_changes_to_configini()

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

    def delete_game_labels__(self):
        """
        Delete the game labels from the game_labels_panel.
        """
        self.game_labels_panel_3.leveling_delete_labels()

    def update_high_score_labels_(self):
        """
        Update the high score labels in the game_labels_panel.
        """
        self.game_labels_panel_3.leveling_update_high_score_labels()

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
        self.game_labels_panel_3.leveling_update_game_labels()
        self.game_labels_panel_3.leveling_update_high_score_labels()
        self.game_logger.log_game_event("Updated high score labels.")
        self.state = 'start_screen'
        self.config.set('Leveling_Snake_Settings', 'state', self.state)
        self.write_changes_to_configini()
        self.game_logger.log_game_event("Set the game state to start_screen. And wrote changes to config.ini.") # pylint: disable=line-too-long

    def start_game(self, event=None):
        """
        Start the game.
        """
        # pylint: disable=unused-argument
        self.bind_and_unbind_keys()
        self.state = 'playing'

        self.config.set('Leveling_Snake_Settings', 'state', 'playing')
        self.config.set('Settings', 'home_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_time_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_snake_length_button_state', 'disabled') # pylint: disable=line-too-long
        self.config.set('Settings', 'leveling_reset_high_score_special_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_shorten_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_xp_button_state', 'disabled')
        self.config.set('Settings', 'leveling_reset_high_score_level_button_state', 'disabled')
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
            self.high_score = int(self.config.get('Leveling_Snake_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
            self.high_score_time = int(self.config.get('Leveling_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
            self.snake_length_high_score = int(self.config.get('Leveling_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
            self.xp_high_score = int(self.config.get('Leveling_Snake_Values', 'xp_high_score', fallback='0')) # pylint: disable=line-too-long
            self.level_high_score = int(self.config.get('Leveling_Snake_Values', 'level_high_score', fallback='0')) # pylint: disable=line-too-long
            self.game_labels_panel_3.leveling_update_high_score_labels()
            self.config.set('Leveling_Snake_Settings', 'state', 'game')
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.xp = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas.delete("all")
        self.game_logger.log_game_event("Deleted all items on the canvas")

        #Spawn food and look for the snakes coordinates
        snake_coordinates = self.snake.get_coordinates()
        self.game_logger.log_game_event("Got the snake coordinates.")
        self.food.spawn_food(snake_coordinates)
        self.game_logger.log_game_event("Spawned food.")
        self.game_logger.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)

    def next_turn(self, snake, food):
        """
        Move the snake and check for collisions.
        """
        x, y = snake.coordinates[0]

        try:
            self.config.read('config.ini')
            self.score = int(self.config.get('Leveling_Snake_Values', 'score', fallback='0'))
            self.next_special_food_score = int(self.config.get('Leveling_Snake_Values', 'next_special_food_score', fallback='50')) # pylint: disable=line-too-long
            self.next_shorten_food_score = int(self.config.get('Leveling_Snake_Values', 'next_shorten_food_score', fallback='100')) # pylint: disable=line-too-long
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
            self.config.set('Leveling_Snake_Values', 'time_score', str(self.total_time_played))
            self.write_changes_to_configini()

        food_eaten = False
        for food_id in list(food.food_items.keys()):
            food_item = food.food_items[food_id]
            if x == food_item['x'] and y == food_item['y']:
                food_eaten = True
                del food.food_items[food_id]
                self.snake_canvas.delete(food_item['tag'])

        if food_eaten:
            self.score += 1
            self.xp += 1
            self.snake_length += 1

            if self.xp >= self.initial_xp_needed:
                self.level_up()

            if len(food.food_coordinates) < 2:
                food.spawn_food(snake.get_coordinates())
                self.config.set('Leveling_Snake_Values', 'score', str(self.score))
                self.config.set('Leveling_Snake_Values', 'snake_length', str(self.snake_length))
                self.config.set('Leveling_Snake_Values', 'xp', str(self.xp))
                self.write_changes_to_configini()
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
        square = self.snake_canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, # pylint: disable=line-too-long
                                                    fill=self.game_config.SNAKE_COLOR, outline=self.game_config.SNAKE_OUTLINE) # pylint: disable=line-too-long
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)
        self.config.set('Leveling_Snake_Values', 'time_score', str(self.total_time_played))
        self.write_changes_to_configini()

        if self.check_collisions(snake):
            self.game_logger.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = 150 - int(self.game_config.SPEED)
            self.snake_canvas.after(delay, self.next_turn, snake, food)

        self.has_changed_direction = False
        self.game_labels_panel_3.leveling_update_game_labels()
        self.game_labels_panel_3.leveling_update_high_score_labels()
        self.snake_canvas.update()

    def level_up(self):
        """
        Level up the snake.
        """
        self.level += 1
        self.xp = 0
        if self.level % self.levels_to_increase_xp == 0:
            self.initial_xp_needed += self.xp_increase_amount
        self.config.set('Leveling_Snake_Values', 'level', str(self.level))
        self.config.set('Leveling_Snake_Values', 'xp', str(self.xp))
        self.write_changes_to_configini()

    def change_direction(self, new_direction):
        """
        Change the direction of the snake.
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

    def game_over(self):
        """
        End the game.
        """
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("bound and unbound keys.")
        self.game_logger.log_game_event(f"Total play time: {self.total_time_played}")

        try:
            self.config.set('Leveling_Snake_Settings', 'state', 'game_over')
            self.config.set('Settings', 'home_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_time_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_snake_length_button_state', 'normal') # pylint: disable=line-too-long
            self.config.set('Settings', 'leveling_reset_high_score_special_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_shorten_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_xp_button_state', 'normal')
            self.config.set('Settings', 'leveling_reset_high_score_level_button_state', 'normal')
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.create_button_panel.update_button_state()

        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.coordinates}")

        self.snake_canvas.delete("all")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover") # pylint: disable=line-too-long
        # Unbind any previous bindings to avoid conflicts
        self.snake_canvas.unbind('<space>')
        self.game_logger.log_game_event("Unbound space key.")
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")

        self.high_score = int(self.config.get('Leveling_Snake_Values', 'high_score', fallback='0'))
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Score: {self.score}")

        try:
            self.config.read('config.ini')
            self.high_score = int(self.config.get('Leveling_Snake_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
            self.write_changes_to_configini()
        except FileNotFoundError as e:
            traceback.print_exc(e)

        if self.score > self.high_score:
            self.config.set('Leveling_Snake_Values', 'high_score', str(self.score))

        if self.xp > self.xp_high_score:
            self.config.set('Leveling_Snake_Values', 'xp_high_score', str(self.xp))

        if self.level > self.level_high_score:
            self.config.set('Leveling_Snake_Values', 'level_high_score', str(self.level))

        self.get_time_score = int(self.config.get('Leveling_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
        if self.total_time_played > self.get_time_score:
            self.config.set('Leveling_Snake_Values', 'high_score_time', str(self.total_time_played)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"high_score_time updated to: {self.total_time_played}" ) # pylint: disable=line-too-long

        self.get_snake_length = int(self.config.get('Leveling_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
        if self.snake_length > self.get_snake_length:
            self.config.set('Leveling_Snake_Values', 'snake_length_high_score', str(self.snake_length)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" ) # pylint: disable=line-too-long

        self.write_changes_to_configini()

    def restart_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Restart the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Bound and unbound keys.")
        self.game_logger.log_game_event("Game restarted")
        self.game_over_flag = False
        self.snake_canvas.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Create a new Snake object
        self.snake = Snake(self.game_logger, self.snake_canvas, self.game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas, self.game_config)
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}") # pylint: disable=line-too-long

        try:
            self.config.read('config.ini')
            self.state = 'start_game'
            self.config.set('Leveling_Snake_Values', 'score', '0')
            self.config.set('Leveling_Snake_Values', 'xp', '0')
            self.config.set('Leveling_Snake_Values', 'level', '0')
            self.config.set('Leveling_Snake_Values', 'snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
            self.initial_xp_needed = int(self.config.get('Leveling_Snake_Values', 'initial_xp_needed', fallback='100')) # pylint: disable=line-too-long
        except FileNotFoundError as e:
            traceback.print_exc(e)

        self.current_xp_threshold = self.initial_xp_needed
        self.write_changes_to_configini()

        self.score = 0
        self.xp = 0
        self.level = 0
        self.game_labels_panel_3.leveling_update_game_labels()
        self.start_game()

    def pause_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Pause or resume the game.
        """
        if self.state == 'playing':
            self.game_logger.log_game_event("Game paused")
            self.state = 'paused'
            self.config.set('Leveling_Snake_Settings', 'state', 'paused')
            self.write_changes_to_configini()
            self.create_button_panel_3.update_button_state()
            self.paused_label()
            self.paused = True
            self.paused_time = time.time()
        elif self.state == 'paused':
            self.game_logger.log_game_event("Game resumed")
            self.state = 'playing'
            self.config.set('Leveling_Snake_Settings', 'state', 'playing')
            self.write_changes_to_configini()
            self.create_button_panel_3.update_button_state()
            self.snake_canvas.delete("paused")
            self.paused = False
            self.pause_duration = time.time() - self.paused_time
            self.total_paused_time += self.pause_duration
            self.start_time += self.pause_duration
            self.paused_time = None
        self.bind_and_unbind_keys()

    def paused_label(self):
        """
        Display the paused label on the screen.
        """
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Game Paused", fill="white", tag="paused")

    def check_collisions(self, snake):
        """
        Check for collisions with the walls or the snake's body.
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
        Bind and unbind keys based on the game state.
        """
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
# Shadows Snake Game Snake Leveling Game File
# *****************************************
