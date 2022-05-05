import sys
k=int(sys.stdin.readline())
num=[int(sys.stdin.readline()) for _ in range(k)]
stack=[]
for i in num:
    if i==0:
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))

