def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    if '@' not in sender or not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f"Невозможно отправить письмо с адреса {sender}")
        return

    if '@' not in recipient or not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print(f"Невозможно отправить письмо на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Привет!', 'student@example.ru')
send_email('Привет!', 'student@example.ru', sender='another.sender@mail.ru')
send_email('Привет!', 'invalid.address')
send_email('Привет!', 'university.help@gmail.com')



