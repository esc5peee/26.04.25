from itertools import product

k=0
klk=[('К','О','С','М','О','С')]
alphabet = 'КОСМАТ'
mix = product(alphabet, repeat=6)

mix_filter = []

for i in mix:
    mix_filter.append(i)
mix_filter.sort()
for hj in klk:
    lkl=hj
for jj in mix_filter:
    k=k+1
    if jj==lkl:
        print(k-1)
print(mix_filter[12622])