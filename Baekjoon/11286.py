import sys
import heapq
n=int(sys.stdin.readline())
array=[]
for i in range(n):
    num=int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(array,(abs(num),num))#절대값과 그냥 값을 튜플 형태로 array에 넣는다
#그러면 튜플 0번으로만 비교한다.
    else:
        try:
            print(heapq.heappop(array)[1])#튜플 1번 인덱스 즉 그냥 값을 pop
        except:
            print(0)
            


