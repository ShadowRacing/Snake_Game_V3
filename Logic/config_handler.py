import os
import configparser
import shutil


class ConfigHandler:
    def __init__(self, root_dir, game_logger):
        self.root_dir = root_dir
        self.game_logger = game_logger
        self.config_dir = os.path.join(root_dir, 'Configuration')
        self.default_config_path = os.path.join(self.config_dir, 'default_config.ini')

    def load_config(self, username=None):
        config = configparser.ConfigParser()
        
        if username:
            user_config_path = os.path.join(self.config_dir, f'{username}_config.ini')
            if os.path.exists(user_config_path):
                config.read(user_config_path)
                return config, user_config_path
            else:
                config.read(self.default_config_path)
                return config, user_config_path
        else:
            config.read(self.default_config_path)
            return config, self.default_config_path

    def save_config(self, config, config_path):
        with open(config_path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    def create_user_config(self, username):
        default_config_path = os.path.join(self.config_dir,'..', 'default_config.ini')
        user_config_path = os.path.join(self.config_dir,'..', f'{username}_config.ini')
        # if not os.path.exists(user_config_path):
        #     config = configparser.ConfigParser()
        #     config.read(self.default_config_path)
            
        #     if 'USER' not in config:
        #         config['USER'] = {}
        #     config['USER']['username'] = username
            
        #     self.save_config(config, user_config_path)
        # return user_config_path
    
        if not os.path.exists(user_config_path):
            try:
                # Copy the default config to create the user config
                shutil.copy(default_config_path, user_config_path)

                # Optionally, you can modify the new user config here
                config = configparser.ConfigParser()
                config.read(user_config_path)

                # Example: Set a user-specific value
                if 'USER' not in config:
                    config['USER'] = {}
                config['USER']['username'] = username

                # Write the changes back to the file
                with open(user_config_path, 'w', encoding='utf-8') as configfile:
                    config.write(configfile)

                self.game_logger.log_game_event(f"Created new config for user {username}")
            except Exception as e:
                self.game_logger.log_game_event(f"Error creating config for user {username}: {str(e)}")
        else:
            self.game_logger.log_game_event(f"Config file already exists for user {username}")
