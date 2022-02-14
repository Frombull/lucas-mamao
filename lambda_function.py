import logging as log
from twitter import post_image
from reddit import get_reddit_image
from PIL import Image, ImageDraw, ImageFont
from os import listdir
from random import randrange, choice
from requests import get
from constants import HEADERS

log.basicConfig(level=log.INFO,
                format='[%(levelname)s] (%(asctime)s) - %(message)s',
                datefmt='%H:%M:%S')

IMAGE_PATH = 'tmp/mamao_do_dia.jpg'  # Needs the first '/' to work with aws lambda --> /tmp/


def get_random_rgb() -> tuple:
    return (randrange(0, 256),
            randrange(0, 256),
            randrange(0, 256))


def save_image(url: str, image_path: str):
    r = get(url, headers=HEADERS)

    with open(image_path, 'wb') as img_raw:
        for chunk in r:
            img_raw.write(chunk)


def write_on_image(image_path: str):
    image_pil = Image.open(image_path)
    image_w, image_h = image_pil.size

    font_size = int(image_w / 6)
    font_name = choice(listdir("fonts"))
    font_path = f'fonts/{font_name}'
    font_pil = ImageFont.truetype(font=font_path, size=font_size)
    log.info(f'Writing on image using font: {font_name}')

    image_pil_edit = ImageDraw.Draw(image_pil)
    image_pil_edit.text(
        xy=(image_w / 2,
            font_size / 1.1),
        text='Lucas',
        anchor='ms',
        # fill=get_random_rgb(),
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )
    image_pil_edit.text(
        xy=(image_w / 2,
            image_h - (font_size / 4)),
        text='mamão',
        anchor='ms',
        # fill=get_random_rgb(),
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )

    image_pil.save(image_path)


def lambda_handler(event=None, context=None):
    image_url = get_reddit_image(subreddit='hmmm')
    save_image(url=image_url, image_path=IMAGE_PATH)
    write_on_image(image_path=IMAGE_PATH)
    post_image(image_path=IMAGE_PATH)
    log.info('Image posted successfully.')


lambda_handler()
