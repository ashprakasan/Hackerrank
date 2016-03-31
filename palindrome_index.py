import math


def check_pal(a):
    l = len(a)
    m = (l - 1) / 2
    i = 0
    j = l - 1
    while i < m and j > m:
        if a[i] == a[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


t = int(input())
for each in range(t):
    s = input()
    l = len(s)
    mid = (l - 1) / 2
    i = 0
    j = l - 1
    f = 0
    while i < mid and j > mid:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            print("first check at ", i, j, s[i:j + 1])
            if check_pal(s[i:j]):
                print(j)
                f = 1
                break
            else:
                print(i)
                f = 1
                break
    if f == 0:
        print("-1")
