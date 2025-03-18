import sys

class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            header = lines[0].strip().split(',')
            if len(header) != 2:
                raise ValueError("Неверный формат заголовка")
            for line in lines[1:]:
                values = line.strip().split(',')
                if len(values) != 2 or not all(x in ['0', '1'] for x in values):
                    raise ValueError("Неверная структура данных")
                elif values[0] == values[1]:
                    raise ValueError("Неверная структура данных")
            return ''.join(lines)
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        reader = Research(sys.argv[1])
        content = reader.file_reader()
        if content is not None:
            print(content)
    else:
        print("Передайте путь до файла в качестве аргумента")