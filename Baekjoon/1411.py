import sys
n=int(sys.stdin.readline())
string=[sys.stdin.readline().strip() for _ in range(n)]
k=0 #k는 비교하고 싶은 값이고
count=0
while k!=n-1:#k의 범위는 n-1개이다 
    for i in range(k+1,n):
        dic={}#dic에서 key:비교하고 싶은 값 value: 비교하려는 값
        for j in range(len(string[k])):
            if string[k][j] in dic:#비교하고싶은 값의 문자열 하나의 인덱스가 dic에 있으면 
                if string[i][j] == dic[string[k][j]]:#그 인덱스의 value값과 비교하려는 값의 인덱스 값이 같으면
                    pass#패스
                else:
                    break
            else:
                dic[string[k][j]]=string[i][j]
        else: #break가 걸리지 않으면
            if len(set(dic.values())) == len(dic.values()):#예외) ab bb같은 경우 {a:b,b:a}가 된다.
                count+=1
    k+=1
print(count)
        


