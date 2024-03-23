# *****************************************
# Wims Snake Game Snake Logic File
# *****************************************

class Snake:
    def __init__(self, logfile, canvas, game_config):
        self.logfile = logfile
        self.game_config = game_config  # Add this line to store the game_config
        self.body_size = self.game_config.SNAKE_LENGTH
        self.coordinates = []
        self.squares = []
        self.canvas = canvas
        self.reset_length()

    def reset_length(self):
        # delete the existing squares from the canvas
        for square in self.squares:
            self.canvas.delete(square)

        self.coordinates = [[0, 0] for _ in range(self.body_size)]
        self.squares = []

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y + self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, tag="snake", outline= self.game_config.SNAKE_OUTLINE, width=0.5)
            self.squares.append(square)
        
        self.logfile.log_game_event("Reset snake length")
    
    def get_coordinates(self):
        return self.coordinates

    

# *****************************************
# Wims Snake Game Snake Logic File
# *****************************************