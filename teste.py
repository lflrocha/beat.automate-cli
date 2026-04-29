#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re

url = "https://mais.conasems.org.br/novidades/282_mais-saude-com-agente"

r = requests.get(url)

html = r.text


soup = BeautifulSoup(html, 'html.parser')
h1_text = soup.find('h1').get_text()
h3_text = soup.find('h3').get_text()

section_bg_cover = soup.find('section', class_='!bg-cover')
style_attr = section_bg_cover['style'] if section_bg_cover else ''
url_match = re.search(r'url\((.*?)\)', style_attr)
background_url = url_match.group(1) if url_match else ''

print(h1_text)
print(h3_text)
print(background_url)
