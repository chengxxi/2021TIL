# 선형 Queue 구현하기
"""
선형큐 구현
1. 배열(index)로
2. list의 기능을 활용해서
"""

### Queue 1: array / index

#아래 함수들을 구현하세요
def isEmpty():
    # if f == r: # front와 rear가 같을 경우
    #     return True
    return f == r # True / False

def isFull():
    # if r == len(q)-1 : # rear가 가장 마지막 길이까지 가있고,
    #                 # 모든 원소가 가득 차있을 때 (?)
    #     return True
    return r == len(q) - 1 # True / False

def enQueue(item):
    global r # rear
    if isFull(): print("Queue is Full")
    else:
        r += 1 # rear를 뒤로 한 칸 옮기고
        q[r] = item

def deQueue():
    global f # front
    if isEmpty(): print("Queue is Empty")
    else:
        f += 1 # front를 뒤로 한 칸 옮기고
        # return q[f] # 반환하면서 삭제
        deq = q[f]
        q[f] = 0
        return deq


#초기 공백 큐 생성
n = 5 # size
q = [0] * n # queue
f = -1 # first
r = -1 # rear


print("default queue: {}".format(q))
enQueue(1)
enQueue(2)
enQueue(3)
print("after enqueuing: {}".format(q))
print(deQueue())
print(deQueue())
print(deQueue())
print(isEmpty())
print("after dequeuing: {}".format(q)) # 삭제가 안 되는데?
deQueue()