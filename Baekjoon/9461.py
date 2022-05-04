
import sys
t=int(sys.stdin.readline())
user=[int(sys.stdin.readline())for _ in range(t)]
dp=[1,1,1]
for i in range(3,100):
    dp.append(dp[i-3]+dp[i-2])
for i in user:
    print(dp[i-1])