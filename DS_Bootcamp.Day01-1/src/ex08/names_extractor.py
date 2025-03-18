import sys

def names_extractor(file_path):
    try:
        with open(file_path, 'r') as file:
            emails = file.read().split('\n')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    
    result = []
    for email in emails:
        try:
            if '@' in email:
                name_parts = email.split('@')[0].split('.')
                first_name = name_parts[0].capitalize()
                last_name = name_parts[1].capitalize()
                result.append(f"{first_name}\t{last_name}\t{email}")
        except IndexError as e:
            print(f"Возникла ошибка при обработке строки '{email}'. Пропущенная строка.")
    return result


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    data = names_extractor(input_file_path)

    with open('employees.tsv', 'w') as output_file:
        output_file.write("\n".join(data))