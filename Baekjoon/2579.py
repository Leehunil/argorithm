import sys
n=int(sys.stdin.readline())
stair=[0]+[int(sys.stdin.readline()) for _ in range(n)]#dp와 인덱스 맞춘다
dp=[0]*(n+1)#dp생성
if n<3:#계단의 수가 n개 이하일때는 
    for i in range(1,n+1):# 계단을 다 더해주기만 하면 된다.
        dp[i]=dp[i-1]+stair[i]
else:    
    dp[1]=stair[1]#dp[1]과 dp[2]는 생성해주고
    dp[2]=dp[1]+stair[2]
    for i in range(3,n+1):
        dp[i]=stair[i]+max(stair[i-1]+dp[i-3],dp[i-2])#목표하는 dp값을 구할때 2가지 경우가 있다.
                                                      # 1. 2번째 전의 계단에서 2칸 오른 경우랑, 2.3번째 전의 계단에서 2칸올라서 1번째 계단에 도달한 후 1번째 전의 계단에서 오른 경우  
print(dp[n])
    

