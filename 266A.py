def solve():
    s = "RRRRR"
    n = 3
    s = list(s)
    i = 0
    count = 0
    while i < len(s)-1:
        print(i)
        while s[i] == s[i+1]:
            s.remove(s[i+1])
            count += 1
        i += 1
    print(s)
solve()