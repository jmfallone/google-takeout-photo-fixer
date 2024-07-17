from argparse import ArgumentParser
import glob
import os

from utils.file_utils import update_file_creation_date
from utils.photo_utils import update_photo_creation_date
from utils.takeout_utils import get_takeout_datetime
from utils.video_utils import update_video_creation_date


if __name__ == '__main__':
    parser = ArgumentParser('Google Takeout Photo and Video Fixer')
    parser.add_argument('source', help='The unzipped directory (no subdirs please, run for each year)')
    args = parser.parse_args()

    if os.path.exists(args.source):
        print('Found source dir...')
    else:
        print('ERROR: could not find source dir with path: {args.source}')
        exit(-1)
    
    media_paths = []
    exts = ['.jpg', '.mp4']
    print('Searching for jpg and mp4 files...')
    for root, dirs, files in os.walk(args.source):
        for file in files:
            if file.lower().endswith(tuple(exts)):
                media_paths.append(os.path.abspath(os.path.join(root, file)))

    print(media_paths)
    print(f'Found {len(media_paths)} media files')

    # TODO: parallelism!
    for media_path in media_paths:
        _, ext = os.path.splitext(media_path)
        metadata_path = f'{media_path}.json'
        if not os.path.exists(metadata_path):
            print(f'No metadata file found for {media_path}, skipping...')
            continue

        actual_date = get_takeout_datetime(f'{media_path}.json')
        update_file_creation_date(media_path, actual_date)
        if ext == '.jpg':
            print(f'Running photo changes on {media_path}')
            update_photo_creation_date(media_path, actual_date)
        elif ext == '.mp4':
            print(f'Running video changes on {media_path}')
            update_video_creation_date(media_path, actual_date)
        else:
            print(f'Unexpected file: {media_path}')
            
