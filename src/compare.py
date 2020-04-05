# -*- coding: utf-8 -*-
"""
   File Name：     compare.py
   Description :
   Author :       bobyuan
   date：         2020/04/03
"""
import time
from functools import wraps

threshold_template_size = 3
threshold_template_portion = 0.5
search_steps = 4

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


def get_common_words(sent1, sent2):
    """
    get common words in the two sentences
    :param sent1: a sentence string   type:str
    :param sent1: a sentence string   type:str
    :return:words appears in both sentences  type: list[str,str...]
    """

    return list(set(list(sent1)) & set(list(sent2)))

def index_all(word, sentence):
    """
    get indexes of the word in the sentences
    :param word: a word  type:str
    :param sentence: a string   type:str
    :return: indexes of the words in the sentence, type: list[ini,ini...]
    """
    return [x for x in range(sentence.find(word), len(sentence)) if sentence[x] == word]

def get_position(words, sentence):
    """
    get all words' position in the sentences
    :param words:  a list of words, type: list[str,str..]
    :param sentence: a string   type:str
    :return: positions of the words in the sentence, type: list[ini,ini...]
    """
    positions = []
    for word in words:
        indexes = index_all(word, sentence)
        positions.extend(indexes)

    positions.sort()
    pre_index = 0
    sorted_words = ''
    for index in positions:
        if index > pre_index+1:
            sorted_words += 'X'
        sorted_words += sentence[index]
        pre_index = index
    return sorted_words

def compare(sent1, sent2):
    s1_index = 0
    s2_index = 0
    template = []
    jump_steps = 0
    for w in sent1:
        # print('w=',w)
        if jump_steps > 0:
            jump_steps -= 1
            continue
        if w == sent2[s2_index]:
            template.append(w)
            s1_index += 1
            s2_index += 1
        elif w == 'X':
            # print('1')
            if template[-1] != 'X':
                template.append('X')
            s1_index += 1
            if w == sent1[s1_index]:
                template.append(w)
                s1_index += 1
                s2_index += 1
            else:
                result = sent2[s2_index:s2_index + search_steps].find(w)
                if result != -1:
                    s2_index += result
        elif sent2[s2_index] == 'X':

            if template[-1] != 'X':
                template.append('X')
            s2_index += 1
            if w == sent2[s2_index]:
                template.append(w)
                s1_index += 1
                s2_index += 1
            else:
                result = sent1[s1_index:s1_index+search_steps].find(sent2[s2_index])
                if result != -1:
                    s1_index += result
                    jump_steps += result

        else:
            s1_index += 1
            s2_index += 1
            # continue
    return template

def get_varaibles():
    pass

def get_template(dataset):
    for i in range(len(dataset)):
        head_sent = dataset[i]
        for data in dataset[i+1:]:
            print(head_sent)
            print(data, '\n')

            data = data.replace('X', 'x')
            head_sent = head_sent.replace('X', 'x')
            c_words = get_common_words(head_sent, data)
            if len(c_words) < threshold_template_size:
                break
            head_sent_indexs = get_position(c_words, head_sent)
            data_sent_indexs = get_position(c_words, data)
            print(head_sent_indexs)
            print(data_sent_indexs, '\n')
            template = compare(head_sent_indexs, data_sent_indexs)
            print('template=', template)
            break

        break
