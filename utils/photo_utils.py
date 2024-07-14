import piexif
from datetime import datetime

def update_photo_creation_date(photo_file_path: str, new_date: datetime) -> None:
    """
    Modifies the creation date of a photo file using the pyexiv2 library. 

    :param: photo_file_path: str - the file path being modified
    :param: new_date: datetime - the new datetime to apply for creation date
    """
    formatted_date: str = new_date.strftime('%Y:%m:%d %H:%M:%S')

    # Load the existing EXIF data
    exif_dict = piexif.load(photo_file_path)

    # Update the creation date in EXIF data
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = formatted_date.encode()
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = formatted_date.encode()
    exif_dict['0th'][piexif.ImageIFD.DateTime] = formatted_date.encode()

    # Convert the EXIF data back to bytes and insert into the image
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, photo_file_path)
    print(f"Updated creation date to {formatted_date} for {photo_file_path}")