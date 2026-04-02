

from in_app_database.database_operations import get_all_history, delete_all_history, app_conn, app_conn_cursor
from ui_python_content.ui_basic_calculator_app import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

class Answer:
    def __init__(self, answer:int|float|str):
        self.answer = answer

    def check_answer(self):
        if type(self.answer) == str:
            return False
        return True

    # ADD TO HISTORY
    def add_to_history(self,statement: str):
        app_conn_cursor.execute("""
        INSERT INTO calc_history (statement, result) VALUES (?, ?)""",
                                (statement, self.answer))
        app_conn.commit()

class Operator:

    operators=["+", "-", "*", "/", "%", "^", "\u221A", "p", "c", "?"]

    def __init__(self, operator_symbol: str):
        self.operator_symbol = operator_symbol

    def check_operator(self):
        if self.operator_symbol not in self.operators:
            return False
        return True

class Numeric_Character(object):

    def __init__(self, character:int):
        self.character = character

    numeric_characters=[1,2,3,4,5,6,7,8,9,0]

    def check_numeric_character(self):
        if self.character not in self.numeric_characters:
            return False
        return True

class Non_Numeric_Operations_Button_Actions(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # CLEAR INPUT
    def clear_input(self):
        self.number_input.setText(f"0")
        self.input_display.setText(f"0")
        self.pushButton_dot.setEnabled(True)

    # DELETE INPUT
    def delete_input(self):
        self.number_input.backspace()

    # HIDE HISTORY
    def hide_history_button(self):
        self.historyFrame.setVisible(False)
        self.show_history.setVisible(True)

    # SHOW HISTORY
    def show_history_button(self):
        self.historyFrame.setVisible(True)

    # CLEAR HISTORY
    def clear_history_button(self):
        delete_all_history()
        self.display_on_history_table()

    def display_on_history_table(self):
        self.history_tableWidget.setRowCount(len(get_all_history()))
        for num in range(len(get_all_history())):
            self.history_tableWidget.setItem(num, 0, QTableWidgetItem(str(get_all_history()[num][0])))
            self.history_tableWidget.setItem(num, 1, QTableWidgetItem(str(get_all_history()[num][1])))

    def check_character(self, character:Operator):
        if character in self.input_display.text():
            return True
        return False
