def get_input_parameters():
    n = int(input('Количество клеток: '))
    eff_list = []

    for i in range(n):
        x = int(input(f'Эффективность {i + 1} клетки: '))
        eff_list.append(x)

    return eff_list


def display_result(cells):
    print(f'Неподходящие значения: {cells}')


def select_cells(cells):
    not_in_list = []
    for i in range(len(cells)):
        if i + 1 > cells[i]:
            not_in_list.append(cells[i])
    return not_in_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
