import sys

from collections import deque

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = deque(sys.stdin.readline().strip())
        m = int(sys.stdin.readline().strip())
        b = sys.stdin.readline().strip()
        c = sys.stdin.readline().strip()

        for i in range(len(c)):
            if c[i] == "V":
                a.appendleft(b[i])
            else:
                a.append(b[i])

        print("".join(a))

solve()