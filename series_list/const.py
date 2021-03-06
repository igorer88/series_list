import os


DOWNLOAD_PATH = os.path.expanduser('~/Downloads/series')

ICON_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'series_list_icon.png')

IN_PROGRESS = 0
OK = 1
FAILED = 2

SERIES_TIMEOUT = None
SUBTITLE_TIMEOUT = 3
POSTER_TIMEOUT = 1

SETTINGS_PATH = os.path.expanduser('~/.config/series_list.json')

POSTERS_LOADER = 'IMDBPosterLoader'
SERIES_LOADER = 'EZTVLoader'
SUBTITLES_LOADER = 'SubliminalLoader'

PREVIEW_MINIMUM = 10

NORMAL = 0
NEED_PAUSE = 1
NEED_RESUME = 2

MAX_RETRY = 5
