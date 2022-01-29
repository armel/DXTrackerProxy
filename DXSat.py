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
url = 'https://heavens-above.com/AmateurSats.aspx?alt=0&tz=CET'

# Limit
limit = 10

print('Content-Type: application/html\n\n')

try:
    arg = cgi.FieldStorage()
    latitude = arg['lat'].value
    longitude = arg['lng'].value
    format = arg['format'].value

except:
    latitude = 48.7886
    longitude = 2.2382
    format = 'text'
    pass

urllib3.disable_warnings()
http = urllib3.PoolManager(timeout=1.0)
http = urllib3.PoolManager(
    timeout=urllib3.Timeout(connect=.5, read=.5)
)

page = ''

# Requete HTTP vers le flux heavens-above
try:
    r = http.request('GET', url + '&lat=' + str(latitude) + '&lng=' + str(longitude), timeout=2)
    page = r.data.decode('utf-8')
except:
    exit()

indice = 0

if (page != ''):
    if(format == 'json'):
        sat = []
        data = re.findall(r"<tbody>(.*?)</tbody>", page, re.M|re.I|re.S)
        line = re.findall(r"<tr>(.*?)</tr>", data[0], re.M|re.I|re.S)
        for l in line:
            element = re.findall(r">(.*?)</td>", l, re.M|re.I|re.S)
            name = re.findall(r">(.*?)</a>", element[0], re.M|re.I|re.S)
            sat.append({'Name': name[0], 'Date': element[1], 'Debut': element[2], 'Altitude': element[3].replace("\u00b0", "°"), 'Azimut': element[4].replace("\u00b0", "°"), 'Fin': element[5], 'Frequence': element[6]})
            indice += 1
            if indice == limit:
                break
        print(json.dumps(sat))
    else:
        sat = []
        tmp = ''
        data = re.findall(r"<tbody>(.*?)</tbody>", page, re.M|re.I|re.S)
        line = re.findall(r"<tr>(.*?)</tr>", data[0], re.M|re.I|re.S)
        for l in line:
            element = re.findall(r">(.*?)</td>", l, re.M|re.I|re.S)
            name = re.findall(r">(.*?)</a>", element[0], re.M|re.I|re.S)
            tmp += name[0] + ' - ' + element[2] + ' - ' + element[5] + ' - Alt ' + element[3].replace("\u00b0", "") + ' - Az ' + element[4].replace("\u00b0", "")
            if(element[6] != '.' and element[6] != ''):
                 tmp += ' - ' + element[6].strip() + ' MHz -- '
            else:
                 tmp += ' -- '
            indice += 1
            if indice == limit:
                break
        sat.append({'Incoming': tmp[:-4]})
        print(json.dumps(sat))

# End properly

exit()