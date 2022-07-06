import sys
n=int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))
answer=[]
count=0
for i in sorted(p):
    count+=i
    answer.append(count)
print(sum(answer))