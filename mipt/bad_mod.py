
""" Функции для работы со строками """
def second_index(text: str, line: str) -> [int, None]:
    """
        Возвращает индекс второго вхождения строки line в строку text
    """

    n = text.find(line, text.find(line)+len(line))                   
    return None if n<0 else n

print("123445")
s = input("input")
print(s)


if __name__ == '__main__':
    print('Example:')
    print(second_index("Press", "s"))

    # Блок самотестирования
    assert second_index("Press", "") is None, "0"
    assert second_index("Press", "s") == 4, "1"
    assert second_index("Попади в цель!", "п") is None, "2"
    assert second_index("попади в цель!", "п") == 2, "2+"	
    assert second_index("Привет", " ") is None, "3"
    assert second_index("Привет, дружок", " ") is None, "4"
    assert second_index("Привет, дорогой друг", " ") == 15, "5"
    print('Все тесты пройдёны!')
