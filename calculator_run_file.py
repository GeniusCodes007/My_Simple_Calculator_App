from PySide6.QtWidgets import QApplication
import sys
from main_window_organisation_files.calculator_organisation_file import CalculatorOrganisation

app = QApplication()
window = CalculatorOrganisation()
window.show()
sys.exit(app.exec())