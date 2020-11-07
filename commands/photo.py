import click
import os
from picamera import PiCamera

camera = PiCamera()


@click.command()
@click.option('--img-dir',
              default=lambda: os.environ.get('IMG_DIR', ''))
def cli(img_dir):
    camera.capture(img_dir + 'image.jpg')
    click.echo('photo: %simage.jpg' % img_dir)
