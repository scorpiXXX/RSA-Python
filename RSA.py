import secrets
import math
import random

keySize = 2048
#
# p = secrets.randbits(keySize)
# q = secrets.randbits(keySize)
# n = p * q
# f = (p - 1) * (q - 1)

def isStupidPrime(number):
    if number & 1 == 0: return False
    for nnn in range(3,1000,2):
        if number % nnn == 0: return False
    return True

def sanyaPrime():
    while True:
        ran = secrets.randbits(keySize)
        if isStupidPrime(ran) and fermaTest(ran) and millerRabin(ran):
            return ran
def millerRabin(n):
    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1
    k = 10
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, t, n)
        if x==1 or x == n-1:
            continue
        loopOut = False
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n -1:
                loopOut = True
                break
        if loopOut: continue
    return True
def fermaTest(ran):
    for i in range(0, 100, 1):
        a = (secrets.randbelow((1 << 15)-1) % (ran - 2)) + 2
        if math.gcd(a, ran) != 1:
            return False
        if pow(a, ran-1, ran) != 1:
            return False
    return True


print(sanyaPrime())
# def IsPrime(number0):
#    d = 2
#    while d * d <= number0 and number0 % d != 0:
#        d += 1
#    return d * d > number0
# number = f
# i=0
# a = 18
# b = 30
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(a + b)

# print("Число р = ", p)
# print("Число q = ", q)
# print("Число n = ", n)
# print("Число f = ", f)
# Тест ферма
# алгоритм миллера-рабина
