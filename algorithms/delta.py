# 연습문제 1
from pprint import pprint

# 2차원 배열 생성
arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
# [list(map(int, input().split())) for _ in range(5)]
answer = [[0 for _ in range(5)] for _ in range(5)]

# 각 요소의 결과를 구해 새로운 배열에 넣기
dr = [-1, 0, 1, 0]; dc = [0, 1, 0, -1] # 상하좌우

for r in range(5):
    for c in range(5):
        ans = 0
        for k in range(4): # 4방향 탐색
        # 새로운 좌표를 탐색
            nr = r + dr[k]
            nc = c + dc[k]
            # 새롭게 탐색할 위치가 배열의 범위를 벗어나면 스킵
            if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr):
            #if 0 <= nr < 5 and 0 <= nc < 5:
                continue # 배열의 범위 밖에 접근하지 않도록

            # print(arr[nr][nc], end=" ") : 인접한 수들 출력
            ans += abs(arr[nr][nc] - arr[r][c])
        #answer[r][c] = ans

        answer[r][c] = ans # arr[nr][nc]


pprint(answer)



"""
input:
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4
"""

"""
output
11 10 8 4 7
15 11 17 9 12
9 11 10 10 12
9 21 11 10 7
5 10 11 16 8
"""
