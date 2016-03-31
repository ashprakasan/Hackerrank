def f(n):
    if n in memo:
        return memo[n]
    else:
        val = f(n - 1) * f(n - 1) + f(n - 2)
        memo[n] = val
        return val


line = input().split()
memo = {}
memo[1] = int(line[0])
memo[2] = int(line[1])
n = int(line[2])
print(f(n))
