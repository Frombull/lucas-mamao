import logging as log

import tweepy
from constants import keys


def start_twitter_section() -> tweepy.API:
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    if not api.verify_credentials():
        log.critical('Twitter authentication error')
        quit()

    return api


def post_image(image_path: str):
    api = start_twitter_section()
    img_twitter = api.media_upload(image_path)
    api.update_status(status=None, media_ids=[img_twitter.media_id_string])
