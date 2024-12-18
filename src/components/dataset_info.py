""" This class contains metadata about a dataset. """

from datetime import datetime
from typing import Optional, List
from meta_data import MetaData

class DatasetInfo(MetaData):
    """
        Contains Dataset information.
    """
    def __init__(self, name, uri, version, tags = None, date_created = None, last_updated = None):
        super().__init__(name, uri, version, tags, date_created, last_updated)
        
        self.description = ""
        self.size = ""
        self.shape = ""
        
        self.is_local = False
        self.filepath= ""
        
    def __repr__(self):
        return super().__repr__() + f"\nDescription: {self.description}\nSize: {self.size}\nShape: {self.shape}\nIs Local: {self.is_local}\nFilepath: {self.filepath}"