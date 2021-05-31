from random import randint

nq = int(input("Nombre de questions ? "))
mp = {}
for i in range(50000):
    q = randint(1, nq)
    if q not in mp:
        mp[q] = 0
    mp[q] += 1

print(sorted(mp.items(), key=lambda t: t[1], reverse=True)[:10])