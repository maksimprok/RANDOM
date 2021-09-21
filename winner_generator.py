from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
window = QWidget()
window.setWindowTitle("Первое приложение")

text = QLabel("Нажми, чтобы узнать")
winner = QLabel("?")
button = QPushButton("Кнопка!")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

window.setLayout(line)

def show_result():
    a = randint(1,100)
    a = str(a)
    winner.setText(a)

button.clicked.connect(show_result)

window.show()
app.exec_()