import sys
n=int(sys.stdin.readline())
time=[]#시간 list를 만들어준다.
for i in range(n):
    start,finish=map(int,sys.stdin.readline().split())
    time.append([start,finish])#시간 리스트에 [시작시간,끝나는 시간]를 삽입
time=sorted(time,key=lambda x:x[0])#sorted(정렬할 리스트, key=lambda x:x[0]) 이중 리스트에서 리스트 몇번째로 정렬을 할것인지 정할 수 있다.
time=sorted(time,key=lambda x:x[1])#리스트안에 리스트의 2번째로 튜플상태로 정렬을 한다
#에) time=[[5,0],[4,3],[0,1],[2,5]]
#   time=sorted(time,key=lambda x:x[0]) time=[[0,1],[2,5],[4,3],[5,0]]
#   time=sorted(time,key=lambda x:x[1]) time=[[5,0],[0,1],[4,3],[2,5]]
last=0 #last는 회의가 끝나는 시간이고, 처음은 0이라고 한다.
count=0
for i,j in time:#time list 안에 [start,finish]를 i,j로 나눠서 for문을 돌린다.
    if i >=last:#start가 last보다 크거나 같으면 
        count+=1#count 하나 올리고
        last=j#last를 j 로 바꾸어준다.
print(count)

