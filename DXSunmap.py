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
version = '0.0.2'   # Version

# Settings
img_url = 'https://www.timeanddate.com/scripts/sunmap.php'
img_input = ['/tmp/sunmap_original.jpg', '/tmp/nightmap_original.jpg']
img_output = ['/var/www/html/sunmap.jpg', '/var/www/html/nightmap.jpg'] 
img_output_big = ['/var/www/html/sunmapbig.jpg', '/var/www/html/nightmapbig.jpg']

urllib3.disable_warnings()
http = urllib3.PoolManager(timeout=1.0)
http = urllib3.PoolManager(
    timeout=urllib3.Timeout(connect=.5, read=.5)
)

# Requete HTTP vers le flux heavens-above
for earth in range(2):
    with open(img_input[earth], 'wb') as f:
        try:
            r = http.request('GET', img_url + '?earth=' + str(earth), timeout=2)
            f.write(r.data)
        except:
            f.close()
            exit()

    fd_img = open(img_input[earth], 'rb')

    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [320, 160])
    img.save(img_output[earth], format = img.format, quality = 70, optimize = True)

    fd_img.close()

    fd_img = open(img_input[earth], 'rb')

    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [1024, 512])
    img.save(img_output_big[earth], format = img.format, quality = 40, optimize = True)

    fd_img.close()

# End properly

exit()