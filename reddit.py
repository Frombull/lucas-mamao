import praw
import logging as log
from constants import keys

log.basicConfig(level=log.INFO,
                format='[%(levelname)s] (%(asctime)s) - %(message)s',
                datefmt='%H:%M:%S')


def start_reddit_section() -> praw.Reddit:
    log.info('Starting reddit section')

    return praw.Reddit(
        client_id=keys['client_id'],
        client_secret=keys['client_secret'],
        user_agent="lucas-mamao"
    )


def is_valid_image(post: praw.Reddit.submission) -> bool:
    return True if (post.url.endswith(('jpg', 'png')) and not post.over_18) else False


def get_reddit_image(subreddit: str) -> str:
    """Return the URL of the first SFW image found in the subreddit"""

    reddit = start_reddit_section()
    target_sub = reddit.subreddit(subreddit)

    log.info(f'Searching hot posts from r/{subreddit}')

    for post in target_sub.hot(limit=12):
        if is_valid_image(post):
            log.info('Image found')
            return post.url.strip()
