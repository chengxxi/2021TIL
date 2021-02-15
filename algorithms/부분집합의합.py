# 부분집합의 합

arr = list(map(int, input().split()))
n = len(arr)
result = False

# 부분합 구하기
for i in range(1<<n):
    anslist = []
    for j in range(n):
        if i & (1<<j):
            anslist.append(arr[j])
            #print(arr[j], end=", ")
    #print(anslist)
    #print()
    
if sum(anslist) == 0:
    result = True
    

print(result)


"""
유한 개의 정수로 이루어진 집합의 부분집합 중, 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지
"""
