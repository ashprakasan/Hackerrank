import math


def get_mean(arr, l):
    sum = 0
    for num in arr:
        sum += num
    return sum / l


def get_med(arr, l):
    arr = sorted(arr)
    mid = int(math.floor(l - 1) / 2)
    if l % 2 == 1:
        return arr[mid]
    return (arr[mid] + arr[mid + 1]) / 2


def get_mode(arr, l):
    arr = sorted(arr)
    max_rep = 0
    count = 0
    mode = arr[0]
    for i in range(1, l):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            if count > max_rep:
                max_rep = count
                mode = arr[i - 1]
            count = 0
    return mode


def get_std_dev(arr, l, m):
    var_sum = 0
    for num in arr:
        var_sum += math.pow((num - m), 2)
    var = var_sum / l
    return math.sqrt(var)


n = int(input())
a = []
line = input().split()
for each in line:
    a.append(int(each))
mean = get_mean(a, n)
print(round(mean, 1))
median = get_med(a, n)
print(round(median, 1))
mode = get_mode(a, n)
print(mode)
std_dev = get_std_dev(a, n, mean)
print(round(std_dev, 1))
