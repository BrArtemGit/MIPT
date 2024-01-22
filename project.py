import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QPushButton, \
    QTextEdit, QLabel


class Creator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.nums = []

        self.setWindowTitle('Двумерные матрицы')
        self.setGeometry(0, 0, 1250, 615)

        self.Text = QTextEdit(self)
        self.Text.setGeometry(340, 140, 800, 500)

        self.warn1 = QLabel(self)
        self.warn1.setGeometry(490, 20, 281, 21)
        self.warn1.setText("Введите название файла вида : file.txt")

        self.warn2 = QLabel(self)
        self.warn2.setGeometry(490, 50, 431, 21)
        self.warn2.setText("В файле должны содержаться ряды чисел через пробел")

        self.warn3 = QLabel(self)
        self.warn3.setGeometry(490, 80, 241, 17)
        self.warn3.setText("В конце каждой строчки ставьте ;")

        self.warn4 = QLabel(self)
        self.warn4.setGeometry(490, 110, 291, 17)
        self.warn4.setText("В последней строке ; ставить не нужно!!!")

        self.file_name = QTextEdit(self)
        self.file_name.setGeometry(270, 20, 191, 21)
        # --------------------------------------------------
        self.load_out = QPushButton(self)
        self.load_out.setGeometry(10, 20, 251, 25)
        self.load_out.setText("Выгрузить матрицу из файла")
        self.load_out.clicked.connect(self.out)

        self.rotate_90 = QPushButton(self)
        self.rotate_90.setGeometry(10, 100, 251, 25)
        self.rotate_90.setText("Повернуть матрицу на 90 градусов")
        self.rotate_90.clicked.connect(self.r_90)

        self.rotate_n90 = QPushButton(self)
        self.rotate_n90.setGeometry(10, 140, 251, 25)
        self.rotate_n90.setText("Повернуть матрицу на -90 градусов")
        self.rotate_n90.clicked.connect(self.r_n90)

        self.sort_all_g = QPushButton(self)
        self.sort_all_g.setGeometry(10, 180, 251, 25)
        self.sort_all_g.setText("Отсортировать матрицу по строкам")
        self.sort_all_g.clicked.connect(self.s_a_g)

        self.sort_all_v = QPushButton(self)
        self.sort_all_v.setGeometry(10, 220, 251, 25)
        self.sort_all_v.setText("Отсортировать матрицу по столбцам")
        self.sort_all_v.clicked.connect(self.s_a_v)

        self.sort_g = QPushButton(self)
        self.sort_g.setGeometry(10, 260, 251, 25)
        self.sort_g.setText("Отсортировать строку N")
        self.num_g = QTextEdit(self)
        self.num_g.setGeometry(270, 260, 64, 25)
        self.sort_g.clicked.connect(self.s_g)

        self.sort_v = QPushButton(self)
        self.sort_v.setGeometry(10, 300, 251, 25)
        self.sort_v.setText("Отсортировать столбец N")
        self.num_v = QTextEdit(self)
        self.num_v.setGeometry(270, 300, 64, 25)
        self.sort_v.clicked.connect(self.s_v)

    #     ------for Random button---------
        self.rn_bt = QPushButton(self)
        self.rn_bt.setGeometry(10, 360, 251, 61)
        self.rn_bt.setText("Сгенерировать случайный список")
        self.rn_bt.clicked.connect(self.RANDOM_LIST)

        self.rn_warn = QLabel(self)
        self.rn_warn.setGeometry(10, 430, 71, 20)
        self.rn_warn.setText("Диапазон")

        self.rn_warn1 = QLabel(self)
        self.rn_warn1.setGeometry(10, 500, 67, 17)
        self.rn_warn1.setText("Размеры")

        self.rn_warn2 = QLabel(self)
        self.rn_warn2.setGeometry(100, 430, 21, 17)
        self.rn_warn2.setText("От")

        self.rn_warn3 = QLabel(self)
        self.rn_warn3.setGeometry(100, 470, 21, 17)
        self.rn_warn3.setText("До")

        self.rng_a = QTextEdit(self)
        self.rng_a.setGeometry(130, 430, 131, 21)

        self.rng_b = QTextEdit(self)
        self.rng_b.setGeometry(130, 470, 131, 21)

        self.size_a = QTextEdit(self)
        self.size_a.setGeometry(130, 510, 131, 21)

        self.size_b = QTextEdit(self)
        self.size_b.setGeometry(130, 550, 131, 21)

    def out(self):
        self.Text.setText('')
        nums = open(self.file_name.toPlainText(), encoding="utf-8").read().split(";\n")
        for i in range(len(nums)):
            nums[i] = nums[i].split(" ")
            for j in range(len(nums[i])):
                nums[i][j] = int(nums[i][j])

        for k in range(len(nums)):
            n = ''
            for t in range(len(nums[k])):
                n += str(nums[k][t]) + ("\t" if t != (len(nums[k]) - 1) else "")
            self.Text.append(n)
        self.nums = nums

    def r_90(self):
        self.Text.setText('')
        f = self.nums
        f = np.array(f)
        f = np.rot90(f, -1)
        for k in range(len(f)):
            n = ''
            for t in range(len(f[k])):
                n += str(f[k][t]) + ("\t" if t != (len(f[k]) - 1) else "")
            self.Text.append(n)
        self.nums = f

    def r_n90(self):
        self.Text.setText('')
        f = self.nums
        f = np.array(f)
        f = np.rot90(f)
        for k in range(len(f)):
            n = ''
            for l in range(len(f[k])):
                n += str(f[k][l]) + ("\t" if l != (len(f[k  ]) - 1) else "")
            self.Text.append(n)
        self.nums = f

    def s_a_g(self):
        self.Text.setText('')
        f = self.nums
        for elem in f:
            elem.sort()
        for k in range(len(f)):
            n = ''
            for l in range(len(f[k])):
                n += str(f[k][l]) + ("\t" if l != (len(f[k]) - 1) else "")
            self.Text.append(n)
        self.nums = f

    def s_a_v(self):
        self.Text.setText('')
        f = self.nums
        f = np.array(f)
        f = np.rot90(f)
        for elem in f:
            elem.sort()
        f = np.rot90(f, -1)
        for k in range(len(f)):
            n = ''
            for l in range(len(f[k])):
                n += str(f[k][l]) + ("\t" if l != (len(f[k]) - 1) else "")
            self.Text.append(n)
        self.nums = f

    def s_g(self):
        self.Text.setText('')
        f = self.nums
        k = int(self.num_g.toPlainText())
        f[k].sort()
        for t in range(len(f)):
            n = ''
            for l in range(len(f[t])):
                n += str(f[t][l]) + ("\t" if l != (len(f[k]) - 1) else "")
            self.Text.append(n)
        self.nums = f
        self.num_g.setText("")

    def s_v(self):
        self.Text.setText('')
        f = self.nums
        k = int(self.num_v.toPlainText())
        f = np.array(f)
        f = np.rot90(f, -1)
        f[k][::-1].sort()
        f = np.rot90(f)
        for t in range(len(f)):
            n = ''
            for l in range(len(f[t])):
                n += str(f[t][l]) + ("\t" if l != (len(f[k]) - 1) else "")
            self.Text.append(n)
        self.nums = f
        self.num_v.setText("")

    def RANDOM_LIST(self):
        self.nums = np.random.randint(int(self.rng_a.toPlainText()),
                                      int(self.rng_b.toPlainText()),
                                      int(self.size_a.toPlainText()) * int(self.size_b.toPlainText())).reshape(
            int(self.size_a.toPlainText()), int(self.size_b.toPlainText()))
        f = self.nums
        for t in range(len(f)):
            n = ''
            for l in range(len(f[t])):
                n += str(f[t][l]) + "\t"
            self.Text.append(n)
        self.nums = f
        self.size_a.setText("")
        self.size_b.setText("")
        self.rng_a.setText("")
        self.rng_b.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Creator()
    ex.show()

    sys.exit(app.exec())
