import sys
import timeit
from functools import reduce

def extract_squarinq_with_loop(num_arg):
    total_sum = 0
    for i in range(1, num_arg + 1):
        total_sum += i*i
    return total_sum

def extract_squaring_with_reduce(num_arg):
    result = reduce(lambda x, y: x + y ** 2, [i for i in range(1, num_arg + 1)])
    return result

def main(func_name, num_runs, num_arg):
    try:
        functions = {
                'loop': extract_squarinq_with_loop,
                'reduce': extract_squaring_with_reduce,
            }
        func = functions[func_name]
        time_argv = timeit.timeit(lambda: func(num_arg), number=num_runs)
        print(time_argv)
    except KeyError as e:
        print(f"Такой функции нет: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        func_name = sys.argv[1]
        num_runs = int(sys.argv[2])
        num_arg = int(sys.argv[3])
        main(func_name, num_runs, num_arg)
    else:
        print("Введено неверное количество аргументов")