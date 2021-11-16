#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/11/15 18:11
# @Author : CN-JackZhang
# @File: 20有效的括号.py
'''给定一个只包括( ),{ },[ ]的字符串s,判断字符串是否有效。有效的字符串需满足：
1.左括号必须用相同类型的右括号闭合。2.左括号必须以正确的顺序闭合。
'''

# 分析：1.遇到左括号入栈，遇到右括号出栈，遍历完所有括号后，栈为空，
#  2.遇到右括号，通过哈希表判断括号对应关系，

def isValid(s):
    dic = {'(':')','[':']','{':'}','?':'?'}
    stk = ['?']
    for c in s:
        if c in dic:  # 如果c是左括号，入栈
            stk.append(c)
        elif dic[stk.pop()] != c:  # 不是左括号，栈顶左括号pop，看对应的val右括号是否相同，
            return False    # 不同就false
    return len(stk) == 1    # 最后里面还有一个'?'，长度为1，为true


test = isValid('({[]})')
print(test)










