import phone_book as pb
import view

path = r'phone_book.txt' # в начале ставить r, чтобы бэкслэш не срабатывал



def save_contacts(phone_book: list):
    global path
    ready_book = list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:  # чтобы киррилица читалась нормально
        file.write(ready_book)
    print('Телефонная книга сохранена\n')

def list_to_str(phone_book: list) -> str:
    str_phone_book = ''
    for contact in phone_book:
        new_contact = ';'.join(contact)
        str_phone_book += new_contact + '\n'
    return str_phone_book[:-1]

def str_to_list(phone_book: list) -> list:
    new_list = []
    for contact in phone_book:
        new_contact = contact.strip().split(';') #удаляет справа и слева все ненужные пробелы и бэкслеш n
        new_list.append(new_contact)
    return new_list

def load_contacts():
    global path
    with open(path, 'r', encoding='UTF-8') as file: #чтобы киррилица читалась нормально
        data = file.readlines()
    pb.set_phone_book(str_to_list(data))
    print('Телефонная книга загружена\n')

def find_contacts():
    global path
    with open(path, 'r', encoding='UTF-8') as file: #чтобы киррилица читалась нормально
        data = file.readlines()
    pb.set_phone_book(str_to_list(data))
    print('Телефонная книга загружена\n')

def find_contacts(): # не понимаю, почему ищет только в первой строек из всего файла phone_book.txt
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i in range(len(data)):
        if view.word_for_finding() in data[i].lower():
            print(data[i])
            print()
            break
        else:
            print('Такого контакта нет, попробуйте уточнить запрос')
            print()
            break

def change_contact(): # контакт меняет, но добавляет пустую строчку, прошу помочь разобраться
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    change = view.contact_num()
    data[change] = input('Введите новые данные: ')
    with open(path, 'w', encoding='UTF-8') as file:
        for line in data:
            file.write(line + '\n')

