from main_window_organisation_files.calculator_features_and_appearance import CalculatorFeatures_and_Appearance
from PySide6.QtGui import QIcon

class CalculatorOrganisation(CalculatorFeatures_and_Appearance):
    def __init__(self):
        super(CalculatorOrganisation, self).__init__()
        #self.setupUi(self)

        # Window Icon
        self.setWindowIcon(QIcon("../images/calc_icon.jpg"))

        self.main_window_set_texts()

        self.main_window_buttons_actions()

        self.set_validator()

        self.display_on_history_table()

        self.hide_show_history_push_button()

        self.set_Visibles()


