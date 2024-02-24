def print_file():
    with open(f'notes.cvs', 'r', encoding='utf-8') as file:
        data = file.readlines()
    print()
    print(f"Вывод данных из файла: \n"
              f"{''.join(data)}")


def check_time_filter(n):
    while n<1 or n>2:
        n = int(input("Ошибка, фильтра не "
                      "существует! Введите цифру от 1 до 2\n"
                      "Выберите фильтр:\n"
                      "1. Месяц\n"
                      "2. Остановиться на выбранных фильтрах\n"
                      "Введите номер команды: "))
    return n

def timefilter():
    command = None
    yyyy = 0000
    month = 00
    dd = 00
    hh = 00
    min = 00

    while command != 2:
        command = int(input("Выберите фильтр:\n"
                      "1. Месяц в формете MM\n"
                      "2. Остановиться на выбранных фильтрах\n"
                      "Введите номер команды: "))
        command = check_time_filter(command)
        

        if command == 1:
            month = input("Введите месяц начала отсчета в формете mm ")
            # pass
           
    with open('notes.cvs', 'r') as file:
        lines = file.readlines()
    filtered_lines = []

    for line in lines:
        elements = line.split(';')
        third_element = elements[2]
        third_element_filtr=third_element.split("-")
        
    for line in lines:
            if third_element_filtr[1] >= month:
                print(line)
            
    