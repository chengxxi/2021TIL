# 4836: 색칠하기

from pprint import pprint

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 칠할 영역의 개수
    square = [[0 for _ in range(10)] for _ in range(10)] # 10X10
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 주어진 범위에 color 색칠
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                square[r][c] += color
        
    cnt = 0
    for x in range(10):
        for y in range(10):
            if square[x][y] == 3 : # 빨강과 파랑이 겹치면
                cnt += 1

    #pprint(square)
    #print(cnt)
    print("#{} {}".format(test_case, cnt))


"""
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
"""