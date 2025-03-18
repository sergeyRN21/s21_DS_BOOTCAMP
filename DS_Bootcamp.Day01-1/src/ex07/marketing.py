import sys

clients = ['andrew@gmail.com',
           'jessica@gmail.com',
           'ted@mosby.com',
           'john@snow.is',
           'bill_gates@live.com',
           'mark@facebook.com',
           'elon@paypal.com',
           'jessica@gmail.com'] #Первый список — это адреса электронной почты ваших клиентов
participants = ['walter@heisenberg.com',
                'vasily@mail.ru',
                'pinkman@yo.org',
                'jessica@gmail.com',
                'elon@paypal.com',
                'pinkman@yo.org',
                'mr@robot.gov',
                'eleven@yahoo.com'] #Второй список содержит адреса электронной почты участников вашего последнего мероприятия (некоторые из них были вашими клиентами)
recipients = ['andrew@gmail.com',
              'jessica@gmail.com',
              'john@snow.is'] # Третий список содержит адреса электронной почты ваших клиентов, которые открыли ваше последнее рекламное письмо

def to_set(arr):
    return set(arr)

def get_call_center_emails(clients, recipients):
    clients_set = to_set(clients)
    recipients_set = to_set(recipients)
    return list(clients_set - recipients_set)

def get_potential_customers(participants, clients):
    participants_set = to_set(participants)
    clients_set = to_set(clients)
    return list(participants_set - clients_set)

def get_customers_to_send_info(clients, participants):
    participants_set = to_set(participants)
    clients_set = to_set(clients)
    return list(clients_set - participants_set)


def marketing(customers_info):
    if customers_info == 'call_center':
        return get_call_center_emails(clients, recipients)
    elif customers_info == 'potential_customers':
        return get_potential_customers(participants, clients)
    elif customers_info == 'send_info':
        return get_customers_to_send_info(clients, participants)
    else:
        raise ValueError(f'Задача "{customers_info}" неизвестна. Возможные варианты: "call_center", "potential_customers", "send_info".')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            result = marketing(sys.argv[1])
            print(result)
        except ValueError as e:
            print(e)
    else:
        print("Пожалуйста, введите корректную задачу: call_center, potential_customers или send_info.")