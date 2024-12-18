""" Module to store timing information for training and inference."""

import time
from datetime import datetime

class ModelTimer:
    """Class to store timing information for training and inference,
        with pause/resume functionality."""

    def __init__(self):
        """ Initialize the ModelTimer with default values."""
        self.start_time = None
        self.finish_time = None
        self.training_time = 0.0
        self.inference_time = None
        self.paused_time = None
        self.is_paused = False
        self.start_date = None
        self.finish_date = None

    def start_timer(self):
        """Start the timer and record the start date."""
        self.start_time = time.time()
        self.start_date = datetime.now()
        self.training_time = 0.0
        self.is_paused = False
        self.paused_time = None

    def pause_timer(self):
        """Pause the timer and record the paused time."""
        if self.start_time and not self.is_paused:
            self.paused_time = time.time()
            self.is_paused = True
        else:
            print("Timer is not running or already paused.")

    def resume_timer(self):
        """Resume the timer from the paused state."""
        if self.is_paused:
            pause_duration = time.time() - self.paused_time
            self.start_time += pause_duration
            self.is_paused = False
            self.paused_time = None
        else:
            print("Timer is not paused.")

    def stop_timer(self):
        """Stop the timer and record the finish date."""
        if self.start_time and not self.is_paused:
            self.finish_time = time.time()
            self.finish_date = datetime.now()
            self.training_time = self.finish_time - self.start_time
        elif self.is_paused:
            print("Cannot stop the timer while it's paused. Please resume first.")
        else:
            print("Timer was not started.")

    def record_inference_time(self, start_time, num_predictions):
        """Record the inference time for predictions."""
        self.inference_time = (time.time() - start_time) / num_predictions

    def get_summary(self):
        """Return a summary of timing information."""
        return {
            "start_date": self.start_date,
            "finish_date": self.finish_date,
            "training_time": self.training_time,
            "inference_time": self.inference_time,
        }
