import datetime


def change_note():
    with open(f"notes.cvs", 'r', encoding='utf-8') as file:
        data = file.readlines()
    count_row=len(data)
    number_row = int(input(f"Введите номер строки, которую хотите изменить: от 1 до {count_row}: "))
    while number_row < 1 or number_row > count_row:
        number_row = int(input(f"Ошибка. Введите номер строки: от 1 до {count_row}: "))
    heading_note = input("Введите Заголовок заметки: ")
    body_note = input("Введите текст заметки: ")

    today = datetime.datetime.today()

    data[number_row - 1] = f'{number_row}; {heading_note}; ' +f'{today.strftime("%Y-%m-%d-%H.%M.%S")}; '+ f'{body_note}\n'
    with open(f'notes.cvs', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")
