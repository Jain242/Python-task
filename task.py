import csv
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NotesApp:

    def __init__(self, notes_file="notes.csv"):
        self.notes_file = notes_file
        self.notes = self.load_notes()



    def load_notes(self):

        if not os.path.exists(self.notes_file):
            return []
        notes = []
        with open(self.notes_file, newline='',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                note = Note(int(row['id']), row['title'], row['body'], row['timestamp'])
                notes.append(note)
        return notes

    def save_notes(self):

        with open(self.notes_file, 'w', newline='',encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body', 'timestamp']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for note in self.notes:
                writer.writerow({'id': note.id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp})

    def sort_notes(self):
        """Сортировать заметки по заданному ключу."""
        try:
            self.notes.sort(key=lambda x: x.timestamp)
            print('Сортировка прошла успешно')
        except:
            print('Возникла ошибка при сортировке')
        
   


    def add_note(self, title, body):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(len(self.notes) + 1, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()
        print("Заметка добавлена успешно.")

    def edit_note(self, note_id, new_title, new_body):
 
        self.list_notes(self)
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")

    def delete_note(self, note_id):

        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным ID не найдена.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Дата/время создания: {note.timestamp}")
            print("-" * 20)


def main():
    notes_app = NotesApp()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Показать список заметок")
        print("5. Сортировать заметки")
        print("6. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes_app.add_note(title, body)
        elif choice == "2":
            notes_app.list_notes()
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            notes_app.edit_note(note_id, new_title, new_body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes_app.delete_note(note_id)
        elif choice == "4":
            notes_app.list_notes()
        elif choice == "5":
            notes_app.sort_notes()
            print("Заметки отсортированы.")
            
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")



if __name__ == "__main__":
    main()