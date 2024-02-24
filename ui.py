from add_data import add_note
from change_data import change_note
from delete_data import delete_note
from print_data import print_file
from print_data import timefilter


def check_number(n):
    while n<1 or n>5:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 5\n"
                      "Выберите функцию:\n"
                      "1. Добавить\n"
                      "2. Удалить\n"
                      "3. Изменить\n"
                      "4. Вывод\n"
                      "5. Выход\n"
                      "Введите номер команды: "))
    return n

def check_number2(a):
    while a<1 or a>2:
        a = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 2\n"
                      "Выберите фильтр:\n"
                            "1. Вывести все записи\n"
                            "2. Фильтровать запись по дате создания / изменения\n"
                            "Введите номер команды: "))
    return a


def start_menu():
    command = None
    command2=None
    while command != 5:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить\n"
                            "2. Удалить\n"
                            "3. Изменить\n"
                            "4. Вывод\n"
                            "5. Выход\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_note()
            
        elif command == 2:
            delete_note()
           
        elif command == 3:
            change_note()
            
        elif command == 4:
            command2 = int(input("Выберите фильтр:\n"
                "1. Вывести все записи\n"
                "2. Фильтровать запись по дате создания / изменения\n"
                "Введите номер команды: "))
            command2 = check_number2(command2)
            if command2==1:
                print_file()
            elif command2==2:
                timefilter()
                
            
    print("Спасибо, на этом все")
