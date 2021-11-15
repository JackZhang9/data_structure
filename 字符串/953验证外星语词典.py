#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/11/13 17:47
# @Author : CN-JackZhang
# @File: 953验证外星语词典.py
'''某种外星语也使用英文小写字母，但可能顺序order不同，字母表的顺序(order)是一些小写字母的排列。
给定一组外星语书写的单词words，以及其字母表的顺序order，只有当给定的单词在这种外星语中按字典序排列时，
返回true；否则，返回false。'''

# 分析：order是字母的顺序，所有字母都要遵循。规则为：前面字母一样的单词总长更长的单词应该排在后面，短的单词排在前面，
# 单词从每个字母开始比较，按照order的顺序，

def isAlien(words,order):
    order_index = {c:i for i,c in enumerate(order)}  # 得到索引号和相应字母的字典
    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        for j in range(min(len(word1),len(word2))):  # 每个字母进行比较，按照短字母的长度，从字母第1位开始
            if word1[j] != word2[j]:   # 如果出现不一样的字母，就进行比较，比较的是order顺序
                if order_index[word1[j]] > order_index[word2[j]]:   # 如果前面单词索引号大于后面，则不符合规则
                    return False
                break   # 相反，如果此次字母一样，则跳出此次循环，检测下一个字母
        else:
            if len(word1) > len(word2):     # 前面字母完全一样，长的单词应该在后面，如app,apple这样
                return False
    return True     # 如果所有假情况都不成立，则返回真

test = isAlien(['qaf','qid','hfdj'],'qazwsxedcrfvtgbyhnujmikolp')
print(test)

# 总结：先得到字典，两两比较单词谁更短，如果对应字母不相等，比较顺序，如果字母一样，跳出循环，检测下一个，前面完全相同的话，
# 比较总长度，较长的在后面