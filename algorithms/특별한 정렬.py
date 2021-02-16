# 4843: 특별한 정렬

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split())) # numbers
    
    arr = [0 for _ in range(10)] # blank list (10)
    i = 0 # i : arr ith
    
    while i < 10:
        max_val = 0; min_val = 101
        for a in ai:
            if a > max_val:
                max_val = a
            if a < min_val:
                min_val = a
        arr[i] = max_val
        arr[i+1] = min_val
        
        ai.remove(max_val)
        ai.remove(min_val)

        i += 2
        
    
    print("#{}".format(test_case), end=" ")
    print(*arr)

"""
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 
큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
"""