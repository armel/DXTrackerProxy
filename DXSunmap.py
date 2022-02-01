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
url = 'https://www.timeanddate.com/worldclock/sunearth.html'

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
    img_url = 'https://www.timeanddate.com/scripts/sunmap.php'
    img_input = '/tmp/sunmap_original.jpg'
    img_outut = '/var/www/html/sunmap.jpg'

    with open(img_input, 'wb') as f:
        r = http.request('GET', img_url, timeout=2)
        f.write(r.data)

    fd_img = open(img_input, 'rb')
    
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [320, 160])
    img.save(img_outut, img.format)
    
    fd_img.close()

# End properly

exit()