import sys
c=int(sys.stdin.readline())

for i in range(c):
    kind_n=[]
    n=int(sys.stdin.readline())
    for j in range(n):
        cloth,kind=sys.stdin.readline().split()
        kind_n.append(kind)

    dic={}
    for i in kind_n:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    count=1
    for i in dic: #key값만 들고온다.
        count*=(dic[i]+1)
    print(count-1)

