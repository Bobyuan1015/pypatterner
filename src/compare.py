# -*- coding: utf-8 -*-
"""
   File Name：     compare.py
   Description :
   Author :       bobyuan
   date：         2020/04/03
"""
import time

from functools import wraps


def func_timer(function):
    '''
    timer
    :param function: counting time consumption
    :return: None
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} start...]'.format(name = function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.6f}s]'.format(name = function.__name__,time = t1 - t0))
        return result
    return function_timer


def get_position(words, sentence):
    """
    get all words' position in the sentences
    :param words:  a list of words, type: list[str,str..]
    :param sentence: a string   type:str
    :return: positions of the words in the sentence, type: list[ini,ini...]
    """
    return ''.join([sentence[sentence.index(word)] for word in words])

def get_common_words(sent1, sent2):
    """
    get common words in the two sentences
    :param sent1: a sentence string   type:str
    :param sent1: a sentence string   type:str
    :return:words appears in both sentences  type: list[str,str...]
    """
    return list(set(list(sent1)) & set(list(sent2)))


def get_varaibles():
    pass

# def anagramSolution1(s1,s2):
#     alist = list(s2)
#
#     pos1 = 0
#     stillOK = True
#
#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         while pos2 < len(alist) and not found:
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
#
#         if found:
#             alist[pos2] = None
#         else:
#             stillOK = False
#
#         pos1 = pos1 + 1
#
#     return stillOK



def get_template(dataset):
    for i in range(len(dataset)):
        head_sent = dataset[i]

        for data in dataset[i+1:]:
            c_words = get_common_words(head_sent, data)
            head_sent_indexs = get_position(c_words, head_sent)
            data_sent_indexs = get_position(c_words, data)
            print(head_sent_indexs,'-------------',head_sent)
            print(data_sent_indexs,'-------------',data)
            from difflib import SequenceMatcher

            # string1 = "apple pie available"
            # string2 = "come have some apple pies"

            match = SequenceMatcher(None, head_sent_indexs, data_sent_indexs).find_longest_match(0, len(head_sent_indexs), 0, len(data_sent_indexs))

            print(match)  # -> Match(a=0, b=15, size=9)
            print(head_sent_indexs[match.a: match.a + match.size])  # -> apple pie
            print(data_sent_indexs[match.b: match.b + match.size])  # -> apple pie

            # template = pylcs.lcs(head_sent_indexs,data_sent_indexs)
            # print(template)
            break

        break
    print(data)








