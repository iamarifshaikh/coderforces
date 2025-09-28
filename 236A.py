import sys

def solve():
    username = sys.stdin.readline().strip()

    username = set(username)

    if len(username) % 2 == 0:
        return "CHAT WITH HER!"
    else: return "IGNORE HIM!"

print(solve())