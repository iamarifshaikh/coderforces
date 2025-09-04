import sys

def solve():
    # t = int(sys.stdin.readline().strip())

    # for _ in range(t):
        # n = int(sys.stdin.readline().strip())
        # arr = list(map(int,sys.stdin.readline().strip()))
        arr = [30, 10, 12, 10, 10, 9,    18]
        z = 1
        for i in range(1,len(arr)):
            z = arr[i-1] / arr[i] * z 
        
        if z == 1:
            print("YES")
        else:
            print("NO")

solve()