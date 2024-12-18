""" A wrapper class for machine learning models that provides utility methods for
    training, prediction, evaluation, saving, and loading models,
    as well as obtaining a model summary. """

from typing import Any
import joblib

class ModelWrapper:
    """
    A wrapper class for machine learning models that provides utility
    methods for training, prediction, evaluation, saving, and loading models,
    as well as obtaining a model summary.

    Attributes:
        name (str): The full name of the model.
        short_name (str): A shorter identifier for the model.
        model (BaseEstimator): The machine learning model (e.g., sklearn model).
        parameters (dict): Hyperparameters for the model.
        comment (str): Optional field for additional notes about the model.
        description (str): Optional longer description of the model.
    """

    def __init__(self, name: str, short_name: str, model: Any,
                 parameters=dict, comment: str = "", description: str = ""):
        """
        Initializes the ModelWrapper with the given metadata and model.

        Args:
            name (str): The full name of the model.
            short_name (str): A shorter identifier for the model.
            model (BaseEstimator): The machine learning model (e.g., sklearn model).
            parameters (dict, optional): Hyperparameters for the model. Defaults to None.
            comment (str, optional): A comment about the model. Defaults to "".
            description (str, optional): A description of the model. Defaults to "".
        """
        self.name = name
        self.short_name = short_name
        self.model = model
        self.parameters = parameters if parameters else {}
        self.comment = comment
        self.description = description

    def save_model(self, file_path):
        """
        Save the trained model to a file using joblib.

        Args:
            file_path (str): Path where the model will be saved.
        """
        joblib.dump(self.model, file_path)

    def load_model(self, file_path):
        """
        Load a model from a file.

        Args:
            file_path (str): Path from which to load the model.

        Returns:
            model (BaseEstimator): The loaded model.
        """
        self.model = joblib.load(file_path)
        return self.model

    def get_summary(self):
        """
        Get a summary of the model wrapper, including model metadata.

        Returns:
            dict: A dictionary containing model metadata and parameters.
        """
        return {
            'name': self.name,
            'short_name': self.short_name,
            'parameters': self.parameters,
            'comment': self.comment,
            'description': self.description,
            'model_params': self.model.get_params()  # Get model's hyperparameters
        }

    def __repr__(self):
        """
        Return a string representation of the ModelWrapper instance.

        Returns:
            str: A string summarizing the ModelWrapper instance.
        """
        return f"ModelWrapper(name={self.name}, short_name={self.short_name}," \
                " description={self.description})"
