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
import json
import datetime

# Version
version = '0.0.1'   # Version

# Settings
url = 'https://www.hamqth.com/dxc_csv.php?limit=50'

print('Content-Type: text/html\n\n')

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

print(page)

# End properly

exit()