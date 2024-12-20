""" Evaluatoin Metrics contains all the metrics used to evaluate the model. """

from typing import Dict, Any
from src.experiment.metric import Metric

class EvaluationMetrics:

    """  Evaluation metrics contains the metrics for any phase,
        test, or model evaluation.
    """

    def __init__(self, metrics: Dict[str, Any]):
        """
        Initializes the EvaluationMetrics with the given metrics.

        Args:
            metrics (Dict[str, Any], optional): A dictionary of metrics. Defaults to {}.
        """
        self.metrics = metrics

    def add_metric(self, metric: Metric) -> None:
        """i
        Add a metric to the evaluation metrics.

        Args:
            metric (Metric): The metric to add.
        """
        self.metrics[metric.name] = metric

    def get_metric(self, metric_name: str) -> Metric:
        """
        Get a metric by name.

        Args:
            metric_name (str): The name of the metric to get.

        Returns:
            Metric: The metric with the given name.
        """
        return Metric(metric_name, 0, "Default")
