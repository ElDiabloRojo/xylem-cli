import click
import os
import time
from picamera import PiCamera

camera = PiCamera()


@click.command()
@click.option('--img-dir',
              default=lambda: os.environ.get('IMG_DIR', ''))
@click.option('--file-name',
              default='xylem-photo-' + time.strftime("%Y%m%d-%H%M%S") + '.jpg')
def cli(img_dir):
    camera.capture(img_dir + 'image.jpg')
    click.echo('photo: %simage.jpg' % img_dir)
