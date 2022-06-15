import sys 
n=list(map(int,sys.stdin.readline().split()))
num=0
for i in n:
    num+=i**2
print(num%10)

