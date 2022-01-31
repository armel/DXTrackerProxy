#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'''
DXSat version Web
73 & 88 de F4HWN Armel
'''

import cgi
import sys
import urllib3
import re
import requests
from io import StringIO
from io import BytesIO
from PIL import Image
from resizeimage import resizeimage

# Version
version = '0.0.1'   # Version

# Settings
url = 'https://dx.qsl.net/propagation/greyline.html'

urllib3.disable_warnings()
http = urllib3.PoolManager(timeout=1.0)
http = urllib3.PoolManager(
    timeout=urllib3.Timeout(connect=.5, read=.5)
)

page = ''

# Requete HTTP vers le flux heavens-above
try:
    r = http.request('GET', url, timeout=2)
    page = r.data.decode('utf-8')
except:
    exit()

if (page != ''):
    img_url = re.findall(r"<img src=\"(.*?)\"", page, re.M|re.I|re.S)
    filename = '/var/www/html/original.jpg' #local name to be saved
    img = requests.get(img_url[0])
    img = io.BytesIO(img.content)
    img = Image.open(img)
    img = resizeimage.resize_cover(img, [320, 160])
    img.save(filename, img.format)



'''
if (page != ''):
    img_url = re.findall(r"<img src=\"(.*?)\"", page, re.M|re.I|re.S)

    response = requests.get(img_url[0])
    in_memory_file = io.BytesIO(response.content)
    im = Image.open(in_memory_file)
    img = resizeimage.resize_cover(img, [320, 160])
    #img.save('/tmp/greyline.jpg', img.format)
'''

# End properly

exit()