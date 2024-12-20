""" This file contains the tests for the Configuration class."""

import os
import unittest
from src.experiment.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    """ Define a test to demonstrate saving and loading settings. """

    def setUp(self):
        """ Set up the Configuration object for the tests. """
        self.config_file = "test_config.yaml"
        self.config = Configuration(self.config_file)

    def test_load_config(self):
        """ Test loading the configuration file. """
        self.assertEqual(self.config.config, {})

    def test_add_config(self):
        """ Test adding configuration settings. """
        new_config = {"setting1": 1, "setting2": 2}
        self.config.add_config(new_config)
        self.assertEqual(self.config.config, new_config)

    def test_add_config_from_file(self):
        """ Test adding configuration settings from a file. """
        new_config = {"setting3": 3, "setting4": 4}
        new_config_file = "new_config.yaml"
        with open(new_config_file, "w") as file:
            file.write("setting3: 3\nsetting4: 4\n")
        
        self.config.add_config_from_file(new_config_file)
        self.assertEqual(self.config.config, new_config)

        # Clean up the new configuration file
        os.remove(new_config_file)
    
