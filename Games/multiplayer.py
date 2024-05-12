# *****************************************
# Shadows Snake Leveling Game File
# *****************************************

"""
This module contains the MultiPlayer class which is responsible for creating the multiplayer version of the Shadows Snake game. # pylint: disable=line-too-long
"""

import traceback
import configparser
import time
from os import path
import customtkinter as ctk

from Configuration.constants_snake_game import FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import LevelingFood
from Logic.snake_logic_snake_game import Snake
from Logic.labelpanel_snake_game import GameLabelsPanel


class MultiPlayer(ctk.CTkCanvas):
    """
    Class for creating the multiplayer version of the Shadows Snake game.
    """
    def __init__ (self, parent, game_config, game_logger, functions, create_button_panel):
        """
        Initialize the MultiPlayer class.
        """
        self.game_config = game_config
        self.game_logger = game_logger
        self.functions = functions
        self.create_button_panel = create_button_panel
        self.game_config = game_config

        self.state = 'start_game'
        self.game_logger.log_game_event(f"Game_state: {self.state}")

        self.score = 0
        self.high_score = 0
        self.high_score_time = 0
        self.snake_length_high_score = 0
        self.xp_high_score = 0
        self.level_high_score = 0

        self.start_time = None
        self.current_time = 0
        self.total_time_played = 0
        self.get_time_score = 0

        self.paused = False
        self.paused_time = 0
        self.pause_duration = 0
        self.total_paused_time = 0

        self.xp = 0
        self.level = 1
        self.initial_xp_needed = 0
        self.current_xp_threshold = 0

        self.get_snake_length = 0

        self.game_over_flag = False
        self.direction = self.game_config.DIRECTIONOFFSNAKE
        self.last_direction_change_time = 0
        self.has_changed_direction = False
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND

        super().__init__(parent, bg='Grey20', width=self.width, height=self.height,
                         highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long

        # Create the snake and the food

        self.snake_canvas_1 = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height, # pylint: disable=line-too-long
                                            highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.snake_canvas_1.place(x=500, y=50)

        self.snake_canvas_2 = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height, # pylint: disable=line-too-long
                                            highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.snake_canvas_2.place(x=1000, y=600)

        self.snake = Snake(self.game_logger, self.snake_canvas_1, game_config)
        self.snake = Snake(self.game_logger, self.snake_canvas_2, game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas_1, game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas_2, game_config)
        self.game_labels_panel_4 = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'snake_multiplayer')
        self.game_labels_panel_4.leveling_create_game_labels()
        self.snake_length = self.game_config.SNAKE_LENGTH

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        try:
            self.config.set('Settings', 'game_mode', 'multiplayer')
        except configparser.Error as e:
            traceback.print_exc(e)

        # Start the game loop
        self.start_screen()
        self.bind_and_unbind_keys()

    def delete_game_labels___(self):
        """
        Delete the game labels.
        """
        self.game_labels_panel_4.leveling_delete_labels()

    def update_high_score_labels_(self):
        """
        Update the high score labels.
        """
        self.game_labels_panel_4.leveling_update_high_score_labels()

    def start_screen(self):
        """
        Display the start screen of the game.
        """
        self.state = 'start_game'
        self.config.set('Multiplayer_Snake_Settings', 'state', 'start_game')

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.snake_canvas_1.delete("all")
        self.snake_canvas_1.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Press 'Space' to start", fill="white", tag="start") # pylint: disable=line-too-long

        self.snake_canvas_2.delete("all")
        self.snake_canvas_2.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Press 'Space' to start", fill="white", tag="start") # pylint: disable=line-too-long
        self.snake_canvas_1.focus_set()
        self.snake_canvas_2.focus_set()
        self.games_focused()
        self.bind_and_unbind_keys()
        self.game_labels_panel_4.leveling_update_game_labels()
        self.game_labels_panel_4.leveling_update_high_score_labels()

    def pause_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Pause the game.
        """
        if self.state == 'game':
            self.game_logger.log_game_event("Game paused")
            self.state = 'pause'
            self.paused_label()
            self.paused = True
            self.paused_time = time.time()
        elif self.state == 'pause':
            self.game_logger.log_game_event("Game resumed")
            self.state = 'game'
            self.snake_canvas_1.delete("pause")
            self.snake_canvas_2.delete("pause")
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
        self.snake_canvas_1.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Game Paused", fill="white", tag="pause")
        self.snake_canvas_2.create_text(self.width / 2, self.height / 2,
                            font= FONT_LIST[12], text="Game Paused", fill="white", tag="pause")

    def games_focused(self, event=None):
        # pylint: disable=unused-argument
        """
        Focus on the game.
        """
        self.snake_canvas_1.configure(highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.snake_canvas_2.configure(highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground) # pylint: disable=line-too-long
        self.game_logger.log_game_event("Game focused")

    def start_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Start the game.
        """
        self.bind_and_unbind_keys()
        self.state = 'game'
        self.bind_and_unbind_keys()
        self.config.read(self.config_path)
        self.high_score = int(self.config.get('Multiplayer_Snake_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
        self.high_score_time = int(self.config.get('Multiplayer_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
        self.snake_length_high_score = int(self.config.get('Multiplayer_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
        self.xp_high_score = int(self.config.get('Multiplayer_Snake_Values', 'xp_high_score', fallback='0')) # pylint: disable=line-too-long
        self.level_high_score = int(self.config.get('Multiplayer_Snake_Values', 'level_high_score', fallback='0')) # pylint: disable=line-too-long
        self.game_labels_panel_4.leveling_update_high_score_labels()
        self.config.set('Multiplayer_Snake_Values', 'state', 'game')

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.xp = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas_1.delete("all")
        self.snake_canvas_2.delete("all")

        #Spawn food and look for the snakes coordinates
        snake_coordinates = self.snake.get_coordinates()
        self.food.spawn_food(snake_coordinates)

        self.game_logger.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)

    def next_turn(self, snake, food):
        """
        Calculate the next turn of the snake.
        """
        x, y = snake.coordinates[0]

        if self.paused:
            self.snake_canvas_1.after(self.game_config.SPEED, self.next_turn, snake, food)
            self.snake_canvas_2.after(self.game_config.SPEED, self.next_turn, snake, food)
            return

        # Calculate total_time_played only when the game is not paused
        if not self.paused:
            self.current_time = time.time()
            self.total_time_played = int(self.current_time - self.start_time - self.total_paused_time) # pylint: disable=line-too-long
            self.game_logger.log_game_event(self.total_time_played)
            self.config.set('Leveling_Snake_Values', 'time_score', str(self.total_time_played))
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        food_eaten = False
        for food_id in list(food.food_items.keys()):
            food_item = food.food_items[food_id]
            if x == food_item['x'] and y == food_item['y']:
                food_eaten = True
                del food.food_items[food_id]
                self.snake_canvas_1.delete(food_item['tag'])
                self.snake_canvas_2.delete(food_item['tag'])

        if food_eaten:
            self.score += 1
            self.xp += 1
            self.snake_length += 1

            if self.xp >= self.initial_xp_needed:
                self.level_up()

            if len(food.food_coordinates) < 2:
                food.spawn_food(snake.get_coordinates())
                self.config.set('Multiplayer_Snake_Values', 'score', str(self.score))
                self.config.set('Multiplayer_Snake_Values', 'snake_length', str(self.snake_length))
                self.config.set('Multiplayer_Snake_Values', 'xp', str(self.xp))
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)

        else:
            del snake.coordinates[-1]
            self.snake_canvas_1.delete(snake.squares[-1])
            self.snake_canvas_2.delete(snake.squares[-1])
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
        square = self.snake_canvas_1.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y +
                                                      self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, # pylint: disable=line-too-long
                                                      outline=self.game_config.SNAKE_OUTLINE)
        square = self.snake_canvas_2.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y +
                                                      self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, # pylint: disable=line-too-long
                                                      outline=self.game_config.SNAKE_OUTLINE)
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)
        self.config.set('Leveling_Snake_Values', 'time_score', str(self.total_time_played))
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

        if self.check_collisions(snake):
            self.game_logger.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = 150 - int(self.game_config.SPEED)
            self.snake_canvas_1.after(delay, self.next_turn, snake, food)
            self.snake_canvas_2.after(delay, self.next_turn, snake, food)

        self.has_changed_direction = False

        self.game_labels_panel_4.leveling_update_game_labels()
        self.game_labels_panel_4.leveling_update_high_score_labels()
        self.snake_canvas_1.update()
        self.snake_canvas_2.update()

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

    def check_collisions(self, snake):
        """
        Check for collisions.
        """
        x, y = snake.coordinates[0]

        if x < 0 or x >= self.game_config.GAME_WIDTH or y < 0 or y >= self.game_config.GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        """
        Display the game over screen.
        """
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.config.set('Leveling_Snake_Settings', 'state', 'game_over')
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.coordinates}")
        self.snake_canvas_1.delete("all")
        self.snake_canvas_2.delete("all")
        self.snake_canvas_1.create_text(self.snake_canvas_1.winfo_width()/2, self.snake_canvas_1.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas_1.create_text(self.snake_canvas_1.winfo_width()/2, self.snake_canvas_1.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover") # pylint: disable=line-too-long
        self.snake_canvas_2.create_text(self.snake_canvas_2.winfo_width()/2, self.snake_canvas_2.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas_2.create_text(self.snake_canvas_2.winfo_width()/2, self.snake_canvas_2.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover") # pylint: disable=line-too-long
        # Unbind any previous bindings to avoid conflicts
        self.snake_canvas_1.unbind('<space>')
        self.snake_canvas_2.unbind('<space>')
        self.bind_and_unbind_keys()
        self.high_score = int(self.config.get('Leveling_Snake_Values', 'high_score', fallback='0'))
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Score: {self.score}")
        if self.score > self.high_score:
            self.config.set('Multiplayer_Snake_Values', 'high_score', str(self.score))

        if self.xp > self.xp_high_score:
            self.config.set('Multiplayer_Snake_Values', 'xp_high_score', str(self.xp))

        if self.level > self.level_high_score:
            self.config.set('Multiplayer_Snake_Values', 'level_high_score', str(self.level))

        self.get_time_score = int(self.config.get('Multiplayer_Snake_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
        if self.total_time_played > self.get_time_score:
            self.config.set('Multiplayer_Snake_Values', 'high_score_time', str(self.total_time_played)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"high_score_time updated to: {self.total_time_played}" )


        self.get_snake_length = int(self.config.get('Multiplayer_Snake_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
        if self.snake_length > self.get_snake_length:
            self.config.set('Multiplayer_Snake_Values', 'snake_length_high_score', str(self.snake_length)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" )

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def restart_game(self, event=None):
        # pylint: disable=unused-argument
        """
        Restart the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Game restarted")
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_over_flag = False
        self.snake_canvas_1.delete('game_over')
        self.snake_canvas_2.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Create a new Snake object
        self.snake = Snake(self.game_logger, self.snake_canvas_1, self.game_config)
        self.snake = Snake(self.game_logger, self.snake_canvas_2, self.game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas_1, self.game_config)
        self.food = LevelingFood(self.game_logger, self.snake_canvas_2, self.game_config)
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}") # pylint: disable=line-too-long

        self.config.read('config.ini')

        self.config.set('Multiplayer_Snake_Values', 'score', '0')
        self.config.set('Multiplayer_Snake_Values', 'xp', '0')
        self.config.set('Multiplayer_Snake_Values', 'level', '1')
        self.config.set('Multiplayer_Snake_Values', 'snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
        self.initial_xp_needed = int(self.config.get('Multiplayer_Snake_Values', 'initial_xp_needed', fallback='100')) # pylint: disable=line-too-long
        self.current_xp_threshold = self.initial_xp_needed
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
            # start the game again
            self.state = 'start_game'
        self.score = 0
        self.xp = 0
        self.level = 1
        self.game_labels_panel_4.leveling_update_game_labels()
        self.start_game()

    def bind_and_unbind_keys(self):
        """
        Bind and unbind keys based on the game state.
        """
        # Unbind all events to avoid conflicts
        self.snake_canvas_1.unbind('<space>') # start the game
        self.snake_canvas_1.unbind('<Escape>') # pause the game
        self.snake_canvas_1.unbind('<left>') # change direction
        self.snake_canvas_1.unbind('<Right>') # change direction
        self.snake_canvas_1.unbind('<Up>') # change direction
        self.snake_canvas_1.unbind('<Down>') # change direction
        self.snake_canvas_1.unbind('<r>') # restart the game
        self.snake_canvas_1.unbind('<R>') # restart the game
        self.snake_canvas_1.unbind('<a>') # change direction
        self.snake_canvas_1.unbind('<d>') # change direction
        self.snake_canvas_1.unbind('<w>') # change direction
        self.snake_canvas_1.unbind('<s>') # change direction

        if self.state == 'start_game':
            self.snake_canvas_1.bind('<space>', self.start_game)
        elif self.state == 'game_over':
            self.snake_canvas_1.bind("<r>", self.restart_game)
            self.snake_canvas_1.bind("<R>", self.restart_game)
        elif self.state == 'game':
            self.snake_canvas_1.bind("<Escape>", self.pause_game)
            self.snake_canvas_1.bind('<Left>', lambda event: self.change_direction('left'))
            self.snake_canvas_1.bind('<Right>', lambda event: self.change_direction('right'))
            self.snake_canvas_1.bind('<Up>', lambda event: self.change_direction('up'))
            self.snake_canvas_1.bind('<Down>', lambda event: self.change_direction('down'))
            self.snake_canvas_1.bind('<a>', lambda event: self.change_direction('left'))
            self.snake_canvas_1.bind('<d>', lambda event: self.change_direction('right'))
            self.snake_canvas_1.bind('<w>', lambda event: self.change_direction('up'))
            self.snake_canvas_1.bind('<s>', lambda event: self.change_direction('down'))
        elif self.state == 'pause':
            self.snake_canvas_1.bind('<Escape>',self.pause_game)
        elif self.state == 'settings_menu':
            self.snake_canvas_1.unbind('<Escape>')


# *****************************************
# Shadows Snake Leveling Game File
# *****************************************
