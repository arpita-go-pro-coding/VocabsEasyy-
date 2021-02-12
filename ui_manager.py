

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from gui_py.mongo_login_window import *
from gui_py.main_window import *
from mongoDatabaseInteraction.db_manager import *
from gui_py.verb_target_window import *
from gui_py.ready_window import *


class GUIManager:

    def __init__(self,my_window):
        ### vocabseasyy Login Window object creation
        self.vocabseasyy_login_page = Ui_LoginWindow()
        self.vocabseasyy_login_window = QtWidgets.QMainWindow()
        self.vocabseasyy_login_page.setupUi(self.vocabseasyy_login_window)

        ### vocabseasyy Main Window object creation
        self.vocabseasyy_main_page = Ui_MainWindow()
        self.vocabseasyy_main_window = QtWidgets.QMainWindow()
        self.vocabseasyy_main_page.setupUi(self.vocabseasyy_main_window)


        ### vocabseasyy Verb Target Window object creation
        self.verb_target_page=Ui_VerbTargetWindow()
        self.verb_target_window=QtWidgets.QMainWindow()
        self.verb_target_page.setupUi(self.verb_target_window)



        ### Verb Target Window
        self.verb_target_page.verb_target_back_pushButton.clicked.connect(self.handle_back_verb_target_window)
        self.verb_target_page.verb_target_no_lineEdit.textChanged.connect(self.activate_letsgo_pushButton)
        self.verb_target_page.verb_target_go_pushButton.clicked.connect(self.check_valid_entry)


        ### vocabseasyy Verb Ready Window object creation
        self.verb_ready_page = Ui_ReadyWindow()
        self.verb_ready_window = QtWidgets.QMainWindow()
        self.verb_ready_page.setupUi(self.verb_ready_window)

        ### Login page
        self.disable_host_port()
        self.vocabseasyy_login_page.done_pushButton.clicked.connect(self.check_admin_access)
        self.vocabseasyy_login_page.reset_pushButton.clicked.connect(self.reset_login)

        ### vocabseasyy Main Window
        self.vocabseasyy_main_page.main_go_pushButton.clicked.connect(self.vocabseasyy_check_combo_option)


        ## DB Manager: to call db related methods
        self.dbManager = DBManager(self,self.vocabseasyy_main_page,self.vocabseasyy_main_window,self.vocabseasyy_login_window)
        self.vocabseasyy_login_page.login_pushButton.clicked.connect(self.dbManager.login_mongo)

        ### Ready Window

        self.verb_ready_page.ready_page_back_pushButton.clicked.connect(self.handle_back_verb_ready_window)

    def display_vocabseasyy_login_window(self):
        """Show login window"""
        self.vocabseasyy_login_window.show()
        self.vocabseasyy_login_page.login_pushButton.setEnabled(False)
        self.vocabseasyy_login_page.reset_pushButton.setEnabled(False)

    def check_admin_access(self):
        """Checks if the current user has admin access"""

        if self.vocabseasyy_login_page.access_comboBox.currentText()=='No':
            self.disable_host_port()
            self.display_vocabseasyy_main_window_no_admin()
        else:
            self.enable_host_port()



    def disable_host_port(self):
        """Disable host and port line edits as the user doesn't have admin access"""
        self.vocabseasyy_login_page.host_lineEdit.setEnabled(False)
        self.vocabseasyy_login_page.port_lineEdit.setEnabled(False)

    def enable_host_port(self):
        """Enable host and port line edits as the user has admin access"""
        self.vocabseasyy_login_page.host_lineEdit.setEnabled(True)
        self.vocabseasyy_login_page.port_lineEdit.setEnabled(True)
        self.vocabseasyy_login_page.reset_pushButton.setEnabled(True)
        self.vocabseasyy_login_page.login_pushButton.setEnabled(True)


    def reset_login(self):
        """Reset all fields in Login page"""
        self.vocabseasyy_login_page.host_lineEdit.clear()
        self.vocabseasyy_login_page.port_lineEdit.clear()


    ### Main Window

    def display_vocabseasyy_main_window_no_admin(self):
        """Show Main window without menubar access (since user is not an admin)"""
        self.vocabseasyy_main_window.show()
        self.vocabseasyy_login_window.hide()
        self.vocabseasyy_main_page.menubar.hide()

    def vocabseasyy_check_combo_option(self):
        """Check combo box option before going to next page"""

        # print(self.vocabseasyy_main_page.main_options_comboBox.currentIndex())
        try:
            if self.vocabseasyy_main_page.main_options_comboBox.currentText() == 'Verbs':
                self.access_verb_target_page()
            else:
                print("To DO ", self.vocabseasyy_main_page.main_options_comboBox.currentText())
        except Exception as e:
            print(e)

    ### Verb Target Window Methods

    def verb_target_page_initial_load(self):
        """Deactivate go learn button until you enter no. of verbs to be learnt"""
        self.verb_target_page.verb_target_go_pushButton.setEnabled(False)

    def access_verb_target_page(self):
        """Access the Verb Target page"""
        self.verb_target_window.show()
        self.verb_target_page_initial_load()
        self.vocabseasyy_main_window.hide()

    def handle_back_verb_target_window(self):
        """Back button leads us to Main Window"""
        self.vocabseasyy_main_window.show()
        self.verb_target_window.hide()

    def activate_letsgo_pushButton(self):
        """Let's Go pushbutton should be activated when a valid number is entered"""
        self.verb_target_page.verb_target_go_pushButton.setEnabled(True)


    def check_valid_entry(self):
        """Check for valid entry by the user"""
        user_entered=self.verb_target_page.verb_target_no_lineEdit.text()
        # print(user_entered)
        if user_entered.isdigit():
            self.access_verb_ready_page()
        else:
            self.popup_wrong_entry()
            self.verb_target_page.verb_target_go_pushButton.setEnabled(False)

    def popup_wrong_entry(self):
        """No. of verbs can't be other than than numbers"""
        verb_entry_msg=QMessageBox()
        verb_entry_msg.setWindowTitle("Invalid entry!")
        verb_entry_msg.setText("Enter number please!")
        verb_entry_msg.setIcon(QMessageBox.Critical)
        x=verb_entry_msg.exec_()

### Verb Ready Window Methods
    def access_verb_ready_page(self):
        """Show Ready Page"""
        self.verb_ready_window.show()
        self.verb_target_window.hide()


    def handle_back_verb_ready_window(self):
        """Go back to Verb Target Page again"""
        self.verb_target_window.show()
        self.verb_ready_window.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_window = QtWidgets.QMainWindow()
    main_obj = GUIManager(my_window)
    main_obj.display_vocabseasyy_login_window()
    sys.exit(app.exec_())