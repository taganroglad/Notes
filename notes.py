class Notes:
    def __init__(self):
        self.notes = {}

    def add_note(self, name_of_note, description):
        self.notes[name_of_note] = description

    def update_note(self, name_of_note, new_desription):
        if name_of_note in self.notes:
            self.notes[name_of_note] = new_desription
            print(f"Контакт {name_of_note} успешно добавлен")
        else:
            print(f"Контакт {name_of_note} не найден.")

    def delete_note(self,name_of_note):
        if name_of_note in self.notes:
            del self.notes[name_of_note]
            print(f"Контакт {name_of_note} успешно удален")
        else:
            print(f"Контакт {name_of_note} не найден.")

