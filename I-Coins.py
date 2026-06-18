import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    p = [float(x) for x in input_data[1:]]
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  
    for i in range(n):
        head_prob = p[i]
        tail_prob = 1.0 - head_prob
        for j in range(i + 1, -1, -1):
            if j == 0:
                dp[j] = dp[j] * tail_prob
            else:
                dp[j] = (dp[j] * tail_prob) + (dp[j - 1] * head_prob)
    min_heads_needed = (n + 1) // 2
    ans = sum(dp[min_heads_needed:])
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
