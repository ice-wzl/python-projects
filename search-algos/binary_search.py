#!/usr/bin/python3
from random import randint

def generate_array(size):
    array = []
    for i in range(1, size):
        array.append(randint(1,1000))
    return sorted(array)


def generate_target(array):
    target = randint(0, len(array))
    return target


def b_search(target, array, lo, hi):
    if hi >= lo:
        m = (hi + lo) // 2

        if target == m:
            return f"Found target: {array[target]} at index {m}"
    
        elif target > m:
            return b_search(target, array, m+1, len(array))
        elif target < m:
            return b_search(target, array, lo, m-1)




if __name__ == '__main__':

    generated_array = generate_array(100)
    print("*"*75)
    print(generated_array)

    target_index = generate_target(generated_array)
    print(f"Target index: generated_array[{target_index}]")
    print(f"Target value: {generated_array[target_index]}")
    print("*"*75)

    binary_search = b_search(target_index, generated_array, 0, len(generated_array))
    print(binary_search)