# Uses python3
import sys

def gcd_fast(a, b):
    r = 1

    l = max(a, b)
    s = min(a, b)

    while r != 0:
        r = l % s
        l = s
        s = r

    return l

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    # s = min(a, b)
    # l = max(a, b)

    gcd = gcd_fast(a, b)

    return int(a * b / gcd)

if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_fast(a, b))
    # print(lcm_naive(a, b))
