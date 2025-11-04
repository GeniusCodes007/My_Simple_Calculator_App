from  main_running_files.ui_basic_calculator_app import Ui_MainWindow
from formulasAndFunctions.advanced_basic_methods import AdvancedBasicMethods
from formulasAndFunctions.basic_frequent_functions import BasicFrequentFunctions
from formulasAndFunctions.trig_methods import TrigMethods, Inverse

class Solving(Ui_MainWindow):
    operator = ""
    val_1 = ""
    val_2 = ""
    answer = ""

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

            elif self.operator == "^3":
                if self.val_2 == 0:
                    val_to_use = 1
                else:
                    val_to_use = self.val_2
                self.input_display.setText(f"{self.val_1}\u00B3")
                self.number_input.setText(f"{val_to_use}")
                self.answer = val_to_use * BasicFrequentFunctions().cube(self.val_1)

            elif self.operator == "^2":
                if self.val_2 == 0:
                    val_to_use = 1
                else:
                    val_to_use = self.val_2
                self.input_display.setText(f"{self.val_1}\u00B2")
                self.number_input.setText(f"{val_to_use}")
                self.answer = val_to_use * BasicFrequentFunctions().square(self.val_1)

            elif self.operator == "√":
                if self.val_2 == 0:
                    val_to_use = 1
                else:
                    val_to_use = self.val_2
                self.input_display.setText(f"{self.operator}({self.val_1})")
                self.number_input.setText(f"{val_to_use}")
                self.answer = val_to_use * BasicFrequentFunctions().square_root(self.val_1)

            elif self.operator == "3√":
                if self.val_2 == 0:
                    val_to_use = 1
                else:
                    val_to_use = self.val_2
                self.input_display.setText(F"{self.operator}({self.val_1})")
                self.number_input.setText(f"{val_to_use}")
                self.answer = val_to_use * BasicFrequentFunctions().cube_root(self.val_1)

    #Yet to touch
            elif self.operator == "sin":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} sin({self.val_2})")
                self.answer = TrigMethods().sine(self.val_2) * self.val_1
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            elif self.operator == "cos":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} cos({self.val_2})")
                self.answer = TrigMethods().cos(self.val_2) *self.val_1
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            elif self.operator == "tan":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} tan({self.val_2})")
                self.answer = TrigMethods().tan(self.val_2) *self.val_1
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            elif self.operator == "arc_sine":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} sin({self.val_2})-1")
                self.answer = self.val_1 * Inverse().arc_sine(self.val_2)
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            elif self.operator == "arc_cos":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} cos({self.val_2})-1")
                self.answer = self.val_1 * Inverse().arc_cosine(self.val_2)
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            elif self.operator == "arc_tan":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"{self.val_1} tan({self.val_2})-1")
                self.answer = self.val_1 * Inverse().arc_tangent(self.val_2)
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            #OUTSTANDINGS


            elif self.operator == "fact":
                self.val_2 = float(self.number_input.text())
                self.input_display.setText(f"fact({self.val_1})")
                self.answer = AdvancedBasicMethods().factorial(self.val_1)
                self.result_display.display(f"{self.answer:.5f}")
                self.number_input.setText(f"{self.answer:.5f}")

            self.result_display.display(f"{self.answer}")
            self.input_display.setText(f"{self.answer}")
            self.number_input.setText(f"0")

        except ValueError:
            self.result_display.display(f"0")
            self.input_display.setText(f"0")
            self.number_input.setText(f"0")