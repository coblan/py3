# encoding:utf-8

import requests
import bs4
import jieba
import nltk
import re

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'})
# rt  = requests.get('http://new.qq.com/omn/20171215A00SZN.html')

soup=bs4.BeautifulSoup(rt.content)
contents= soup.select('.qq_conent .LEFT')
content=contents[0].get_text()
content_tokens = list(jieba.cut(content))
content_tokens=[x for x in content_tokens if len(x)>1 and re.match('\w+',x)]
fq = nltk.FreqDist(content_tokens)
print(fq)