# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    r = 1

    l = max(a, b)
    s = min(a, b)

    while r != 0:
        r = l % s
        l = s
        s = r

    return l

if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
    # print(gcd_naive(a, b))
