'''
Created on Aug 20, 2012

@author: Naved
'''
from imagekit import ImageSpec, register
from pilkit.processors.resize import ResizeToFit

class IThumbnail(ImageSpec):
    processors = [ResizeToFit(90, 130)]
    format = 'JPEG'
    options = {'quality': 80}

class IDetail(ImageSpec):
    processors = [ResizeToFit(364, 520)]
    format = 'JPEG'
    options = {'quality': 80}
    
class IList(ImageSpec):
    processors = [ResizeToFit(182, 260)]
    format = 'JPEG'
    options = {'quality': 80}

class IStamp(ImageSpec):
    processors = [ResizeToFit(45, 65)]
    format = 'JPEG'
    options = {'quality': 80}

class ILarge(ImageSpec):
    processors = [ResizeToFit(768, 1024)]
    format = 'JPEG'
    options = {'quality': 80}    

register.generator('base:thumbnail', IThumbnail)
register.generator('base:detail', IDetail)
register.generator('base:list', IList)
register.generator('base:stamp', IStamp)
register.generator('base:large', ILarge)
