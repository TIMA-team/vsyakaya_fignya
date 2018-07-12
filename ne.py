import re
from collections import defaultdict
import json
from vsyakaya_fignya import names


tokens = [defaultdict(int), defaultdict(int), defaultdict(int)]
counter = 0
reg2 = r'{\S*}'

with open(names.dataset, 'r', encoding='utf-8') as f:
    for line in f:
        counter += 1
        if counter % 10000 == 0:
            print(counter)
        for id, el in enumerate(re.findall(reg2, line)):
            for tk, tv in json.loads(el).items():
                tokens[id][tk] += tv

with open(names.tokens1f, 'w', encoding='utf-8') as t1:
    for k, v in tokens[0].items():
        t1.write(str(k) + '\t' + str(v) + '\n')

with open(names.tokens2f, 'w', encoding='utf-8') as t2:
    for k, v in tokens[1].items():
        t2.write(str(k) + '\t' + str(v) + '\n')

with open(names.tokens3f, 'w', encoding='utf-8') as t3:
    for k, v in tokens[2].items():
        t3.write(str(k) + '\t' + str(v) + '\n')
