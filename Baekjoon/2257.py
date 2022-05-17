import sys
n=sys.stdin.readline()
dic={'H':1, 'C':12, 'O':16}
stack=[]
for i in range(len(n.strip())):
    if n[i]=='(':
        stack.append('(')
    elif n[i] in dic:
        stack.append(dic[n[i]])
    elif n[i]==')':
        num=len(stack)-1
        count=0
        while True:
            if stack[num]=='(':
                stack.pop()
                stack.append(count)
                break
            else:
                count+=stack[num]
                stack.pop()
                num-=1
    else:
        stack[-1]=stack[-1]*int(n[i])
print(sum(stack))
        

    