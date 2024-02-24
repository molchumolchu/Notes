def delete_note():
    
    with open (f"notes.cvs", 'r', encoding='utf-8') as file:
        data = file.readlines()
        count_row = len(data)
    if count_row == 0:
        print("Файл пустой")
    else:
        number_row = int(input(f"Введите номер строки: "
                               f"от 1 до {count_row} "))
        while number_row <1 or number_row > count_row:
            number_row = int(input(f"Ошибка. Введите номер строки: "
                                   f"от 1 до {count_row} "))
        del data[number_row - 1]
        data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3] }'
                # f'{data[i].split(";")[4]}' 
                for i in range(len(data))]
        with open(f'notes.cvs', 'w', encoding='utf-8') as file:
            file.writelines(data)
        print("Строка успешно удалена!")

