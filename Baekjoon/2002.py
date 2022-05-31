import sys
n=int(sys.stdin.readline())
enter=[sys.stdin.readline().strip() for _ in range(n)]# 들어간 차량 리스트
exit=[sys.stdin.readline().strip() for _ in range(n)]# 나온 차량 리스트
count=0 #추월한 차량 수
for i in range(n):
    if enter[i]!=exit[i]:# for문으로 들어온차량과 나간 차량을 비교해서 다르면
        del enter[enter.index(exit[i])]#enter리스트에서 추월한 차량 인덱스를 찾아서 삭제 시킨후에
        enter.insert(i,exit[i])#현재 인덱스에 넣어준다.
        count+=1 
print(count)