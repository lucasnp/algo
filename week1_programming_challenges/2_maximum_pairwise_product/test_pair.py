import max_pairwise_product as fn
import random

def test_max(cnt, n, m):

    for c in range(cnt):
        print('Run #: {}'.format(c))

        arr_len = random.randint(2, n)
        arr = []
        for i in range(arr_len):
            arr.append(random.randint(0, m))

        res_naive = fn.max_pairwise_product(arr)
        res_fast = fn.max_pairwise_product_fast(arr)

        if res_naive != res_fast:
            print('ERROR: naive: {} - fast: {} - diff: {}'.format(
                res_naive, res_fast, res_naive - res_fast))
        else:
            print('OK')


if __name__ == '__main__':
    test_max(10, 5, 100)