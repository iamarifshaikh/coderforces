import sys

def solve():
    k,n,w = map(int,sys.stdin.readline().split())

    sum = w * (w + 1) / 2
    if (k * sum - n) < 1:
        print("0")
    else:
        print(int(k * sum - n))

l = [1,2,3]
print(l)
print(*l)