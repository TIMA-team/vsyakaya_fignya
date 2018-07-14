import json
from vsyakaya_fignya import names


t_freq_dicts = [{}, {}, {}]
with open(names.tokens1f, 'r', encoding='utf-8') as f:
    for line in f:
        tl = line.split('\t')
        t_freq_dicts[0][tl[0]] = tl[1][:-1]
with open(names.tokens2f, 'r', encoding='utf-8') as f:
    for line in f:
        tl = line.split('\t')
        t_freq_dicts[1][tl[0]] = tl[1][:-1]
with open(names.tokens3f, 'r', encoding='utf-8') as f:
    for line in f:
        tl = line.split('\t')
        t_freq_dicts[2][tl[0]] = tl[1][:-1]


fc1 = open(names.fcounter1, 'w', encoding='utf-8')
fc2 = open(names.fcounter2, 'w', encoding='utf-8')
fc3 = open(names.fcounter3, 'w', encoding='utf-8')
fld = open(names.labels_ld, 'w', encoding='utf-8')
# fad = open(names.labels_ld, 'w', encoding='utf-8')
fom = open(names.othermetrics, 'w', encoding='utf-8')

with open(names.v4, 'r', encoding='utf-8') as mf:
    # prev_good_cuid = ''
    # need_for_check = False
    for line in mf:
        line_list = line[:-1].split('\t')
        label = line_list[0]
        fld.write(line_list[0] + '\n')
        fom.write(line_list[1] + '\t' + line_list[-1] + '\n')
        for k, el in json.loads(line_list[2]).items():
            fc1.write((t_freq_dicts[0][k] + '\t') * int(el) + '\n')
        for k, el in json.loads(line_list[3]).items():
            fc2.write((t_freq_dicts[1][k] + '\t') * int(el) + '\n')
        for k, el in json.loads(line_list[4]).items():
            fc3.write((t_freq_dicts[2][k] + '\t') * int(el) + '\n')

fc1.close()
fc2.close()
fc3.close()
fld.close()
# fad.close()
fom.close()
