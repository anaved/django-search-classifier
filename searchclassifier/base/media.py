#-------------------------------------------------------------------------------
# Copyright (c) 2013 Findable.in
# All rights reserved. This program and the accompanying materials
# are property of Findable.in
# 
# Contributors:
#     naved - initial API and implementation
#-------------------------------------------------------------------------------
from shiv.media import Media

class PBaseMedia(Media):
    css = ['vendor/jasny-bootstrap.min.css','vendor/bootstrap.united.min.css','base.css',]    
    js = ['vendor/jquery-1.10.1.min.js','vendor/bootstrap.min.js','vendor/jquery.cookie.js','vendor/underscore-min.js','base.js','base/csrf_safe.js']