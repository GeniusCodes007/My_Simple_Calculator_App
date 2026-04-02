from PySide6.QtGui import QFont
from actions_files.non_numeric_operations.non_numeric_operations_buttons_actions import \
    Non_Numeric_Operations_Button_Actions, Operator, Answer # , Operator
from formulasAndFunctions.trig_methods import TrigMethods, Inverse
from formulasAndFunctions.calculator_mathematical_functions import Calculator_Mathematical_Functions




class ButtonActions(Non_Numeric_Operations_Button_Actions):
    def __init__(self):
        super().__init__()
        self.operator:Operator = Operator("+")
        self.val_1 = ""
        self.val_2 = ""
        self.answer = ""

        my_font = QFont()
        my_font.setPointSize(10)
        my_font.setBold(True)



#Most Basic Buttons Operations
    def plus_button(self):
        self.operator:Operator = Operator("+")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(
                    F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def minus_button(self):
        self.operator:Operator = Operator("-")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")
        self.number_input.setText(F"0")


    def multiply_button(self):
        self.operator:Operator = Operator("*")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def divide_button(self):
        self.operator:Operator = Operator("/")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def percentage_button(self):
        self.operator:Operator = Operator("%")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def raise_to_power_button(self):
        self.operator:Operator = Operator("^")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def roots_button(self):
        self.operator:Operator = Operator("\u221A")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def permutate_button(self):
        self.operator:Operator = Operator("p")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


    def combine_button(self):
        self.operator:Operator = Operator("c")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")

    def what_percent_button(self):
        self.operator:Operator = Operator("?")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator.operator_symbol}")
        else:
            if self.input_display.text()[len(self.input_display.text()) - 1] in self.operator.operators:
                self.input_display.setText(
                    F"{self.input_display.text().replace(self.input_display.text()[len(self.input_display.text()) - 1], self.operator.operator_symbol)}")

        self.number_input.setText(F"0")


