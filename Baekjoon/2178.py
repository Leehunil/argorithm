import sys
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
n,m= map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))    
dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs(0,0))
#1. graph를 만들어준다.
#2. 이동할 4가지 방향 (상,하,좌,우)리스트를 만들어준다
#3. bfs함수를 만들어준다.
#4. bfs함수에는 시작점 x,y가 들어간다.
#5. deque를 이용해 queue를 만들어준다.
#6. queue에 x,y를 튜플형태로 넣어준다.
#7. while queue에 값이 있으면
#8. queue.popleft() 가장 왼쪽에 있는 값을 pop시켜준다.
#9. 미로에서 벗어난 경우에는 continue
#10. graph가 0인 경우에도 continue
#11. graph가 1인 경우에는 
#12. 그전 그래프값에 +1해서 한칸 움직인 칸에 넣어준다.
#13. 그리고 queue에 append
#14. 마지막  graph[n-1][m-1]의 값을 리턴하면 된다.

