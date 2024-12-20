""" This class contains the main interface for working with metrics"""
from typing import Any

class Metric:
    """ A Class to store and manipulate metrics """
    def __init__(self, name: str, value: Any, description: str = ""):
        """
        Initializes the Metric with the given metadata and value.

        Args:
            name (str): The name of the metric.
            value (Any): The value of the metric.
            description (str, optional): A description of the metric. Defaults to "".
            phase (str, optional): The phase of the experiment (e.g., train, test). Defaults to "".
        """
        self.name = name
        self.value = value
        self.description = description

    def __repr__(self) -> str:
        """
        Return a string representation of the Metric object.

        Returns:
            str: A string representation of the Metric object.
        """
        return f"Metric(name={self.name}, value={self.value}, description={self.description})"
