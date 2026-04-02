
from in_app_database.database_operations import add_to_history
from actions_files.button_actions import ButtonActions
from formulasAndFunctions.calculator_mathematical_functions import Calculator_Mathematical_Functions


class Solving(ButtonActions):


    def one(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"1")
        else:
            self.number_input.setText(f"{self.number_input.text()}1")

    def two(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"2")
        else:
            self.number_input.setText(f"{self.number_input.text()}2")

    def three(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"3")
        else:
            self.number_input.setText(f"{self.number_input.text()}3")

    def four(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"4")
        else:
            self.number_input.setText(f"{self.number_input.text()}4")

    def five(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"5")
        else:
            self.number_input.setText(f"{self.number_input.text()}5")

    def six(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"6")
        else:
            self.number_input.setText(f"{self.number_input.text()}6")

    def seven(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"7")
        else:
            self.number_input.setText(F"{self.number_input.text()}7")

    def eight(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"8")
        else:
            self.number_input.setText(F"{self.number_input.text()}8")

    def nine(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"9")
        else:
            self.number_input.setText(F"{self.number_input.text()}9")

    def zero(self):
        if self.number_input.text() == "0" or self.number_input.text() == "" or self.number_input.text() == "0.0":
            self.number_input.setText(f"0")
        else:
            self.number_input.setText(f"{self.number_input.text()}0")

    def dot(self):
        if "."  not in self.number_input.text():
            self.number_input.setText(F"{self.number_input.text()}.")


    def ans(self):
        try:
            self.val_1 = float(self.input_display.text()[0: len(self.input_display.text()) -1])
            self.val_2 = float(self.number_input.text())

            if self.operator == "+": self.answer = Calculator_Mathematical_Functions().add(self.val_1, self.val_2)

            elif self.operator == "-": self.answer = Calculator_Mathematical_Functions().difference(self.val_1, self.val_2)

            elif self.operator == "*": self.answer = Calculator_Mathematical_Functions().multiply(self.val_1, self.val_2)

            elif self.operator == "/": self.answer = Calculator_Mathematical_Functions().divide(self.val_1, self.val_2)

            elif self.operator == "%": self.answer = Calculator_Mathematical_Functions().percentage(self.val_1, self.val_2)

            elif self.operator == "^": self.answer = Calculator_Mathematical_Functions().raise_to_power(self.val_1, self.val_2)

            elif self.operator == "\u221A": self.answer = Calculator_Mathematical_Functions().roots(int(self.val_1), self.val_2)

            elif self.operator == "p": self.answer = Calculator_Mathematical_Functions().permutate(int(self.val_1), int(self.val_2))

            elif self.operator == "c": self.answer = Calculator_Mathematical_Functions().combine(int(self.val_1), int(self.val_2))

            add_to_history(f"{self.input_display.text()} {self.number_input.text()} = ",
                           f"{self.answer}")
            self.display_on_history_table()

            self.result_display.setText(f"{self.answer}")
            self.input_display.setText(f"0")
            self.number_input.setText(f"0")

        except ValueError:
            self.result_display.setText(f"------------")
            self.input_display.setText(f"0")
            self.number_input.setText(f"0")