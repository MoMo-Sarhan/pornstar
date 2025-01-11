#!/bin/env python
import os
import django
from django.core.files import File
from projectA import settings
import random
import re

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectA.settings')
django.setup()

# Import your model
from pornstars.models import Pornstar

# Create and save the new row


media2_dir=settings.MEDIA2_ROOT


def find_directories_in_directory(parent_directory, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Get all directories inside the parent directory
    directories = [
        dir_name for dir_name in os.listdir(parent_directory)
        if os.path.isdir(os.path.join(parent_directory, dir_name)) and regex.match(dir_name)
    ]
    
    return directories

def get_one_image(pornstar_realpath):
    # Get all images in the directory
    if not os.path.isdir(pornstar_realpath):
        return
    images = [
        image_name for image_name in os.listdir(pornstar_realpath)
        if image_name.endswith(('.jpg', '.png', '.gif', '.bmp'))
        ]
    photo=random.sample(images,1)[0]
    photo_realpath=os.path.join(pornstar_realpath,photo)
    return  photo_realpath
# Example usage:


for pornstar in os.listdir(media2_dir):
    try:
        if os.path.isdir(os.path.join(media2_dir,pornstar)):
            age=random.randint(20,30)
            height=random.randint(160,190)
            eye_color=random.sample(['red','blue','green','brown','yellow'],1)[0]
            hair_color=random.sample(['red','blue','green','brown','yellow'],1)[0]
            image=get_one_image(os.path.join(media2_dir,pornstar))

            pattern = fr'^{re.escape(pornstar)}*'  # Regular expression pattern to match directory names like 'dir_123'
            categories=find_directories_in_directory(media2_dir,pattern=pattern)

            new_row = Pornstar(name=pornstar,age=age,height=height,eye_color=eye_color,hair_color=hair_color,sex='male',isalive=True,)
            new_row.set_list(categories)

            with open(image ,'rb') as file:
                new_row.image_link.save(os.path.basename(image),File(file),save=True)
            new_row.save()

            print(f'{pornstar:<25} uploadded successfuly.....')
    except:
        continue
