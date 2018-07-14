from collections import defaultdict
from vsyakaya_fignya import names

cuids_and_labels = defaultdict(lambda:'-1')
with open(names.data_answers, 'r', encoding='utf-8') as f:
    first_line = True
    for l in f:
        if first_line:
            first_line = False
            continue
        cuids_and_labels[l[:32]] = l[-2]

v2 = open(names.v2, 'w', encoding='utf-8')
v3 = open(names.v3, 'w', encoding='utf-8')
v4 = open(names.v4, 'w', encoding='utf-8')

with open(names.dataset, 'r', encoding='utf-8') as f:
    prev_cuid = ''
    for line in f:
        other_line = line[32:]
        label = cuids_and_labels[line[:32]]
        v2.write(label + other_line)
        if label != '-1':
            v3.write(label + other_line)
            if label == '1':
                if prev_cuid == line[:32]:
                    label = '0'
                else:
                    prev_cuid = line[:32]
            v4.write(label + other_line)

v2.close()
v3.close()
v4.close()
