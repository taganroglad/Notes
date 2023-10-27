class Notes:
    def __init__(self):
        self.notes = {}

    def add_note(self, name_of_note, description):
        self.notes[name_of_note] = description

    def update_note(self, name_of_note, new_desription):
        if name_of_note in self.notes:
            self.notes[name_of_note] = new_desription
            print(f"Заметка {name_of_note} успешно добавлена")
        else:
            print(f"Заметка {name_of_note} не найдена.")

    def delete_note(self,name_of_note):
        if name_of_note in self.notes:
            del self.notes[name_of_note]
            print(f"Заметка {name_of_note} успешно удалена")
        else:
            print(f"Заметка {name_of_note} не найдена.")

    def find_note(self,name_of_note):
        if name_of_note in self.notes:
            return f"Заметка,{name_of_note}, описание:{self.notes[name_of_note]}"
        else: print(f"заметка{name_of_note} не найдена")

    def display_notes(self):
        for name_of_note, description in self.notes.items():
            print(f"Заметка: {name_of_note}, Описание: {description}")

def main():
    nottes = Notes()

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Изменить заметку")
        print("3. Удалить заметку")
        print("4. Найти заметку")
        print("5. Показать все заметки")
        print("6. Выйти")
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
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()