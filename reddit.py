import logging as log

import praw
from requests import get

from constants import HEADERS
from constants import keys


def _start_reddit_section() -> praw.Reddit:
    log.info('Starting reddit section')

    return praw.Reddit(
        client_id=keys['client_id'],
        client_secret=keys['client_secret'],
        user_agent="lucas-mamao"
    )


def _save_image(url: str, image_path: str):
    r = get(url, headers=HEADERS)

    log.info('Saving image')
    with open(image_path, 'wb') as img_raw:
        for chunk in r:
            img_raw.write(chunk)


def _is_valid_image(post: praw.Reddit.submission) -> bool:
    return True if (post.url.endswith(('jpg', 'png')) and not post.over_18) else False


def get_reddit_image(subreddit: str, save_path: str):
    """Saves the first SFW image found in the subreddit"""
    reddit = _start_reddit_section()
    target_sub = reddit.subreddit(subreddit)

    log.info(f'Searching hot posts from r/{subreddit}')
    for post in target_sub.hot(limit=12):
        if _is_valid_image(post):
            image_url = post.url.strip()
            log.info(f'Valid image found: {image_url}')
            _save_image(url=image_url, image_path=save_path)
            return
