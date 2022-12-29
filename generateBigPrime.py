import random
import  math

def get_n():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
    # генерируем k - количество различных простых чисел в произедении
    k = random.randint(5, 15)
    # список простых множителей:
    pi = []
    for i in range(k):
        random.shuffle(primes)
        pi.append(primes.pop(0))
    # список их степеней:
    ai = [0] * k
    n = 1
    for i in range(k):
        p = random.randint(1, 5)
        n *= pi[i] ** p
        ai[i] += p
        if (n >= 2 ** 123) and (n <= 2 ** 128):
            break
    i = 0
    while (n > 2 ** 128):
        # в произведении должно быть каждое из k чисел хотя бы в 1 степени:
        if ai[i % k] > 1:
            n //= pi[i % k]
            ai[i % k] -= 1
        i += 1
    if n < 2 ** 123:
        n = n * (2 ** random.randint(124, 128) // n)
    return n, pi
    

def fast_exp(a, w, n):
    # вернёт (a ** w) % n

    w = bin(w)[2:][::-1]
    s = 1
    c = a
    for i in range(len(w)):
        if w[i] == '1':
            s = (s * c) % n
        c = (c * c) % n
    return s
    
    
def get_prime():
    while True:
        n, pi = get_n()
        for a in range(2, math.floor(math.log(n, 2))):
            if fast_exp(a, n, n + 1) == 1:
                # print(a)
                f = True
                for p in pi:
                    if fast_exp(a, n // p, n + 1) == 1:
                        f = False
                        break
                if f:
                    return n + 1    
    
print(get_prime())



