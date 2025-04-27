from itertools import product


k=0
alphabet = '012'
mix = product(alphabet, repeat=5)
gh='1'

mix_filter = []

for i in mix:
    pp=''.join(i)
    if pp.startswith(gh):
        mix_filter.append(pp)
for s in mix_filter:
    l=''.join(mix_filter)
    s=int(s)
    if s%3==0:
        k=k+1
print(k)