# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):

    if n <= 1:
        return n

    this_num = 1
    prev_num = 1
    for i in range(2, n):
        tmp = this_num
        this_num += prev_num
        prev_num = tmp
    return this_num

if __name__ == '__main__':
    n = int(input())
    # print(calc_fib(n))
    print(calc_fib_fast(n))
