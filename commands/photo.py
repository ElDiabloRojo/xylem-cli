import click
import os
import time
import boto3
import botocore.exceptions
from picamera import PiCamera

camera = PiCamera()
timestr = time.strftime("%Y%m%d-%H%M%S")

@click.command()
@click.option('-i', '--img-dir', type=str, envvar='IMG_DIR',
	      default='/tmp/', help='local directory to store images')
@click.option('-f', '--file-name', type=str,
              default='xylem-photo-' + timestr + '.jpg',
	      help='output image file name')
@click.option('-r', '--resolution', type=(int, int), 
	      default=(1920, 1080), help='image resolution, width x height') 
@click.option('-u', '--upload', is_flag=True, help='enable for upload to s3')
def cli(img_dir, file_name, resolution, upload):
    camera.resolution = (resolution[0], resolution[1]) 
    camera.capture(img_dir + file_name) 
    click.echo('photo: %s%s' % (img_dir, file_name))
    if upload:
        upload_to_s3(img_dir, file_name)


def upload_to_s3(img_dir, file_name):
    s3 = boto3.client('s3') 
    bucket = str('xylem-bucket')
    local_file = img_dir + file_name
    dest_key = 'dir/' + file_name 

    try:
        s3.upload_file(local_file, bucket, dest_key)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
