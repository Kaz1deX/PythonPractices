def main(table):
    # Удаление дублирующегося столбца
    my_table = []
    for line in table:
        my_table.append([])
        for item in line:
            if item not in my_table[-1]:
                my_table[-1].append(item)
    for line in my_table:
        # Разделение по :
        line[0], phone_number = line[0].split(":")
        # Замена на Y и N
        if line[2] == "Выполнено":
            line[2] = "Y"
        else:
            line[2] = "N"
        # Замена / на .
        line[1] = line[1].replace('/', '.')
        # Округление чисел
        line[0] = str(round(float(line[0]), 1))
        # Добавление номер в конец таблицы
        phone_number = phone_number[2:]
        area_code = phone_number[:3]
        first_part = phone_number[3:6]
        second_part = phone_number[6:8]
        third_part = phone_number[8:]
        number = f"({area_code}) {first_part}-{second_part}-{third_part}"
        line.append(number)
    # Транспонирование таблицы
    result_table = [[0 for j in range(len(my_table))]
                    for i in range(len(my_table[0]))]
    for i in range(len(my_table)):
        for j in range(len(my_table[0])):
            result_table[j][i] = my_table[i][j]
    return result_table
