""" Test the ModelWrapper class. """

import os
import unittest
from unittest.mock import MagicMock
import joblib
from src.components.model_wrapper import ModelWrapper

class TestModelWrapper(unittest.TestCase):
    """ Test the ModelWrapper class. """

    def setUp(self):
        """Set up the initial environment and objects for the tests."""
        # Mocking a simple model object
        mock_model = MagicMock()
        mock_model.get_params.return_value = {"param1": 0.1, "param2": 0.2}

        # Instantiate the ModelWrapper
        self.model_wrapper = ModelWrapper(
            name="Test Model",
            short_name="TM",
            model=mock_model,
            parameters={"param1": 0.1, "param2": 0.2},
            comment="This is a test model.",
            description="A longer description of the test model."
        )

    def test_model_wrapper_init(self):
        """Test the initialization of the ModelWrapper class."""
        self.assertEqual(self.model_wrapper.name, "Test Model")
        self.assertEqual(self.model_wrapper.short_name, "TM")
        self.assertIsNotNone(self.model_wrapper.model)
        self.assertEqual(self.model_wrapper.parameters, {"param1": 0.1, "param2": 0.2})
        self.assertEqual(self.model_wrapper.comment, "This is a test model.")
        self.assertEqual(self.model_wrapper.description, "A longer description of the test model.")

    def test_get_summary(self):
        """Test the get_summary method."""
        summary = self.model_wrapper.get_summary()

        self.assertEqual(summary['name'], "Test Model")
        self.assertEqual(summary['short_name'], "TM")
        self.assertEqual(summary['parameters'], {"param1": 0.1, "param2": 0.2})
        self.assertEqual(summary['comment'], "This is a test model.")
        self.assertEqual(summary['description'], "A longer description of the test model.")
        self.assertEqual(summary['model_params'], {"param1": 0.1, "param2": 0.2})

    def test_save_model(self):
        """Test the save_model method."""
        # Use a temporary directory for saving the model
        with self.subTest(msg="Test save_model"):
            file_path = "test_model.pkl"

            # Save the model
            self.model_wrapper.save_model(file_path)

            # Check if the file is created
            self.assertTrue(os.path.exists(file_path))

            # Load the model back and check it
            loaded_model = joblib.load(file_path)
            self.assertEqual(loaded_model, self.model_wrapper.model)

            # Clean up
            os.remove(file_path)

    def test_load_model(self):
        """Test the load_model method."""
        with self.subTest(msg="Test load_model"):
            # Save a model to a temporary directory
            file_path = "test_model.pkl"
            self.model_wrapper.save_model(file_path)

            # Create a new ModelWrapper instance and load the model
            new_model_wrapper = ModelWrapper(
                name="New Test Model",
                short_name="NTM",
                model=MagicMock(),
                parameters={},
                comment="",
                description=""
            )

            # Load the model into the new wrapper
            new_model_wrapper.load_model(file_path)

            # Check if the model is correctly loaded
            self.assertEqual(new_model_wrapper.model, self.model_wrapper.model)

            # Clean up
            os.remove(file_path)

    def test_repr(self):
        """Test the __repr__ method."""
        repr_string = repr(self.model_wrapper)
        self.assertIn("ModelWrapper(name=Test Model,", repr_string)
        self.assertIn("short_name=TM", repr_string)
        self.assertIn("description=A longer description of the test model.", repr_string)

if __name__ == "__main__":
    unittest.main()
