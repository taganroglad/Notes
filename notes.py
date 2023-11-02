import uuid
from datetime import datetime
import json
class Note:
    def __init__(self, title, description):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.timestamp = datetime.now()
class Notes:
    def __init__(self):
        self.notes = []

    def save_notes_to_json(self, file_path):
        with open(file_path, "w") as file:
            notes_data = [note.__dict__ for note in self.notes]
            json.dump(notes_data, file)

    def load_notes_from_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                notes_data = json.load(file)
                self.notes = [Note(**note_data) for note_data in notes_data]
        except FileNotFoundError:
            self.notes = []

    def add_note(self, title, description):
        note = Note(title, description)
        self.notes.append(note)

    def update_note(self, note_id, new_description):
        for note in self.notes:
            if note.id == note_id:
                note.description = new_description
                note.timestamp = datetime.now()
                print(f"Заметка {note.title} успешно обновлена")
                return
        print(f"Заметка с идентификатором {note_id} не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                print(f"Заметка {note.title} успешно удалена")
                return
        print(f"Заметка с идентификатором {note_id} не найдена.")

    def find_note(self,name_of_note):
        if name_of_note in self.notes:
            return f"Заметка,{name_of_note}, описание:{self.notes[name_of_note]}"
        else: print(f"заметка {name_of_note}    не найдена")

    def display_notes(self):
        def display_notes(self):
            for note in self.notes:
                print(f"Заметка: {note.title}, Описание: {note.description}, Время создания: {note.timestamp}")

def main():
    nottes = Notes()

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Изменить заметку")
        print("3. Удалить заметку")
        print("4. Найти заметку")
        print("5. Показать все заметки")
        print("6. Сохранить заметки")
        print("7. Загрузить заметки")
        print("8. Выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            name_of_note = input("Введите заголовок заметки: ")
            description = input("Введите описание заметки: ")
            nottes.add_note(name_of_note,description)
        elif choice == "2":
            name_of_note = input("Введите имя(заголовок заметки) для изменения: ")
            new_description = input("Введите новое описание заметки: ")
            nottes.update_note(name_of_note, new_description)
        elif choice == "3":
            name_of_note = input("Введите имя(заголовок) заметки для удаления: ")
            nottes.delete_note(name_of_note)
        elif choice == "4":
            name_of_note = input("Введите имя(заголовок) заметки для поиска: ")
            result = nottes.find_note(name_of_note)
            print(result)
        elif choice == "5":
            nottes.display_notes()
        elif choice == "6":
            file_path = input("Введите имя файла для сохранения: ")
            nottes.save_notes_to_json(file_path)
        elif choice == "7":
            file_path = input("Введите имя файла для загрузки: ")
            nottes.load_notes_from_json(file_path)
        elif choice == "8":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")
if __name__ == "__main__":
    main()