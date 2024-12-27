# Решение kp_1.1
def calc_reverse_notation(text):
    '''Возвращает результат обратной бесскобочной записи выражения'''
    res = []
    for el in text.split():
        if el.isnumeric():
            res.append(int(el))
        else:
            i = len(res)
            if el == "+":
                res[i - 2] = res[i - 2] + res[i - 1]
                res.pop(i - 1)
            elif el == '-':
                res[i - 2] = res[i - 2] - res[i - 1]
                res.pop(i - 1)
            else:
                res[i - 2] = res[i - 2] * res[i - 1]
                res.pop(i - 1)
    return res[0]
