import json
from datetime import datetime

import view


def load_notes(file_name):
    try:
        with open(file_name, 'r') as f:
            notes = json.load(f)
            return notes
    except FileNotFoundError:
        pass


def save_notes(file_name, notes):
    with open(file_name, 'w') as f:
        json.dump(notes, f)


def find_notes_id(notes, note_id):
    result = []
    for note in notes:
        if note['id'] == note_id:
            result.append(note)
    return result


def find_notes_date(notes, date):
    result = []
    for note in notes:
        if date in note['date']:
            result.append(note)
    return result


def add_note(file_name, notes):
    title = view.input_data('Введите заголовок: ')
    body = view.input_data('Введите текст: ')
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note_id = 1
    for note in notes:
        if note["id"] == note_id:
            note_id += 1
    note = {'id': note_id, 'title': title, 'body': body, 'date': date}
    notes.append(note)

    notes.sort(key=lambda x: x['id'])

    save_notes(file_name, notes)


def edit_note(file_name, notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            note['title'] = view.input_data('Введите новый заголовок: ')
            note['body'] = view.input_data('Введите новы: ')
            note['date'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            save_notes(file_name, notes)
            return 1


def delete_note(file_name, notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(file_name, notes)
            return 1