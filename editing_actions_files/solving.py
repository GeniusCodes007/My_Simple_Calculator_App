
from editing_actions_files.button_actions import *
from PySide6.QtWidgets import QLabel

class Solving(ButtonActions):

    operator = ""
    val_1 = ""
    val_2 = ""
    answer = ""
    position = 0

    def one(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"1")
        else:
            self.number_input.setText(f"{self.number_input.text()}1")

    def two(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"2")
        else:
            self.number_input.setText(f"{self.number_input.text()}2")

    def three(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"3")
        else:
            self.number_input.setText(f"{self.number_input.text()}3")

    def four(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"4")
        else:
            self.number_input.setText(f"{self.number_input.text()}4")

    def five(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"5")
        else:
            self.number_input.setText(f"{self.number_input.text()}5")

    def six(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"6")
        else:
            self.number_input.setText(f"{self.number_input.text()}6")

    def seven(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"7")
        else:
            self.number_input.setText(F"{self.number_input.text()}7")

    def eight(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"8")
        else:
            self.number_input.setText(F"{self.number_input.text()}8")

    def nine(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"9")
        else:
            self.number_input.setText(F"{self.number_input.text()}9")

    def zero(self):
        if self.number_input.text() == "0" or self.number_input.text() == "":
            self.number_input.setText(f"0")
        else:
            self.number_input.setText(f"{self.number_input.text()}0")

    def dot(self):
        self.number_input.setText(F"{self.number_input.text()}.")
        self.pushButton_dot.setEnabled(False)



    def ans(self):
        try:
            self.val_1 = float(self.input_display.text()[0: len(self.input_display.text()) -1])
            self.val_2 = float(self.number_input.text())

            if self.operator == "+": self.answer = BasicFrequentFunctions().add(self.val_1, self.val_2)

            elif self.operator == "-": self.answer = BasicFrequentFunctions().difference(self.val_1, self.val_2)

            elif self.operator == "*": self.answer = BasicFrequentFunctions().multiply(self.val_1, self.val_2)

            elif self.operator == "/": self.answer = BasicFrequentFunctions().divide(self.val_1, self.val_2)

            elif self.operator == "%": self.answer = BasicFrequentFunctions().percentage(self.val_1, self.val_2)

            elif self.operator == "^": self.answer = BasicFrequentFunctions().raise_to_power(self.val_1, self.val_2)

            elif self.operator == "r": self.answer = AdvancedBasicMethods().roots(self.val_1, int(self.val_2))

            elif self.operator == "p": self.answer = AdvancedBasicMethods().permutate(int(self.val_1), int(self.val_2))

            elif self.operator == "c": self.answer = AdvancedBasicMethods().combine(int(self.val_1), int(self.val_2))

            my_font = QFont()
            my_font.setPointSize(10)
            my_font.setBold(True)

            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName("answer_label")
            label.setFont(my_font)

            label.setText(f"{self.input_display.text()} {self.number_input.text()} = {self.answer}")
            label.adjustSize()
            self.result_display.display(f"{self.answer}")
            self.input_display.setText(f"0")
            self.number_input.setText(f"0")
            self.gridLayout.addWidget(label, self.position, 0)
            self.position = self.position + 1

        except ValueError:
            self.result_display.display(f"You May Have Given The Wrong Inputs")
            self.input_display.setText(f"0")
            self.number_input.setText(f"0")