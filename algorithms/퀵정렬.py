# 연습문제1: 퀵 정렬

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, l, r):
    p = arr[l] # pivot value
    i = l; j = r
    while i <= j:
        # 왼쪽에서 오른쪽으로 이동하며 pivot보다 큰 값 찾기
        if arr[i] <= p:
            i += 1
        # 오른쪽에서 왼쪽으로 이동하며 pivot보다 작은값 찾기
        if arr[j] >= p:
            j -= 1
        # pivot보다 큰 값과 pivot보다 작은 값 위치 변경
        if i < j:
            swap(arr, i, j)

    # 피봇과 최솟값 위치 변경
    swap(arr, l, j)

    return j


def quicksort(arr, l, r): # array, left, right
    if l >= r: return
    if l < r:
        pt = partition(arr, l, r)
        quicksort(arr, l, pt-1)
        quicksort(arr, pt+1, r)




for _ in range(1, int(input())+1):
    # print('#{}'.format(tc))
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr)-1)
    print(arr)



'''
배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.
'''