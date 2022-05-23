import sys
from collections import deque #bfs를 풀기위해 deque를 가져온다.
def dfs(graph,v,visited):
    visited[v]=True #방문한 숫자는 False에서 True로 바꿔준다.
    print(v,end=" ")#출력
    for i in sorted(graph[v]):#숫자와 관련된 graph로 가서 for문 돌린다. 
        if not visited[i]:#만약 visited[i]가 False이면 재귀함수 수행
            dfs(graph,i,visited)
def bfs(graph,start,visited):
    queue=deque([start])#queue라는 deque list를 만든다
    visited[start]=True 
    while queue: #queue에 값이 있으면 반복문을 수행한다
        v=queue.popleft() #list.popleft() 큐의 맨 앞의 수를 pop시킨고 V변수에 넣는다
        print(v,end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:   
                queue.append(i)
                visited[i]=True
n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]#빈 graph를 만들어준다.
for i in range(m):#graph에 값을 넣어준다.
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
dfs(graph,v,visited)
print()
visited=[False]*(n+1)
bfs(graph,v,visited)