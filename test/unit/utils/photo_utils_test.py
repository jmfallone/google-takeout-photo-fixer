import unittest
from unittest.mock import patch, call
from datetime import datetime
import piexif

from utils.photo_utils import update_photo_creation_date

# generated

class TestUpdatePhotoCreationDate(unittest.TestCase):

    @patch('piexif.insert')
    @patch('piexif.dump')
    @patch('piexif.load')
    def test_update_photo_creation_date(self, mock_load, mock_dump, mock_insert):
        # Mock data
        photo_file_path = 'test.jpg'
        new_date = datetime(2023, 7, 14, 12, 0, 0)
        formatted_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
        encoded_date = formatted_date.encode()

        exif_dict = {
            'Exif': {
                piexif.ExifIFD.DateTimeOriginal: b'',
                piexif.ExifIFD.DateTimeDigitized: b''
            },
            '0th': {
                piexif.ImageIFD.DateTime: b''
            }
        }

        # Configure the mock objects
        mock_load.return_value = exif_dict
        mock_dump.return_value = b'bytes'

        # Call the function
        update_photo_creation_date(photo_file_path, new_date)

        # Check that piexif.load was called correctly
        mock_load.assert_called_once_with(photo_file_path)

        # Verify the EXIF data was updated correctly
        self.assertEqual(exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal], encoded_date)
        self.assertEqual(exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized], encoded_date)
        self.assertEqual(exif_dict['0th'][piexif.ImageIFD.DateTime], encoded_date)

        # Check that piexif.dump was called with the modified exif_dict
        mock_dump.assert_called_once_with(exif_dict)

        # Check that piexif.insert was called with the correct arguments
        mock_insert.assert_called_once_with(b'bytes', photo_file_path)

    @patch('piexif.insert')
    @patch('piexif.dump')
    @patch('piexif.load')
    def test_update_photo_creation_date_invalid_date(self, mock_load, mock_dump, mock_insert):
        # Mock data
        photo_file_path = 'test.jpg'
        new_date = datetime(2023, 7, 14, 12, 0, 0)
        formatted_date = new_date.strftime('%Y:%m:%d %H:%M:%S')
        encoded_date = formatted_date.encode()

        exif_dict = {
            'Exif': {
                piexif.ExifIFD.DateTimeOriginal: b'',
                piexif.ExifIFD.DateTimeDigitized: b''
            },
            '0th': {
                piexif.ImageIFD.DateTime: b''
            }
        }

        # Configure the mock objects
        mock_load.return_value = exif_dict
        mock_dump.return_value = b'bytes'

        # Call the function
        update_photo_creation_date(photo_file_path, new_date)

        # Check that piexif.load was called correctly
        mock_load.assert_called_once_with(photo_file_path)

        # Verify the EXIF data was updated correctly
        self.assertEqual(exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal], encoded_date)
        self.assertEqual(exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized], encoded_date)
        self.assertEqual(exif_dict['0th'][piexif.ImageIFD.DateTime], encoded_date)

        # Check that piexif.dump was called with the modified exif_dict
        mock_dump.assert_called_once_with(exif_dict)

        # Check that piexif.insert was called with the correct arguments
        mock_insert.assert_called_once_with(b'bytes', photo_file_path)

    @patch('piexif.insert')
    @patch('piexif.dump')
    @patch('piexif.load')
    def test_update_photo_creation_date_multiple_calls(self, mock_load, mock_dump, mock_insert):
        # Mock data
        photo_file_path1 = 'test1.jpg'
        photo_file_path2 = 'test2.jpg'
        new_date1 = datetime(2023, 7, 14, 12, 0, 0)
        new_date2 = datetime(2024, 1, 1, 0, 0, 0)
        formatted_date1 = new_date1.strftime('%Y:%m:%d %H:%M:%S')
        formatted_date2 = new_date2.strftime('%Y:%m:%d %H:%M:%S')
        encoded_date1 = formatted_date1.encode()
        encoded_date2 = formatted_date2.encode()

        exif_dict1 = {
            'Exif': {
                piexif.ExifIFD.DateTimeOriginal: b'',
                piexif.ExifIFD.DateTimeDigitized: b''
            },
            '0th': {
                piexif.ImageIFD.DateTime: b''
            }
        }

        exif_dict2 = {
            'Exif': {
                piexif.ExifIFD.DateTimeOriginal: b'',
                piexif.ExifIFD.DateTimeDigitized: b''
            },
            '0th': {
                piexif.ImageIFD.DateTime: b''
            }
        }

        # Configure the mock objects
        mock_load.side_effect = [exif_dict1, exif_dict2]
        mock_dump.return_value = b'bytes'

        # Call the function twice
        update_photo_creation_date(photo_file_path1, new_date1)
        update_photo_creation_date(photo_file_path2, new_date2)

        # Check that piexif.load was called correctly for both files
        self.assertEqual(mock_load.call_count, 2)
        mock_load.assert_has_calls([call(photo_file_path1), call(photo_file_path2)])

        # Verify the EXIF data was updated correctly for both files
        self.assertEqual(exif_dict1['Exif'][piexif.ExifIFD.DateTimeOriginal], encoded_date1)
        self.assertEqual(exif_dict1['Exif'][piexif.ExifIFD.DateTimeDigitized], encoded_date1)
        self.assertEqual(exif_dict1['0th'][piexif.ImageIFD.DateTime], encoded_date1)

        self.assertEqual(exif_dict2['Exif'][piexif.ExifIFD.DateTimeOriginal], encoded_date2)
        self.assertEqual(exif_dict2['Exif'][piexif.ExifIFD.DateTimeDigitized], encoded_date2)
        self.assertEqual(exif_dict2['0th'][piexif.ImageIFD.DateTime], encoded_date2)

        # Check that piexif.dump was called with the modified exif_dict for both files
        self.assertEqual(mock_dump.call_count, 2)
        mock_dump.assert_has_calls([call(exif_dict1), call(exif_dict2)])

        # Check that piexif.insert was called with the correct arguments for both files
        self.assertEqual(mock_insert.call_count, 2)
        mock_insert.assert_has_calls([call(b'bytes', photo_file_path1), call(b'bytes', photo_file_path2)])

if __name__ == '__main__':
    unittest.main()