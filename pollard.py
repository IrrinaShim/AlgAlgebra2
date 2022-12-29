import random
import  math

def factorial(a):
    s = 1
    for i in range(2, a + 1):
        s = s * i;
    return s

def NOD(a, b):
    if (a == 0 or b == 0):
        return (a + b)
    elif (a > b):
        return NOD(a - b, b)
    else:
        return NOD(a, b - a)
    
def get_bk(a, k, n):
    # вернёт (a ** w) % n
#    k = factorial(k)
    k = bin(k)[2:][::-1]
    s = 1
    c = a
    for i in range(len(k)):
        if k[i] == '1':
            s = (s * c) % n
        c = (c * c) % n
    s = s - 1
    if (s < 0):
        s = s + n
    return s
    
n = int(input())
N = int(input())

flag = False;
a = 2;

while ((a < n) and not flag):
    for k in range(1, N):
        b_k = get_bk(a, k, n)
        p = NOD(b_k, n)
        if (p != 1 and p != n):
            flag = True
            p = NOD(b_k, n)
        if flag:
            break
    a = a + 1

if flag:
    print(p)
else:
    print(1)
