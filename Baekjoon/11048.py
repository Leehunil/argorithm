import sys
n,m=map(int,sys.stdin.readline().split())
dp=(n+1)*[[0]*(m+1)]#dp하나를 만든다.
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+graph[i-1][j-1]#전에 것과 위에 것 대각선 전 것 확인해서 max값이랑 현재 그래프 값을 더한다.
print(dp[n][m])#dp마지막을 출력한다.