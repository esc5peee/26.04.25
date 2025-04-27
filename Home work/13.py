from itertools import product, permutations

k=0
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
fdd='0123456789'
mix = permutations(alphabet, 3)
mixx = product(fdd, repeat=3)


for g in mix:
    d=''.join(g)
    k=k+1
    for ss in mixx:
        ff=''.join(ss)
        ff=int(ff)
        if ff&5==0 and ff//100!=0 and ff//10!=0:
            k=k+1

print(k)

