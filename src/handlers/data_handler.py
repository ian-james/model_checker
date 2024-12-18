""" This Class abstracts the handling of data for the model."""
from dataset_info import DatasetInfo

""" This class contains metadata about a dataset. """
class DataHandler:
    """
    Contains Dataset information.
    """
    def __init__(self, dataset_info: DatasetInfo):
        self.dataset_info = dataset_info
        self.data = None
        self.target = None

    def load_data(self):
        """
        Load data from a file.

        Args:
            file_path (str): Path to the file containing the data.
        """
        pass

    def save_data(self, file_path: str):
        """
        Save data to a file.

        Args:
            file_path (str): Path to the file where the data will be saved.
        """
        pass

    def get_data_summary(self):
        """
        Get a summary of the data.

        Returns:
            dict: A dictionary containing metadata about the data.
        """
        pass