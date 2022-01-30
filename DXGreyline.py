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
    filename = 'original.jpg' #local name to be saved
    with open(filename, 'wb') as f:
        r = http.request('GET', img_url[0], timeout=2)
        f.write(r.data)

    fd_img = open('original.jpg', 'rb')
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [320, 160])

    print('Content-Type: image/jpeg\n\n')
    print(img)

    #img.save('greyline.jpg', img.format)
    fd_img.close()

'''
if (page != ''):
    img_url = re.findall(r"<img src=\"(.*?)\"", page, re.M|re.I|re.S)
    r = http.request('GET', img_url[0], timeout=2)
    img = Image.open(BytesIO(r.data))
    img = img.resize((320, 160), Image.ANTIALIAS)

    print('Content-Type: image/jpeg\n\n')
    print(img)
'''

# End properly

exit()