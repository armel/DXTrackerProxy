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
    img_input = '/tmp/greyline_original.jpg'
    img_output = '/var/www/html/greyline.jpg'

    with open(img_input, 'wb') as f:
        r = http.request('GET', img_url[0], timeout=2)
        f.write(r.data)

    fd_img = open(img_input, 'rb')
    
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [320, 160])
    img.save(img_output, format = img.format, quality = 50, optimize = True)
    
    fd_img.close()

# End properly

exit()