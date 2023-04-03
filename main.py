# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# имя
# номер
# коммент
dict_phnbk = []
def meny():

    while True:
        arc = int(input("Введите код желаемого действия: \n"
            "1: Открыть файл телефонной книги\n"
            "2: Сохранить файл телефонной книги\n"
            "3: Показать все контакты\n"
            "4: Найти контакт\n"
            "5: Добавить контакт\n"
            "6: Изменить контакт\n"
            "7: Удалить контакт\n"
            "8: Выход: "))

        if arc == 1:
            open_read_dir()
            print("open")
        elif arc == 2:
            save_dir()
            print("safe")
        elif arc == 3:
            show_contacts(dict_phnbk, "Телефонная книга пуста или не открыта")
        elif arc == 4:
            name = input("Введите имя контакта: ")
            contact = find_contact(dict_phnbk, name)
            if contact:
                print(f"Контакт найден: {contact}")
            else:
                print(f"Контакт с именем {name} не найден.")
        elif arc == 5:
            new_contact = add_contact()
            print(f"Контакт {new_contact['name']} добавлен.")
        elif arc == 6:
            index = int(input('Введите номер изменяемого контакта: '))
            if 1 <= index <= len(dict_phnbk):
                new_contact = change_contact(dict_phnbk, index)
                if new_contact is not None:
                    dict_phnbk.pop(index - 1)
                    dict_phnbk[index - 1] = new_contact
                    print(f'Контакт {dict_phnbk[index - 1].get("name")} успешно изменен!')
                else:
                    print('Изменения не были внесены')
            else:
                print('Неверный номер контакта')

        elif arc == 7:
            index = int(input('Введите номер удаляемого контакта: '))
            if 1 <= index <= len(dict_phnbk):
                dict_phnbk.pop(index - 1)
                print('Контакт успешно удален!')

        elif arc == 8:
            print("Конец")
            break
        else:
            print("Введите корректные данные: ")


def open_read_dir():
    with open("phonebook.txt", "r", encoding="UTF-8") as f:
        data = f.readlines()
    for fields in data:
        fields = fields.strip().split(";")
        contact = {"name": fields[0],
                   "phone": fields[1],
                   "comment": fields[2]}
        dict_phnbk.append(contact)

def save_dir():
    data = []
    for contact in dict_phnbk:
        data.append(contact["name"] + ";" + contact["phone"] + ";" + contact["comment"] + "\n")
        with open("phonebook.txt", "w", encoding="UTF-8") as f:
            f.writelines(data)


def add_contact() -> dict:
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    contact = {'name': name, 'phone': phone, 'comment': comment}
    dict_phnbk.append(contact)
    return contact

def show_contacts(dict_phnbk: list[dict], error_message: str):
    if not dict_phnbk:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(dict_phnbk, 1):
            print(f"{i}. {contact.get('name'): <20} "
                f" {contact.get('phone'): <20}"
                f" {contact.get('comment'): <20}")
        return True

def find_contact(phone_book, name):
    for contact in phone_book:
        if contact['name'] == name:
            return contact
    return None

def change_contact(dict_phnbk: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    if not contact:
        return dict_phnbk[index - 1]
    else:
        dict_phnbk[index - 1]['name'] = contact.get('name', dict_phnbk[index - 1]['name'])
        dict_phnbk[index - 1]['phone'] = contact.get('phone', dict_phnbk[index - 1]['phone'])
        dict_phnbk[index - 1]['comment'] = contact.get('comment', dict_phnbk[index - 1]['comment'])
        return dict_phnbk[index - 1]


    # contact = {}
    # name = input("Введите имя: ")
    # phone = input("Введите номер телефона: ")
    # comment = input("Введите комментарий: ")
    # if name:
    #     contact['name'] = name
    # else:
    #     contact['name'] = dict_phnbk[index - 1]['name']
    # if phone:
    #     contact['phone'] = phone
    # else:
    #     contact['phone'] = dict_phnbk[index - 1]['phone']
    # if comment:
    #     contact['comment'] = comment
    # else:
    #     contact['comment'] = dict



meny()