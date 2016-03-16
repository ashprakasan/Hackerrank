def update_candies():
    for i in range(1, N):
        if a[i] > a[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(N - 2, 0, -1):
        if a[i] > a[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1


N = int(input())
a = []
for each in range(N):
    a.append(int(input()))
candies = [1] * N
update_candies()
total = 0
for each in candies:
    total += each
print(total)

print(candies)