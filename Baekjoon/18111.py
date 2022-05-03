import sys
N,M,B=map(int,sys.stdin.readline().split())
ground=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
height=0
mini=sys.maxsize
for i in range(257):
    minus=0
    plus=0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                minus+=(i-ground[j][k])
                
            else:
                plus+=(ground[j][k]-i)
    inventory=plus+B
    if inventory<minus :
        continue
    time=2*plus+minus
    if time <= mini:
        mini=time
        height=i
print(mini,height)