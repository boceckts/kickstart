T = int(input())
for T_1 in range(T):

    N = int(input())
    H = [int(i) for i in input().split(' ')]

    peaks = 0
    for H_i in range(N):
        if 0 < H_i < N - 1:
            if H[H_i] > H[H_i - 1] and H[H_i] > H[H_i + 1]:
                peaks += 1

    print('Case #{}: {}'.format(T_1 + 1, peaks))
