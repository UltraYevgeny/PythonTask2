# Задача 10:
"""
coins = [int(i) for i in input('введите числа 1 или 0, через пробел \
где 1 - орел, а 0 - решка: \n').split()]
count0 = 0; count1 = 0

for i in range(len(coins)):
    if coins[i] == 0:
        count0 += 1
    if coins[i] == 1:
        count1 += 1

if count0 < count1:
    print('решек меньше: ', count0)
else:
    print('орлов меньше: ', count1)
"""


# Задача 12:
"""
import random
x = random.randint(0, 1000)
y = random.randint(0, 1000)
print(f'Петя задумал число Х={x} и число Y={y}')
s = x + y
p = x * y
print(f'Сума этих чисел: {s}, а произведение: {p}')

for i in range(s):
    s1 = s-i
    p1 = s1 * i
    if p1 == p:
        k1 = s1
        k2 = i

print(f'Катя угодала числа, это {k1} и {k2}')
"""

# Задача 14
"""
z = 1
n = int(input('Введи число N: '))
while z < n:
    print(z)
    z *= 2
"""

