# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.gridspec as gspec
#

def draw_funcs(x_start, x_end, x_num, *args):
    """
        функция, графически решает любую систему уравнений,
        получая в качестве параметров строки, задающие функции f1_str и f2_str,
        записанные по правилам  вычисления в Python.
        x-start, x_end - диапазон значений по x, на котором строится график
        x_num -  число разбиений по x
    """

    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(x_start, x_end, x_num)

    obj = []
    for i, el in enumerate(args):
        if i % 2 == 0:
            obj.append(el)
        else:
            obj.append(el)
            plt.plot(x, eval(obj[0]), obj[1])
            obj.clear()

    return plt.show()

draw_funcs(-10, 10, 50, '-x**2+5', 'r', '4*x +5', 'b', 'x**2', 'y')
