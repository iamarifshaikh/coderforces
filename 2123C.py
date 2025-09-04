import sys

def prefixMinSuffixMax():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        array = list(map(int,sys.stdin.readline().strip()))
        prefix = [0] * len(array)
        suffix = [0] * len(array)
        
        prefix[0] = array[0]
        suffix[-1] = array[-1]

        for i in range(1,len(array)):
            prefix[i] = min(prefix[i-1],array[i])

        for j in range(len(array)-2,-1,-1):
            suffix[j] = max(suffix[j+1],array[j])
        
        ans = ""

        for i in range(len(array)):
            if array[i] == prefix[i] or array[i] == suffix[i]:
                ans += "1"
            else: ans += "0"

prefixMinSuffixMax()