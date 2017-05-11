# -*- coding: utf-8 -*-
import tushare as ts
import os

data = ts.get_index()
path = '1.csv'
data.to_csv(path, encoding='utf-8')
print (path)