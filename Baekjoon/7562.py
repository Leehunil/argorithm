def bfs(x,y,ax,ay):
    graph[x][y]=0
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if x==ax and y==ay:# 끝나는 노드이면 while문을 종료한다.
            break
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:# 나이트가 갈 수 있는 루트의 최솟값은 노드가 0일때이다.
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1 #엄마 노드의 그래프값에 1을 더한다.
    
    return graph[ax][ay]# 끝나는 노드 반환            
import sys
from collections import deque
n=int(sys.stdin.readline())
for i in range(n):
    m=int(sys.stdin.readline())
    graph=[[0]* m for i in range(m)]
    start_x,start_y=map(int,sys.stdin.readline().split())
    finish_x,finish_y=map(int,sys.stdin.readline().split())
    dx=[-2,-1,1,2,2,1,-1,-2]
    dy=[-1,-2,-2,-1,1,2,2,1]
    print(bfs(start_x,start_y,finish_x,finish_y))

