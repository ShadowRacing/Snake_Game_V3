# *****************************************
# Shadows Snake Game key logic File
# *****************************************


class MovementOffSnake:
    def __init__(self, game_config, logfile, snake_canvas):
        self.snake_canvas = snake_canvas
        self.game_config = game_config
        self.logfile = logfile

    def bind_and_unbind_keys(self):
        # Unbind all events to avoid conflicts
        self.snake_canvas.unbind('<space>')
        self.snake_canvas.unbind('<Escape>')
        self.snake_canvas.unbind('<left>')
        self.snake_canvas.unbind('<Right>')
        self.snake_canvas.unbind('<Up>')
        self.snake_canvas.unbind('<Down>')

        if self.state == 'start_game' or self.state == 'game_over':
            self.snake_canvas.after(3000, self.bind_spacebar)
        elif self.state == 'game':
            self.snake_canvas.bind("<Escape>", self.pause_game)
            self.snake_canvas.bind('<Left>', lambda event: self.change_direction('left'))
            self.snake_canvas.bind('<Right>', lambda event: self.change_direction('right'))
            self.snake_canvas.bind('<Up>', lambda event: self.change_direction('up'))
            self.snake_canvas.bind('<Down>', lambda event: self.change_direction('down'))
        elif self.state == 'start_screen':
            self.snake_canvas.bind('<space>', self.start_game)
            self.snake_canvas.focus_set()
        elif self.state == 'pause':
            self.snake_canvas.bind('<Escape>',self.start_game)
        elif self.state == 'settings_menu':
            self.snake_canvas.unbind('<Escape>')
        elif self.state == 'setup':
            pass
        else:
            self.logfile.log_game_event("No state found")

    def bind_spacebar(self):
        self.snake_canvas.bind("<space>", self.start_game)