import unittest
from datetime import datetime
from src.components.meta_data import MetaData

class TestMetadata(unittest.TestCase):
    """
    Unit tests for the Metadata class.
    """

    def setUp(self):
        """
        Set up a default Metadata instance for tests.
        """
        self.metadata = MetaData(
            name="TestResource",
            uri="http://example.com/resource",
            version="1.0",
            tags=["test", "example"],
        )

    def test_initialization(self):
        """
        Test that the Metadata class initializes with correct values.
        """
        self.assertEqual(self.metadata.name, "TestResource")
        self.assertEqual(self.metadata.uri, "http://example.com/resource")
        self.assertEqual(self.metadata.version, "1.0")
        self.assertEqual(self.metadata.tags, ["test", "example"])
        self.assertIsInstance(self.metadata.date_created, datetime)
        self.assertIsInstance(self.metadata.last_updated, datetime)

    def test_update_tags(self):
        """
        Test updating the tags and ensuring the last_updated field changes.
        """
        old_last_updated = self.metadata.last_updated
        new_tags = ["updated", "metadata"]

        # Capture the time before updating tags
        time_before_update = datetime.now()
        self.metadata.update_tags(new_tags)

        # Assertions
        self.assertEqual(self.metadata.tags, new_tags)
        self.assertGreaterEqual(self.metadata.last_updated, time_before_update)
        self.assertNotEqual(self.metadata.last_updated, old_last_updated)


    def test_to_dict(self):
        """
        Test the to_dict method returns the correct dictionary representation.
        """
        metadata_dict = self.metadata.to_dict()
        self.assertEqual(metadata_dict["name"], "TestResource")
        self.assertEqual(metadata_dict["uri"], "http://example.com/resource")
        self.assertEqual(metadata_dict["version"], "1.0")
        self.assertEqual(metadata_dict["tags"], ["test", "example"])
        self.assertIsInstance(metadata_dict["date_created"], str)
        self.assertIsInstance(metadata_dict["last_updated"], str)

    def test_repr(self):
        """
        Test the string representation of the Metadata instance.
        """
        expected_repr = "<Metadata(name=TestResource, version=1.0, uri=http://example.com/resource)>"
        self.assertEqual(repr(self.metadata), expected_repr)


if __name__ == "__main__":
    unittest.main()
