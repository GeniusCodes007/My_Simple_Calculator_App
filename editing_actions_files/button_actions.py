from PySide6.QtGui import QFont

from main_running_files.ui_basic_calculator_app import Ui_MainWindow
from formulasAndFunctions.trig_methods import TrigMethods, Inverse
from formulasAndFunctions.advanced_basic_methods import AdvancedBasicMethods
from formulasAndFunctions.basic_frequent_functions import BasicFrequentFunctions



class ButtonActions(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.operator = ""
        self.val_1 = ""
        self.val_2 = ""
        self.answer = ""

        my_font = QFont()
        my_font.setPointSize(10)
        my_font.setBold(True)




    def clear(self):
        self.number_input.setText(f"0")
        self.input_display.setText(f"0")
        self.pushButton_dot.setEnabled(True)

    def delete(self):
        self.number_input.backspace()

#Most Basic Buttons Operations
    def plus_button(self):
        self.operator = "+"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def minus_button(self):
        self.operator = "-"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def multiply_button(self):
        self.operator = "*"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def divide_button(self):
        self.operator = "/"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def percentage_button(self):
        self.operator = "%"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def raise_to_power_button(self):
        self.operator = "^"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def roots_button(self):
        self.operator = "\u221A"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{self.number_input.text()} {self.operator}")
        else:
            self.input_display.setText(F"{self.input_display.text()} {self.operator}")
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

#More Complex Buttons Operations
    def cube_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{BasicFrequentFunctions().cube(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{BasicFrequentFunctions().cube(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{BasicFrequentFunctions().cube(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)

    def square_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{BasicFrequentFunctions().square(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{BasicFrequentFunctions().square(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{BasicFrequentFunctions().square(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)

    def reciprocal_button(self):
        self.operator = "1/n"
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{BasicFrequentFunctions().recip(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{BasicFrequentFunctions().recip(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{BasicFrequentFunctions().recip(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)
    
    def cube_root_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{BasicFrequentFunctions().cube_root(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{BasicFrequentFunctions().cube_root(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{BasicFrequentFunctions().cube_root(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)
    
    def square_root_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{BasicFrequentFunctions().square_root(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{BasicFrequentFunctions().square_root(float(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{BasicFrequentFunctions().square_root(float(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)

    def factorial_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{AdvancedBasicMethods().factorial(int(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{AdvancedBasicMethods().factorial(int(self.number_input.text()))}")
        else:
            self.input_display.setText(F"{AdvancedBasicMethods().factorial(int(self.input_display.text()[0: len(self.input_display.text()) -1]))}")
        
        self.pushButton_dot.setEnabled(True)

    def permutate_button(self):
        pass

    def combine_button(self):
        pass


#NOT YET TOUCHED
    def sine_button(self):
        if self.input_display.text() == "0":
            self.input_display.setText(f"{TrigMethods().sine(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0":
            self.number_input.setText(f"{TrigMethods().sine(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)

    def cos_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{TrigMethods().cos(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{TrigMethods().cos(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)

    def tan_button(self):
        if self.input_display.text() == "0" or self.input_display.text() == "":
            self.input_display.setText(f"{TrigMethods().tan(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0" and self.number_input.text() != "0":
            self.number_input.setText(f"{TrigMethods().tan(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)

    def arc_sine_button(self):
        if self.input_display.text() == "0":
            self.input_display.setText(f"{Inverse().arc_sine(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0":
            self.number_input.setText(f"{Inverse().arc_sine(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)

    def arc_cos_button(self):
        if self.input_display.text() == "0":
            self.input_display.setText(f"{Inverse().arc_cosine(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0":
            self.number_input.setText(f"{Inverse().arc_cosine(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)

    def arc_tan_button(self):
        if self.input_display.text() == "0":
            self.input_display.setText(f"{Inverse().arc_tangent(float(self.number_input.text()))}")
            self.number_input.setText(F"0")
        elif self.input_display.text() != "0":
            self.number_input.setText(f"{Inverse().arc_tangent(float(self.number_input.text()))}")
        
        self.pushButton_dot.setEnabled(True)


#OUTSTANDINGS
    def what_percent_button(self):
        self.operator = "what"
        self.input_display.setText(F"{self.number_input.text()} {self.operator}")
        self.val_1 = float(self.number_input.text())
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)

    def absolute_button(self):
        self.operator = "abs"
        self.input_display.setText(f"abs({self.number_input.text()})")
        self.val_1 = float(self.number_input.text())
        self.number_input.setText(F"0")
        self.pushButton_dot.setEnabled(True)


# Non-Arithmetical Buttons
    #def clear_history(self):


