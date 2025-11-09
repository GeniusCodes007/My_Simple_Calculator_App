from editing_actions_files.solving import *
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtGui import QIcon

class CalculatorFirst( QMainWindow, Solving):
    def __init__(self):
        super(CalculatorFirst, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon("calc_icon.jpg"))

        self.pushButton_permutation.setText(f"P\u207F\u1D63")
        self.pushButton_combination.setText(f"C\u207F\u1D63")
        self.pushButton_cube_root.setText(f"\u00B3\u221Ay")
        self.pushButton_square_root.setText(f"\u00B2\u221Ay")
        self.pushButton_square.setText(f"y\u00B2")
        self.pushButton_cube.setText(f"y\u00B3")
        self.pushButton_sine.setText(f"Sin(y)")
        self.pushButton_cosine.setText(f"Cos(y)")
        self.pushButton_tangent.setText(f"Tan(y)")
        self.pushButton_arc_sine.setText(f"Sin(y)\u207B\u00B9")
        self.pushButton_arc_cosine.setText(f"Cos(y)\u207B\u00B9")
        self.pushButton_arc_tan.setText(f"Tan(y)\u207B\u00B9")
        self.pushButton_root.setText(f"\u207F\u221Ay")
        self.pushButton_raise_to_power.setText(f"y\u207F")
        self.pushButton_factorial.setText(f"n!")
        self.pushButton_reciprocal.setText(f"1/n")
        self.pushButton_percent.setText(f"%")
        self.pushButton_delete.setText(f"Del")
        self.pushButton_clear.setText(f"C")
        self.show_history.setText("History")

        self.number_input.setText(f"0")
        self.input_display.setText(f"0")
        self.result_display.display(f"0")

        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_clear.clicked.connect(self.clear)

        self.pushButton_one.clicked.connect(self.one)
        self.pushButton_two.clicked.connect(self.two)
        self.pushButton_three.clicked.connect(self.three)
        self.pushButton_four.clicked.connect(self.four)
        self.pushButton_five.clicked.connect(self.five)
        self.pushButton_six.clicked.connect(self.six)
        self.pushButton_seven.clicked.connect(self.seven)
        self.pushButton_eight.clicked.connect(self.eight)
        self.pushButton_nine.clicked.connect(self.nine)
        self.pushButton_zero.clicked.connect(self.zero)

        self.pushButton_dot.clicked.connect(self.dot)

        self.pushButton_plus.clicked.connect(self.plus_button)
        self.pushButton_minus.clicked.connect(self.minus_button)
        self.pushButton_multiply.clicked.connect(self.multiply_button)
        self.pushButton_divide.clicked.connect(self.divide_button)
        self.pushButton_percent.clicked.connect(self.percentage_button)
        self.pushButton_raise_to_power.clicked.connect(self.raise_to_power_button)
        self.pushButton_root.clicked.connect(self.roots_button)
        self.pushButton_cube.clicked.connect(self.cube_button)
        self.pushButton_cube_root.clicked.connect(self.cube_root_button)
        self.pushButton_square.clicked.connect(self.square_button)
        self.pushButton_square_root.clicked.connect(self.square_root_button)
        self.pushButton_reciprocal.clicked.connect(self.reciprocal_button)
        self.pushButton_sine.clicked.connect(self.sine_button)
        self.pushButton_cosine.clicked.connect(self.cos_button)
        self.pushButton_tangent.clicked.connect(self.tan_button)
        self.pushButton_arc_sine.clicked.connect(self.arc_sine_button)
        self.pushButton_arc_cosine.clicked.connect(self.arc_cos_button)
        self.pushButton_arc_tan.clicked.connect(self.arc_tan_button)
        self.pushButton_factorial.clicked.connect(self.factorial_button)
        self.pushButton_permutation.clicked.connect(self.permutate_button)
        self.pushButton_combination.clicked.connect(self.combine_button)

        self.pushButton_equal_to.clicked.connect(self.ans)

        self.pushButton_hide.clicked.connect(self.hide_button)
        self.show_history.clicked.connect(self.show_button)

    def hide_button(self):
        self.historyFrame.hide()

    def show_button(self):
        self.historyFrame.show()

import sys
app = QApplication()
window = CalculatorFirst()
window.show()
sys.exit(app.exec())