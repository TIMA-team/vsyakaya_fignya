import re
import names
import tensorflow as tf


print('loading...')
tokens = [{}, {}, {}]
tokens_lens = [2053602, 20275, 1057788]
d_shape = [3131665]
with open(names.tokens1, 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[0][l[:-1]] = i
        i += 1
with open(names.tokens2, 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[1][l[:-1]] = i
        i += 1
with open(names.tokens3, 'r', encoding='utf-8') as f:
    i = 0
    for l in f:
        tokens[2][l[:-1]] = i
        i += 1
reg = r'{\S*}'
reg2 = r'\"\d+\"'
reg3 = r':\d+'
print('loading complete!')


def counter_to_vec(counter_line, conter_num):
    return tf.SparseTensor(
        indices=[[tokens[conter_num][el[1:-1]]] for el in re.findall(reg2, counter_line)],
        values=[int(el[1:]) for el in re.findall(reg3, counter_line)],
        dense_shape=[tokens_lens[conter_num]]
    )


def line_to_vec(line):
    l = re.findall(reg, line)
    vl = []
    for i in range(3):
        vl.append(counter_to_vec(l[i], i))


def line_to_second_sparse_vec(line):
    l = re.findall(reg, line)
    return counter_to_vec(l[1], 1)
