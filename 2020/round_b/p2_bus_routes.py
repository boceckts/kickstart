T = int(input())
for T_1 in range(T):

    N, D = [int(i) for i in input().split(' ')]
    X = [int(i) for i in input().split(' ')]

    last_day = D
    for i in range(N - 1, -1, -1):
        factor = int(last_day / X[i])
        if (factor * X[i]) < last_day:
            last_day = factor * X[i]

    print('Case #{}: {}'.format(T_1 + 1, last_day))
