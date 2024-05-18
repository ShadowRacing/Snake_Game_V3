# *****************************************
# Shadows Snake Game Snake Logic File
# *****************************************

"""
This module contains the Snake class which is responsible for managing the snake in the Shadows Snake game. # pylint: disable=line-too-long
"""

import traceback

class Snake:
    """
    Class for managing the snake in the Shadows Snake game.
    """
    def __init__(self, game_logger, canvas, game_config):
        self.game_logger = game_logger
        self.game_config = game_config  # Add this line to store the game_config
        self.body_size = self.game_config.SNAKE_LENGTH
        self.coordinates = []
        self.squares = []
        self.canvas = canvas
        self.reset_length()

        #HEllo

    def reset_length(self):
        """
        Reset the length of the snake to the initial size.
        """
        # delete the existing squares from the canvas
        try:
            for square in self.squares:
                self.canvas.delete(square)

            self.coordinates = [[0, 0] for _ in range(self.body_size)]
            self.squares = []

            for x, y in self.coordinates:
                square = self.canvas.create_rectangle(x, y, x + self.game_config.CELL_SIZE, y +
                                                      self.game_config.CELL_SIZE, fill=self.game_config.SNAKE_COLOR, # pylint: disable=line-too-long
                                                      tag="snake", outline= self.game_config.SNAKE_OUTLINE, width=0.5) # pylint: disable=line-too-long
                self.squares.append(square)

            self.game_logger.log_game_event("Reset snake length")
        except ValueError as e:
            traceback.print_exc(e)

    def get_coordinates(self):
        """
        Get the coordinates of the snake.
        """
        return self.coordinates

# *****************************************
# Shadows Snake Game Snake Logic File
# *****************************************
