# -*- conding:utf8 -*-

import urllib.request
import codecs

from bs4 import BeautifulSoup

f = codecs.open('sake.csv', 'w', 'utf-8')
f.write('code,meigara,kana,kuramoto,ken,shi,address'+ "¥n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'}

tpl_url = 'http://www.sakeno.com/all_meigara_todou/{0}'

for i in range(1, 48):
    url = tpl_url.format(i)
    req = urllib.request.Request(url, headers=headers)
    soup = BeautifulSoup(urllib.request.urlopen(req).read())
    tr_arr = soup.find('table', {'class':'hyoji'}).findAll('tr')

    for tr in tr_arr:
        lrg = tr.find('strong', {'class':'lrg'})
        if lrg is None:
            continue
        meigara = lrg.find('a').string
        code = lrg.a.get("href").split("/")[-1]
        kana = tr.find('div', {'class':"smls"}).string

        td = tr.find('td', {"class": "smll"})
        kuramoto = td.find('strong').find('a').string
        kenshi = td.findAll('a')
        ken = kenshi[1].string

        if len(kenshi) > 2:
            shi = kenshi[2].string
            tag = td.text
            address = tag.split(u"TEL")[0].split(" ")
            address = ken + address[1]
            address = address.split("（")[0]
        else:
            shi = ''
            address = ''

        if kana is None:
            kana = ''

        if meigara is not None:
            meigara = meigara.split("（")[0]
        else:
            meigara = ""

        if kuramoto is not None:
            kuramoto = kuramoto.split("（")[0]
        else:
            kuramoto = ""

        print(code, meigara, kana, kuramoto, ken, shi, address)
        f.write(code + ',' + meigara + ',' + kana + ',' + kuramoto + ',' + ken + ',' + shi + ',' + address + "\n")

f.close()