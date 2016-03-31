line = input().split()
n = int(line[0])
m = int(line[1])
K = int(line[2])

a = [[] for each in range(n)]
i = 0
x = 0
y = 0

for b in range(n):
    line = list(input().rstrip())
    for j in range(len(line)):
        a[b].append(line[j])
        if line[j] == '*':
            y = j
            x = i
    i += 1

INF = 999999999
f = [[[INF] * (m) for each in range(n)] for each in range(K + 1)]
ans = INF
for k in range(K + 1):
    for i in range(n):
        for j in range(m):
            if k == 0:
                if i == 0 and j == 0:
                    f[k][i][j] = 0
                else:
                    f[k][i][j] = INF
            else:
                res = INF
                if i > 0:
                    if a[i - 1][j] == 'D':
                        res = min(res, f[k - 1][i - 1][j])
                    else:
                        res = min(res, (f[k - 1][i - 1][j] + 1))
                if i < (n - 1):
                    if a[i + 1][j] == 'U':
                        res = min(res, f[k - 1][i + 1][j])
                    else:
                        res = min(res, f[k - 1][i + 1][j] + 1)
                if j > 0:
                    if a[i][j - 1] == 'R':
                        res = min(res, f[k - 1][i][j - 1])
                    else:
                        res = min(res, f[k - 1][i][j - 1] + 1)
                if j < (m - 1):
                    try:
                        if a[i][j + 1] == 'L':
                            res = min(res, f[k - 1][i][j + 1])
                        else:
                            res = min(res, f[k - 1][i][j + 1] + 1)
                    except IndexError:
                        print("Values of i,j,k and n are ", i, j, k, n)
                f[k][i][j] = min(res, f[k - 1][i][j])

ans = f[K][x][y]
if ans == INF:
    print("-1")
else:
    print(ans)
