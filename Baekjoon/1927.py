import sys
import heapq #heapq를 사용하기 위해서 불러와야한다.
n=int(sys.stdin.readline())
array=[]# 0이 아니면 넣을 배열
for i in range(n):
    num=int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(array,num)#입력받은 값이 0이 아니면 heapq.heappush(넣을 리스트, 넣을값)
    else:
        try:
            print(heapq.heappop(array))# array리스트에서 가장 작은 값을 팝시킨다.heapq.heappop(list)
        except:# 리스트에 값이 없을때 0이면 뜨는 에러
            print(0)
