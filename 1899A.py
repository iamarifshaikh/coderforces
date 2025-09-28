import sys

input = sys.stdin.readline
output = sys.stdout.write

t = int(input())

answer = []
for _ in range(t):
    n = int(input())

    if n % 3 != 0: answer.append("First")
    else:answer.append("Second")

output("\n".join(answer))