from random import randint
m = []
for i in range(1000):
    m.append(randint(1, 10000000))
def add(a, b, c):
    if ((a + c) > b) and ((c + b) > a) and ((a + b) > c):
        return True
    else:
        return False
def add1(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
m1 = []
for i in range(len(m) - 2):
    a = m[i]
    b = m[i + 1]
    c = m[i + 2]
    m1.append(add1(a, b, c))
    if add(a, b, c) == True:
        print("a = ", a, "b = ", b, "c = ", c, "S = ", add1(a, b, c))
    else:
        print("треугольник не существует")
for i in range(len(m1)):
    if type(m1[i]) == complex:
        m1[i] = 0
print(m1)
print("Max S = ", max(m1))
