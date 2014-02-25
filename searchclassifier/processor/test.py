'''
Created on 25-Feb-2014

@author: naved
'''

from django.core.exceptions import ValidationError
from django.core.management import setup_environ
from django.core.validators import URLValidator
from django.template.defaultfilters import slugify
from urllib import urlretrieve
import BeautifulSoup
import httplib
import json
import os
import random
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

import os

dump = open('Google - Web History.html').read()            
doc = BeautifulSoup.BeautifulSoup(dump, convertEntities="html")
for e in doc.findAll('span',text=re.compile('Searched for')):
    a=e.findParent('td').find('a')
    print a.string