import sys
import math as m
input = sys.stdin.readline 

def solve1(x, b):
    if x == 0:
        print(0)
    
    digits = []
    temp = abs(b)
    
    while x != 0:
        r = x % temp  
        x = (x - r) // b  
        digits.append(str(r))
    
    print("".join(reversed(digits)))
        
def solve2(x, b):
    digits = []
    temp = abs(x)
    while temp > 0:
        digits.append(str(temp % b))
        temp //= b
    digits.reverse()
    if x < 0:
        print("-"+"".join(digits))
    elif x > 0:
        print("".join(digits))
    else:
        print(0)
x, b = map(int, input().split())
if b < -1:
    solve1(x, b)
    
elif b > 1:
    solve2(x, b)
