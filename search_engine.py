# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:18:19 2020

@author: User
"""

import pandas as pd
import json
import os

with open('image_info_test2014.json', encoding='utf-8') as f:
    line = f.readline()
    d = json.loads(line)
    f.close()

inf=pd.DataFrame(d['images'])

inputlist=os.listdir('input/')
url_list=list(inf[inf['file_name'].isin(inputlist)]['coco_url'])

for url in url_list:
    os.system("python search.py "+url+' '+url[-30:]+' 1')
