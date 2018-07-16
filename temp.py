from vsyakaya_fignya import names


labels_v3 = []
labels_v4 = []
dt_diff = []
label_c = []

with open(names.othermetrics, 'r', encoding='utf-8') as f:
    for l in f:
        dt_diff.append(int(l.split('\t')[1]))

with open(names.v3, 'r', encoding='utf-8') as f:
    for l in f:
        labels_v3.append(int(l[0]))

with open(names.v4, 'r', encoding='utf-8') as f:
    for l in f:
        labels_v4.append(int(l[0]))
print(len(labels_v3) == len(labels_v4) == len(dt_diff))
dt_max = 0
dt_min = 0
start_id = -1
k = 10
zl = zip(labels_v4, labels_v3, dt_diff)
last_was_good = False
for id, el in enumerate(zl):
    if id%125000 == 0:
        print(id*100/12874345)
    if (not last_was_good) and el[1] == el[0] == 0:
        label_c.append(0)
        continue
    elif el[0] == 1 == el[1]:
        start_id = id
        dt_min = el[2]
        last_was_good = True
        continue
    elif el[1] == 0 and last_was_good:
        dt_max = dt_diff[id - 1]
        for i in range(start_id, id):
            if dt_min == dt_max:
                label_c.append(1)
            else:
                label_c.append(
                    ((dt_max - dt_diff[i]) / (dt_max - dt_min)) ** k
                )
        last_was_good = False

with open(names.labels_clever, 'w', encoding='utf-8') as f:
    for el in label_c:
        f.write("{:.4f}".format(el) + '\n')
