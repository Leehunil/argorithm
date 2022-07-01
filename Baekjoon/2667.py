from collections import deque
def bfs(x,y):
    queue=deque()# 먼저 deque를 만들고
    queue.append((x,y)) # 들어온 x,y를 튜플 형태로 넣어준다.
    graph[x][y]=0 #그리고 graph[x][y]는 0으로 만들어서 방문표시를 한다.
    count=1# 연결된 노드 수를 센다.
    while queue:# queue에 값이 있을때까지 수행한다.
        x,y=queue.popleft()# queue의 가장 왼쪽의 값을 꺼낸다.
        for i in range(4):#상하좌우를 확인한다.
            nx=x +dx[i]
            ny=y+dy[i]
            if nx<0 or ny>=n or nx>=n or ny<0: # 해당 노드의 상하좌우가 그래프를 넘어가게되면 continue
                continue
            if graph[nx][ny]==0:#해당 노드의 상하좌우가 0일때도 continue
                continue
            if graph[nx][ny]==1:#해당 노드의 상하좌우가 1일떄
                queue.append((nx,ny)) #queue에 넣어주고
                graph[nx][ny]=0 #그 노드를 방문 표시해준다.
                count+=1
    return count 
import sys
n=int(sys.stdin.readline()) 
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
#좌우상하로 움직일 수 있게 dx,dy를 만들어둔다.
dx=[-1,1,0,0] 
dy=[0,0,-1,1]
answer=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:#그래프가 1일때만 
            answer.append(bfs(i,j))
print(len(answer))
for i in sorted(answer):
    print(i)