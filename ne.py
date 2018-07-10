import re
import names


tokens = [set(), set(), set()]
counter = 0
reg = r'\"\d+\"'
reg2 = r'{\S*}'


with open(names.dataset, 'r', encoding='utf-8') as f:
    for line in f:
        counter += 1
        if counter % 10000 == 0:
            print(counter)
        ll = re.findall(reg2, line)
        for i in range(3):
            for el in re.findall(reg, ll[i]):
                tokens[i].add(el[1:-1])

with open(names.tokens1, 'w', encoding='utf-8') as t1:
    for el in tokens[0]:
        t1.write(el + '\n')

with open(names.tokens2, 'w', encoding='utf-8') as t2:
    for el in tokens[1]:
        t2.write(el + '\n')

with open(names.tokens3, 'w', encoding='utf-8') as t3:
    for el in tokens[2]:
        t3.write(el + '\n')
