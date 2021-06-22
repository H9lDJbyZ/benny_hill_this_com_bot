BENNY_HILL_THIS = 'bennyhillthis.com/'
YOUTUBECOM = 'youtube.com/watch'
YOUTUBE = 'youtu.be/'
HELP = 'Пришли ссылку на ютуб'


def benny_hill_this(url):
    url = url.replace('www.', '', 1)
    if YOUTUBECOM in url:
        url = url.replace(YOUTUBECOM, BENNY_HILL_THIS)
    elif YOUTUBE in url:
        url = url.replace(YOUTUBE, f'{BENNY_HILL_THIS}?v=')
    else:
        url = HELP
    return url
