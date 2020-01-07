import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QPoint
from random import randrange
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawing = False
        self.pb_draw.clicked.connect(self.draw)

    def draw(self):
        self.drawing = True
        self.update()

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            for i in range(5):
                qp.setPen(QPen(QColor(*[randrange(255) for _ in range(3)])))
                x, y = randrange(self.size().width()), randrange(self.size().height())
                r = randrange(1, 50)
                qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
            self.drawing = False


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
