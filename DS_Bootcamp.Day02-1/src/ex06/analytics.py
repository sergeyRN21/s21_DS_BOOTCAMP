import logging
import os.path
from random import randint
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(message)s')

file_handler = logging.FileHandler('analytics.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data
            logger.info("Инициализируется объект Calculations.")

        @staticmethod
        def counts(data):
            heads_count = sum([row[0] for row in data])
            tails_count = sum([row[1] for row in data])
            logger.info(f"Подсчёт количества орлов и решек: {heads_count}, {tails_count}.")
            return heads_count, tails_count

        @staticmethod
        def fractions(heads_count, tails_count):
            total = heads_count + tails_count
            heads_fraction = (heads_count / total) * 100
            tails_fraction = (tails_count / total) * 100
            logger.info(f"Расчёт вероятностей: головы - {heads_fraction:.2f}%, хвосты - {tails_fraction:.2f}%.")
            return heads_fraction, tails_fraction

    class Analytics(Calculations):
        def predict_random(self, n_predictions=10):
            predictions = []
            for _ in range(n_predictions):
                coin_flip = randint(0, 1)
                prediction = [coin_flip, 1 - coin_flip]
                predictions.append(prediction)
            logger.info(f"Случайные предсказания сделаны: {predictions}.")
            return predictions

        def predict_last(self):
            prediction = self.data[-1]
            logger.info(f"Последнее предсказание: {prediction}.")
            return prediction

        def save_result_to_file(self, result, filename, extension='txt'):
            full_path = f'{filename}.{extension}'
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(result)
            logger.info(f"Результат сохранён в файл: {full_path}.")
            print(f'Результат сохранен в файл: {full_path}')

    def __init__(self, filename):
        self.filename = filename
        logger.info(f"Инициализируется объект Research с файлом {filename}.")

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

            logger.info(f"Данные прочитаны из файла {self.filename}: {data}.")
            return data
        except FileNotFoundError:
            logger.error(f"Файл {self.filename} не найден.")
            print(f"Файл {self.filename} не найден.")
        except Exception as e:
            logger.exception(f"Произошла ошибка при чтении файла: {e}")
            print(f"Произошла ошибка при чтении файла: {e}")

    def send_telegram_message(self, message, bot_token, chat_id):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logger.info(f"Сообщение '{message}' успешно отправлено в Telegram.")
        else:
            logger.warning(f"Не удалось отправить сообщение '{message}' в Telegram. Код ответа: {response.status_code}.")