#More Complex Buttons Operations
    def cube_button(self):
        my_answer = Answer(Calculator_Mathematical_Functions().cube(float(self.number_input.text())))
        my_answer.add_to_history(f"{self.number_input.text()}\u00B3")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{my_answer.answer}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{my_answer.answer}")
        else:
            self.input_display.setText(F"{Calculator_Mathematical_Functions().cube(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def square_button(self):
        my_answer = Answer(Calculator_Mathematical_Functions().square(float(self.number_input.text())))
        my_answer.add_to_history(f"{self.number_input.text()}\u00B2")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{Calculator_Mathematical_Functions().square(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{Calculator_Mathematical_Functions().square(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{Calculator_Mathematical_Functions().square(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def reciprocal_button(self):
        my_answer=Answer(Calculator_Mathematical_Functions().recip(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"1/{self.number_input.text()} = ")
            self.input_display.setText(f"{Calculator_Mathematical_Functions().recip(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"1/{self.number_input.text()} = ")
            self.number_input.setText(f"{Calculator_Mathematical_Functions().recip(float(self.number_input.text()))}")
        else:
            my_answer.add_to_history(f"1/{self.number_input.text()} = ")
            self.input_display.setText(F"{Calculator_Mathematical_Functions().recip(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def cube_root_button(self):
        my_answer=Answer(Calculator_Mathematical_Functions().cube_root(float(self.number_input.text())))

        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"\u00B3\u221A{self.number_input.text()} = ")
            self.input_display.setText(f"{Calculator_Mathematical_Functions().cube_root(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"\u00B3\u221A{self.number_input.text()} = ")
            self.number_input.setText(f"{Calculator_Mathematical_Functions().cube_root(float(self.number_input.text()))}")
        else:
            my_answer.add_to_history(f"\u00B3\u221A{self.number_input.text()} = ")
            self.input_display.setText(F"{Calculator_Mathematical_Functions().cube_root(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def square_root_button(self):
        my_answer=Answer(Calculator_Mathematical_Functions().square_root(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"\u00B2\u221A{self.number_input.text()} = ")
            self.input_display.setText(f"{Calculator_Mathematical_Functions().square_root(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"\u00B2\u221A{self.number_input.text()} = ")
            self.number_input.setText(f"{Calculator_Mathematical_Functions().square_root(float(self.number_input.text()))}")
        else:
            my_answer.add_to_history(f"\u00B2\u221A{self.number_input.text()} = ")
            self.input_display.setText(F"{Calculator_Mathematical_Functions().square_root(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def factorial_button(self):
        my_answer=Answer(Calculator_Mathematical_Functions().factorial(int(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"{self.number_input.text()}! = ")
            self.input_display.setText(f"{Calculator_Mathematical_Functions().factorial(int(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"{self.number_input.text()}! = ")
            self.number_input.setText(f"{Calculator_Mathematical_Functions().factorial(int(self.number_input.text()))}")
        else:
            my_answer.add_to_history(f"{self.number_input.text()}! = ")
            self.input_display.setText(F"{Calculator_Mathematical_Functions().factorial(int(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        self.display_on_history_table()

    def sine_button(self):
        my_answer=Answer(TrigMethods().sine(float(self.number_input.text())))
        if self.input_display.text() == "0":
            my_answer.add_to_history(f"Sine({self.number_input.text()}) = ")
            self.input_display.setText(f"{TrigMethods().sine(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0":
            my_answer.add_to_history(f"Sine({self.number_input.text()}) = ")
            self.number_input.setText(f"{TrigMethods().sine(float(self.number_input.text()))}")
        self.display_on_history_table()

    def cos_button(self):
        my_answer=Answer(TrigMethods().cos(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"Cos({self.number_input.text()}) = ")
            self.input_display.setText(f"{TrigMethods().cos(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"Cos({self.number_input.text()}) = ")
            self.number_input.setText(f"{TrigMethods().cos(float(self.number_input.text()))}")
        self.display_on_history_table()

    def tan_button(self):
        my_answer=Answer(TrigMethods().tan(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"Tan({self.number_input.text()}) = ")
            self.input_display.setText(f"{TrigMethods().tan(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"Tan({self.number_input.text()}) = ")
            self.number_input.setText(f"{TrigMethods().tan(float(self.number_input.text()))}")
        self.display_on_history_table()

    def arc_sine_button(self):
        my_answer=Answer(Inverse().arc_sine(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"Sin({self.number_input.text()})\u207B\u00B9 = ")
            if type(my_answer.answer) == int|float :
                self.input_display.setText(f"{Inverse().arc_sine(float(self.number_input.text()))}")
            else:
                self.input_display.setText("0")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"Sin({self.number_input.text()})\u207B\u00B9 = ")
            self.number_input.setText(f"{Inverse().arc_sine(float(self.number_input.text()))}")
        self.display_on_history_table()

    def arc_cos_button(self):
        my_answer=Answer(Inverse().arc_cosine(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"Cos({self.number_input.text()})\u207B\u00B9 = ")
            self.input_display.setText(f"{Inverse().arc_cosine(float(self.number_input.text()))}")
            if type(my_answer.answer) == int|float :
                self.input_display.setText(f"{Inverse().arc_cosine(float(self.number_input.text()))}")
            else:
                self.input_display.setText("0")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"Cos({self.number_input.text()})\u207B\u00B9 = ")
            self.number_input.setText(f"{Inverse().arc_cosine(float(self.number_input.text()))}")
        self.display_on_history_table()

    def arc_tan_button(self):
        my_answer=Answer(Inverse().arc_tangent(float(self.number_input.text())))
        if self.input_display.text() == "0" or self.input_display.text() == "":
            my_answer.add_to_history(f"Tan({self.number_input.text()})\u207B\u00B9 = ")
            self.input_display.setText(f"{Inverse().arc_tangent(float(self.number_input.text()))}")
            if type(my_answer.answer) == int|float :
                self.input_display.setText(f"{Inverse().arc_tangent(float(self.number_input.text()))}")
            else:
                self.input_display.setText("0")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            my_answer.add_to_history(f"Tan({self.number_input.text()})\u207B\u00B9 = ")
            self.number_input.setText(f"{Inverse().arc_tangent(float(self.number_input.text()))}")
        self.display_on_history_table()


#OUTSTANDINGS



    def absolute_button(self):
        my_answer = Answer(abs(float(self.number_input.text())))
        my_answer.add_to_history(f"abs({self.number_input.text()})")
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{my_answer.answer}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{my_answer.answer}")
        else:
            self.input_display.setText(
                F"{abs(float(self.input_display.text()[0: len(self.input_display.text()) - 1]))}")
        self.display_on_history_table()

