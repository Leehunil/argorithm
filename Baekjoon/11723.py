import sys

m = int(sys.stdin.readline())
S = set()#set으로 중복된 숫자는 없앤다.

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:#temp의 길이가 1이면 all이랑 empty가 있다.
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:#empty이면
            S = set()#비워준다.
    
    else:
        func, x = temp[0], temp[1]#함수와 숫자로 나눈다
        x = int(x)

        if func == "add":#add이면
            S.add(x)#숫자를 더하고
        elif func == "remove":
            S.discard(x)#숫자를 버린다.
        elif func == "check":
            print(1 if x in S else 0)# s에 숫자가 있으면 1 없으면 0을 출력
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)



