import sys
import psutil

def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Файл не найден")

def main(path):
    try:
        lines = read_file(path)

        for line in lines:
            pass

        process = psutil.Process()

        peak_memory_usage = process.memory_info().rss / (1024 ** 3)
        cpu_time = process.cpu_times().user + process.cpu_times().system

        print(f"Peak Memory Usage = {peak_memory_usage:.3f} GB")
        print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Введите корректное количество аргументов")
    else:
        try:
            main(sys.argv[1])
        except Exception as e:
            print(f"Произошла ошибка: {e}")
