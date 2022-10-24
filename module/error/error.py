def deln(number):
    a = sum([i for i in range(i, number) if number % i == 0])
    return a

m = 10000
cnt = (m)//40

ls1 = []
ls2 = []
answ = []
for i in range(1, m + 1):
    ls1.append(i)
    ls2.append(deln(i))
  

for i in range(m):
    for ii in range(i, m):
        if i + 1 == ls2[ii] and ii + 1 == ls2[i]:
            answ.append((i + 1, ls2[ii]+ii-i))

for a in answ:
    print(*a, sep=', ')