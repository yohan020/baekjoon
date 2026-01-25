import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    Q = int(input())
    MAX_VAL = 200005
    box_to_cards = [[] for _ in range(N + 1)]
    card_to_boxes = {}

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            i, j = query[1], query[2]
            box_to_cards[j].append(i)
            if i not in card_to_boxes:
                card_to_boxes[i] = set()
            card_to_boxes[i].add(j)
        elif query[0] == 2:
            i = query[1]
            print(*sorted(box_to_cards[i]))
        elif query[0] == 3:
            i = query[1]
            if i in card_to_boxes:
                print(*sorted(list(card_to_boxes[i])))
            else:
                print()


    

if __name__ == "__main__":
    solve()