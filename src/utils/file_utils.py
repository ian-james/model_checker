""" File Utilities for opening different kinds of files."""
import os
import tempfile
import shutil
import yaml

def safe_yaml_dump(data, file_path):
    """
    Safely dump the data to a YAML file.

    Args:
        data (Any): The data to dump to the file.
        file_path (str): The path where the data will be saved.
    """
    try:
        with tempfile.NamedTemporaryFile('w', delete=False, dir=os.path.dirname(file_path)) as file:
            safe_yaml_dump(data, file)
            tmp_name = file.name

        # Replace the original file with the temporary file
        shutil.move(tmp_name, file_path)
    except (OSError, yaml.YAMLError) as e:
        print(f"Error writing to file {file_path}: {e}")
        if os.path.exists(tmp_name):
            os.remove(tmp_name)

def safe_ymal_load(file_path):
    """
    Safely load data from a YAML file.

    Args:
        file_path (str): The path from which to load the data.

    Returns:
        Any: The data loaded from the file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file {file_path} not found.")

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            config = yaml.safe_load(file)

            if not isinstance(config, dict):
                raise ValueError(f"Configuration file {file_path} is not a valid YAML file.")

            return config

    except (OSError, yaml.YAMLError) as e:
        print(f"Error loading configuration file {file_path}: {e}")
        raise

