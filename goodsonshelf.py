import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    
    output = []
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        # Step 1: Identify all contiguous blocks
        # Each block stores: (value, start_index, end_index)
        blocks = []
        block_freq = {}
        unique_vals = set()
        
        i = 0
        while i < n:
            j = i
            while j < n and a[j] == a[i]:
                j += 1
            
            val = a[i]
            start_idx = i
            end_idx = j - 1
            
            blocks.append((val, start_idx, end_idx))
            block_freq[val] = block_freq.get(val, 0) + 1
            unique_vals.add(val)
            
            i = j
            
        C = len(blocks)
        U = len(unique_vals)
        if C == U:
            output.append("YES")
            continue
        if C - U > 4:
            output.append("NO")
            continue
        candidates = {0, n - 1}
        
        for val, start, end in blocks:
            if block_freq[val] > 1:
                # Endpoints of scattered blocks
                candidates.add(start)
                candidates.add(end)
                
                # Immediate neighbors of scattered blocks
                if start > 0:
                    candidates.add(start - 1)
                if end < n - 1:
                    candidates.add(end + 1)
                    
        candidates_list = sorted(list(candidates))
        num_candidates = len(candidates_list)
        possible = False
        for idx_i in range(num_candidates):
            for idx_j in range(idx_i + 1, num_candidates):
                i_pos = candidates_list[idx_i]
                j_pos = candidates_list[idx_j]
                a[i_pos], a[j_pos] = a[j_pos], a[i_pos]
                current_blocks = 1
                for k in range(1, n):
                    if a[k] != a[k - 1]:
                        current_blocks += 1
                        
                if current_blocks == U:
                    possible = True
                    a[i_pos], a[j_pos] = a[j_pos], a[i_pos]
                    break
                a[i_pos], a[j_pos] = a[j_pos], a[i_pos]
                
            if possible:
                break
                
        if possible:
            output.append("YES")
        else:
            output.append("NO")
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
