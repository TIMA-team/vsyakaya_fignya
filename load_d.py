import numpy as np
from vsyakaya_fignya import names
from vsyakaya_fignya import line_to_v

print('loading train data...')
lines_full = 20275 #  12874345
labels = np.zeros(shape=(lines_full,))
all_vecs = np.array([])
av = []
first = True
with open(names.v3, 'r', encoding='utf-8') as f:
    ln = 0
    for l in f:
        labels[ln] = int(l[0])
        # if first:
        #     all_vecs = np.append([all_vecs], [line_to_v.line_to_vec2(l)])
        #     first = False
        # else:
        #     all_vecs = np.append(all_vecs, line_to_v.line_to_vec2(l), axis=0)
        av.append(line_to_v.line_to_vec2(l))
        ln += 1
        if ln == 1000:
            print('loading complete!')
            break
# all_vecs = all_vecs.reshape((1000, 20275))
def load_data():
    # return (all_vecs[:800, :], labels[:800]), (all_vecs[800:1000, :], labels[800:1000])
    return (av[:800], labels[:800]), (av[800:1000], labels[800:1000])
