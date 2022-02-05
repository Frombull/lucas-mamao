import tweepy
from constants import keys


def start_twitter_section() -> tweepy.API:
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    return tweepy.API(auth)


def post_image(image_path: str):
    api = start_twitter_section()
    img_twitter = api.media_upload(image_path)
    api.update_status(status=None, media_ids=[img_twitter.media_id_string])

# base_path = r'C:/Users/marco/Documents/Repos/lucas-mamao/tmp'
# for file in listdir(base_path):
#     write_on_image(f'{base_path}/{file}')
