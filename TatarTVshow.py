t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    remainder_counts = {}
    
    for i in range(n):
        if s[i] == '1':
            rem = i % k  
            if rem in remainder_counts:
                remainder_counts[rem] += 1
            else:
                remainder_counts[rem] = 1
    possible = True
    
    for count in remainder_counts.values():
        if count % 2 != 0:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")
