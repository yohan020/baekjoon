import sys
from io import StringIO
import G

def test():
    input_str = """3 5
S.x.G
.....
..?.o"""
    
    sys.stdin = StringIO(input_str)
    
    # Expected output: 
    # S(0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)?(switch) -> (1,2) -> (1,1) -> (0,1) -> (0,2)x(now o) -> (0,3) -> (0,4)G
    # Distance: 
    # (0,0)0
    # (0,1)1
    # (1,1)2
    # (1,2)3
    # (2,2)4 (switch=1)
    # (1,2)5
    # (1,1)6
    # (0,1)7
    # (0,2)8 (passable)
    # (0,3)9
    # (0,4)10
    
    # Wait, is there a shorter path?
    # S(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2)? -> (2,3) -> (2,4)o(now x) -> blocked
    # So we must go back to top row.
    
    # Let's just run it and see.
    G.solve()

if __name__ == "__main__":
    test()
