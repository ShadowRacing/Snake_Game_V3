import os
import configparser
import shutil

class ConfigHandler:
    def __init__(self, root_dir, game_logger):
        self.root_dir = root_dir
        self.game_logger = game_logger
        self.config_dir = os.path.join(root_dir, 'Login')
        # Create the Login directory if it doesn't exist
        os.makedirs(self.config_dir, exist_ok=True)
        self.default_config_path = os.path.join(self.config_dir, 'default_config.ini')

    def load_config(self, username=None):
        config = configparser.ConfigParser()
        
        if username:
            user_config_path = os.path.join(self.config_dir, 'Login', f'{username}_config.ini')
            if os.path.exists(user_config_path):
                config.read(user_config_path)
                print(f"Loaded user config for {username}")
                return config, user_config_path
            else:
                print(f"User config not found for {username}. Creating new config.")
                config.read(os.path.join(self.config_dir, 'config.ini'))
                self.create_user_config(username)
                return config, user_config_path
        else:
            default_config_path = os.path.join(self.config_dir, 'config.ini')
            config.read(default_config_path)
            print("No user specified. Using default config.")
            return config, default_config_path

    def save_config(self, config, config_path):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    def create_user_config(self, username):
        user_config_path = os.path.join(self.config_dir, f'{username}_config.ini')
        print(f"create user config {user_config_path}")
        if not os.path.exists(user_config_path):
            try:
                # Copy the default config to create the user config
                shutil.copy(self.default_config_path, user_config_path)

                # Modify the new user config
                config = configparser.ConfigParser()
                config.read(user_config_path)

                if 'USER' not in config:
                    config['USER'] = {}
                config['USER']['username'] = username

                # Write the changes back to the file
                self.save_config(config, user_config_path)

                self.game_logger.log_game_event(f"Created new config for user {username}")
            except Exception as e:
                self.game_logger.log_game_event(f"Error creating config for user {username}: {str(e)}")
        else:
            self.game_logger.log_game_event(f"Config file already exists for user {username}")

    def create_default_config(self):
        config = configparser.ConfigParser()
        config['Settings'] = {
            'screen_size': 'Default',
            'theme': 'Default',
            'contrast': 'Default',
            'button_press_time_limit': '0.5',
            # Add other default settings here
        }
        
        self.save_config(config, self.default_config_path)
        self.game_logger.log_game_event("Created default config file")