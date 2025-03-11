from collections import deque

def isDead(x, y):
    if x <= 0 or N < x or y <= 0 or N < y:
        return True
    return False

N = int(input())
K = int(input())
apple = set()
for _ in range(K):
    a, b = map(int, input().split())
    apple.add((b, a))
L = int(input())
rotate = {}
for _ in range(L):
    a, b = map(str, input().split())
    rotate[int(a)] = b

time = 0

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

body = deque([(1,1)])
body_set = set(body)
head = (1,1)
while True:
    temp_x = head[0] + dir[d][1]
    temp_y = head[1] + dir[d][0]
    time += 1

    if isDead(temp_x, temp_y) or (temp_x, temp_y) in body_set: break #벽 또는 몸통에 부딪힌 여부

    if (temp_x, temp_y) in apple:
        apple.remove((temp_x, temp_y))
    else:
        tail = body.popleft()
        body_set.remove(tail)
    body.append((temp_x, temp_y))
    body_set.add((temp_x, temp_y))
    head = (temp_x, temp_y)

    if time in rotate:
        if rotate[time] == 'L':
            d = (d + 3) % 4
        if rotate[time] == 'D':
            d = (d + 1) % 4
    
print(time)