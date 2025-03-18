import timeit

def extract_gmail_adress_with_loop(emails):
    new_email = []
    for email in emails:
        if '@gmail.com' in email:
            new_email.append(email)
    return new_email

def extract_gmail_adress_with_list_comprehension(emails):
    return[email for email in emails if '@gmail.com' in email]

def extract_gmail_adress_with_map(emails):
    gmail_addresses = map(lambda email: email if email.endswith('@gmail.com') else '', emails)
    return gmail_addresses


def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
    emails *= 5

    loop_time = timeit.timeit(lambda: extract_gmail_adress_with_loop(emails), number = 900000)
    list_comprehension_time = timeit.timeit(lambda: extract_gmail_adress_with_list_comprehension(emails), number=900000)
    map_time = timeit.timeit(lambda: extract_gmail_adress_with_map(emails), number = 900000)
    if loop_time > list_comprehension_time and map_time > list_comprehension_time:
        print("it is better to use a list comprehension")
    elif list_comprehension_time > loop_time and map_time > loop_time:
        print("it is better to use a loop")
    else:
        print("it is better to use a map")

    print(f"{loop_time} vs {list_comprehension_time} vs {map_time}")


if __name__ == '__main__':
    main()