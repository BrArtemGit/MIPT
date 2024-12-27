def min_word(n):
    '''Функция находит самое короткое слово в предложении'''
    a = n.split()
    elem = a[0]
    len_elem = len(a[0])

    for el in a:
        if len(el) < len_elem:
            elem = el
            len_elem = len(el)
    return elem


if __name__ == "__main__":
    print(min_word.__doc__)
    assert min_word("The Tower of London was built in the 15th century") == "of"
    assert min_word("Функция выводит в стандартный поток вывода свои именованные аргументы") == "в"
    assert min_word("Кто is 1st here") == "is"
    print("Блок тестов пройден!")
