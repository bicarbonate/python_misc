# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 01:10:49 2017

@author: skeer
"""

import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
txt = response.text
print(txt)

