import os
import shutil
import tempfile
from moviepy.editor import VideoFileClip
from datetime import datetime
import ffmpeg


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
    formatted_date = new_date.strftime("%Y-%m-%d %H:%M:%S")

    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
        temp_output = temp_file.name

    try:
        stream = ffmpeg.input(video_file_path)

        stream = ffmpeg.output(stream, temp_output,
                               **{'metadata:g:0': f"date={formatted_date}",
                                  'metadata:g:1': f"creation_time={formatted_date}"},
                               codec='copy')
        ffmpeg.run(stream, overwrite_output=True, quiet=True)

        # remove + copy rather than replace due wsl fun times
        os.remove(video_file_path)
        shutil.move(temp_output, video_file_path)
    except ffmpeg.Error as e:
        error_message = e.stderr.decode() if e.stderr else str(e)
        raise ValueError(f"Error processing video file: {error_message}")
    finally:
        if os.path.exists(temp_output):
            os.remove(temp_output)
