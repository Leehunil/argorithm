import sys
N=int(sys.stdin.readline())
member=[]
for i in range(N):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(member[i][0],member[i][1])