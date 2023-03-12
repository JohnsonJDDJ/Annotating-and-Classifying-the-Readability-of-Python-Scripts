'''
백준 2589. 보물섬
https://www.acmicpc.net/problem/2589


5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

8
'''
import sys
from collections import deque
n, m = map(int, input().split())
island = [list(input()) for _ in range(n)]    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 가장 긴 거리를 찾는다.
def bfs(i, j):
    
    dq = deque([(i, j, 0)])
    distance = 0
    visit2 = [[0] * m for _ in range(n)]
    visit2[i][j] = 1
    
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nnx = x + dx[i]
            nny = y + dy[i]
            
            if 0 <= nnx < n and 0 <= nny < m and visit2[nnx][nny] == 0 and island[nnx][nny] == "L":
                # print(f'nnx: {nnx}, nny: {nny}, cnt: {cnt+1}, visit: {visit2}')
                visit2[nnx][nny] = 1
                dq.append((nnx, nny, cnt+1))
                distance = max(distance, cnt+1)
    
    return distance
                
            
            
            

for i in range(n):
    for j in range(m):
        if island[i][j] == "L":
            dq = deque([(i, j, 0)])
            visit = [[0] * m for _ in range(n)]       
            visit[i][j] = 1
            ans = [0, 0, 0]
            
            while dq:
                x, y, cnt = dq.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and island[nx][ny] == "L":
                        visit[nx][ny] = 1
                        dq.append((nx, ny, cnt+1))
                        
                        
                        if ans[0] < cnt+1:
                            ans = [cnt+1, nx, ny]
                            # print(f'nx: {nx}, ny: {ny}, cnt: {cnt+1}, visit: {visit}')
            
            answer = max(answer, bfs(ans[1], ans[2]))

print(answer)
                
                

