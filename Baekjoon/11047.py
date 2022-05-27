import sys
n,k=map(int,sys.stdin.readline().split())
coin=[int(sys.stdin.readline()) for _ in range(n)]
count=0
for i in reversed(coin):#list.reserve()는 list가 바뀌어 버리니 reserved(list)로 임시로 바꿔준다.
    if k>=i:
        count+=(k//i)
        k=(k%i)
    else:
        continue
print(count)