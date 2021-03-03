# 순열 / 수업

def perm(k): # k: 선택한 원소가 들어갈 자리 (sel에 원소를 넣은 횟수) / 몇 번째 자리에 넣을 것인가?
    if k == N: # 원소 선택이 끝나면,
        print(sel) # 출력하고
        return # 끝냄

    for i in range(N): # 가지고 있는 원소를 다 살펴본다
        if visited[i] == 0: # 아직 선택한 게 아니면
            sel[k] = arr[i] # sel의 k번째에 arr[i]가 위치하도록 한다
            visited[i] = 1 # 선택되었다고 표시
            perm(k+1) # 다음 숫자
            visited[i] = 0 # 다음을 위해 방문배열 초기화
            # visited 없으면 중복순열


arr = [1, 2, 3] # 순열을 만들기 위한 원소
N = len(arr) # 순열의 길이
sel = [0] * N # 만들어진 순열 저장
visited = [0] * N # 선택여부 저장하기 위한 배열
# visited 없으면 중복순열 생성됨

perm(0)

