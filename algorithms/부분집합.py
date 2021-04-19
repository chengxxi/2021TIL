# 연습문제2: 부분집합

### 백트래킹 (210419 수업내용) ###
# def backtracking(arr, idx):
#     global ans
#
#     # pruning
#     if sum(arr) > 10 or idx >= len(arr):
#         return
#     if sum(arr) == 10:
#         ans.append(arr)
#         return
#
#     ans.append(arr[idx])
#     backtracking(arr, idx+1)
#     ans.pop(-1) # arr[idx]
#     backtracking(arr, idx+1)
#
# 외않되

def powerset(arr, idx, total): # array, index, total
    global subset

    if idx == len(arr):
        if total == 10:
            print(subset)
        return

    if total > 10: return # pruning

    powerset(arr, idx+1, total)
    subset.append(arr[idx])
    powerset(arr, idx+1, total + arr[idx])
    subset.pop()



data = [i for i in range(1, 11)]
subset = []
powerset(data, 0, 0)




### 비트 연산 활용 (210216 참고) ###

data = [i for i in range(1, 6)]
length = len(data)
ans = []

for i in range(1<<length):
    anslist = []
    for j in range(length):
        if i & (1<<j):
            anslist.append(data[j])

    if sum(anslist) == 10:
        ans.append(anslist)
    # print(anslist)
    # print()


for a in ans:
    print(a)


'''
{1, 2, ... , 10}의 Powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
'''