def solve(k):
    print("O", end='')
    k -= 1
    row_count = 0
    colcount = 1
    while k > 0:
        print(".", end='')
        colcount += 1
        if colcount == 8:
            print()
            row_count += 1
            colcount = 0
        k -= 1
    while row_count < 8:
        print("X", end='')
        colcount += 1
        if colcount == 8:
            print()
            row_count += 1
            colcount = 0


t = int(input())
for _ in range(t):
    k = int(input())
    solve(k)