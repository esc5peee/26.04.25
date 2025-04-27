from itertools import product

k=0
klk=[('И','Н','Ф','О','Р','М')]
alphabet = 'ИНФОРМ'
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
        print(f'Номер слова ИНФОРМ:{k-1}')
print(mix_filter[3805])