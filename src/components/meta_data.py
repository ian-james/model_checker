from typing import List, Optional
from datetime import datetime

class MetaData:
    """
    Represents metadata information for a resource.
    """

    def __init__(
        self,
        name: str,
        uri: str,
        version: str,
        tags: Optional[List[str]] = None,
        date_created: Optional[datetime] = None,
        last_updated: Optional[datetime] = None,
    ):
        """
        Initializes a Metadata instance.

        :param name: The name of the resource.
        :param uri: The URI of the resource.
        :param version: The version of the resource.
        :param tags: Optional list of tags associated with the resource.
        :param date_created: Optional creation date. Defaults to now.
        :param last_updated: Optional last updated date. Defaults to now.
        """
        self.name = name
        self.uri = uri
        self.version = version
        self.tags = tags or []
        self.date_created = date_created or datetime.now()
        self.last_updated = last_updated or datetime.now()

    def update_tags(self, new_tags: List[str]) -> None:
        """
        Updates the tags with new values.

        :param new_tags: A list of new tags to replace existing ones.
        """
        self.tags = new_tags
        self.last_updated = datetime.now()

    def to_dict(self) -> dict:
        """
        Returns the metadata as a dictionary.

        :return: A dictionary representing the metadata.
        """
        return {
            "name": self.name,
            "uri": self.uri,
            "version": self.version,
            "tags": self.tags,
            "date_created": self.date_created.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the Metadata instance.

        :return: A string representation.
        """
        return f"<Metadata(name={self.name}, version={self.version}, uri={self.uri})>"
