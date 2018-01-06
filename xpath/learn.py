#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-03 20:20:04
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import requests
from lxml import etree as tree 


page = requests.get("https://movie.douban.com/").text

html = tree.HTML(page)


filmName = html.xpath('//li[@class="poster"]//img/@alt')
filmPoster = html.xpath('//li[@class="poster"]//img/@src')
score = html.xpath('//li[@class="rating"]//span/text()')


print(filmName)
print(filmPoster)
print(score)



