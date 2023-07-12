from datetime import datetime

import view
import service

notes = []
file_name = "notes.json"

def start():
    view.print_message("Заметки")
    while True:
        action = int(view.input_data(
            "Введите номер операции:\n1 — Показать все заметки\n2 — Найти заметку по ID\n3 — Найти заметку по дате создания\n4 — Добавить заметку\n5 — Редактировать заметку\n6 - Удалить заметку "
            "\n7 - Завершить работу\n>>> "))
        match action:
            case 1:
                view.print_notes(service.load_notes(file_name))
            case 2:
                note_id = int(view.input_data('Введите ID: '))
                find_result = service.find_notes_id(service.load_notes(file_name), note_id)
                if not find_result:
                    view.print_message('Нет результатов поиска')
                else:
                    view.print_notes(find_result)
            case 3:
                date = view.input_data('Введите дату создания заметки в формате ДД.ММ.ГГГГ: ')
                find_result = service.find_notes_date(service.load_notes(file_name), date)
                if not find_result:
                    view.print_message('Нет результатов поиска')
                else:
                    view.print_notes(find_result)
            case 4:
                service.add_note(file_name, notes)
                view.print_message('Заметка добавлена')
            case 5:
                note_id = int(view.input_data('Введите ID редактируемой заметки: '))
                edit_result = service.edit_note(file_name, service.load_notes(file_name), note_id)
                if not edit_result:
                    view.print_message('Нет результатов поиска')
                else:
                    view.print_message('Заметка отредактирована')
            case 6:
                note_id = int(view.input_data('Введите ID удаляемой заметки: '))
                delete_result = service.delete_note(file_name, service.load_notes(file_name), note_id)
                if not delete_result:
                    view.print_message('Нет результатов поиска')
                else:
                    view.print_message('Заметка удалена')
            case 7:
                break
            case default:
                view.print_message("Неправильный номер операции.")