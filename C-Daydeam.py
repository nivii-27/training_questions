import sys

def main():
    s = sys.stdin.read().strip()
    s_rev = s[::-1]
    s_rev = s_rev.replace("resare", "")  
    s_rev = s_rev.replace("esare", "")   
    s_rev = s_rev.replace("remaerd", "") 
    s_rev = s_rev.replace("maerd", "")   
    if not s_rev:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
