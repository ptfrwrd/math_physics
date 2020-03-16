import sys  # sys нужен для передачи argv в QApplication
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import *
import start


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Расчёт динамического поля концентрации вещества'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.length_l = QLabel("Длина трубки, l: ", self)
        self.length_l.move(20,20)
        self.length_l.resize(200, 20)
        self.section_s = QLabel("Сечение трубки, s: ", self)
        self.section_s.move(20,60)
        self.section_s.resize(200, 20)
        self.coeff_D = QLabel("Коэффициент пропорциональности, D: ", self)
        self.coeff_D.move(20,100)
        self.coeff_D.resize(200, 20)
        self.coeff_C = QLabel("Коэффициент пористости, c: ", self)
        self.coeff_C.move(20, 140)
        self.coeff_C.resize(200, 20)
        self.coeff_alpha = QLabel("Коэффициет диффузии, alpha: ", self)
        self.coeff_alpha.move(20, 180)
        self.coeff_alpha.resize(200, 20)
        self.coeff_T = QLabel("Временной промежуток 0 < t < T, T: ", self)
        self.coeff_T.move(20, 220)
        self.coeff_T.resize(200, 20)
        self.grid_I = QLabel("Неявная схема. Параметр сетки по x, I:", self)
        self.grid_I.move(20, 260)
        self.grid_I.resize(200, 20)
        self.grid_K = QLabel("Неявная схема. Параметр сетки по t, k: ", self)
        self.grid_K.move(20,300)
        self.grid_K.resize(200, 20)
        self.enter_l = QLineEdit(self)
        self.enter_l.move(300, 20)
        self.enter_s = QLineEdit(self)
        self.enter_s.move(300, 60)
        self.enter_D = QLineEdit(self)
        self.enter_D.move(300, 100)
        self.enter_C = QLineEdit(self)
        self.enter_C.move(300, 140)
        self.enter_alpha = QLineEdit(self)
        self.enter_alpha.move(300, 180)
        self.enter_T = QLineEdit(self)
        self.enter_T.move(300, 220)
        self.enter_I = QLineEdit(self)
        self.enter_I.move(300, 260)
        self.enter_K = QLineEdit(self)
        self.enter_K.move(300, 300)
        self.button = QPushButton('Рассчитать', self)
        self.button.move(20, 360)
        self.button.clicked.connect(self.on_click)
        self.show()


    @pyqtSlot()
    def on_click(self):
        l_value = float(self.enter_l.text())
        D_value = float(self.enter_D.text())
        c_value = float(self.enter_C.text())
        alpha_value = float(self.enter_alpha.text())
        T_value = float(self.enter_T.text())
        I_value = int(self.enter_I.text())
        K_value = int(self.enter_K.text())
        start.alg(l_value, D_value, c_value, alpha_value, T_value, I_value, K_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


