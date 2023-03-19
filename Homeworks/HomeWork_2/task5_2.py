import sys


def print_analog(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    # Преобразуем все аргументы в строки
    result_string = ''
    for arg in args:
        result_string += str(arg)

    # Объединяем аргументы с помощью разделителя
    output = sep.join(result_string)
    # Добавляем символ окончания строки
    output += end
    # Записываем строку в файл вывода
    file.write(output)
    # Если нужно, сбрасываем буфер вывода
    if flush:
        file.flush()


print_analog("Hello", "world", "!")
print_analog("The answer is", 42, sep='')
print_analog("This is a test", end="", flush=True)
