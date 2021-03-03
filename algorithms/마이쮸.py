# 마이쮸

N = 20 # 전체 개수

queue = [(1,0)] # 초기화
# (0, 0) [0] : 사람 번호
# (0, 0) [1] : 직전까지 받은 개수

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0) # 0번째 index
    # 받으러 온 사람 번호와, 지난번까지 받은 개수

    last_people = num # 마지막으로 받으러 온 사람
    cnt += 1 # 저번보다 하나 더 챙겨간다

    N -= cnt # num이 cnt만큼 가져감
    new_people += 1

    queue.append((num, cnt)) # 맨 뒤로가서 다시 줄을 선다
    queue.apppend((new_people, 0)) # 새로운 사람 등장


print(last_people) # 2
