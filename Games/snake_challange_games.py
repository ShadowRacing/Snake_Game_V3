# *****************************************
# Shadows Snake Challange File
# *****************************************

'''
Module for the Snake Challange game in the Shadows Snake game.
'''

import time
import configparser
import traceback
from os import path
import customtkinter as ctk

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import ChallangeFood
from Logic.snake_logic_snake_game import Snake
from Logic.labelpanel_snake_game import GameLabelsPanel


class FoodTimeAttack(ctk.CTkCanvas):
    '''
    Class representing the food in the time attack mode of the game.
    '''
    def __init__(self, parent, game_config, game_logger, functions, create_button_panel):
        """
        Class representing the food in the time attack mode of the game.

        This class inherits from CTkCanvas and 
        is responsible for the behavior of the food in the time attack mode.
        """
        self.parent = parent
        self.game_config = game_config
        self.game_logger = game_logger
        self.functions = functions
        self.create_button_panel = create_button_panel

        self.score = 0
        self.high_score = 0
        self.high_score_time = 0
        self.snake_length_high_score = 0

        self.current_time = 0
        self.total_time_played = 0
        self.get_time_score = 0
        self.get_snake_length = 0

        self.start_time = None
        self.paused_time = None
        self.total_paused_time = 0

        self.state = 'start_game'
        self.game_over_flag = False
        self.direction = self.game_config.DIRECTIONOFFSNAKE
        self.last_direction_change_time = 0
        self.has_changed_direction = False

        self.width = game_config.GAME_WIDTH

        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event("Snake challange game started")
        self.game_logger.log_game_event(
            f"Game width: {self.width}"
        )
        self.height = game_config.GAME_HEIGHT
        self.game_logger.log_game_event(
            f"Game height: {self.height}"
        )
        self.game_logger.log_game_event(f"Snake length from game_config: {game_config.SNAKE_LENGTH}") # pylint: disable=line-too-long
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        super().__init__(parent, bg='Grey20', width=self.width, height=self.height,
                         highlightthickness=self.highlightthickness,
                         highlightbackground=self.highlightbackground)

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,
                                          highlightthickness=self.highlightthickness,
                                          highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=500, y=50)

        # Create the snake and the food
        self.snake = Snake(self.game_logger, self.snake_canvas, game_config)
        self.food = ChallangeFood(self.game_logger, self.snake_canvas, game_config)
        self.game_labels_panel_4 = GameLabelsPanel(parent, self.game_logger,  self.game_config)
        self.game_config = GameConfig(self.game_logger, 'food_time_attack')
        self.game_labels_panel_4.challange_create_game_labels()
        self.snake_length = self.game_config.SNAKE_LENGTH

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.configfile()

    def configfile(self):
        '''
        This method is responsible for setting the initial configuration of the game.
        '''
        try:
            self.config.set('Settings', 'game_mode', 'food_time_attack')
        except configparser.Error as e:
            traceback.print_exc(e)

        if not self.config.has_option('food_time_attack_Values', 'score'):
            self.config.set('food_time_attack_Values','score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'high_score'):
            self.config.set('food_time_attack_Values','high_score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'time_score'):
            self.config.set('food_time_attack_Values','time_score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'high_score_time'):
            self.config.set('food_time_attack_Values','high_score_time', '0')
            self.game_logger.log_game_event("high_score_time added")
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'snake_length'):
            self.config.set('food_time_attack_Values','snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'snake_length_high_score'):
            self.config.set('food_time_attack_Values','snake_length_high_score', '0')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('food_time_attack_Values', 'state'):
            self.config.set('food_time_attack_Values', 'state', 'start_screen')
            with open('config.ini', 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

        self.key_bindings = {
            'Up': self.config.get('KeyBindings', 'Up').split(', '),
            'Down': self.config.get('KeyBindings', 'Down').split(', '),
            'Left': self.config.get('KeyBindings', 'Left').split(', '),
            'Right': self.config.get('KeyBindings', 'Right').split(', '),
            'StartGame': self.config.get('KeyBindings', 'StartGame').split(', '),
            'PauseGame': self.config.get('KeyBindings', 'PauseGame').split(', '),
            'RestartGame': self.config.get('KeyBindings', 'RestartGame').split(', '),
            'ExitGame': self.config.get('KeyBindings', 'ExitGame').split(', ')
        }

        # Start the game loop
        self.start_screen()
        self.bind_and_unbind_keys()

    def delete_game_labels___(self):
        """
        This method is responsible for deleting the game labels.
        """
        self.game_labels_panel_4.challange_delete_labels__()

    def update_high_score_labels(self):
        """
        This method is responsible for updating the high score labels.
        """
        self.game_labels_panel_4.challange_update_high_score_labels()

    def start_screen(self):
        """
        This method is responsible for displaying the start screen of the game.
        """
        self.state = 'start_game'
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.config.set('food_time_attack_Settings', 'state', 'start_game')

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

        self.snake_canvas.delete('all')
        self.snake_canvas.create_text(self.width/2, self.height/2,
                                      text="Press 's' to start the game",
                                      font=FONT_LIST[12], fill='white')
        self.snake_canvas.focus_set()
        self.bind_and_unbind_keys()
        self.game_labels_panel_4.challange_update_game_labels()
        self.game_labels_panel_4.challange_update_high_score_labels()

    def start_game(self, event=None):
        # pylint: disable=unused-argument
        """
        This method is responsible for starting the game.
        """
        self.bind_and_unbind_keys()
        self.state = 'game'
        self.config.set('food_time_attack_Settings', 'state', 'game')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.bind_and_unbind_keys()
        self.config.read(self.config_path)
        self.high_score = int(self.config.get('food_time_attack_Values', 'high_score'))
        self.high_score_time = int(self.config.get('food_time_attack_Values', 'high_score_time'))
        self.snake_length_high_score = int(self.config.get('food_time_attack_Values', 'snake_length_high_score')) # pylint: disable=line-too-long
        self.game_labels_panel_4.challange_update_game_labels()

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas.delete("all")
        snake_coordinates = self.snake.get_coordinates()
        self.food.spawn_food(snake_coordinates)
        self.game_logger.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)

    def next_turn(self, snake, food):
        """
        This method is responsible for the next turn of the game.
        """
        x, y = snake.coordinates[0]

        food_eaten = False
        for food_id in list(food.food_items.keys()):
            food_item = food.food_items[food_id]
            if x == food_item['x'] and y == food_item['y']:
                food_eaten = True
                del food.food_items[food_id]
                self.snake_canvas.delete(food_item['tag'])

        if food_eaten:
            self.score += 1
            self.snake_length += 1
            if len(food.food_coordinates) < 2:
                food.spawn_food(snake.get_coordinates())
                self.config.set('food_time_attack_Values', 'score', str(self.score))
                self.config.set('food_time_attack_Values', 'snake_length', str(self.snake_length))
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    self.config.write(configfile)

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
                                                    self.game_config.CELL_SIZE,
                                                    fill=self.game_config.SNAKE_COLOR,
                                                    outline=self.game_config.SNAKE_OUTLINE)
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)
        self.config.set('food_time_attack_Values', 'time_score', str(self.total_time_played))
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

        if self.score == 10:
            self.win_condition()

        elif self.check_collisions(snake):
            self.game_logger.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = 150 - int(self.game_config.SPEED)
            self.snake_canvas.after(delay, self.next_turn, snake, food)

        self.has_changed_direction = False
        self.game_labels_panel_4.challange_update_game_labels()
        self.game_labels_panel_4.challange_update_high_score_labels()
        self.snake_canvas.update()

    def change_direction(self, new_direction):
        """
        This method is responsible for changing the direction of the snake.
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
        This method is responsible for checking the collisions of the snake.
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
        This method is responsible for the game over state.
        """
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.config.set('food_time_attack_Settings', 'state', 'game_over')
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.coordinates}")
        self.snake_canvas.delete("all")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover") # pylint: disable=line-too-long
        # Unbind any previous bindings to avoid conflicts
        self.snake_canvas.unbind('<space>')
        self.bind_and_unbind_keys()
        self.high_score = int(self.config.get('food_time_attack_Values', 'high_score', fallback='0')) # pylint: disable=line-too-long
        self.game_logger.log_game_event(f"High score: {self.high_score}")
        self.game_logger.log_game_event(f"Score: {self.score}")
        if self.score > self.high_score:
            self.config.set('food_time_attack_Values', 'high_score', str(self.score))


        self.get_time_score = int(self.config.get('food_time_attack_Values', 'high_score_time', fallback='0')) # pylint: disable=line-too-long
        if self.total_time_played > self.get_time_score:
            self.config.set('food_time_attack_Values', 'high_score_time', str(self.total_time_played)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"high_score_time updated to: {self.total_time_played}" ) # pylint: disable=line-too-long


        self.get_snake_length = int(self.config.get('food_time_attack_Values', 'snake_length_high_score', fallback='0')) # pylint: disable=line-too-long
        if self.snake_length > self.get_snake_length:
            self.config.set('food_time_attack_Values', 'snake_length_high_score', str(self.snake_length)) # pylint: disable=line-too-long
            self.game_logger.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" ) # pylint: disable=line-too-long

        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def restart_game(self, event=None):
        # pylint: disable=unused-argument
        """
        This method is responsible for restarting the game.
        """
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("Game restarted")
        self.game_logger.log_game_event(f"Game state: {self.state}")
        self.game_over_flag = False
        self.snake_canvas.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE

        # Create a new Snake object
        self.snake = Snake(self.game_logger, self.snake_canvas, self.game_config)
        self.food = ChallangeFood(self.game_logger, self.snake_canvas, self.game_config)
        self.game_logger.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}") # pylint: disable=line-too-long

        self.config.read('config.ini')

        self.config.set('food_time_attack_Values', 'score', '0')
        self.config.set('food_time_attack_Values', 'snake_length', str(self.game_config.SNAKE_LENGTH)) # pylint: disable=line-too-long

        self.state = 'start_game'
        self.config.set('food_time_attack_Settings', 'state', 'start_game')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
            # start the game again
        self.score = 0
        self.game_labels_panel_4.challange_update_game_labels()
        self.start_game()

    def win_condition(self):
        """
        This method is responsible for the win condition of the game.
        """
        self.state = 'win'
        self.bind_and_unbind_keys()
        self.config.set('food_time_attack_Settings', 'state', 'win')
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        self.snake_canvas.delete('all')
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2, # pylint: disable=line-too-long
                        font= FONT_LIST[16], text="YOU WIN", fill="green", tag="win")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2 + 100, # pylint: disable=line-too-long
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="win")
        self.bind_and_unbind_keys()
        self.game_logger.log_game_event("You win")
        self.game_logger.log_game_event(f"Game state: {self.state}")

    # def bind_and_unbind_keys(self):
    #     """
    #     This method is responsible for binding and unbinding keys.
    #     """
    #     # Unbind all events to avoid conflicts
    #     self.snake_canvas.unbind('<space>') # start the game
    #     self.snake_canvas.unbind('<Escape>') # pause the game
    #     self.snake_canvas.unbind('<left>') # change direction
    #     self.snake_canvas.unbind('<Right>') # change direction
    #     self.snake_canvas.unbind('<Up>') # change direction
    #     self.snake_canvas.unbind('<Down>') # change direction
    #     self.snake_canvas.unbind('<r>') # restart the game
    #     self.snake_canvas.unbind('<R>') # restart the game
    #     self.snake_canvas.unbind('<a>') # change direction
    #     self.snake_canvas.unbind('<d>') # change direction
    #     self.snake_canvas.unbind('<w>') # change direction
    #     self.snake_canvas.unbind('<s>') # change direction

    #     if self.state == 'start_game':
    #         self.snake_canvas.bind('<space>', self.start_game)
    #     elif self.state == 'game_over':
    #         self.snake_canvas.bind("<r>", self.restart_game)
    #         self.snake_canvas.bind("<R>", self.restart_game)
    #     elif self.state == 'game':
    #         self.snake_canvas.bind('<Left>', lambda event: self.change_direction('left'))
    #         self.snake_canvas.bind('<Right>', lambda event: self.change_direction('right'))
    #         self.snake_canvas.bind('<Up>', lambda event: self.change_direction('up'))
    #         self.snake_canvas.bind('<Down>', lambda event: self.change_direction('down'))
    #         self.snake_canvas.bind('<a>', lambda event: self.change_direction('left'))
    #         self.snake_canvas.bind('<d>', lambda event: self.change_direction('right'))
    #         self.snake_canvas.bind('<w>', lambda event: self.change_direction('up'))
    #         self.snake_canvas.bind('<s>', lambda event: self.change_direction('down'))
    #     elif self.state == 'settings_menu':
    #         self.snake_canvas.unbind('<Escape>')
    #     elif self.state == 'win':
    #         self.snake_canvas.bind("<r>", self.restart_game)
    #         self.snake_canvas.bind("<R>", self.restart_game)

    def bind_and_unbind_keys(self):
        """
        Method to bind and unbind keys based on the game state.
        """
        # Unbind all events to avoid conflicts
        for key in self.key_bindings.values():
            for k in key:
                k = k.replace("'", "")
                self.snake_canvas.unbind(f'<{k}>')
                print(f"Unbinding {k}")

        if self.state == 'start_game':
            for key in self.key_bindings['StartGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.start_game)

        elif self.state == 'game_over':
            for key in self.key_bindings['RestartGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.restart_game)

        elif self.state == 'game':
            for key in self.key_bindings['Up']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('up'))
            for key in self.key_bindings['Down']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('down'))
            for key in self.key_bindings['Left']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('left'))
            for key in self.key_bindings['Right']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', lambda event: self.change_direction('right'))

        elif self.state == 'win':
            for key in self.key_bindings['RestartGame']:
                key = key.replace("'", "")
                self.snake_canvas.bind(f'<{key}>', self.restart_game)

# *****************************************
# Shadows Snake Challange File
# *****************************************
