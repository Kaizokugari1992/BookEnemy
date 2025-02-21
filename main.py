from utils.function_base import FootballEvent
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QTextEdit, QPushButton, QMessageBox, QRadioButton
import sys


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.prompt = ("---Type the number of games you want to simulate in the <b>'Simulated Games'</b> field and press <b>Enter</b>"
                       " to access the rest of the options.---")
        self.dashspace = "-----------------------------------------------------"
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 550)
        self.setWindowTitle("BookEnemy")
        self.setFixedSize(self.width(), self.height())
        second_line = 200
        home_label = QLabel("Home Odds", self)
        tie_label = QLabel("Tie Odds", self)
        away_label = QLabel("Away Odds", self)
        your_odd_label = QLabel("Your Odds", self)
        mockentry_label = QLabel("Simulated Games", self)
        home_label.setGeometry(35, 10, 60, 20)
        tie_label.setGeometry(180, 10, 60, 20)
        away_label.setGeometry(325, 10, 60, 20)
        your_odd_label.setGeometry(35, second_line, 60, 20)
        mockentry_label.setGeometry(20, second_line + 270, 80, 20)

        self.hentry = QLineEdit(self)
        self.tentry = QLineEdit(self)
        self.aentry = QLineEdit(self)
        self.ownentry = QLineEdit(self)
        self.mockentry = QLineEdit(self)
        self.hentry.setGeometry(10, 30, 100, 20)
        self.tentry.setGeometry(155, 30, 100, 20)
        self.aentry.setGeometry(300, 30, 100, 20)
        self.ownentry.setGeometry(10, second_line + 20, 100, 20)
        self.mockentry.setGeometry(10, second_line + 290, 100, 20)
        self.ownentry.setEnabled(False)
        self.mockentry.setEnabled(False)
        self.mockentry.returnPressed.connect(self.get_mockgames)
        self.submitbutton = QPushButton("Submit", self)
        self.submitbutton.setGeometry(155, 55, 100, 20)
        self.submitbutton.clicked.connect(self.get_odd_value)
        self.myoddbutton = QPushButton("Submit", self)
        self.myoddbutton.setGeometry(10, second_line + 105, 100, 20)
        self.myoddbutton.setEnabled(False)
        self.myoddbutton.clicked.connect(self.my_odd_button_validation)
        self.unlock1button = QPushButton("Unlock", self)
        self.unlock1button.setGeometry(270, 55, 50, 20)
        self.unlock1button.clicked.connect(self.unlock1)
        self.unlock1button.setEnabled(False)
        self.unlock2button = QPushButton("Unlock", self)
        self.unlock2button.setGeometry(10, second_line + 130, 50, 20)
        self.unlock2button.clicked.connect(self.unlock2)
        self.unlock2button.setEnabled(False)
        self.mockresetbutton = QPushButton("Reset", self)
        self.mockresetbutton.setGeometry(10, second_line + 315, 100, 20)
        self.mockresetbutton.setEnabled(False)
        self.mockresetbutton.clicked.connect(self.reset_mockgames)

        self.option1button = QPushButton("Minimum Bets", self)
        self.option2button = QPushButton("All Scenarios", self)
        self.option3button = QPushButton("Won Games", self)
        self.option1button.setGeometry(10, second_line + 165, 100, 20)
        self.option2button.setGeometry(10, second_line + 195, 100, 20)
        self.option3button.setGeometry(10, second_line + 225, 100, 20)
        self.option1button.setEnabled(False)
        self.option2button.setEnabled(False)
        self.option3button.setEnabled(False)
        self.option1button.clicked.connect(self.option1)
        self.option2button.clicked.connect(self.option2)
        self.option3button.clicked.connect(self.option3)

        message_box = QTextEdit(self)
        message_box.setGeometry(10, 80, 390, 120)
        message_box.setReadOnly(True)
        self.message_box = message_box
        message_box.setText("Press the <b>'Submit'</b> button to initialize an event and get the rake value.")
        bigmessage_box = QTextEdit(self)
        bigmessage_box.setGeometry(160, second_line + 20, 240, 285)
        bigmessage_box.setReadOnly(True)
        self.bigmessage_box = bigmessage_box
        self.radio1 = QRadioButton("Home", self)
        self.radio2 = QRadioButton("Tie", self)
        self.radio3 = QRadioButton("Away", self)
        self.radio1.move(10, second_line + 45)
        self.radio2.move(10, second_line + 65)
        self.radio3.move(10, second_line + 85)
        self.radio1.setEnabled(False)
        self.radio2.setEnabled(False)
        self.radio3.setEnabled(False)
        self.radio1.setChecked(True)

    def reset_mockgames(self):
        self.mockentry.setEnabled(True)
        self.mockentry.clear()
        self.mockresetbutton.setEnabled(False)
        self.option2button.setEnabled(False)
        self.option3button.setEnabled(False)

        return

    def unlock1(self):
        self.hentry.setEnabled(True)
        self.tentry.setEnabled(True)
        self.aentry.setEnabled(True)
        self.message_box.setText("Press the 'Submit' button to initialize an event and get the rake value.")
        self.bigmessage_box.setText("")
        self.radio1.setEnabled(False)
        self.radio2.setEnabled(False)
        self.radio3.setEnabled(False)
        self.myoddbutton.setEnabled(False)
        self.ownentry.clear()
        self.ownentry.setEnabled(False)
        self.unlock2button.setEnabled(False)
        self.option1button.setEnabled(False)
        self.option2button.setEnabled(False)
        self.option3button.setEnabled(False)
        self.unlock1button.setEnabled(False)
        self.submitbutton.setEnabled(True)
        self.mockentry.setEnabled(False)
        return

    def unlock2(self):
        self.ownentry.setEnabled(True)
        self.radio1.setEnabled(True)
        self.radio2.setEnabled(True)
        self.radio3.setEnabled(True)
        self.myoddbutton.setEnabled(True)
        self.option1button.setEnabled(False)
        self.option2button.setEnabled(False)
        self.option3button.setEnabled(False)
        self.bigmessage_box.setText("Insert <b>the estimated true odd</b> for any event of your choice.")
        self.unlock2button.setEnabled(False)
        self.mockentry.setEnabled(False)
        return

    def get_odd_value(self):
        try:
            home = float(self.hentry.text())
            tie = float(self.tentry.text())
            away = float(self.aentry.text())
            if (home and tie and away) > 1 and (home and tie and away) <= 1000:
                self.b = FootballEvent(home, tie, away)
                self.hentry.setEnabled(False)
                self.tentry.setEnabled(False)
                self.aentry.setEnabled(False)
                self.message_box.setText(str(self.b))
                self.ownentry.setEnabled(True)
                self.radio1.setEnabled(True)
                self.radio2.setEnabled(True)
                self.radio3.setEnabled(True)
                self.myoddbutton.setEnabled(True)
                self.bigmessage_box.setText("Insert the <b>estimated true odd</b> for any event of your choice.")
                self.unlock1button.setEnabled(True)
                self.submitbutton.setEnabled(False)
            else:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input.\nPlease enter odds between 1 and 1000.\n Remember"
                                               " to also use '.' instead of ',' as a decimal separator.")
            return

    def my_odd_button_validation(self):
        if self.radio1.isChecked():
            self.place = "h"
            self.fullplace = "Home"
            comparison_odd = self.b.home
        elif self.radio2.isChecked():
            self.place = "t"
            self.fullplace = "Tie"
            comparison_odd = self.b.tie
        elif self.radio3.isChecked():
            self.place = "a"
            self.fullplace = "Away"
            comparison_odd = self.b.away

        try:
            self.my_odd = float(self.ownentry.text())
            if 1 < self.my_odd <= 1000 and self.my_odd < comparison_odd:
                self.option1button.setEnabled(True)
                self.ownentry.setEnabled(False)
                self.radio1.setEnabled(False)
                self.radio2.setEnabled(False)
                self.radio3.setEnabled(False)
                self.unlock2button.setEnabled(True)
                self.myoddbutton.setEnabled(False)
                self.mockentry.setEnabled(True)
                current_text = self.bigmessage_box.toHtml()
                self.new_text = (f"{current_text}\n{self.dashspace}\nYour estimated true odd for the <u>'{self.fullplace}'</u> option is "
                                 f"<b>{self.my_odd}</b>, instead of the booker's estimation of "
                                 f"<b>{comparison_odd}</b>.\n{self.dashspace}\n{self.prompt}")
                self.bigmessage_box.setHtml(self.new_text)

            elif 1 < self.my_odd <= 1000 and self.my_odd >= comparison_odd:
                QMessageBox.warning(self, "Error",
                                    "No luck in this betting option! Try something else.\nYou need to choose"
                                    " odds smaller than the offered odds by the booker.")
            else:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input.\nPlease enter your odds estimation between 1"
                                               " and 1000.\n Remember to also use '.' instead of ',' "
                                               "as a decimal separator.")
            return

    def option1(self):
        games, wins = self.b.n_of_bets_for_profit(self.my_odd, self.place)
        self.bigmessage_box.setHtml(
            f"{self.new_text}\n{self.dashspace}\nTo not lose your betting money on the long run for a <b>{self.my_odd}</b> odd on the "
            f"<b>{self.fullplace}</b> option, you need to play at least <b>{games}</b> similar games. "
            f"In these games, you'll achieve the minimum number of required <b>{wins}</b> wins to get profit (or go equal)"
            f" with a confidence of at least <b>95%</b>.")

    def option2(self):
        result = self.b.set_games_profit_scenarios(self.my_odd, self.place, self.mockgames)
        new_result = "<br>".join(map(str, result))
        self.bigmessage_box.setHtml(self.new_text + f"\n{self.dashspace}\n" + new_result)

    def option3(self):
        self.get_mockgames()
        self.b.estimated_wins_for_set_games(self.my_odd, self.mockgames)
        self.bigmessage_box.setHtml(
            self.new_text + f"\n{self.dashspace}\n" + self.b.estimated_wins_for_set_games(self.my_odd, self.mockgames))

    def get_mockgames(self):
        try:
            self.mockgames = int(self.mockentry.text())
            if 0 < self.mockgames <= 10000:
                self.mockentry.setEnabled(False)
                self.mockresetbutton.setEnabled(True)
                self.option2button.setEnabled(True)
                self.option3button.setEnabled(True)
                return True
            else:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input.\nPlease enter a number between 1 and 10000.")
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
