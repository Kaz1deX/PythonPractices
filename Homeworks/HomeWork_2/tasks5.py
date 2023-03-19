def generate_groups():
    # Название группы и количество
    list_groups = ('ИВБО', 'ИКБО', 'ИМБО', 'ИНБО')
    miss = 1
    for name in list_groups:
        print(name)
        # Выбор количества групп
        match name:
            case 'ИВБО':
                counts = 8
            case 'ИКБО':
                counts = 33
            case 'ИМБО':
                counts = 2
            case 'ИНБО':
                counts = 13
        # Проход по каждому номеру группы
        for number in range(counts):
            # Некоторых групп нет
            if (name == 'ИКБО') and (((number+1) == 23) or ((number+1) == 29)):
                continue
            # Вывод всех групп из одной категории
            print(f"{name}-{(number+1):02d}-21", end=' ')
            # Условие из-за отсутствующих групп
            if name == "ИКБО":
                if (miss % 10 == 0):
                    print()
                miss += 1
            elif (number+1) % 10 == 0:
                print()
        # Условие для перехода на новую строку после блока всех номеров группы
        if name == "ИНБО":
            print()
        else:
            print('\n')


generate_groups()
