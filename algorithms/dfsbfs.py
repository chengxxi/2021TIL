# DFS & BFS

def dfs(i):
    print(i, end=" ")
    visited[i] = 1 # 방문표시

    for j in range(1, n+1):
        if adj[i][j] == 1 and visited[j] == 0:
            dfs(j)


def bfs(i):
    visited = [0] * (n+1)
    q = [] # queue
    q.append(i)
    visited[i] = 1

    while q:
        cur = q.pop(0) # 맨 앞
        print(cur, end=" ")

        for j in range(1, n+1):
            if adj[cur][j] == 1 and visited[j] == 0:
                q.append(j)
                visited[j] = 1


n, m, v = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    n1, n2 = edge[i][0], edge[i][1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1


# print("dfs result:", end=" ")
dfs(v)
# print()
# print("bfs result:", end=" ")
bfs(v)


'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과(재귀)를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

입력1
4 5 1
1 2
1 3
1 4
2 4
3 4

출력1
1 2 4 3
1 2 3 4

입력2
5 5 3
5 4
5 2
1 2
3 4
3 1

출력2
3 1 2 5 4
3 1 4 2 5

입력1
1000 1 1000
999 1000

출력2
1000 999
1000 999
'''