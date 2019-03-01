#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:18:01 2019

@author: ankur
"""

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
d=[]
html=urlopen("https://www.amazon.in/Nike-Mens-Chroma-Thong-Black/dp/B00278ZKXK/ref=sr_1_2?ie=UTF8&qid=1551414230&sr=8-2&keywords=nike").read()
bsobj=BeautifulSoup(html,"lxml")
namelist =bsobj.findAll("span",{"class":"a-list-item"})
for name in namelist:
    d.append(name.get_text())

    
import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
d=[]
opener = AppURLopener()
response = opener.open('https://www.amazon.in/Nike-Mens-Chroma-Thong-Black/dp/B00278ZKXK/ref=sr_1_2?ie=UTF8&qid=1551414230&sr=8-2&keywords=nike')
bsobj=BeautifulSoup(response,"lxml")

x =bsobj.findAll("ul",{"class":"a-unordered-list a-vertical a-spacing-none"})
z=BeautifulSoup(str(x)[1:-1],"lxml")
q=z.findAll("span","a-list-item")
for i,name in enumerate(q):
    d.append(name.get_text())
    print(i,d[i])
    print('\n')