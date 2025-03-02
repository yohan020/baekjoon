n = int(input())


for _ in range(n):
    n1, n2 = map(int, input().split())
    n1_str = ""
    n2_str = ""
    result1 = n1 * n2
    result2 = ""
    if len(str(n1)) > len(str(n2)):
        n2_str += '1' * (len(str(n1)) - len(str(n2)))
    else:
        n1_str += '1' * (len(str(n2)) - len(str(n1)))
    n1_str += str(n1)
    n2_str += str(n2)
    for i in range(len(n1_str)):
        result2 += str(int(n1_str[i]) * int(n2_str[i]))
    print(1 if result1 == int(result2) else 0)
