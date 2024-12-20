""" This is basic configuration file to store experiment settings.
    It uploads settings from a yaml file and stores them in a dictionary."""

from typing import Dict
from src.utils.file_utils import safe_yaml_dump, safe_ymal_load

class Configuration:
    """ Configuration class to store experiment settings. """

    def __init__(self, config_file: str):
        """
        Initializes the Configuration with the given configuration file.

        Args:
            config_file (str): The path to the configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """
        Load the configuration from the configuration file.

        Returns:
            Dict: A dictionary containing the configuration settings.
        """
        config = {}
        try:
            config = safe_ymal_load(self.config_file)
        except FileNotFoundError:
            print(f"Configuration file not found: {self.config_file}")

        return config

    def add_config(self, new_config: Dict, overwrite_duplicates: bool = False):
        """
        Add configuration settings to the existing configuration.

        Args:
            new_config (Dict): The configuration settings to add.
        """
        if self.check_duplicate_keys(new_config) and not overwrite_duplicates:
            return

        self.config.update(new_config)

    def add_config_from_file(self, file_path: str):
        """
        Add configuration settings from a file.

        Args:
            file_path (str): The path to the file containing the configuration settings.
        """
        new_config = safe_ymal_load(file_path)
        if not new_config:
            print(f"Configuration file not found: {file_path}")
            return

        self.add_config(new_config)

    def check_duplicate_keys(self, new_config: Dict) -> bool:
        """
        Check for duplicate keys in the configuration settings.

        Args:
            new_config (Dict): The configuration settings to check for duplicates.
        """
        duplicate_keys = set(self.config.keys()) & set(new_config.keys())
        if duplicate_keys:
            print(f"Duplicate keys found in configuration: {duplicate_keys}")
            return True
        return False

    def get_config(self) -> Dict:
        """
        Get the configuration settings.

        Returns:
            Dict: A dictionary containing the configuration settings.
        """
        return self.config

    def get_value(self, key: str):
        """
        Get the value of a specific key from the configuration settings.

        Args:
            key (str): The key for which to retrieve the value.

        Returns:
            Any: The value of the specified key.
        """
        return self.config[key]

    def set_value(self, key: str, value):
        """
        Set the value of a specific key in the configuration settings.

        Args:
            key (str): The key for which to set the value.
            value (Any): The value to set for the specified key.
        """
        self.config[key] = value

    def save_config(self, file_path: str):
        """
        Save the configuration to a file.

        Args:
            file_path (str): The path where the configuration will be saved.
        """
        safe_yaml_dump(self.config, file_path)

    def __repr__(self) -> str:
        """
        Return a string representation of the Configuration object.

        Returns:
            str: A string representation of the Configuration object.
        """
        return f"Configuration(config_file={self.config_file}, config={self.config})"
