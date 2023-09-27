import unittest

from src.needledrop.extract import get_channel_upload_id

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.channel_content_details = {
            "items": [{"contentDetails": {"relatedPlaylists": {"likes": "",
                                                               "uploads": "foobar"}}}]
        }

    def test_get_channel_upload_id_returns_str_given_dict(self):
        id = get_channel_upload_id(self.channel_content_details)
        self.assertIsInstance(id, str)

