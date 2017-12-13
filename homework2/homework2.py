# example 1
l = [1, 5, 6, 2, 9, 3]
l.sort(key=lambda x: x//5 == 0)
print(l)

# example 2
d = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6'}

for key, value in d.items():
    print(key, value)

# example 3
t = (1.2, 3.2, 4.8, 5.3, 7.5, 4.4, 6.1, 5.5, 7.9, 8.6)
l = list(t)
l.sort()
print(l[0], l[-1])

# example 3.1
n = t[0]
m = t[0]
for i in t:
    if i > n:
        n = i
    elif i < m:
        m = i
print(m, n)

# example 4

l = ['Earth', 'Russia', 'Moscow']
s = '->'.join(l)
print(s)

# example 5

s = '/bin:/usr/bin:/usr/local/bin'
l = s.split(':')
print(l)

# example 6


l1 = []
l2 = []
for i in range(1, 101):
    if i % 7 == 0:
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)

# example 7
print('---------------')
l = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

n = 0
for row in l:
    for i in row:
        print(i, end=' ')
    print('')

while n != len(l[0]):
    for row in l:
        print(row[n])
    n += 1

# example 8

l = [1, 'yes', (0, 1), None, True, [1,]]

for ind in enumerate(l):
    print(ind)

# example 9

l = [1, 'qwert', 'to-delete', (1,), 45, 'to-delete']

for i in l:
    if i == 'to-delete':
        l.remove(i)
print(l)

# example 10

for i in range(1, 11)[::-1]:
    print(i)