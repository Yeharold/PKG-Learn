#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-04 17:03:54
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import requests
from lxml import etree as tree 


page = requests.get('https://www.autohome.com.cn/grade/carhtml/J.html').text

html = tree.HTML(page)


carName = html.xpath('//h4/a/text()')

print(carName)