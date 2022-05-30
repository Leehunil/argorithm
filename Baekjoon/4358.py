import sys
result={}#dic을 만든다.
count=0 # 횟수를 저장할 변수를 생성한다.
while True:
    n=sys.stdin.readline().strip()
    
    if n!="":# 공백이 아니면
        count+=1#횟수를 하나 증가시킨다.     
        if n in result:#result 딕셔너리에 n이 있으면 value 갑 하나 증가
            result[n]+=1
        else:# 딕셔너리에 n이 없으면 
            result[n]=1 #dic에 추가
        
    else: #공백일때 break해준다.
        break
for key in sorted(result):#
    print(key,'{:.4f}'.format((result[key]/count)*100))
    #print("{:.nf}".format(number)) number의 소수점 n+1번째 자릿수에서 반올림해서
    #소수점 n번째 자릿수까지 출력함


