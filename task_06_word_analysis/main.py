def get_input_parameters():
    my_word = input('Введите слово: ')

    return my_word


def display_result(number_unique_letters):

    print(f'Количество уникальных букв: {number_unique_letters}')


def count_number_unique_letters(word):
    new_word = []

    for ch in list(word):
        count = 0
        for new_ch in list(word):
            if ch == new_ch:
                count += 1
        if count == 1:
            new_word.append(ch)

    return len(new_word)


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
