T = int(input())
for T_1 in range(T):
    P = input()

    decode = P
    for i in range(P.count('(')):
        start = decode.rfind('(')
        end = decode.find(')', start)
        n = int(decode[start - 1])

        decode_tmp = decode[:start - 1]

        for _ in range(n):
            decode_tmp += decode[start + 1:end]

        decode_tmp += decode[end + 1:]
        decode = decode_tmp

    x, y = 1, 1
    north = decode.count('N')
    y = y - north % 10 ** 9
    east = decode.count('E')
    x = x + east % 10 ** 9
    south = decode.count('S')
    y = y + south % 10 ** 9
    west = decode.count('W')
    x = x - west % 10 ** 9

    if x <= 0:
        x += 10 ** 9
    if y <= 0:
        y += 10 ** 9

    print('Case #{}: {} {}'.format(T_1 + 1, x, y))
