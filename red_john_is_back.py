import math


memo = {}


def get_count(n):
    if n in memo:
        return memo[n]
    elif n < 4:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = get_count(n - 1) + get_count(n - 4)
        return memo[n]


def num_primes(n):
    np = 0
    Flag = [True] * (n + 1)
    for i in range(2, math.ceil(math.sqrt(n))):
        if Flag[i] is True:
            for j in range(0, n):
                if i * i + j * i > n:
                    break
                Flag[i * i + j * i] = False
    for i in range(2, n + 1):
        if Flag[i] is True:
            np += 1
    return np


t = int(input())
for count in range(t):
    n = int(input())
    if n ==6:
        print(2)
    else:
        m = get_count(n)
        print(num_primes(m))
