#!/usr/bin/env python

from datetime import date
    
digits = ['一', '二', '三', '四', '五', '六', '七', '八', '九']

def get_thousands(num):
    """Return the number of thousands in the year"""
    if num == 0:
        return '' 
    sen = '千'
    j_str = ''
    first = num // 1000
    # for 1000, you don't need to say 1
    if first > 1:
        j_str += digits[first - 1]
        return j_str + sen 
    return sen 

def get_hundreds(num):
    """Return the number of hundreds in the year"""
    if num == 0:
        return '' 
    j_str = ''
    hyaku = '百'
    first = num // 100
    if first > 1:
        j_str += digits[first - 1]
        return j_str + hyaku 
    return hyaku 

def get_tens(num):
    """Return the number of tens in the year"""
    if num == 0:
        return '' 
    j_str = ''
    juu = '十'
    first = num // 10
    if first > 1:
        j_str += digits[first - 1]
        return j_str + juu
    return juu

def get_ones(num):
    """Return the number of ones in the year"""
    if num == 0:
        return '' 
    return digits[num - 1]


def parse_year(year):
    """Parse the year into its separate parts and return an array of the parts"""
    multipliers = [1000, 100, 10, 1]
    places = []
    count = 0
    # assumes that we won't ever make it to year 10,000
    for number in str(year):
       places.append(int(number) * multipliers[count]) 
       count += 1
    j_thousands = get_thousands(places[0])
    j_hundreds = get_hundreds(places[1])
    j_tens = get_tens(places[2])
    j_ones = get_ones(places[3])
    j_year = j_thousands + j_hundreds + j_tens + j_ones + '年'
    return j_year

# get the current date
today = date.today()

# get refs to the year, month, and day (number)
year = today.year
month = today.month
day = today.day

# array of months and days of the months, up to 31
month_arr = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
day_arr = ['一日', 'ニ日', '三日', '四日', '五日', '六日', '七日', '八日', '九日', '十日', '十一日', '十二日', '十三日', '十四日', '十五日', '十六日', '十七日', '十八日', '十九日', '二十日', '二十一日', '二十二日', '二十三日', '二十四日', '二十五日', '二十六日', '二十七日', '二十八日', '二十九日', '三十日', '三十一日']

# month - 1 cuz 0-indexed arrs
j_month = month_arr[month - 1]
j_day = day_arr[day - 1]
j_year = parse_year(year)
# with year as a stirng of numbers istead of japanese characters
# print(j_month+j_day+str(year)+'年')
print(j_month+j_day+j_year)
