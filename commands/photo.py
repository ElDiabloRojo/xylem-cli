import click
import os
import time
import boto3
from picamera import PiCamera

camera = PiCamera()
timestr = time.strftime("%Y%m%d-%H%M%S")

@click.command()
@click.option('-i', '--img-dir', type=str,
              default=lambda: os.environ.get('IMG_DIR', ''))
@click.option('-f', '--file-name', type=str,
              default='xylem-photo-' + timestr + '.jpg')
@click.option('-r', '--resolution', type=(int, int), 
	      default=(1920, 1080)) 
@click.option('-u', '--upload', is_flag=True)
def cli(img_dir, file_name, resolution, upload):
    camera.resolution = (resolution[0], resolution[1]) 
    camera.capture(img_dir + file_name) 
    click.echo('photo: %s%s' % (img_dir, file_name))
    if upload:
        upload_to_s3(img_dir, file_name)


def upload_to_s3(img_dir, file_name):
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    bucket = str('xylem-bucket')
    local_file=img_dir + file_name

    try:
        s3.upload_file(local_file, bucket, file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
#[TODO: add cleanup for locally created file]

