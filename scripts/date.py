#!/usr/bin/env python

from datetime import date

# get the current date
today = date.today()

year = today.year
month = today.month
day = today.day

month_arr = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']

day_arr = ['一日', 'ニ日', '三日', '四日', '五日', '六日', '七日', '八日', '九日', '十日', '十一日', '十二日', '十三日', '十四日', '十五日', '十六日', '十七日', '十八日', '十九日', '二十日', '二十一日', '二十二日', '二十三日', '二十四日', '二十五日', '二十六日', '二十七日', '二十八日', '二十九日', '三十日', '三十一日']

j_month = month_arr[month]
j_day = day_arr[day]
print(j_month+j_day+str(year)+'年')