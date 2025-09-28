import sys

def translation(t,s):
    if s == t[::-1]: 
        print("YES")
    else: 
        print("NO")

if __name__ == "__main__":
    t = str(sys.stdin.readline().strip())
    s = str(sys.stdin.readline().strip())

    if len(s) != len(t):
        print("NO")
    else:
        translation(t,s)