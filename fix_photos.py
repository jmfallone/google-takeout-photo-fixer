from argparse import ArgumentParser
import os


if __name__ == '__main__':
    parser = ArgumentParser('Google Takeout Photo Fixer')
    parser.add_argument('source', help='The unzipped directory (no subdirs please, run for each year)')
    args = parser.parse_args()

    if os.path.exists(args.source):
        print('Found source dir...')
    else:
        print('ERROR: could not find source dir with path: {args.source}')
        exit(-1)
