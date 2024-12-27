# Решение kp_1.3
def find_expensive_book(data: list):
    """
        Функция, которая находит самую дорогую книгу из списка (если книг таких несколько, то выводит первую в
        в алфавитном порядке)
    """
    if len(data) == 0:
        return None
    data = sorted(data, key = lambda x: x["price"], reverse = True)
    prices = []
    new_data = []
    for el in data:
        prices.append(el["price"])
    mx_price = max(prices)
    for el in data:
        if el["price"] == mx_price:
            new_data.append(el)

    return sorted(new_data, key = lambda x: x["name"])[0]


if __name__ == '__main__':
    assert find_expensive_book([]) is None
    assert find_expensive_book([
        {"name": "Пушкин А.С. Сказки", "price": 170}
    ]) ==     {"name": "Пушкин А.С. Сказки", "price": 170}

    assert find_expensive_book([
        {"name": "Пушкин А.С. Сказки", "price": 170},
        {"name": "Лермонтов М.Ю. Мцыри ", "price": 160},
        {"name": "Бунин И.А. Тёмные аллеи", "price": 166},
        {"name": "Чуковский К.И. Тараканище", "price": 186}
    ]) == {"name": "Чуковский К.И. Тараканище", "price": 186}

    assert find_expensive_book([
        {"name": "Чехов А.П. Повести и пьесы", "price": 186},
        {"name": "Лермонтов М.Ю. Мцыри", "price": 160},
        {"name": "Бунин И.А. Тёмные аллеи", "price": 166},
        {"name": "Горький М. Мать", "price": 186}
    ]) == {"name": "Горький М. Мать", "price": 186}

    assert find_expensive_book([
        {"name": "Чехов А.П. Повести и пьесы", "price": 186},
        {"name": "Лермонтов М.Ю. Мцыри", "price": 160},
        {"name": "Бунин И.А. Тёмные аллеи", "price": 166},
        {"name": "Иванов А. Сердце пармы", "price": 186},
        {"name": "Горький М. Мать", "price": 186}
    ]) == {"name": "Горький М. Мать", "price": 186}

    print('Все тесты пройдены')