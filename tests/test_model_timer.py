""" Unit tests for the ModelTimer class. """

import unittest
import time
from src.components.model_timer import ModelTimer # Assuming ModelTiming is saved in model_timing.py

class TestModelTimer(unittest.TestCase):
    """ Unit tests for the ModelTimer class. """

    def setUp(self):
        """Set up a fresh instance of ModelTiming before each test."""
        self.timing = ModelTimer()

    def test_start_timer(self):
        """Test that start_timer correctly sets the start time and start date."""
        self.timing.start_timer()
        self.assertIsNotNone(self.timing.start_time)
        self.assertIsNotNone(self.timing.start_date)
        self.assertFalse(self.timing.is_paused)

    def test_pause_timer(self):
        """Test pausing the timer."""
        self.timing.start_timer()
        time.sleep(1)
        self.timing.pause_timer()
        self.assertTrue(self.timing.is_paused)
        self.assertIsNotNone(self.timing.paused_time)

    def test_resume_timer(self):
        """Test resuming the timer after pausing."""
        self.timing.start_timer()
        time.sleep(1)
        self.timing.pause_timer()
        paused_time = self.timing.paused_time

        time.sleep(1)  # Simulate some delay while paused
        self.timing.resume_timer()

        self.assertFalse(self.timing.is_paused)
        self.assertIsNone(self.timing.paused_time)
        self.assertGreater(self.timing.start_time, paused_time)  # Start time should be adjusted

    def test_stop_timer(self):
        """Test stopping the timer and recording training time."""
        self.timing.start_timer()
        time.sleep(2)
        self.timing.stop_timer()

        self.assertIsNotNone(self.timing.finish_time)
        self.assertIsNotNone(self.timing.finish_date)
        # At least 2 seconds of training time
        self.assertGreaterEqual(self.timing.training_time, 2.0)

    def test_pause_and_resume_affect_training_time(self):
        """Test that pausing and resuming affects the recorded training time correctly."""
        self.timing.start_timer()
        time.sleep(1)

        self.timing.pause_timer()
        time.sleep(1)  # This should not be counted in the training time
        self.timing.resume_timer()

        time.sleep(1)
        self.timing.stop_timer()

        # Training time should be approximately 2 seconds, not 3
        self.assertAlmostEqual(self.timing.training_time, 2.0, delta=0.1)

    def test_stop_timer_while_paused(self):
        """Test that stopping the timer while paused gives an error message."""
        self.timing.start_timer()
        time.sleep(1)
        self.timing.pause_timer()

        with self.assertLogs(level='INFO') as log:
            self.timing.stop_timer()
        self.assertIn("Cannot stop the timer while it's paused", log.output[0])

    def test_inference_time(self):
        """Test recording inference time for multiple predictions."""
        num_predictions = 5
        start_time = time.time()
        time.sleep(0.5)  # Simulate inference delay
        self.timing.record_inference_time(start_time, num_predictions)

        self.assertIsNotNone(self.timing.inference_time)
        self.assertAlmostEqual(self.timing.inference_time, 0.1, delta=0.01)

    def test_get_summary(self):
        """Test the summary output."""
        self.timing.start_timer()
        time.sleep(1)
        self.timing.stop_timer()

        summary = self.timing.get_summary()
        self.assertIn("start_date", summary)
        self.assertIn("finish_date", summary)
        self.assertIn("training_time", summary)
        self.assertIsInstance(summary["training_time"], float)

if __name__ == '__main__':
    unittest.main()
