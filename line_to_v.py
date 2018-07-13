import re
from vsyakaya_fignya import names
import tensorflow as tf
import json
import numpy as np


print('loading...')
tokens = [{}, {}, {}]
tokens_lens = [2053602, 20275, 1057788]
tl = [0, 2053602, 2073877]
d_shape = [3131665]
with open('tokens_first_group.tsv', 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[0][l[:-1]] = i
        i += 1
with open('tokens_second_group.tsv', 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[1][l[:-1]] = i
        i += 1
with open('tokens_third_group.tsv', 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[2][l[:-1]] = i
        i += 1
reg = r'{\S*}'
reg2 = r'\"\d+\"'
reg3 = r':\d+'
print('loading complete!')


# def counter_to_vec(counter_line, conter_num):
#     varr = np.zeros(shape=(tokens_lens[conter_num],))
#     a = json.loads(counter_line)
#     for k, val in a.items():
#         varr[int(k)] = val
#     return varr

def line_to_vec(line):
    l = re.findall(reg, line)
    varr = np.zeros(shape=(3131665,), dtype=np.int8)
    for id, el in enumerate(l):
        for k, val in json.loads(el).items():
            varr[tokens[id][k] + tl[id]] = val
    return varr


def line_to_vec2(line):
    l = re.findall(reg, line)
    varr = np.zeros(shape=(20275,), dtype=np.int8)
    for k, val in json.loads(l[1]).items():
        varr[tokens[1][k]] = val
    return varr
