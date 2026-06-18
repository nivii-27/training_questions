import sys

def get_divisors(num):
    divisors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

def solve():
    N = int(sys.stdin.read().strip())
    
    if N == 2:
        print(1)
        return
        
    ans = set()
    
    for K in get_divisors(N):
        if K < 2:
            continue
        temp = N
        while temp % K == 0:
            temp //= K
        if temp % K == 1:
            ans.add(K)
            
    for K in get_divisors(N - 1):
        if K < 2:
            continue
        ans.add(K)
        
    print(len(ans))

if __name__ == '__main__':
    solve()
