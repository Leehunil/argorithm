import sys
n=int(sys.stdin.readline())
num=[0,1]
for i in range(n):
    num.append((num[i]+num[i+1])%10007)
print(num[n+1])
