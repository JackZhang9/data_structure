#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/11/15 13:56
# @Author : CN-JackZhang
# @File: 451根据字符出现频率排序.py
'''给定一个字符串，请将字符串里的字符按照出现的频率降序排列'''

# 分析：用字典保存每个字母出现频率，用列表取出字典，对列表进行降序排序，然后遍历组合

def strFrequen(s):
    count = {}
    for c in s:   # 遍历字符串的每个字母，
        count[c] = count.get(c,0) + 1   # 利用get方法，key在字典中返回对应值，不在字典中返回0，统计字母频率
    items = [(-val,key) for key,val in count.items()]  # 把字典变成一个key,value元组组成的列表
    res = ''
    for val, key in sorted(items):   # 遍历降序排列后的结果，val是次数，key是字母
        res += key*(-val)
    return res

test = strFrequen('hello')
print(test)

# 总结：1.遍历，获取字母次数，用字典保存，
#      2.转化成列表，进行降序排序，
#   3.遍历列表取出，组合结果