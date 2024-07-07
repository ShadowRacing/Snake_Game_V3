"""
File containing the code for the little snake game for Info general.
"""

import secrets

class MiniSnakeGame:
    """
    Class representing the small snake game for Info general.
    """
    def __init__(self, canvas, size, game_logger):
        self.canvas = canvas
        self.size = size
        self.game_logger = game_logger
        self.food = (0, 0)
        self.food_eaten = 0
        self.max_x = 6  # Maximum x-coordinate
        self.max_y = 6  # Maximum y-coordinate
        self.speed = 1
        self.snake = [(0, 0)]
        self.visited_squares = set(self.snake)  # Initialize visited squares
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.running = False
        self.reset_possible = False
        self.current_direction_index = 0
        self.special_foods = []  # New attribute for special foods
        self.start_snake()

    def start_snake(self):
        """
        Start the snake game.
        """
        self.reset_snake()

    def reset_snake(self):
        """
        Reset the snake to its initial state.
        """
        self.game_logger.log_game_event("Resetting snake")
        self.snake = [(0, 0)]
        self.visited_squares = set(self.snake)  # Initialize visited squares
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
        self.current_direction_index = 0
        self.food = self.spawn_food()
        self.special_foods = []  # Reset special foods
        self.food_eaten = 0
        self.running = True
        self.reset_possible = False
        self.update_direction(0)
        self.reset_speed()

    def reset_speed(self):
        """
        Reset the speed of the snake.
        """
        self.speed = 1

    def spawn_food(self):
        """
        Spawn a new food item on the canvas.
        """
        possible_positions = set((x, y) for x in range(self.max_x) for y in range(self.max_y)) - set(self.snake) # pylint: disable=line-too-long
        return secrets.choice(list(possible_positions))

    def safe_directions(self):
        """
        Get the safe directions for the snake to move in.
        """
        head = self.snake[0]
        safe_dirs = []
        for i, direction in enumerate(self.directions):
            new_head = (head[0] + direction[0], head[1] + direction[1])
            if (0 <= new_head[0] < self.max_x and 0 <= new_head[1] < self.max_y and new_head not in self.snake): # pylint: disable=line-too-long
                safe_dirs.append(i)
        return safe_dirs

    def is_enclosed(self, new_head):
        """
        Check if the snake would be enclosed by moving to a new head position.
        """
        # Create a grid representing the game field
        grid = [[0 for _ in range(self.max_y)] for _ in range(self.max_x)]
        for segment in self.snake:
            grid[segment[0]][segment[1]] = 1
        grid[new_head[0]][new_head[1]] = 1

        # Simulate the snake's movement in each direction
        for direction in self.directions:
            simulated_head = new_head
            for _ in range(self.speed):
                simulated_head = (simulated_head[0] + direction[0], simulated_head[1] + direction[1]) # pylint: disable=line-too-long
                if not (0 <= simulated_head[0] < self.max_x and 0 <= simulated_head[1] < self.max_y and simulated_head not in self.snake): # pylint: disable=line-too-long
                    break
            else:
                # If the snake didn't get enclosed after moving in this direction, return False
                return False

        # If the snake got enclosed in all directions, return True
        self.reset_possible = True
        return True

    def a_star(self, grid, start, end):
        """
        Find the shortest path from the start to the end using the A* algorithm.
        """
        # This is a simplified version of the A* algorithm
        # You might need to use a more complete implementation for your game
        open_list = [start]
        came_from = {start: None}

        while open_list:
            current = open_list.pop(0)
            if current == end:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                return path

            for neighbor in self.get_neighbors(grid, current):
                if neighbor not in came_from:
                    open_list.append(neighbor)
                    came_from[neighbor] = current

        return None

    def get_neighbors(self, grid, node):
        """
        Get the neighbors of a node in the grid.
        """
        neighbors = []
        for direction in self.directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if (0 <= neighbor[0] < self.max_x and 0 <= neighbor[1] < self.max_y and (grid[neighbor[0]][neighbor[1]] == 0 or neighbor == self.snake[-1])): # pylint: disable=line-too-long
                neighbors.append(neighbor)
        return neighbors

    def update(self):
        """
        Update the snake's position on the canvas.
        """
        # Stop updating if not running
        if not self.running:
            return

        self.choose_direction()

        # Check safe directions and update direction if needed
        safe_dirs = self.safe_directions()
        if not safe_dirs:
            self.running = False
            return
        elif self.current_direction_index not in safe_dirs:
            self.current_direction_index = secrets.choice(safe_dirs)

        # Move the snake
        direction = self.directions[self.current_direction_index]
        head = self.snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        if self.is_enclosed(new_head):
            self.running = False
            return
        self.snake.insert(0, new_head)
        self.visited_squares.add(new_head)

        # Check if the snake has eaten the food
        if new_head == self.food:
            self.food = self.spawn_food()
            self.food_eaten += 1
        else:
            self.snake.pop()

        # Reset the snake if it has eaten 1000 food items
        if self.food_eaten >= 1000:
            self.running = False

        # Change direction if necessary
        self.change_direction_towards_food()

        # Draw the snake and the food
        self.canvas.delete('all')
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0]*self.size, segment[1]*self.size,
                                        (segment[0]+1)*self.size, (segment[1]+1)*self.size,
                                        fill="green")
        self.canvas.create_oval(self.food[0]*self.size, self.food[1]*self.size,
                                    (self.food[0]+1)*self.size, (self.food[1]+1)*self.size,
                                    fill="red")

        # Schedule the next update
        self.canvas.after(100, self.update)

    def update_direction(self, new_direction_index):
        """
        Update the snake's direction based on the new direction index.
        """
        # Check if the new direction is the opposite of the current direction
        current_direction = self.directions[self.current_direction_index]
        new_direction = self.directions[new_direction_index]
        if (current_direction[0] + new_direction[0] == 0 and
            current_direction[1] + new_direction[1] == 0):
            # The new direction is the opposite of the current direction, so ignore the update
            return

        # Check if the new direction moves into itself
        head = self.snake[0]
        next_square = (head[0] + new_direction[0], head[1] + new_direction[1])
        if next_square in self.snake:
            return

        # Check if the new direction exceeds maximum limits
        if (head[0] + new_direction[0] >= self.max_x) or (head[1] + new_direction[1] >= self.max_y): # pylint: disable=line-too-long
            return

        # Update the direction
        self.current_direction_index = new_direction_index

    def choose_direction(self):
        """
        Choose the best direction for the snake to move in.
        """
        head = self.snake[0]
        safe_dirs = self.safe_directions()

        if not safe_dirs:
            # No safe directions, game over
            self.reset_possible = True
            self.running = False
            return

        # Calculate distances to food and tail for each safe direction
        distances_to_food = []
        distances_to_tail = []
        for direction in safe_dirs:
            new_head = (head[0] + self.directions[direction][0], head[1] + self.directions[direction][1]) # pylint: disable=line-too-long
            distance_to_food = self.calculate_distance_to_food(new_head)
            distance_to_tail = self.calculate_distance_to_tail(new_head)
            distances_to_food.append(distance_to_food)
            distances_to_tail.append(distance_to_tail)

        # Choose the direction that minimizes distance to food while avoiding tail
        best_index = distances_to_food.index(min(distances_to_food))
        best_direction = safe_dirs[best_index]
        if distances_to_tail[best_index] > 1:
            # Avoid tail collision if possible
            self.update_direction(best_direction)
        else:
            # If tail collision is imminent, choose any safe direction
            self.update_direction(secrets.choice(safe_dirs))

    def calculate_distance_to_tail(self, position):
        """
        Calculate the Manhattan distance from a position to the tail of the snake.
        """
        tail_x, tail_y = self.snake[-1]
        return abs(position[0] - tail_x) + abs(position[1] - tail_y)

    def calculate_distance_to_food(self, position):
        """
        Calculate the Manhattan distance from a position to the food.
        """
        food_x, food_y = self.food
        return abs(position[0] - food_x) + abs(position[1] - food_y)

    def change_direction_towards_food(self):
        """
        Change the snake's direction towards the food.
        """
        head = self.snake[0]
        food_x, food_y = self.food
        head_x, head_y = head

        # Determine the new direction based on the food position
        if head_x < food_x:
            self.update_direction(0)  # Move right
        elif head_x > food_x:
            self.update_direction(2)  # Move left
        elif head_y < food_y:
            self.update_direction(1)  # Move down
        elif head_y > food_y:
            self.update_direction(3)  # Move up

    def reset_game(self):
        """
        Reset the game to its initial state.
        """
        if self.reset_possible is True:
            self.reset_snake()
            self.running = True
            self.update()
            self.reset_speed()
        else:
            self.game_logger.log_game_event("Reset not possible at this time.")
