def stock_max(A, n):
    max = A[n - 1]
    profit = 0
    spent = 0
    num_stocks = 0
    for i in range(n - 2, -1, -1):
        if A[i] < max:
            num_stocks += 1
            spent += A[i]
        if A[i] > max:
            earnt = max * num_stocks
            profit += (earnt - spent)
            num_stocks = 0
            max = A[i]
            spent =0
    earnt = max * num_stocks
    profit += (earnt - spent)
    return profit

t = int(input())
for count in range(t):
    n = int(input())
    A = []
    line = input().split()
    for each in line:
        A.append(int(each))
    print(stock_max(A, n))
