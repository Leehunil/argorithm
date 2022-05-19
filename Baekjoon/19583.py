import sys
s,e,q= sys.stdin.readline().split() #문자열도 비교 가능하다.
dic={}
check=[]
while True:
    try:
        time,user=sys.stdin.readline().split()
        if time<= s:
            dic[user]=time# key는 사용자, value는 시간
        elif e<=time<=q:
            if user in dic:#dic에 사용자가 있으면 check리스트에 넣어준다.
                check.append(user)
    except:#얼마만큼 학생의 채팅이 있을지 모르니 except로 break해준다.
        break
print(len(set(check)))#마지막에 겹치는 사용자는 없애고 길이를 출력한다.

    
  



    
