import phone_book as pb

def main_menu():
    print('Выберите команду меню:')
    print('1. Показать телефонную книгу')
    print('2. Загрузить телефонную книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1,8) or choice == 0:
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')


def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    print()


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта, который надо удалить:  '))
    return id


def word_for_finding():
    word = input('Кого ищем? ')
    return word.lower()

def contact_num():
    num = int(input('Введите номер контакта, который хотите поменять'))
    res = num - 1
    return res
