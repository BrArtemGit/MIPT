import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gspec

x = np.linspace(-np.pi, np.pi, 100)


fg = plt.figure(figsize=(15, 5))
fg.suptitle('Графики') # заголовок рисунка
gs = gspec.GridSpec(ncols = 2 , nrows = 1, figure=fg, wspace=1, hspace=1)
axe00 = fg.add_subplot(gs[0, 0]) #Добавим область рисования в левую верхнюю клетку
axe00.set_title('Область 00')    #Заголовок области рисования
axe00.set_xlabel('x 00')         #Подпишем оси. x
axe00.set_ylabel('y 00')         #Подпишем оси. y
axe00.grid()                     #Построим в этой области рисования сетку
plt.plot(x, x**2, 'purple')

axe01 = fg.add_subplot(gs[0, 1])
axe01.set_xlabel('x 01')
axe01.set_ylabel('y 01')
axe01.grid()
plt.plot(x, -2*x, 'r', x, np.cos(-x) + np.sin(x), 'b')

plt.show()