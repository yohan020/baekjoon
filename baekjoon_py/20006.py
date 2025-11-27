import sys

input = sys.stdin.readline

def main():
    p, m = map(int, input().split())
    room = [[]]
    for _ in range(p):
        level, player = map(str, input().split())
        for r in room:
            if len(r) == 0:
                r.append((int(level), player))
                break
            elif r[0][0] - 10 <= int(level) <= r[0][0] + 10 and len(r) < m:
                r.append((int(level), player))
                break
            elif r == room[-1]:
                room.append([(int(level), player)])
                break
    for r in room:
        r.sort(key=lambda x: x[1])
        if len(r) < m:
            print('Waiting!')
            for p in r:
                print(*p)
        else:
            print('Started!')
            for p in r:
                print(*p)
    
if __name__ == "__main__":
    main()