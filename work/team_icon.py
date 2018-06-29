import requests
from bs4 import BeautifulSoup
import re
import os
import hashlib
import sqlite3
conn = sqlite3.connect('flags.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE flags
             #(enName text, flag text)''')


def spideFlagFromCtyLink(link): 
    rt = requests.get(link)
    soup = BeautifulSoup(rt.text)
    img = soup.select_one('#flag-detail img')
    src = 'http:' + img.get('src')
    return src

def saveImg(src, parPath): 
    rt = requests.get(src)
    m = hashlib.md5()
    m.update(rt.content)
    name = m.hexdigest()  
    sufix = ''
    mt = re.search(r'\.\w+$', src)
    if mt:
        sufix = mt.group()
    with open(os.path.join(parPath, name + sufix), 'wb') as f:
        f.write(rt.content)
    return name + sufix

def run(): 
    url = 'http://flagpedia.net/index'
    rt = requests.get(url)
    soup = BeautifulSoup(rt.text)
    for contryLink in soup.select('.td-country a'):
        link = 'http://flagpedia.net' + contryLink.get('href')
        name = contryLink.text
        if is_spidered(name):
            continue
        img = spideFlagFromCtyLink(link)
        flag = saveImg(img, 'flags')
        c.execute('''INSERT INTO flags VALUES ("%s","%s")''' % (name, flag))
        conn.commit()
        print(name)

def is_spidered(name): 
    c2 = conn.cursor()
    c2.execute('SELECT enName FROM flags WHERE enName = "%s"' % name)
    if c2.fetchone():
        return True
    else:
        return False

run()
