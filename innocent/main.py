dict_1 = {"первый":"the first",
        "второй":"the second",
        "третий":"the third"}

def print_kargs(**a):
    """ Функция выводит в стандартный поток вывода свои именованные аргументы"""
    for arg in a:
        print(f"{arg} :  {a[arg]}")


print_kargs(**dict_1)

def wert(q, *args, **kwargs):
    return