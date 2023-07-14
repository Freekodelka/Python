def read_file(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as file:
        for names in file:
            data = names.strip().split(';')
            surname = data[0]
            name = data[1]
            fathername = data[2]
            phonenumber = data[3]
            phone_book.append((surname, name, fathername, phonenumber))
    return phone_book

def write_file(filename, data):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(data)

def delete_user(phone_book, surname):       
    for user in phone_book:
        if user[0] == surname:
            phone_book.remove(user)
    return phone_book

def find_names(phone_book, surname):
    result = []
    for user in phone_book:
        if user[0] == surname:
            result.append(user)
    return result

def menu():
    filename = 'd:\Python\lesson8\Contacts.txt'
    phone_book = read_file(filename)
    while True:
        print('Выберите действие:')
        print('1 - Вывести всю информацию на экран')
        print('2 - Добавить номер в справочник')
        print('3 - Поиск номера телефона по фамилии')
        print('4 - Удалить номер из справочника')
        print('0 - Выйти из программы')
        n = int(input())
        if n == 0:
            break
        elif n == 1:
            for user in sorted(phone_book):
                print(f'{user[0]} {user[1]} {user[2]} {user[3]}')
            break

        elif n == 2:
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            fathername = input('Введите отчество: ')
            phone = input('Введите номер телефона: ')
            phone_book.append((surname, name, fathername, phone))
            write_file(filename, f'{surname};{name};{fathername};{phone}\n')
            
        elif n == 3:
            surname = input('Введите фамилию: ')
            result = find_names(phone_book, surname)
            if not result:
                print('Такой фамилии нет в справочнике')
            else:
                for user in sorted(result):
                    print(f'{user[0]} {user[1]} {user[2]} {user[3]}')
            
        elif n == 4:
            surname = input('Введите фамилию: ')
            phone_book = delete_user(phone_book, surname)
        else:
            print('Такого пользователя не существует')
        

if __name__ == '__main__':
    menu()