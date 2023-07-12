def print_notes(notes):
    for note in notes:
        print(
            f"ID: {note['id']}, Title: {note['title']}, Text: {note['body']}, Create/Edit: {note['date']}")
        if not notes:
            print('Нет результатов поиска')


def print_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))


def input_data(message: str):
    data = input(message)
    return data