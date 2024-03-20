import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, message):
    notes = load_notes()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def read_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Сообщение: {note['message']}, Дата/Время: {note['timestamp']}")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def filter_notes_by_date(date):
    notes = load_notes()
    filtered_notes = [note for note in notes if note["timestamp"].split()[0] == date]
    if not filtered_notes:
        print("Нет заметок за указанную дату.")
        return
    for note in filtered_notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Сообщение: {note['message']}, Дата/Время: {note['timestamp']}")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку")
        print("4. Редактировать заметку")
        print("5. Выборка заметок по дате")
        print("6. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            add_note(title, message)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            edit_note(note_id, title, message)
        elif choice == "5":
            date = input("Введите дату в формате YYYY-MM-DD: ")
            filter_notes_by_date(date)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
