""" This class runs the experiment for the given model and conditions. """
from src.experiment.experiment_conditions import ExperimentConditions

class Experiment:
    """ Experiment class to run the experiment. """

    def __init__(self, conditions: ExperimentConditions):
        """
        Initializes the Experiment with the given conditions.
        """
        self.conditions = conditions
        self.results = None

    def setup_experiment(self) -> None:
        """
        Setup the experiment with the given conditions.
        """

    def preprocess(self) -> None:
        """
        Preprocess the data for the experiment.
        """

    def run(self) -> None:
        """
        Run the experiment with the given conditions.
        """

    def postprocess(self) -> None:
        """
        Postprocess the data for the experiment.
        """

    def evaluate(self):
        """
        Evaluate the experiment with the given conditions.
        """

    def convert_results(self) -> None:
        """
        Convert the results of the experiment postprocessing.
        """

    def safe_results(self):
        """
        Save the results of the experiment.
        """
