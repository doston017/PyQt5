from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont


dastur = QApplication([])
oyna = QWidget()
oyna.setWindowTitle("Calculator")
oyna.setFixedSize(300, 400)


yozuv1 = QLabel("", oyna)
yozuv1.move(50, 10)
yozuv1.setStyleSheet("font-size:30px;color:black")

input_field = QLineEdit(oyna)
input_field.setGeometry(5, 50, 290, 30)
input_field.setFont(QFont("Calibri", 30))
input_field.setStyleSheet("font-size: 30px;border: 1px solid black")
input_field.setPlaceholderText("")

def calc():
    button = dastur.sender()
    current_text = input_field.text()
    button_text = button.text()

    if button_text == "=":
        try:
            result = eval(current_text)
            input_field.setText(str(result))
        except Exception as e:
            input_field.setText("Error")
    else:
        input_field.setText(current_text + button_text)

# 1st row
bt1 = QPushButton("1", oyna)
bt1.setGeometry(30, 200, 60, 50)
bt1.setStyleSheet("font-size: 20px;")
bt1.clicked.connect(calc)

bt2 = QPushButton("2", oyna)
bt2.setGeometry(90, 200, 60, 50)
bt2.setStyleSheet("font-size: 20px;")
bt2.clicked.connect(calc)

bt3 = QPushButton("3", oyna)
bt3.setGeometry(150, 200, 60, 50)
bt3.setStyleSheet("font-size: 20px;")
bt3.clicked.connect(calc)

divide = QPushButton("/", oyna)
divide.setGeometry(210, 200, 60, 50)
divide.setStyleSheet("font-size: 20px;")
divide.clicked.connect(calc)

# 2nd row
bt4 = QPushButton("4", oyna)
bt4.setGeometry(30, 250, 60, 50)
bt4.setStyleSheet("font-size: 20px;")
bt4.clicked.connect(calc)

bt5 = QPushButton("5", oyna)
bt5.setGeometry(90, 250, 60, 50)
bt5.setStyleSheet("font-size: 20px;")
bt5.clicked.connect(calc)

bt6 = QPushButton("6", oyna)
bt6.setGeometry(150, 250, 60, 50)
bt6.setStyleSheet("font-size: 20px;")
bt6.clicked.connect(calc)

multiply = QPushButton("*", oyna)
multiply.setGeometry(210, 250, 60, 50)
multiply.setStyleSheet("font-size: 20px;")
multiply.clicked.connect(calc)

# 3rd row
bt7 = QPushButton("7", oyna)
bt7.setGeometry(30, 300, 60, 50)
bt7.setStyleSheet("font-size: 20px;")
bt7.clicked.connect(calc)

bt8 = QPushButton("8", oyna)
bt8.setGeometry(90, 300, 60, 50)
bt8.setStyleSheet("font-size: 20px;")
bt8.clicked.connect(calc)

bt9 = QPushButton("9", oyna)
bt9.setGeometry(150, 300, 60, 50)
bt9.setStyleSheet("font-size: 20px;")
bt9.clicked.connect(calc)

minus = QPushButton("-", oyna)
minus.setGeometry(210, 300, 60, 50)
minus.setStyleSheet("font-size: 20px;")
minus.clicked.connect(calc)

# 4th row
zero = QPushButton("0", oyna)
zero.setGeometry(30, 350, 80, 50)
zero.setStyleSheet("font-size: 20px;")
zero.clicked.connect(calc)

equal = QPushButton("=", oyna)
equal.setGeometry(110, 350, 80, 50)
equal.setStyleSheet("font-size: 20px;")
equal.clicked.connect(calc)

plus = QPushButton("+", oyna)
plus.setGeometry(190, 350, 80, 50)
plus.setStyleSheet("font-size: 20px;")
plus.clicked.connect(calc)



oyna.show()
dastur.exec_()
