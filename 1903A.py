import sys

input = sys.stdin.readline
output = sys.stdout.write

t = int(input())

answer = []

def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array)-1))

for _ in range(t):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))

    if is_sorted(array) or k > 1: answer.append("YES")
    else: answer.append("NO")

output("\n".join(answer))