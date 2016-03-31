def count(s, m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    if n == 0:
        memo[(m, n)] = 1
        return 1
    if n < 0:
        memo[(m, n)] = 0
        return 0
    if m < 0:
        memo[(m, n)] = 0
        return 0
    val = count(s, m - 1, n) + count(s, m, n - s[m])
    memo[(m, n)] = val
    return val


line = input().split()
n = int(line[0])
m = int(line[1]) - 1
line = input().split()
s = []
for each in line:
    s.append(int(each))
memo = {}
print(count(s, m, n))
