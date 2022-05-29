import sys
def decimal(num):#num=받은 숫자
    if num==1:#1은 소수가 아니기 때문에 제외
        return False
    else:
        for i in range(2,int(num**0.5)+1):#2부터 제곱근까지만 범위로 한다.
            if num%i==0:#받은 숫자와 그숫자의 제곱근 밑에까지 나눠보면서 0이면 제외
                return False    
        return True# 나눠서 0이 아니면 소수이기 때문에 True
        
n,m=map(int,sys.stdin.readline().split())
for i in range(n,m+1):#범위 n부터 m+1까지 해야한다.
    if decimal(i):#숫자 하나씩 받아서 함수에 넣어 True일때만 출력
        print(i)
