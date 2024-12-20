""" This Class abstracts the handling of data for the model."""
from src.components.dataset_info import DatasetInfo

class DataHandler:
    """
    DataHandler for interfacing with different types of data.
    """
    def __init__(self, dataset_info: DatasetInfo):
        self.dataset_info = dataset_info
        self.data = None
        self.target = None
        self.type = "csv"
        self.name = "default-datahandler"

    def load_data(self):
        """
        Load data from a file.

        Args:
            file_path (str): Path to the file containing the data.
        """

    def save_data(self, file_path: str):
        """
        Save data to a file.

        Args:
            file_path (str): Path to the file where the data will be saved.
        """

    def get_data_summary(self):
        """
        Get a summary of the data.

        Returns:
            dict: A dictionary containing metadata about the data.
        """
        return {
            'name': self.name,
            'type': self.type,
            'dataset_info': self.dataset_info.to_dict(),
        }
