import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def antonAndDanik(s):
    anton = s.count("A")
    danik = s.count("D")

    if anton > danik: return "Anton"
    elif anton < danik: return "Danik"
    else: return "Friendship"

print(antonAndDanik(s))