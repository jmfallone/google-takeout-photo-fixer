from datetime import datetime, timezone
import unittest
from unittest.mock import mock_open, patch

from utils.takeout_utils import get_takeout_datetime

# generated

class TestGetTakeoutDatetime(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''
    {
      "title": "IMG_20170820_155122.jpg",
      "description": "",
      "imageViews": "16",
      "creationTime": {
        "timestamp": "1503270137",
        "formatted": "20 Aug 2017, 23:02:17 UTC"
      },
      "photoTakenTime": {
        "timestamp": "1603265882",
        "formatted": "20 Oct 2020, 21:51:22 UTC"
      }
    }
    ''')
    @patch('json.load')
    def test_get_takeout_datetimee(self, mock_json_load, mock_open):
        # Mocking the return value of json.load
        mock_json_load.return_value = {
            "title": "IMG_20170820_155122.jpg",
            "description": "",
            "imageViews": "16",
            "photoTakenTime": {
                "timestamp": "1413237004",
                "formatted": "13 Oct 2014, 21:50:04 UTCC"
            }
        }

        expected_datetime = datetime(2014, 10, 13, 21, 50, 4, tzinfo=timezone.utc)
        result = get_takeout_datetime('dummy_path.json')
        self.assertEqual(result, expected_datetime)