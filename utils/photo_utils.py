import piexif
from datetime import datetime

def update_photo_creation_date(photo_file_path: str, new_date: datetime) -> None:
    """
    Updates the EXIF creation date of a photo to a new date.

    This function modifies the EXIF metadata of a photo file to update its creation date.
    It changes the `DateTimeOriginal`, `DateTimeDigitized`, and `DateTime` fields to the
    new specified date.

    Parameters:
    photo_file_path (str): The file path to the photo whose creation date needs to be updated.
    new_date (datetime): The new creation date to set in the EXIF metadata.

    Returns:
    None

    Example:
    >>> from datetime import datetime
    >>> new_date = datetime(2020, 5, 17, 10, 30, 45)
    >>> update_photo_creation_date('photo.jpg', new_date)
    Updated creation date to 2020:05:17 10:30:45 for photo.jpg

    The function will print a message indicating the new creation date and the file path of the updated photo.
    """
    formatted_date: str = new_date.strftime('%Y:%m:%d %H:%M:%S')

    exif_dict = piexif.load(photo_file_path)

    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = formatted_date.encode()
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = formatted_date.encode()
    exif_dict['0th'][piexif.ImageIFD.DateTime] = formatted_date.encode()

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, photo_file_path)
    print(f"Updated creation date to {formatted_date} for {photo_file_path}")