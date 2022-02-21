import logging as log

import tweepy

from constants import keys


def _start_twitter_section() -> tweepy.API:
    log.info('Starting twitter section')

    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    if api.verify_credentials():
        return api
    else:
        log.critical('Twitter authentication error')
        quit()


def post_image_to_twitter(image_path: str):
    api = _start_twitter_section()
    log.info('Posting image to twitter')
    img_twitter = api.media_upload(image_path)
    api.update_status(status=None, media_ids=[img_twitter.media_id_string])
    log.info('Image posted successfully.')
