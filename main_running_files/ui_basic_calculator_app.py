# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_calculator_appsNBobY.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import my_calc_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(931, 551)
        MainWindow.setMinimumSize(QSize(440, 467))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(170, 170, 127);\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QSize(30, 24))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainCalculatorFrame = QFrame(self.centralwidget)
        self.mainCalculatorFrame.setObjectName(u"mainCalculatorFrame")
        self.mainCalculatorFrame.setMinimumSize(QSize(694, 533))
        self.mainCalculatorFrame.setMaximumSize(QSize(1000, 1000))
        self.mainCalculatorFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.mainCalculatorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainCalculatorFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.displayFrame = QFrame(self.mainCalculatorFrame)
        self.displayFrame.setObjectName(u"displayFrame")
        self.displayFrame.setStyleSheet(u"\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLCDNumber{\n"
"border-radius: 5px;\n"
"}")
        self.displayFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.displayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.displayFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_display = QLineEdit(self.displayFrame)
        self.input_display.setObjectName(u"input_display")
        self.input_display.setEnabled(False)
        self.input_display.setMinimumSize(QSize(379, 22))
        self.input_display.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.input_display.setFont(font)
        self.input_display.setStyleSheet(u"\n"
"background-color: rgb(206, 255, 240);")

        self.verticalLayout.addWidget(self.input_display)

        self.number_input = QLineEdit(self.displayFrame)
        self.number_input.setObjectName(u"number_input")
        self.number_input.setEnabled(True)
        self.number_input.setMinimumSize(QSize(379, 22))
        self.number_input.setMaximumSize(QSize(16777215, 16777215))
        self.number_input.setFont(font)
        self.number_input.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.number_input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhFormattedNumbersOnly|Qt.InputMethodHint.ImhPreferNumbers)

        self.verticalLayout.addWidget(self.number_input)

        self.result_display = QLCDNumber(self.displayFrame)
        self.result_display.setObjectName(u"result_display")
        self.result_display.setMinimumSize(QSize(331, 23))
        self.result_display.setMaximumSize(QSize(16777215, 23))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.result_display.setFont(font1)
        self.result_display.setStyleSheet(u"background-color: rgb(217, 245, 255);\n"
"font: 700 10pt \"Times New Roman\";")
        self.result_display.setFrameShape(QFrame.Shape.WinPanel)
        self.result_display.setLineWidth(0)
        self.result_display.setMidLineWidth(10)
        self.result_display.setDigitCount(25)
        self.result_display.setProperty(u"value", 0.000000000000000)

        self.verticalLayout.addWidget(self.result_display)


        self.verticalLayout_3.addWidget(self.displayFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.buttonHousingFrame = QFrame(self.mainCalculatorFrame)
        self.buttonHousingFrame.setObjectName(u"buttonHousingFrame")
        self.buttonHousingFrame.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: rgb(170, 170, 127);\n"
"}")
        self.buttonHousingFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.buttonHousingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.buttonHousingFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.firstRowFrame = QFrame(self.buttonHousingFrame)
        self.firstRowFrame.setObjectName(u"firstRowFrame")
        self.firstRowFrame.setMinimumSize(QSize(652, 59))
        self.firstRowFrame.setFrameShape(QFrame.Shape.Box)
        self.firstRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.firstRowFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_permutation = QPushButton(self.firstRowFrame)
        self.pushButton_permutation.setObjectName(u"pushButton_permutation")
        self.pushButton_permutation.setMinimumSize(QSize(61, 41))
        self.pushButton_permutation.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setItalic(True)
        self.pushButton_permutation.setFont(font2)
        self.pushButton_permutation.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pushButton_permutation.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.pushButton_permutation)

        self.pushButton_combination = QPushButton(self.firstRowFrame)
        self.pushButton_combination.setObjectName(u"pushButton_combination")
        self.pushButton_combination.setMinimumSize(QSize(61, 41))
        self.pushButton_combination.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_combination.setFont(font2)
        self.pushButton_combination.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_8.addWidget(self.pushButton_combination)

        self.pushButton_factorial = QPushButton(self.firstRowFrame)
        self.pushButton_factorial.setObjectName(u"pushButton_factorial")
        self.pushButton_factorial.setMinimumSize(QSize(61, 41))
        self.pushButton_factorial.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_factorial.setFont(font2)
        self.pushButton_factorial.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_8.addWidget(self.pushButton_factorial)

        self.pushButton_reciprocal = QPushButton(self.firstRowFrame)
        self.pushButton_reciprocal.setObjectName(u"pushButton_reciprocal")
        self.pushButton_reciprocal.setMinimumSize(QSize(61, 41))
        self.pushButton_reciprocal.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_reciprocal.setFont(font2)
        self.pushButton_reciprocal.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pushButton_reciprocal.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_reciprocal)

        self.pushButton_raise_to_power = QPushButton(self.firstRowFrame)
        self.pushButton_raise_to_power.setObjectName(u"pushButton_raise_to_power")
        self.pushButton_raise_to_power.setMinimumSize(QSize(61, 41))
        self.pushButton_raise_to_power.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_raise_to_power.setFont(font2)
        self.pushButton_raise_to_power.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_8.addWidget(self.pushButton_raise_to_power)


        self.verticalLayout_2.addWidget(self.firstRowFrame)

        self.secondRowFrame = QFrame(self.buttonHousingFrame)
        self.secondRowFrame.setObjectName(u"secondRowFrame")
        self.secondRowFrame.setMinimumSize(QSize(652, 59))
        self.secondRowFrame.setFrameShape(QFrame.Shape.Box)
        self.secondRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.secondRowFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_sine = QPushButton(self.secondRowFrame)
        self.pushButton_sine.setObjectName(u"pushButton_sine")
        self.pushButton_sine.setMinimumSize(QSize(61, 41))
        self.pushButton_sine.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_sine.setFont(font2)
        self.pushButton_sine.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout.addWidget(self.pushButton_sine)

        self.pushButton_cosine = QPushButton(self.secondRowFrame)
        self.pushButton_cosine.setObjectName(u"pushButton_cosine")
        self.pushButton_cosine.setMinimumSize(QSize(61, 41))
        self.pushButton_cosine.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_cosine.setFont(font2)
        self.pushButton_cosine.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout.addWidget(self.pushButton_cosine)

        self.pushButton_tangent = QPushButton(self.secondRowFrame)
        self.pushButton_tangent.setObjectName(u"pushButton_tangent")
        self.pushButton_tangent.setMinimumSize(QSize(61, 41))
        self.pushButton_tangent.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_tangent.setFont(font2)
        self.pushButton_tangent.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout.addWidget(self.pushButton_tangent)

        self.pushButton_delete = QPushButton(self.secondRowFrame)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(61, 41))
        self.pushButton_delete.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_delete.setFont(font2)
        self.pushButton_delete.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButton_delete)

        self.pushButton_clear = QPushButton(self.secondRowFrame)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(61, 41))
        self.pushButton_clear.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_clear.setFont(font2)
        self.pushButton_clear.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_clear.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout_2.addWidget(self.secondRowFrame)

        self.thirdRowFrame = QFrame(self.buttonHousingFrame)
        self.thirdRowFrame.setObjectName(u"thirdRowFrame")
        self.thirdRowFrame.setMinimumSize(QSize(652, 59))
        self.thirdRowFrame.setFont(font2)
        self.thirdRowFrame.setFrameShape(QFrame.Shape.Box)
        self.thirdRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.thirdRowFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_arc_sine = QPushButton(self.thirdRowFrame)
        self.pushButton_arc_sine.setObjectName(u"pushButton_arc_sine")
        self.pushButton_arc_sine.setMinimumSize(QSize(61, 41))
        self.pushButton_arc_sine.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_arc_sine.setFont(font2)
        self.pushButton_arc_sine.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_arc_sine)

        self.pushButton_arc_cosine = QPushButton(self.thirdRowFrame)
        self.pushButton_arc_cosine.setObjectName(u"pushButton_arc_cosine")
        self.pushButton_arc_cosine.setMinimumSize(QSize(61, 41))
        self.pushButton_arc_cosine.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_arc_cosine.setFont(font2)
        self.pushButton_arc_cosine.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_arc_cosine)

        self.pushButton_arc_tan = QPushButton(self.thirdRowFrame)
        self.pushButton_arc_tan.setObjectName(u"pushButton_arc_tan")
        self.pushButton_arc_tan.setMinimumSize(QSize(61, 41))
        self.pushButton_arc_tan.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_arc_tan.setFont(font2)
        self.pushButton_arc_tan.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_arc_tan)

        self.pushButton_percent = QPushButton(self.thirdRowFrame)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setMinimumSize(QSize(61, 41))
        self.pushButton_percent.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_percent.setFont(font2)
        self.pushButton_percent.setStyleSheet(u"\n"
"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_percent)

        self.pushButton_square_root = QPushButton(self.thirdRowFrame)
        self.pushButton_square_root.setObjectName(u"pushButton_square_root")
        self.pushButton_square_root.setMinimumSize(QSize(61, 41))
        self.pushButton_square_root.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_square_root.setFont(font2)
        self.pushButton_square_root.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_square_root)


        self.verticalLayout_2.addWidget(self.thirdRowFrame)

        self.fourthRowFframe = QFrame(self.buttonHousingFrame)
        self.fourthRowFframe.setObjectName(u"fourthRowFframe")
        self.fourthRowFframe.setMinimumSize(QSize(652, 58))
        self.fourthRowFframe.setFrameShape(QFrame.Shape.Box)
        self.fourthRowFframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fourthRowFframe)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_seven = QPushButton(self.fourthRowFframe)
        self.pushButton_seven.setObjectName(u"pushButton_seven")
        self.pushButton_seven.setMinimumSize(QSize(61, 41))
        self.pushButton_seven.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_seven.setFont(font2)
        self.pushButton_seven.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_3.addWidget(self.pushButton_seven)

        self.pushButton_eight = QPushButton(self.fourthRowFframe)
        self.pushButton_eight.setObjectName(u"pushButton_eight")
        self.pushButton_eight.setMinimumSize(QSize(61, 41))
        self.pushButton_eight.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_eight.setFont(font2)
        self.pushButton_eight.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_3.addWidget(self.pushButton_eight)

        self.pushButton_nine = QPushButton(self.fourthRowFframe)
        self.pushButton_nine.setObjectName(u"pushButton_nine")
        self.pushButton_nine.setMinimumSize(QSize(61, 41))
        self.pushButton_nine.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_nine.setFont(font2)
        self.pushButton_nine.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_3.addWidget(self.pushButton_nine)

        self.pushButton_divide = QPushButton(self.fourthRowFframe)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setMinimumSize(QSize(61, 41))
        self.pushButton_divide.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_divide.setFont(font2)
        self.pushButton_divide.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.horizontalLayout_3.addWidget(self.pushButton_divide)

        self.pushButton_cube_root = QPushButton(self.fourthRowFframe)
        self.pushButton_cube_root.setObjectName(u"pushButton_cube_root")
        self.pushButton_cube_root.setMinimumSize(QSize(61, 41))
        self.pushButton_cube_root.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_cube_root.setFont(font2)
        self.pushButton_cube_root.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_3.addWidget(self.pushButton_cube_root)


        self.verticalLayout_2.addWidget(self.fourthRowFframe)

        self.fifthRowFrame = QFrame(self.buttonHousingFrame)
        self.fifthRowFrame.setObjectName(u"fifthRowFrame")
        self.fifthRowFrame.setMinimumSize(QSize(652, 59))
        self.fifthRowFrame.setFrameShape(QFrame.Shape.Box)
        self.fifthRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fifthRowFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_four = QPushButton(self.fifthRowFrame)
        self.pushButton_four.setObjectName(u"pushButton_four")
        self.pushButton_four.setMinimumSize(QSize(61, 41))
        self.pushButton_four.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_four.setFont(font2)
        self.pushButton_four.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_4.addWidget(self.pushButton_four)

        self.pushButton_five = QPushButton(self.fifthRowFrame)
        self.pushButton_five.setObjectName(u"pushButton_five")
        self.pushButton_five.setMinimumSize(QSize(61, 41))
        self.pushButton_five.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_five.setFont(font2)
        self.pushButton_five.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_4.addWidget(self.pushButton_five)

        self.pushButton_six = QPushButton(self.fifthRowFrame)
        self.pushButton_six.setObjectName(u"pushButton_six")
        self.pushButton_six.setMinimumSize(QSize(61, 41))
        self.pushButton_six.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_six.setFont(font2)
        self.pushButton_six.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_4.addWidget(self.pushButton_six)

        self.pushButton_multiply = QPushButton(self.fifthRowFrame)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setMinimumSize(QSize(61, 41))
        self.pushButton_multiply.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_multiply.setFont(font2)
        self.pushButton_multiply.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_multiply)

        self.pushButton_root = QPushButton(self.fifthRowFrame)
        self.pushButton_root.setObjectName(u"pushButton_root")
        self.pushButton_root.setMinimumSize(QSize(61, 41))
        self.pushButton_root.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_root.setFont(font2)
        self.pushButton_root.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_root)


        self.verticalLayout_2.addWidget(self.fifthRowFrame)

        self.sixthRowFrame = QFrame(self.buttonHousingFrame)
        self.sixthRowFrame.setObjectName(u"sixthRowFrame")
        self.sixthRowFrame.setMinimumSize(QSize(652, 59))
        self.sixthRowFrame.setFrameShape(QFrame.Shape.Box)
        self.sixthRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.sixthRowFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_one = QPushButton(self.sixthRowFrame)
        self.pushButton_one.setObjectName(u"pushButton_one")
        self.pushButton_one.setMinimumSize(QSize(61, 41))
        self.pushButton_one.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_one.setFont(font2)
        self.pushButton_one.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_5.addWidget(self.pushButton_one)

        self.pushButton_two = QPushButton(self.sixthRowFrame)
        self.pushButton_two.setObjectName(u"pushButton_two")
        self.pushButton_two.setMinimumSize(QSize(61, 41))
        self.pushButton_two.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_two.setFont(font2)
        self.pushButton_two.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_5.addWidget(self.pushButton_two)

        self.pushButton_three = QPushButton(self.sixthRowFrame)
        self.pushButton_three.setObjectName(u"pushButton_three")
        self.pushButton_three.setMinimumSize(QSize(61, 41))
        self.pushButton_three.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_three.setFont(font2)
        self.pushButton_three.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_5.addWidget(self.pushButton_three)

        self.pushButton_minus = QPushButton(self.sixthRowFrame)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setMinimumSize(QSize(61, 41))
        self.pushButton_minus.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_minus.setFont(font2)
        self.pushButton_minus.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.horizontalLayout_5.addWidget(self.pushButton_minus)

        self.pushButton_square = QPushButton(self.sixthRowFrame)
        self.pushButton_square.setObjectName(u"pushButton_square")
        self.pushButton_square.setMinimumSize(QSize(61, 41))
        self.pushButton_square.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_square.setFont(font2)
        self.pushButton_square.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_5.addWidget(self.pushButton_square)


        self.verticalLayout_2.addWidget(self.sixthRowFrame)

        self.seventhRowFrame = QFrame(self.buttonHousingFrame)
        self.seventhRowFrame.setObjectName(u"seventhRowFrame")
        self.seventhRowFrame.setMinimumSize(QSize(652, 58))
        self.seventhRowFrame.setFrameShape(QFrame.Shape.Box)
        self.seventhRowFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.seventhRowFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_zero = QPushButton(self.seventhRowFrame)
        self.pushButton_zero.setObjectName(u"pushButton_zero")
        self.pushButton_zero.setMinimumSize(QSize(61, 41))
        self.pushButton_zero.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_zero.setFont(font2)
        self.pushButton_zero.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_6.addWidget(self.pushButton_zero)

        self.pushButton_dot = QPushButton(self.seventhRowFrame)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setMinimumSize(QSize(61, 41))
        self.pushButton_dot.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_dot.setFont(font2)
        self.pushButton_dot.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_6.addWidget(self.pushButton_dot)

        self.pushButton_equal_to = QPushButton(self.seventhRowFrame)
        self.pushButton_equal_to.setObjectName(u"pushButton_equal_to")
        self.pushButton_equal_to.setMinimumSize(QSize(61, 41))
        self.pushButton_equal_to.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_equal_to.setFont(font2)
        self.pushButton_equal_to.setStyleSheet(u"background-color: rgb(199, 199, 148);")

        self.horizontalLayout_6.addWidget(self.pushButton_equal_to)

        self.pushButton_plus = QPushButton(self.seventhRowFrame)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(61, 41))
        self.pushButton_plus.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_plus.setFont(font2)
        self.pushButton_plus.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.horizontalLayout_6.addWidget(self.pushButton_plus)

        self.pushButton_cube = QPushButton(self.seventhRowFrame)
        self.pushButton_cube.setObjectName(u"pushButton_cube")
        self.pushButton_cube.setMinimumSize(QSize(61, 41))
        self.pushButton_cube.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_cube.setFont(font2)
        self.pushButton_cube.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout_6.addWidget(self.pushButton_cube)


        self.verticalLayout_2.addWidget(self.seventhRowFrame)


        self.verticalLayout_3.addWidget(self.buttonHousingFrame)


        self.horizontalLayout_7.addWidget(self.mainCalculatorFrame)

        self.historyFrame = QFrame(self.centralwidget)
        self.historyFrame.setObjectName(u"historyFrame")
        self.historyFrame.setMinimumSize(QSize(211, 501))
        self.historyFrame.setMaximumSize(QSize(270, 1000))
        self.historyFrame.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.historyFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.historyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.historyFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.historyFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(71, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.pushButton_clear_history = QPushButton(self.historyFrame)
        self.pushButton_clear_history.setObjectName(u"pushButton_clear_history")
        self.pushButton_clear_history.setMinimumSize(QSize(100, 30))
        self.pushButton_clear_history.setMaximumSize(QSize(110, 30))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.pushButton_clear_history.setFont(font3)
        self.pushButton_clear_history.setStyleSheet(u"background-color: rgb(58, 175, 86);\n"
"")
        icon = QIcon()
        icon.addFile(u":/myIcons/clear_history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_clear_history.setIcon(icon)
        self.pushButton_clear_history.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.pushButton_clear_history)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.historyLabel = QLabel(self.historyFrame)
        self.historyLabel.setObjectName(u"historyLabel")
        self.historyLabel.setMinimumSize(QSize(189, 60))
        self.historyLabel.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        self.historyLabel.setFont(font4)
        self.historyLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.historyLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.historyLabel.setIndent(60)

        self.verticalLayout_4.addWidget(self.historyLabel)

        self.historyWidget = QWidget(self.historyFrame)
        self.historyWidget.setObjectName(u"historyWidget")
        self.historyWidget.setMinimumSize(QSize(189, 411))
        self.verticalLayout_5 = QVBoxLayout(self.historyWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.history_label_2 = QLabel(self.historyWidget)
        self.history_label_2.setObjectName(u"history_label_2")

        self.gridLayout.addWidget(self.history_label_2, 1, 0, 1, 1)

        self.history_label_7 = QLabel(self.historyWidget)
        self.history_label_7.setObjectName(u"history_label_7")

        self.gridLayout.addWidget(self.history_label_7, 6, 0, 1, 1)

        self.history_label_8 = QLabel(self.historyWidget)
        self.history_label_8.setObjectName(u"history_label_8")

        self.gridLayout.addWidget(self.history_label_8, 7, 0, 1, 1)

        self.history_label_9 = QLabel(self.historyWidget)
        self.history_label_9.setObjectName(u"history_label_9")

        self.gridLayout.addWidget(self.history_label_9, 8, 0, 1, 1)

        self.history_label_6 = QLabel(self.historyWidget)
        self.history_label_6.setObjectName(u"history_label_6")

        self.gridLayout.addWidget(self.history_label_6, 5, 0, 1, 1)

        self.history_label_5 = QLabel(self.historyWidget)
        self.history_label_5.setObjectName(u"history_label_5")

        self.gridLayout.addWidget(self.history_label_5, 4, 0, 1, 1)

        self.history_label_3 = QLabel(self.historyWidget)
        self.history_label_3.setObjectName(u"history_label_3")

        self.gridLayout.addWidget(self.history_label_3, 2, 0, 1, 1)

        self.history_label_1 = QLabel(self.historyWidget)
        self.history_label_1.setObjectName(u"history_label_1")
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(True)
        self.history_label_1.setFont(font5)

        self.gridLayout.addWidget(self.history_label_1, 0, 0, 1, 1)

        self.history_label_4 = QLabel(self.historyWidget)
        self.history_label_4.setObjectName(u"history_label_4")

        self.gridLayout.addWidget(self.history_label_4, 3, 0, 1, 1)

        self.history_label_10 = QLabel(self.historyWidget)
        self.history_label_10.setObjectName(u"history_label_10")

        self.gridLayout.addWidget(self.history_label_10, 9, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.historyWidget)


        self.horizontalLayout_7.addWidget(self.historyFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Calculator", None))
        self.number_input.setText("")
        self.pushButton_permutation.setText("")
        self.pushButton_combination.setText("")
        self.pushButton_factorial.setText("")
        self.pushButton_reciprocal.setText("")
        self.pushButton_raise_to_power.setText("")
        self.pushButton_sine.setText("")
        self.pushButton_cosine.setText("")
        self.pushButton_tangent.setText("")
        self.pushButton_delete.setText("")
        self.pushButton_clear.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_clear.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace, Del", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_arc_sine.setText("")
        self.pushButton_arc_cosine.setText("")
        self.pushButton_arc_tan.setText("")
        self.pushButton_percent.setText("")
        self.pushButton_square_root.setText("")
        self.pushButton_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_seven.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_eight.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_nine.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.pushButton_divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_cube_root.setText("")
        self.pushButton_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_four.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_five.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_six.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.pushButton_multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_root.setText("")
        self.pushButton_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_one.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_two.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_three.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_square.setText("")
        self.pushButton_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_zero.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.pushButton_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_equal_to.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_equal_to.setShortcut(QCoreApplication.translate("MainWindow", u"Enter, =", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_cube.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.pushButton_clear_history.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.historyLabel.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.history_label_2.setText("")
        self.history_label_7.setText("")
        self.history_label_8.setText("")
        self.history_label_9.setText("")
        self.history_label_6.setText("")
        self.history_label_5.setText("")
        self.history_label_3.setText("")
        self.history_label_1.setText("")
        self.history_label_4.setText("")
        self.history_label_10.setText("")
    # retranslateUi

