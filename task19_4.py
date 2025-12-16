#4

n = 6

for i in range(n):
    for j in range(n - i, n + 1):
        print(j, end='')
    print()
