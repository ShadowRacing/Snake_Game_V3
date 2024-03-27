# *****************************************
# Wims Snake Game Snake Classic Game File
# *****************************************

import customtkinter as ctk, time, configparser, traceback
from os import path

# Importing thhe necessary modules from other folders
from Configuration.constants_snake_game import FONT_LIST
from Configuration.gameconfig_snake_game import GameConfig
from Logic.food_logic_snake_game import ClassicFood
from Logic.snake_logic_snake_game import Snake
from Logic.labelpanel_snake_game import GameLabelsPanel

#global variabels


class Snake_Classic_Game(ctk.CTkCanvas):
    def __init__(self, parent, game_config, logfile, functions, create_button_panel):
        # Create the game logger
        self.logfile = logfile
        self.game_config = game_config
        self.functions = functions
        self.create_button_panel = create_button_panel
        self.state = 'start_game'
        self.logfile.log_game_event(self.state)
        self.score = 0
        self.start_time = None
        self.paused_time = None
        self.total_paused_time = 0
        self.total_time_played = 0
        self.total_time_paused = 0
        self.game_over_flag = False
        self.paused = False
        self.direction = self.game_config.DIRECTIONOFFSNAKE
        self.last_direction_change_time = 0
        self.width = game_config.GAME_WIDTH
        self.height = game_config.GAME_HEIGHT
        self.highlightthickness = game_config.HIGHLIGHTTHICKNESS
        self.highlightbackground = game_config.HIGHLIGHTBACKGROUND
        super().__init__(parent, bg='Grey20', width=self.width, height=self.height, highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground)
        

        self.snake_canvas = ctk.CTkCanvas(self, bg="black", width= self.width, height= self.height,  highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground)
        self.snake_canvas.place(x=500, y=50)
        

        # Create the snake and the food
        self.snake = Snake(self.logfile, self.snake_canvas, game_config)
        self.food = ClassicFood(self.logfile, self.snake_canvas, game_config)
        self.game_labels_panel = GameLabelsPanel(self.logfile, parent, self.game_config)
        self.game_config = GameConfig(self.logfile, 'classic_snake')
        self.game_labels_panel.classic_create_game_labels()
        self.snake_length = self.game_config.SNAKE_LENGTH

        

        self.config_dir = path.dirname(__file__)
        self.config_path = path.join(self.config_dir, '..','config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        try:  
            self.config.set('Settings', 'game_mode', 'classic_snake')
        except:
            traceback.print_exc()
        
        if not self.config.has_option('Classic_Snake_Values', 'score'):
            self.config.set('Classic_Snake_Values','score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('Classic_Snake_Values', 'high_score'):
            self.config.set('Classic_Snake_Values','high_score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        if not self.config.has_option('Classic_Snake_Values', 'time_score'):
            self.config.set('Classic_Snake_Values','time_score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('Classic_Snake_Values', 'high_score_time'):
            self.config.set('Classic_Snake_Values','high_score_time', '0')
            self.logfile.log_game_event("high_score_time added")
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('Classic_Snake_Values', 'snake_length'):
            self.config.set('Classic_Snake_Values','snake_length', str(self.game_config.SNAKE_LENGTH))
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        if not self.config.has_option('Classic_Snake_Values', 'snake_length_high_score'):
            self.config.set('Classic_Snake_Values','snake_length_high_score', '0')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        if not self.config.has_option('Classic_Snake_Settings', 'state'):
            self.config.set('Classic_Snake_Settings', 'state', 'start_screen')
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
                
        # Start the game loop
        self.start_screen()
        self.bind_and_unbind_keys()
 
    def delete_game_labels(self):
        self.game_labels_panel.classic_delete_labels()
    
    def update_high_score_labels_(self):
        self.game_labels_panel.classic_update_high_score_labels()
    
    def start_screen(self):
        self.state = 'start_game'
        self.config.set('Classic_Snake_Settings', 'state', 'start_game')
       
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

        self.logfile.log_game_event(f"Game state: {self.state}")
        self.snake_canvas.delete("all")
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Press 'Space' to start", fill="white", tag="start")
        self.snake_canvas.focus_set()
        self.games_focused()
        self.bind_and_unbind_keys()
        self.game_labels_panel.classic_update_game_labels()
        self.game_labels_panel.classic_update_high_score_labels()

    def pause_game(self, event=None):
        if self.state == 'game':
            self.logfile.log_game_event("Game paused")
            self.state = 'pause'
            self.paused_label()
            self.paused = True
            self.paused_time = time.time()
        elif self.state == 'pause':
            self.logfile.log_game_event("Game resumed")
            self.state = 'game'
            self.snake_canvas.delete("pause")
            self.paused = False
            self.pause_duration = time.time() - self.paused_time
            self.total_paused_time += self.pause_duration
            self.start_time += self.pause_duration
            self.paused_time = None
        self.bind_and_unbind_keys()

    def paused_label(self):
        self.snake_canvas.create_text(self.width / 2, self.height / 2,
                         font= FONT_LIST[12], text="Game Paused", fill="white", tag="pause")

    def games_focused(self, event=None):
        self.snake_canvas.configure(highlightthickness=self.highlightthickness, highlightbackground=self.highlightbackground)
        self.logfile.log_game_event("Game focused")

    def start_game(self, event=None):
        self.bind_and_unbind_keys()
        self.state = 'game'
        self.bind_and_unbind_keys()
        self.config.read(self.config_path)
        self.high_score = int(self.config.get('Classic_Snake_Values', 'high_score', fallback='0'))
        self.high_score_time = int(self.config.get('Classic_Snake_Values', 'high_score_time', fallback='0'))
        self.snake_length_high_score = int(self.config.get('Classic_Snake_Values', 'snake_length_high_score', fallback='0'))
        self.game_labels_panel.classic_update_high_score_labels()
        self.config.set('Classic_Snake_Settings', 'state', 'game')

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.logfile.log_game_event(f"Game state: {self.state}")
        self.start_time = time.time()
        self.total_paused_time = 0
        self.score = 0
        self.snake_length = self.game_config.SNAKE_LENGTH
        self.snake_canvas.delete("all")

        #Spawn food and look for the snakes coordinates
        snake_coordinates = self.snake.get_coordinates()
        self.food.spawn_food(snake_coordinates)

        self.logfile.log_game_event(f"Snake coordinates at start: {self.snake.coordinates}")
        self.next_turn(self.snake, self.food)
    
    def next_turn(self, snake, food):
        x, y = snake.coordinates[0]

        if self.paused:
            self.snake_canvas.after(self.game_config.SPEED, self.next_turn, snake, food)
            return

        # Calculate total_time_played only when the game is not paused
        if not self.paused:
            self.current_time = time.time()
            self.total_time_played = int(self.current_time - self.start_time - self.total_paused_time)
            self.logfile.log_game_event(self.total_time_played)
            self.config.set('Classic_Snake_Values', 'time_score', str(self.total_time_played))
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

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
                self.config.set('Classic_Snake_Values', 'score', str(self.score))
                self.config.set('Classic_Snake_Values', 'snake_length', str(self.snake_length))
                with open('config.ini', 'w') as configfile:
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
        square = self.snake_canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, outline=self.game_config.SNAKE_OUTLINE)
        snake.squares.insert(0, square)

        self.current_time = time.time()
        self.total_time_played = int(self.current_time - self.start_time)
        self.config.set('Classic_Snake_Values', 'time_score', str(self.total_time_played))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

        

        if self.check_collisions(snake):
            self.logfile.log_game_event("snake has a collision")
            self.game_over()
        else:
            delay = int(110 - self.game_config.SPEED) 
            self.snake_canvas.after(delay, self.next_turn, snake, food)
            
        self.game_labels_panel.classic_update_game_labels()
        self.game_labels_panel.classic_update_high_score_labels()
        
        self.snake_canvas.update()

    def change_direction(self, new_direction):

        current_time = time.time()
        if current_time - self.last_direction_change_time < 0.01:
            return

        opposite_directions = [('up', 'down'), ('down', 'up'), ('left', 'right'), ('right', 'left'),
                            ('w', 's'), ('s', 'w'), ('a', 'd'), ('d', 'a')]

        if any([self.direction == current and new_direction == opposite for current, opposite in opposite_directions]):
            return

        self.direction = new_direction
        self.last_direction_change_time = current_time
        
    
    def check_collisions(self, snake):
        x, y = snake.coordinates[0]

        if x < 0 or x >= self.game_config.GAME_WIDTH or y < 0 or y >= self.game_config.GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.state = 'game_over'
        self.bind_and_unbind_keys()
        self.config.set('Classic_Snake_Settings', 'state', 'game_over')
        self.logfile.log_game_event(f"Game state: {self.state}")
        self.logfile.log_game_event(f"Snake coordinates after reset: {self.snake.coordinates}")
        self.snake_canvas.delete("all")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2,
                        font= FONT_LIST[16], text="GAME OVER", fill="red", tag="gameover")
        self.snake_canvas.create_text(self.snake_canvas.winfo_width()/2, self.snake_canvas.winfo_height()/2 + 100,
                        font= FONT_LIST[10], text="Press R to play again", fill="white", tag="gameover")
        # Unbind any previous bindings to avoid conflicts
        self.snake_canvas.unbind('<space>')
        self.bind_and_unbind_keys()
        self.high_score = int(self.config.get('Classic_Snake_Values', 'high_score', fallback='0'))
        self.logfile.log_game_event(f"High score: {self.high_score}")
        self.logfile.log_game_event(f"Score: {self.score}")
        if self.score > self.high_score:
            self.config.set('Classic_Snake_Values', 'high_score', str(self.score))


        self.get_time_score = int(self.config.get('Classic_Snake_Values', 'high_score_time', fallback='0'))
        if self.total_time_played > self.get_time_score:
            self.config.set('Classic_Snake_Values', 'high_score_time', str(self.total_time_played))
            self.logfile.log_game_event(f"high_score_time updated to: {self.total_time_played}" )

        
        self.get_snake_length = int(self.config.get('Classic_Snake_Values', 'snake_length_high_score', fallback='0'))
        if self.snake_length > self.get_snake_length:
            self.config.set('Classic_Snake_Values', 'snake_length_high_score', str(self.snake_length))
            self.logfile.log_game_event(f"snake_length_high_score updated to: {self.snake_length}" )
            
        with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

    def restart_game(self, event=None):
        self.bind_and_unbind_keys()
        self.logfile.log_game_event("Game restarted")
        self.logfile.log_game_event(f"Game state: {self.state}")
        self.game_over_flag = False
        self.snake_canvas.delete('game_over')
        self.direction = self.game_config.DIRECTIONOFFSNAKE
        
        # Create a new Snake object
        self.snake = Snake(self.logfile, self.snake_canvas, self.game_config)
        self.food = ClassicFood(self.logfile, self.snake_canvas, self.game_config)
        self.logfile.log_game_event(f"Snake coordinates after reset: {self.snake.get_coordinates()}")

        self.config.read('config.ini')

        self.config.set('Classic_Snake_Values', 'score', '0')
        self.config.set('Classic_Snake_Values', 'snake_length', str(self.game_config.SNAKE_LENGTH))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            # start the game again
            self.state = 'start_game'
        self.score = 0
        self.game_labels_panel.classic_update_game_labels()
        self.start_game()

    def bind_and_unbind_keys(self):
        # Unbind all events to avoid conflicts
        self.snake_canvas.unbind('<space>') # start the game
        self.snake_canvas.unbind('<Escape>') # pause the game
        self.snake_canvas.unbind('<left>') # change direction
        self.snake_canvas.unbind('<Right>') # change direction
        self.snake_canvas.unbind('<Up>') # change direction
        self.snake_canvas.unbind('<Down>') # change direction
        self.snake_canvas.unbind('<r>') # restart the game
        self.snake_canvas.unbind('<R>') # restart the game
        self.snake_canvas.unbind('<a>') # change direction
        self.snake_canvas.unbind('<d>') # change direction
        self.snake_canvas.unbind('<w>') # change direction
        self.snake_canvas.unbind('<s>') # change direction

        if self.state == 'start_game':
            self.snake_canvas.bind('<space>', self.start_game)
        elif self.state == 'game_over':
            self.snake_canvas.bind("<r>", self.restart_game)
            self.snake_canvas.bind("<R>", self.restart_game)
        elif self.state == 'game':
            self.snake_canvas.bind("<Escape>", self.pause_game)
            self.snake_canvas.bind('<Left>', lambda event: self.change_direction('left'))
            self.snake_canvas.bind('<Right>', lambda event: self.change_direction('right'))
            self.snake_canvas.bind('<Up>', lambda event: self.change_direction('up'))
            self.snake_canvas.bind('<Down>', lambda event: self.change_direction('down'))
            self.snake_canvas.bind('<a>', lambda event: self.change_direction('left'))
            self.snake_canvas.bind('<d>', lambda event: self.change_direction('right'))
            self.snake_canvas.bind('<w>', lambda event: self.change_direction('up'))
            self.snake_canvas.bind('<s>', lambda event: self.change_direction('down'))
        elif self.state == 'pause':
            self.snake_canvas.bind('<Escape>',self.pause_game)
        elif self.state == 'settings_menu':
            self.snake_canvas.unbind('<Escape>')

# *****************************************
# Wims Snake Game Snake Classic Game File
# *****************************************