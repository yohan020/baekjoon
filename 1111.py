N = int(input())
arr = list(map(int, input().split()))

def find():
    temp = arr[0] - arr[1]
    if temp == 0:
        if arr[2] - arr[1] == 0:
            temp = 1
        else:
            return None
    temp1 = arr[1] - arr[2]
    a = temp1 // temp
    b = arr[1] - arr[0] * a
    return (a, b)


def check(A, B):
    for i in range(N - 1):
        if arr[i] * A + B != arr[i + 1]:
            return False
    return True

# 예외 처리
if len(arr) == 1:
    print('A')
    exit()

if len(arr) == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')
    exit()

result = find()

if result:
    A, B = result
    if check(A, B):
        print(arr[N - 1] * A + B)
    else:
        print('B')
else:
    print('B')
