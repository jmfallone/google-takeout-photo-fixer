import json
from datetime import datetime, timezone

def get_takeout_datetime(json_file_path):
    """
    Extracts the photo taken datetime from a JSON file containing Google Takeout photo metadata.

    This function reads a JSON file, parses it to extract the `photoTakenTime` timestamp, and converts
    the timestamp to a `datetime` object.

    Parameters:
    json_file_path (str): The file path to the JSON file containing the photo metadata.

    Returns:
    datetime: A datetime object representing when the photo was taken.

    Example:
    >>> photo_datetime = get_takeout_datetime('photo_data.json')
    >>> print(photo_datetime)
    2017-08-20 21:51:22

    The JSON file should have a structure similar to:
    {
      "title": "IMG_20170820_155122.jpg",
      "description": "",
      "imageViews": "16",
      "creationTime": {
        "timestamp": "1503270137",
        "formatted": "20 Aug 2017, 23:02:17 UTC"
      },
      "photoTakenTime": {
        "timestamp": "1503265882",
        "formatted": "20 Aug 2017, 21:51:22 UTC"
      },
      ...
    }
    """
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        
    photo_taken_timestamp = int(data['photoTakenTime']['timestamp'])
    
    return datetime.fromtimestamp(photo_taken_timestamp, tz=timezone.utc)