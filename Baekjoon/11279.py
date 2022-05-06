import sys
import heapq
n=int(sys.stdin.readline())
heap=[]
for i in range(n):
    num=int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(heap,(-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
#heapq
#완전이진트리로 만들어주는 함수로
#가장 작은값이 root 노드이고, 그밑으로 트리 형태로 노드를 생성한다.
# push
# heapq.heappush(넣을 list, 넣을 값)
# 새로운 값이 들어오면 부모노드와 비교하여 더작은 값이면 스위치한다.
# pop
# heapq.pop(list)
# 팝하면 제일 작은값 즉 root 노드가 pop이되고, 
# 팝이 되는 과정은 제일 밑에있는 노드와 root노드를 스위치하여 pop시키고 root노드는 자식 노드와 비교하여 스위치하여 올바른 자리에 둔다.
# 최대heap은 값을 다 -로 바꾸어서 사용한다. 