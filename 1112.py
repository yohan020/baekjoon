import sys
input = sys.stdin.readline

def convert(x, b):
    if x == 0:
        return "0"

    if b > 0:
        sign = ""
        if x < 0:
            sign = "-"
            x = -x
        digits = []
        while x:
            digits.append(str(x % b))
            x //= b
        return sign + "".join(reversed(digits))
    else:
        temp_b = -b
        digits = []
        while x != 0:
            r = x % temp_b
            x = (x - r) // b
            digits.append(str(r))
        return "".join(reversed(digits))

x, b = map(int, input().split())
sys.stdout.write(convert(x, b))
