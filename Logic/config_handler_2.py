import os
import json

class ConfigHandler:
    def __init__(self, root_dir, game_logger):
        self.root_dir = root_dir
        self.game_logger = game_logger
        self.config_dir = os.path.join(root_dir, 'Login')
        os.makedirs(self.config_dir, exist_ok=True)
        self.default_config_path = os.path.join(root_dir, 'default_config.json')

    def load_config(self, username=None):
        if username:
            config_path = os.path.join(self.config_dir, f'{username}_data.json')
            if not os.path.exists(config_path):
                print(f"User config not found for {username}. Creating new config.")
                config = self.create_user_config(username)
                return config, config_path
        else:
            config_path = self.default_config_path

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as file:
                    config = json.load(file)
                print(f"Loaded config from {config_path}")
                return config, config_path
            except json.JSONDecodeError:
                print(f"Error reading config from {config_path}. Creating new default config.")
                config = self.create_default_config()
                self.save_config(config, config_path)
                return config, config_path
        else:
            print(f"Config not found at {config_path}. Creating new default config.")
            config = self.create_default_config()
            self.save_config(config, config_path)
            return config, config_path
    
    def create_user_config(self, username):
        user_config_path = os.path.join(self.config_dir, f'{username}_data.json')
        print(f"Creating user config {user_config_path}")
        config = self.create_default_config()
        config['USER'] = {'username': username}
        self.save_config(config, user_config_path)
        self.game_logger.log_game_event(f"Created new config for user {username}")
        return config

    def save_config(self, config, config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as file:
            json.dump(config, file, indent=4)

    # def create_user_config(self, username):
    #     user_config_path = os.path.join(self.config_dir, f'{username}_data.json')
    #     print(f"create user config {user_config_path}")
    #     if not os.path.exists(user_config_path):
    #         try:
    #             with open(self.default_config_path, 'r') as file:
    #                 config = json.load(file)
                
    #             if 'USER' not in config:
    #                 config['USER'] = {}
    #             config['USER']['username'] = username

    #             self.save_config(config, user_config_path)
    #             self.game_logger.log_game_event(f"Created new config for user {username}")
    #             return config
    #         except Exception as e:
    #             self.game_logger.log_game_event(f"Error creating config for user {username}: {str(e)}")
    #             return None
    #     else:
    #         self.game_logger.log_game_event(f"Config file already exists for user {username}")
    #         with open(user_config_path, 'r') as file:
    #             return json.load(file)

    def create_default_config(self):
        default_config = {
            "Settings": {
            "initial_theme": "Red",
            "theme": "Red",
            "contrast": "Default",
            "language": "English",
            "snake_color": "Default",
            "screen_size": "800x500",
            "label_needed_theme": "true",
            "button_press_time_limit": 0.5,
            "label_needed_high_score": "Default",
            "label_needed_game_size": "false",
            "game_mode": "classic_snake",
            "snake_speed": 50,
            "initial_game_size": "600x600",
            "game_size": "600x600",
            "home_button_state": "normal",
            "classic_reset_high_score_button_state": "normal",
            "classic_reset_high_score_time_button_state": "normal",
            "classic_reset_high_score_snake_length_button_state": "normal",
            "endless_reset_high_score_button_state": "normal",
            "endless_reset_high_score_time_button_state": "normal",
            "endless_reset_high_score_snake_length_button_state": "normal",
            "endless_reset_high_score_special_button_state": "normal",
            "endless_reset_high_score_shorten_button_state": "normal",
            "leveling_reset_high_score_button_state": "normal",
            "leveling_reset_high_score_time_button_state": "normal",
            "leveling_reset_high_score_snake_length_button_state": "normal",
            "leveling_reset_high_score_special_button_state": "normal",
            "leveling_reset_high_score_shorten_button_state": "normal",
            "leveling_reset_high_score_xp_button_state": "normal",
            "leveling_reset_high_score_level_button_state": "normal"
            },
            "DefaultSettings": {
            "initial_theme": "Default",
            "theme": "Default",
            "contrast": "Default",
            "language": "English",
            "snake_color": "Default",
            "screen_size": "Default",
            "button_press_time_limit": 0.5,
            "game_mode": "classic_snake",
            "label_needed_theme": "false",
            "label_needed_high_score": "Default",
            "label_needed_game_size": "false",
            "snake_speed": 50,
            "initial_game_size": "600x600",
            "game_size": "600x600",
            "home_button_state": "normal",
            "classic_reset_high_score_button_state": "normal",
            "classic_reset_high_score_time_button_state": "normal",
            "classic_reset_high_score_snake_length_button_state": "normal",
            "endless_reset_high_score_button_state": "normal",
            "endless_reset_high_score_time_button_state": "normal",
            "endless_reset_high_score_snake_length_button_state": "normal",
            "endless_reset_high_score_special_button_state": "normal",
            "endless_reset_high_score_shorten_button_state": "normal",
            "leveling_reset_high_score_button_state": "normal",
            "leveling_reset_high_score_time_button_state": "normal",
            "leveling_reset_high_score_snake_length_button_state": "normal",
            "leveling_reset_high_score_special_button_state": "normal",
            "leveling_reset_high_score_shorten_button_state": "normal",
            "leveling_reset_high_score_xp_button_state": "normal",
            "leveling_reset_high_score_level_button_state": "normal"
            },
            "KeyBindings": {
            "move_up": "w",
            "move_left": "a",
            "move_down": "s",
            "move_right": "d",
            "startgame": "space",
            "pausegame": "Escape",
            "restartgame": "r"
            },
            "Default_KeyBindings": {
            "up": "w",
            "down": "s",
            "left": "a",
            "right": "d",
            "startgame": "space",
            "pausegame": "Escape",
            "restartgame": "r"
            },
            "Classic_Snake_Values": {
            "score": 0,
            "high_score": 1,
            "snake_length": 0,
            "snake_length_high_score": 6,
            "time_score": 0,
            "high_score_time": 3
            },
            "Classic_Snake_Settings": {
            "state": "start_game"
            },
            "Endless_Snake_Values": {
            "score": 0,
            "high_score": 270,
            "special_score": 0,
            "special_score_high_score": 4,
            "snake_length": 0,
            "snake_length_high_score": 28,
            "time_score": 0,
            "high_score_time": 55,
            "shorten_score": 0,
            "shorten_snake_high_score": 2,
            "next_special_food_score": 50,
            "next_shorten_food_score": 100
            },
            "Endless_Snake_Settings": {
            "state": "start_game"
            },
            "Leveling_Snake_Values": {
            "score": 0,
            "high_score": 0,
            "special_score": 0,
            "special_score_high_score": 0,
            "snake_length": 0,
            "snake_length_high_score": 0,
            "time_score": 0,
            "high_score_time": 0,
            "shorten_score": 0,
            "shorten_snake_high_score": 0,
            "next_special_food_score": 50,
            "next_shorten_food_score": 100,
            "level": 0,
            "level_high_score": 0,
            "xp": 0,
            "initial_xp_needed": 10,
            "levels_to_increase_xp": 10,
            "xp_increase_amount": 20,
            "xp_high_score": 0
            },
            "Leveling_Snake_Settings": {
            "state": "start_game"
            },
            "food_time_attack_Values": {
            "score": 0,
            "high_score": 10,
            "special_score": 0,
            "special_score_high_score": 0,
            "snake_length": 5,
            "snake_length_high_score": 15,
            "time_score": 0,
            "high_score_time": 21,
            "shorten_score": 0,
            "shorten_snake_high_score": 0,
            "next_special_food_score": 50,
            "next_shorten_food_score": 100,
            "level": 1,
            "level_high_score": 1,
            "xp": 0,
            "xp_high_score": 0,
            "initial_xp_needed": 100,
            "levels_to_increase_xp": 10,
            "xp_increase_amount": 50,
            "state": "start_screen"
            },
            "food_time_attack_Settings": {
            "state": "start_game"
            }
        }
        
        self.save_config(default_config, os.path.join(self.config_dir, 'default_config.json'))
        self.game_logger.log_game_event("Created default config file")
        return default_config