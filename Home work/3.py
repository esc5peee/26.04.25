from itertools import product, permutations

k=0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
fdd='0123456789'
mix = permutations(alphabet, 4)
mixx = product(fdd, repeat=2)


for g in mix:
    d=''.join(g)
    k=k+1
    for ss in mixx:
        ff=''.join(ss)
        ff=int(ff)
        if ff&7==0 and 10<= ff <= 99:
            k=k+1

print(k)

