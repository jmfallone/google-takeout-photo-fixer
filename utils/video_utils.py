from moviepy.editor import VideoFileClip
from datetime import datetime


def update_video_creation_date(video_file_path: str, new_date: datetime) -> None:
    """
    Update the creation date metadata of a video file.

    This function updates the creation date metadata of a video file to the specified new date.

    Parameters:
    - video_file_path (str): The file path of the video whose creation date is to be updated.
    - new_date (datetime): The new creation date to be set.

    Raises:
    - ValueError: If the video file cannot be parsed or if no metadata is found in the video file.

    Example:
        update_video_creation_date('example.mp4', datetime(2023, 7, 14, 12, 0, 0))
    """
    video = VideoFileClip(video_file_path)
    formatted_date: str = new_date.strftime('%Y:%m:%d %H:%M:%S')
    video.meta['creation_date'] = formatted_date

    video.write_videofile(video_file_path)