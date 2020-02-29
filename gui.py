import sys  # sys нужен для передачи argv в QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import *
import start


def charts():
    #values = start.alg()

    mbox = QMessageBox()
    mbox.setText("values")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    qp = QPalette()

    app.setPalette(qp)

    w = QWidget()
    w.resize(500, 600)
    w.setWindowTitle('Расчёт динамического поля концентрации вещества')

    texts = []


    length_l = QLabel("Длина трубки, l: ")
    texts.append(length_l)
    section_s = QLabel("Сечение трубки, s: ")
    texts.append(section_s)
    coeff_D = QLabel("Коэффициент пропорциональности, D: ")
    texts.append(coeff_D)
    coeff_C = QLabel("Коэффициент пористости, c: ")
    texts.append(coeff_C)
    coeff_alpha = QLabel("Коэффициет диффузии, alpha: ")
    texts.append(coeff_alpha)
    coeff_T = QLabel("Временной промежуток 0 < t < T, T: ")
    texts.append(coeff_T)
    grid_I = QLabel("Неявная схема. Параметр сетки по x, I:")
    texts.append(grid_I)
    grid_K = QLabel("Неявная схема. Параметр сетки по t, k: ")
    texts.append(grid_K)


    enters = []

    enter_l = QLineEdit()
    enters.append(enter_l)
    enter_s = QLineEdit()
    enters.append(enter_s)
    enter_D = QLineEdit()
    enters.append(enter_D)
    enter_C = QLineEdit()
    enters.append(enter_C)
    enter_alpha = QLineEdit()
    enters.append(enter_alpha)
    enter_T = QLineEdit()
    enters.append(enter_T)
    enter_I = QLineEdit()
    enters.append(enter_I)
    enter_K = QLineEdit()
    enters.append(enter_K)

    grid = QGridLayout(w)
    for i in range(8):
        texts[i].setFont(QFont("Consolas", 10, QFont.Bold))
        texts[i].adjustSize()
        grid.addWidget(texts[i], i, 0)
        grid.addWidget(enters[i], i, 1)

    button_ok = QPushButton("OK")
    button_ok.resize(100, 50)
    grid.addWidget(button_ok, 9, 0, 1, 2)

    button_ok.clicked.connect(charts())

    w.show()
    sys.exit(app.exec_())