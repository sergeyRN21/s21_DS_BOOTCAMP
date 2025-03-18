import sys

class Research:
    class Calculations:
        @staticmethod
        def counts(data):
            heads_count = sum([row[0] for row in data])
            tails_count = sum([row[1] for row in data])
            return heads_count, tails_count

        @staticmethod
        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            heads_fraction = (heads_count / total) * 100
            tails_fraction = (tails_count / total) * 100
            return heads_fraction, tails_fraction

    def __init__(self, filename):
        self.filename = filename

    def file_reader(self, has_header=True):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            if has_header:
                # Пропустить первую строку, если она заголовок
                data = [[int(value) for value in line.strip().split(',')] for line in lines[1:]]
            else:
                data = [[int(value) for value in line.strip().split(',')] for line in lines]

            for row in data:
                if len(row) != 2 or not all(x in [0, 1] for x in row) or row[0] == row[1]:
                    raise ValueError("Неверная структура данных")

            return data
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        reader = Research(sys.argv[1])
        data = reader.file_reader(has_header=True)
        if data is not None:
            print(data)

            heads_count, tails_count = Research.Calculations.counts(data)
            print(f"{heads_count} {tails_count}")

            heads_fraction, tails_fraction = Research.Calculations.fractions(heads_count, tails_count)
            print(f"{heads_fraction} {tails_fraction}")
    else:
        print("Передайте путь до файла в качестве аргумента")