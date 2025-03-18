import sys

def find_letter(name, file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise ValueError(f"Файл {file_path} не найден.")

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >=2 and parts[0] == name.capitalize():
            return f"Дорогой {parts[0]}, добро пожаловать в нашу команду. Мы уверены, что нам будет приятно работать с вами. Это обязательное условие для профессионалов, которых нанимает наша компания."

    raise ValueError(f"Имя '{name}' не найдено в файле {file_path}.")

if __name__ == "__main__":
    name = sys.argv[1]
    file_path = sys.argv[2]
    try:
        letter = find_letter(name, file_path)
        print(letter)
    except ValueError as e:
        print(e)