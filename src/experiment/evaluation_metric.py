""" Evaluatoin Metrics contains all the metrics used to evaluate the model. """

from typing import Dict, Any
from src.experiment.metric import Metric

class EvaluationMetrics:
    
    """  Evaluation metrics contains the metrics for any phase, 
        test, or model evaluation.
    """
    
    def __init__(self, metrics: Dict[str, Any] = {}):
        """
        Initializes the EvaluationMetrics with the given metrics.

        Args:
            metrics (Dict[str, Any], optional): A dictionary of metrics. Defaults to {}.
        """
        self.metrics = metrics