import itertools

alphabet = 'БАНАНА'
name = 'НН'

mix = itertools.product(alphabet, repeat=6)

mix_filter = []

for i in mix:
    mix_filter.append(i)

n = 0

for j in mix_filter:
    flag = True

    for k in range(len(j) - 1):
        if j[k] in name and j[k + 1] in name: flag = False

    if flag: n += 1

print(n)