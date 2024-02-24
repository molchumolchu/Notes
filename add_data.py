import datetime


def add_note():
    
    heading_note = input("Введите Заголовок заметки: ")
    body_note = input("Введите текст заметки: ")

    today = datetime.datetime.today()
    
    with open (f"notes.cvs", 'r', encoding='utf-8') as file:
        data = file.readlines()
        now_number_row = len(data) + 1


    with open (f"notes.cvs", 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row}; {heading_note}; ' +f'{today.strftime("%Y-%m-%d-%H.%M.%S")}; '+ f'{body_note}\n')
    print("Данные успешно записаны")
