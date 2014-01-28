'''
Created on 16-Sep-2013

@author: naved
'''
from PIL import Image
import os
import re
from django.conf import settings

IMAGE_SIZES = {
             'BIG':(500, 500),
             'THUMB':(1000, 284),
             'STHUMB':(120, 120),
             'SSTHUMB':(60, 60),
             }

def get_img_regex():
    x = []
    for e in IMAGE_SIZES.values():
        x.append('%sx%s' % e)
    return '|'.join(x)

def resize_image(image, new_path, new_name='', size=(500, 500), cformat='RGB', fformat='JPEG'):
        size_prefix = '%sx%s_' % (str(size[0]), str(size[1]))        
        if_path, if_name = os.path.split(new_name) if new_name else os.path.split(image.name)        
        imgFile = Image.open(image.path)
        imgFile = imgFile.convert(cformat)
        working = imgFile.copy()
        working.thumbnail(size, Image.ANTIALIAS)        
        if_name = size_prefix + re.sub('\d+x\d+_', '', if_name)        
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, new_path)):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, new_path))
        new_image = os.path.join(settings.MEDIA_ROOT, new_path, if_name)    
        working.save(new_image, fformat, quality=85)
        return os.path.join(new_path, if_name)

def is_form_valid(form):    
    val = form.is_valid()    
    if not val:
        print form
        return val
    else:
        return form
