import itertools

alphabet = 'РЕСУРС'
raw = 'РР'
cry = 'СС'

mix = itertools.product(alphabet, repeat=6)

mix_filter = []

for i in mix:
    mix_filter.append(i)

n = 0

for j in mix_filter:
    flag = True

    for k in range(len(j) - 1):
        if (j[k] in raw and j[k + 1] in raw) or (j[k] in cry and j[k + 1] in cry): flag = False

    if flag: n += 1

print(n)