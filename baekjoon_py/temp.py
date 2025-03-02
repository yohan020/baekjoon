def clamp_to_edge():
    temp = []
    # 기본 타일 행 확장
    for i in range(U):
        temp.append(tile[i] + tile[i][-1] * (M - V))

    # 마지막 행을 확장해서 추가
    last_row = tile[-1] + tile[-1][-1] * (M - V)
    for _ in range(N - U):
        temp.append(last_row)

    print("\n".join(temp[:N]))


def repeat():
    temp = []
    x = (M + V - 1) // V  # M을 V로 나눈 후 올림 처리
    y = (N + U - 1) // U  # N을 U로 나눈 후 올림 처리

    for i in range(U):
        temp.append((tile[i] * x)[:M])  # 가로 반복 후 잘라내기

    result = []
    for _ in range(y):
        result.extend(temp)

    print("\n".join(result[:N]))  # 세로 크기 맞춰서 출력


def mirrored_repeat():
    temp = [""] * U
    x = (M + V - 1) // V
    y = (N + U - 1) // U

    # 가로 반복 (좌우 반전)
    for i in range(U):
        row = ""
        for j in range(x):
            row += tile[i][::-1] if j % 2 else tile[i]
        temp[i] = row[:M]

    # 세로 반복 (상하 반전)
    result = []
    for j in range(y):
        result.extend(temp[::-1] if j % 2 else temp)

    print("\n".join(result[:N]))


# 입력 처리
N, M = map(int, input().split())  # 출력 크기
U, V = map(int, input().split())  # 타일 크기
tile = [input().strip() for _ in range(U)]  # 타일 패턴 입력
style = input().strip()  # 스타일 입력

# 스타일별 함수 호출
if style == "clamp-to-edge":
    clamp_to_edge()
elif style == "repeat":
    repeat()
elif style == "mirrored-repeat":
    mirrored_repeat()
