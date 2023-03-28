n = 7
for i in range(1, 10):
    res = i * n
    print(n, "X", i, "=", res)

name = " sat ish "
rem_space = name.replace(" ", "")
print(rem_space)

n = 10
summ = 0
for i in range(1, n + 1):
    summ = summ + i
    print(summ)

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(A0)

A1 = range(10)
print(A1)

A2 = sorted([i for i in A1 if i in A0])
print(A2)

A3 = sorted([A0[s] for s in A0])
print(A3)

A4 = [i for i in A1 if i in A3]
print(A4)

A5 = {i: i * i for i in A1}
print(A5)

A6 = [[i, i * i] for i in A1]
print(A6)

names1 = ['Amir', 'Bear', 'Carlton', 'Daman']
# print(names1[:])
names2 = names1
names3 = names1[:]
names2[0] = "Alice"
names3[1] = "Bob"
print(names1)
print(names2)
print(names3)
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)
