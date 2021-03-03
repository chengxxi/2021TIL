# 연습문제3: BFS 구현해서 경로 찾기

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 입력 확인
# 그래프의 표현: 1) 인접행렬 / 인접리스트
# 탐색기법 선정: BFS
# BFS 구현하기
# 방문배열 생성
# 시작 정점을 기준으로 BFS 탐색

'''
큐 생성
시작 정점을 큐에 삽입
시작 정점을 방문했다고 표시

큐가 빌 때까지
    큐에서 정점 cur를 꺼내옴
    정점 cur에 인접한 정점 v를 큐에 넣음
    v를 방문했다고 표시
'''

def bfs(n): # n: 시작정점
    visited = [0] * (V+1) # 정점 개수만큼 방문배열 생성
                          # 0으로 초기화, 방문하면 1로 표시
    q = [] # list queue: 큐 생성
    q.append(n) # 시작 정점 n을 삽입
    visited[n] = 1 # 시작 정점 방문했다고 표시

    while q: # 큐가 비어있지 않은 동안
        cur = q.pop(0) # 큐에서 가장 앞에 있는 원소 꺼내옴
        print(cur, end=" ") # 현재 정점 출력

        for v in range(1, V+1):
            # 정점 cur에 인접하고, 아직 방문하지 않은 v면
            if adj[cur][v] == 1 and visited[v] == 0:
                q.append(v) # 인접 정점을 큐에 넣음
                visited[v] = 1 # 큐에 삽입하면서, 방문표시




V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0 for _ in range(V+1)] for _ in range(V+1)] # 정점크기 * 정점크기 행렬
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1


# 시작정점을 기준으로 BFS 탐색
bfs(1)
bfs(6)
