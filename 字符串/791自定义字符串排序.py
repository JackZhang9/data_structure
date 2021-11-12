#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/11/12 21:24
# @Author : CN-JackZhang
# @File: 791自定义字符串排序.py
import collections
'''791.字符串S和T只包含小写字符。在S中，所有字符只会出现一次。S已经根据某种规则进行了排序。
我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串x也应出现在y之前。
返回任意一种符合条件的字符串T。'''

# 分析:首先找出T里面每个字符出现次数，然后遍历T里面每个字符，如果出现在S里面，加入数组，否则组成输出结果，
# 遍历S中每个字符，如果出现在数组中，拼接起来


def cus_str_sort(S, T):
    c = collections.Counter(T)  # 统计T里面每个字符出现次数
    res, arr = '', []
    for i in c:   # 遍历T里面每个字符key
        if i in S:  # 如果key在S里面，添加进数组
            arr.append(i)
        else:
            res = res + c[i]*i  # 字符*字符出现次数，将不出现的字符拼接起来
    for j in S:
        if j in arr:
            res = res + c[j]*j  # 将不出现的字符和出现的字符拼接起来
    return res

test = cus_str_sort('cba','abccdeef')
print(test)


#总结:T中未出现字符   +   （T中出现字符）的拼接



