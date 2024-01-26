from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont

class quest(QLabel):
    def __init__(self, txt, parent=None):
        super().__init__(txt, parent)
        self.setFont(QFont("Britannic Bold", 20))
        self.setGeometry(100, 20, 500, 50)
        self.setStyleSheet('''
            QLabel {
                font-size: 20px;
            }''')

class Button(QRadioButton):
    def __init__(self, txt, parent=None):
        super().__init__(txt, parent)
        self.setFont(QFont("Berlin Sans FB", 15))
        self.setGeometry(30,140,500,30)
        self.setStyleSheet('''
            QRadioButton {
                font-size: 15px;    
            }''')

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 600, 500, 400)
        self.setWindowTitle("Questionnaire")
        self.setStyleSheet("background-color:lightblue")

        self.questions = [
            {"question": "Janubiy Amerikadagi eng katta davlat", "options": ["Canada", "Amerika", "Argentina", "Braziliya"], "correct": "Braziliya"},
            {"question": "2-Eng Katta Qit'a", "options": ["Yevropa", "Amerika", "Afrika", "Avstraliya"], "correct": "Afrika"},
            {"question": "2-Jahon Urushi Boshlangan Yil", "options": ["1940", "1945", "1939", "1936"], "correct": "1939"},
            {"question": "Eng Uzun Daryo", "options": ["Nil", "Amudaryo", "London", "Amazonka"], "correct": "Nil"},
            {"question": "Eng Katta daryo", "options": ["Nil", "Amudaryo", "London", "Amazonka"], "correct": "Amazonka"},
            {"question": "Eng Uzun Tog' Tizmasi", "options": ["Everest", "Nurota", "Alp", "Himalay"], "correct": "Alp"},
            {"question": "Angilyadagi eng birinchi futbol Jamoa", "options": ["Everton", "Liverpool", "Sheffield", "Manchester United"], "correct": "Sheffield"},
            {"question": "Odamzotning 2-Otasi kim?", "options": ["Odam A.S", "Nuh A.S", "Ayyub A.S", "Iso A.S"], "correct": "Nuh A.S"},
            {"question": "Dunyodagi eng ko'p aholiga ega davlat?", "options": ["Amerika", "Xitoy", "Rossiya", "Hindiston"], "correct": "Hindiston"},
            {"question": "Dunyodagi eng kichik davlat?", "options": ["Malayziya", "Sudan", "Vatikan", "Qatar"], "correct": "Vatikan"}            
        ]

        self.current_question_index = 0
        self.score = 0  

        self.question_label = QLabel("", self)
        self.question_label.setGeometry(20, 40, 500, 30)
        self.question_label.setFont(QFont("Britannic Bold", 12))
        
        self.previous = QPushButton("Previous", self)
        self.previous.move(250, 350)
        self.previous.clicked.connect(self.show_previous_question)
        self.previous.setStyleSheet("QPushButton { background-color: #3498db; color: #ffffff; }")

        self.empty = QPushButton("       ", self)
        self.empty.move(250, 350)
        self.empty.setStyleSheet("QPushButton { background-color: white; color: white and; }")
        
        self.f = QPushButton("Result", self)
        self.f.move(350, 350)
        self.f.clicked.connect(self.result)
        self.f.setStyleSheet("QPushButton { background-color: #e74c3c; color: #ffffff; }")
        
        self.next = QPushButton("Next", self)
        self.next.move(350, 350)
        self.next.clicked.connect(self.show_next_question)
        self.next.setStyleSheet("QPushButton { background-color: #3498db ; color: #ffffff ; }")

        self.q_label = quest("", self)
        self.q_label.move(20, 80)

        self.option_buttons = []
        for i in range(4):
            button = Button("", self)
            button.move(20, 120 + i * 40)
            button.clicked.connect(self.check_answer)
            self.option_buttons.append(button)

        self.show_current_question()

    def show_current_question(self):
        current_question = self.questions[self.current_question_index]
        self.q_label.setText(current_question["question"])

        for i, option in enumerate(current_question["options"]):
            self.option_buttons[i].setText(option)

        total_questions = len(self.questions)
        self.question_label.setText(f"Question {self.current_question_index + 1} of {total_questions}")

    def show_next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            if self.current_question_index==9:
                self.next.hide()
            if self.current_question_index==1:
                self.empty.hide()    
            self.show_current_question()
        else:
            self.result()

    def show_previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_current_question()

    def check_answer(self):
        current_question = self.questions[self.current_question_index]
        selected_option = None

        for i, button in enumerate(self.option_buttons):
            if button.isChecked():
                selected_option = current_question["options"][i]
                break

        if selected_option == current_question["correct"]:
            self.score += 1

    def result(self):
        msg = QMessageBox()
        msg.setWindowTitle("Game Over")
        msg.setText(f"Your final score is: {self.score} out of {len(self.questions)}")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.close()
if __name__ == "__main__":
    app = QApplication([])
    oyna = Window()
    oyna.show()
    app.exec_()
