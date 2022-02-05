from PIL import Image, ImageDraw, ImageFont
from os import listdir, remove
from uuid import uuid4

TEST_IMAGE_NAME = 'mamao.jpg'
IMAGES_FOLDER_IN = 'tmp/test_images_in'
IMAGES_FOLDER_OUT = 'tmp/test_images_out'

FONTS_FOLDER = 'fonts'


def write_on_image(image_path: str, font: str):
    print('-' * 40)
    print(f'Doing stuff on: {image_path}')

    image_name = image_path.split('/')[-1]
    image_pil = Image.open(image_path)
    image_w, image_h = image_pil.size

    font_size = int(image_w / 8)
    font_path = f'{FONTS_FOLDER}/{font}'
    font_pil = ImageFont.truetype(font_path, size=font_size)
    print(f'Using font: {font_path.split("fonts/")[1]}')

    image_pil_edit = ImageDraw.Draw(image_pil)
    image_pil_edit.text(
        xy=(image_w / 2,
            font_size / 1.1),
        text='Lucas',
        anchor='ms',
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )
    image_pil_edit.text(
        xy=(image_w / 2,
            image_h - (font_size / 4)),
        text='mamão',
        anchor='ms',
        font=font_pil,
        stroke_width=2,
        stroke_fill='#000000'
    )

    font_name_only = str(font).split('.ttf')[0]
    random_str = str(uuid4()).split('-')[0]
    img_type = image_name.split('.')[1]
    final_name = f'{IMAGES_FOLDER_OUT}/{font_name_only + "-" + random_str}.{img_type}'
    # final_name e.g. tmp/test_images_out/arial-07b39f44.jpg

    image_pil.save(final_name)


def delete_old_images(folder_path: str):
    print('-' * 80)
    print(f'Removing old images from {folder_path}')

    for file in listdir(path=folder_path):
        if file.endswith('.jpg'):
            print(f'Removing {file}')
            remove(f'{folder_path}/{file}')

    print('Done removing old images')
    print('-' * 80)


def main():
    delete_old_images(folder_path=IMAGES_FOLDER_OUT)

    for font in listdir(FONTS_FOLDER):
        write_on_image(image_path=f'{IMAGES_FOLDER_IN}/{TEST_IMAGE_NAME}',
                       font=font)


if __name__ == '__main__':
    main()
