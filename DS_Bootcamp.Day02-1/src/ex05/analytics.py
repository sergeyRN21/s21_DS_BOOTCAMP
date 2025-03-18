from random import randint

class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data

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

    class Analytics(Calculations):
        def predict_random(self, n_predictions=10):
            predictions = []
            for _ in range(n_predictions):
                coin_flip = randint(0, 1)
                prediction = [coin_flip, 1 - coin_flip]
                predictions.append(prediction)
            return predictions

        def predict_last(self):
            return self.data[-1]
        
        def save_result_to_file(self, result, filename, extension = 'txt'):
            full_path = f'{filename}.{extension}'
            with open(full_path, 'w') as file:
                file.write(result)

    def __init__(self, filename):
        self.filename = filename

    def file_reader(self, has_header=True):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            if has_header:
                # Пропускаем первую строку, если она заголовок
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