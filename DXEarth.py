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
img_url = 'https://www.timeanddate.com/scripts/sunmap.php?iso=&earth=1'
img_input = '/tmp/earth_original.jpg'
img_output = '/var/www/html/earth.jpg'

urllib3.disable_warnings()
http = urllib3.PoolManager(timeout=1.0)
http = urllib3.PoolManager(
    timeout=urllib3.Timeout(connect=.5, read=.5)
)

# Requete HTTP vers le flux heavens-above
with open(img_input, 'wb') as f:
    try:
        r = http.request('GET', img_url, timeout=2)
        f.write(r.data)
    except:
        f.close()
        exit()

fd_img = open(img_input, 'rb')

img = Image.open(fd_img)
img = resizeimage.resize_cover(img, [320, 160])
img.save(img_output, img.format)

fd_img.close()

# End properly

exit()