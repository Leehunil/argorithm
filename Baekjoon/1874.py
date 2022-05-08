n=int(input())
user=[int(input()) for _ in range(n)]
stack=[0]
sit=[]
num=1
j=0
for i in range(2*n):
    if stack[-1]== user[j]:
        j+=1
        stack.pop()
        sit.append('-')
    else:
        stack.append(num)
        num+=1
        sit.append('+')
if len(stack)==1:
    for i in sit:
        print(i)
else:
    print('NO')