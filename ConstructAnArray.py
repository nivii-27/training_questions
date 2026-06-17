t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(1, n + 1):
        odd_number = 2 * i - 1
        ans.append(odd_number)
    print(*ans)
