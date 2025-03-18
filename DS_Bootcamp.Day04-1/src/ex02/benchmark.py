import timeit
import sys

def extract_gmail_adress_with_loop(emails):
    new_email = []
    for email in emails:
        if '@gmail.com' in email:
            new_email.append(email)
    return new_email

def extract_gmail_adress_with_list_comprehension(emails):
    return[email for email in emails if '@gmail.com' in email]

def extract_gmail_adress_with_map(emails):
    return map(lambda email: email if '@gmail.com' else None, emails)

def extract_gmail_adress_with_filter(emails):
    return filter(lambda email: '@gmail.com' in email, emails)

def main(name_extract, numbers):
    try:
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
        emails *= 5

        functions = {
            'loop': extract_gmail_adress_with_loop,
            'list_comprehension': extract_gmail_adress_with_list_comprehension,
            'map': extract_gmail_adress_with_map,
            'filter': extract_gmail_adress_with_filter
        }
        func = functions[name_extract]
        time_argv = timeit.timeit(lambda: func(emails), number = numbers)

        print(time_argv)
    except Exception as e:
        print(f"Нет такой функции: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        function_name = sys.argv[1]
        num_runs = int(sys.argv[2])
        main(function_name, num_runs)
    else:
        print("Введено некорректное количество аргументов")