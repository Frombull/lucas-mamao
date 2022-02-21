import logging as log
from os import listdir
from random import randrange, choice

from PIL import Image, ImageDraw, ImageFont

from reddit import get_reddit_image
from twitter import post_image_to_twitter

log.basicConfig(level=log.INFO,
                format='[%(levelname)s] (%(asctime)s) - %(message)s',
                datefmt='%H:%M:%S')

IMAGE_PATH = 'media/lucas-mamao.jpg'


def random_rgb() -> tuple:
    return (randrange(0, 256),
            randrange(0, 256),
            randrange(0, 256))


def write_on_image(image_path: str):
    image_pil = Image.open(image_path).convert('RGB')
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
        # fill=random_rgb(),
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )
    image_pil_edit.text(
        xy=(image_w / 2,
            image_h - (font_size / 4)),
        text='mamão',
        anchor='ms',
        # fill=random_rgb(),
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )

    image_pil.save(image_path)


def main():
    get_reddit_image(subreddit='hmmm', save_path=IMAGE_PATH)
    write_on_image(image_path=IMAGE_PATH)
    post_image_to_twitter(image_path=IMAGE_PATH)


if __name__ == '__main__':
    main()
