#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/11/12 17:15
# @Author : CN-JackZhang
# @File: 567字符串的排列.py
import collections
'''567.给定两个字符串s1和s2，写一个函数来判断s2是否包含s1的排列'''

# 分析：s2的子串长度必须和s1长度相等，无须把s1每个排列求出来，因为排列的性质是每个字符的个数相等。
# 因此，使用滑动窗口+字典，使用一个长度和s1长度相等的固定长度滑动窗口，在s2上面从左向右滑动，
# 判断s2在滑动窗口内每个字符的个数是否跟s1的每个字符的个数相等。


def checkIn(s1, s2):
    c1 = collections.Counter(s1)    # 统计s1中每个字符出现的次数，一个字典
    left, right = 0, len(s1)-1   # 定义滑动窗口范围是[left,right]，长度和s1长度相等
    c2 = collections.Counter(s2[0:right])   # 统计滑动窗口s2[left,right]中每个字符出现的次数
    while right<len(s2):    # s1长度小于s2长度
        c2[s2[right]] += 1  # 把right位置的字符放到c2中
        if c1 == c2:        # 如果滑动窗口内每个字符出现的次数相等，返回Ture
            return True
        c2[s2[left]] -= 1   # 窗口向右移动前，把当前left位置的字符出现次数-1
        if c2[s2[left]] == 0:   #如果当前left位置的字符出现次数为0，需要从字典中删除，否则这个出现次数为0的字符会影响c1和c2之间的比较
            del c2[s2[left]]
        left += 1            # 窗口向右移动
        right += 1
    return False

test = checkIn('cde','abcdefg')
print(test)

# 总结：1.先用字典将s1和s2中相应的字符出现次数装起来，c2初始化放一部分字符，
#      2.再将c1和c2比较
#      3.先考虑相等，相等就返回True，不相等就把左边字符次数-1，删除该key,同时窗口向右滑动一次，循环这个过程至结束。








