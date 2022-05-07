import sys
n,m=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
start,end= 0,max(tree) # 시작점:가장 짧은 길이 1, 끝점은 나무의 가장 긴 길이
while start <= end: 
    total=0 #자른 나무의 토탈이다.
    mid=(start+end)//2 #중간점
    for i in tree: #자른 나무들을 토탈에 넣는 과정
        if i >= mid: 
            total+=i-mid
    if total<m: # 토탈이 목표값보다 작으면 중간점보다 왼쪽에 있는거니깐 끝점을 옮겨서 중간점을 왼쪽에 두게한다.
        end=mid-1
    else:# 토탈이 목표값보다 크면 중간점을 오른쪽에 두게하기위해 시작점을 옮긴다.
        start=mid+1
print(end)
#이진 탐색이다.
# 이진 탐색: 중간점에서 구하고자 하는 값이 크면 시작점을 옮기고 작으면 끝점을 옮긴다.
