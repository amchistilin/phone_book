import database as db
import view
import phone_book as pb



def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            db.load_contacts()
        case 3:
            db.save_contacts()
        case 4:
            pb.add_contact()
        case 5:
            db.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            db.find_contacts()
        case 0:
            return True

while True:
    choice = view.main_menu()
    if choice_menu(choice): # if true -> break
        break

    # print('Выберите команду меню:')
    # print('1. Показать телефонную книгу')
    # print('2. Загрузить телефонную книгу')
    # print('3. Сохранить телефонную книгу')
    # print('4. Добавить контакт')
    # print('5. Изменить контакт')
    # print('6. Удалить контакт')
    # print('7. Найти контакт')
    # print('0. Выйти из приложения\n')