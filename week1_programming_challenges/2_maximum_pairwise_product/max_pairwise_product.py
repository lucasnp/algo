# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    max_product = 0

    max_num = 0
    i_1 = 0
    i_2 = 0

    for i in range(len(numbers)):
        if numbers[i] > numbers[i_1]:
            i_1 = i
    num_1 = numbers[i_1]
    numbers.pop(i_1)

    for i in range(len(numbers)):
        if numbers[i] > numbers[i_2]:
            i_2 = i
    num_2 = numbers[i_2]

    return num_1 * num_2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
