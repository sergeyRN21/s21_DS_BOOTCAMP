import timeit
import random
from collections import Counter


def my_count_func(list):
    result_dict = {}

    for num in list:
        if num not in result_dict:
            result_dict[num] = 1
        else:
            result_dict[num] += 1

    return result_dict

def my_top_count_func(list):
    count_dict = my_count_func(list)
    sorted_items = sorted(count_dict.items(), key=lambda x:(-x[1], x[0]))
    return sorted_items

def counter_count_func(list):
    return dict(Counter(list))

def counter_top_count_func(list):
    counts = Counter(list)
    return counts.most_common(10)


def main():
    random_list = [random.randint(0, 100) for _ in range(1000000)]

    time_1 = timeit.timeit(lambda: my_count_func(random_list), number=1)
    time_2 = timeit.timeit(lambda: my_top_count_func(random_list), number=1)
    time_3 = timeit.timeit(lambda: counter_count_func(random_list), number=1)
    time_4 = timeit.timeit(lambda: counter_top_count_func(random_list), number=1)

    print(f"my function: {time_1:.7f}")
    print(f"Counter: {time_3:.7f}")
    print(f"my top: {time_2:.7f}")
    print(f"counter's top: {time_4:.7f}")


if __name__ == '__main__':
    main()