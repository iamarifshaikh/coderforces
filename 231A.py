import sys

def totalNoPrograms():
    t = int(sys.stdin.readline().strip())
    count = 0
    for _ in range(t):
        arr = list(map(int,sys.stdin.readline().split()))
        
        if arr.count(1) >= 2:
            count += 1
    
    print(count)

totalNoPrograms()