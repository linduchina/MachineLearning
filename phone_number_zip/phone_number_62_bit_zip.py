# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 02:30:44 2018

@author: Aric
"""
def encode_64(phone):
    table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mylist = []
    while phone != 0:
        mylist.append(table[phone % len(table)])
        phone = int(phone / 62)
    mylist.reverse()
    return ''.join(mylist)


def decode_64(mycode):
    table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table_values = [i for i in range(len(table))]
    table = list(table)
    my_decode_table = dict(map(lambda x,y:[x,y],table,table_values))
    result = 0
    for i in list(mycode):
        result *= len(table)
        result += my_decode_table[i]
    return result
