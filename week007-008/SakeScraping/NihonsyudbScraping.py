# -*- conding:utf8 -*-

import urllib.request
import codecs
import re

p = re.compile(r"<[^>]*?>")

from bs4 import BeautifulSoup

f = codecs.open('nihonsyudb.csv', 'w', 'utf-8')
f.write('id,sakecode,sakename,'+ "¥n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'}

tpl_url = 'http://sake.oisiso.com/archives/{0}'
count = 0

for i in range(1, 2000):
    url = tpl_url.format(i)
    req = urllib.request.Request(url, headers=headers)
    try:
        soup = BeautifulSoup(urllib.request.urlopen(req).read())
    except:
        continue
    sakename = soup.find('h1', {'class':'storytitle'})
    if sakename is not None:
        sakename_sub = p.sub("", str(sakename))
        sakecode = i
        content = soup.find('div', {'class': "storycontent"})
        if content is not None:
            text = content.find('div', {'class': "text"})
            if text is not None:
                li_all = text.findAll('li')
                sakedata = ""
                for li in li_all:
                    li_sub = p.sub("", str(li))
                    sakedata = sakedata + li_sub + ","

                count = count + 1
                sakeid = str(count) + "," + str(sakecode) + "," + sakename_sub
                saketext = sakeid + sakedata
                print(saketext)
                f.write(saketext + "\n")

f.close()