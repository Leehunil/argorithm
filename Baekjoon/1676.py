import sys
def factorial(n):#재귀함수를 이용한 factorial
    if n==0: #재귀함수를 멈추기 위한 조건
        return 1 
    return n * factorial(n-1) 
result=factorial(int(sys.stdin.readline()))#factorial한 값
result=str(result)#뒤집기위해서 문자열로 만들고
count=0
for i in result[::-1]:
    if i=='0':
        count+=1
    else:
        break
print(count)
