import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
s=sys.stdin.readline()
answer,count,i=0,0,0#count는 IOI가 반복되는 횟수이다.
while i<(m-1):#i가 m-2까지 while문을 돈다.
    if s[i:i+3]=='IOI':#s인덱스 가 'IOI'이면
        count+=1#횟수한개 올린다.
        i+=2#i 2개 올린다
        if count==n:# IOI의 횟수랑 O의 갯수와 같으면
            answer+=1# 정답 한개 올리고
            count-=1 #IOI횟수 하나를 뺀다.
    else: 
        i+=1
        count=0 #count는 0으로 만들어야 한다.
print(answer)