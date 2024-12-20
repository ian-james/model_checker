""" This class contains information about what the test conditions where """
from typing import Dict, Any
from src.components.model_wrapper import ModelWrapper

class ExperimentConditions:
    """ ExperimentConditions contains all the conditions of the experiment. """
    def __init__(self, name: str, model: ModelWrapper,  conditions: Dict[str, Any],
                 metrics: Dict[str, Any], dataset_info: Dict[str, Any]):
        """
        Initializes the ExperimentConditions with the given conditions.
        """
        self.name = name
        self.conditions = conditions
        self.evaluation_metrics = metrics
        self.dataset_info = dataset_info
        self.model = model
