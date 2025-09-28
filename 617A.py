import sys

n = sys.stdin.readline()

print(n//5+(0 if n%5==0 else 1))