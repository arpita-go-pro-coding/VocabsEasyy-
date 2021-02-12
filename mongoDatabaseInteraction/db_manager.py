
from gui_py.insert_verbs_window import *
from gui_py.search_verb_window import *
from gui_py.search_verb_result_window import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QCompleter
from PyQt5.QtGui import QPixmap
from mongoengine import connect, disconnect, MultipleObjectsReturned, DoesNotExist
from db_schema.verb_schema import Verb
import sys
from os import path
import os.path

class DBManager:
    def __init__(self, my_window,vmain_page,vmain_window,vlogin_window):

        self.vocabseasyy_main_page=vmain_page
        self.vocabseasyy_main_window=vmain_window
        self.vocabseasyy_login_window=vlogin_window

        ### VocabsEasy Insert Verb Window object creation
        self.admin_insert_verb_page = Ui_Insert_VerbWindow()
        self.admin_insert_verb_window = QtWidgets.QMainWindow()
        self.admin_insert_verb_page.setupUi(self.admin_insert_verb_window)

        ### VocabsEasy Search Verb Window object creation
        self.admin_search_verb_page = Ui_Search_VerbWindow()
        self.admin_search_verb_window = QtWidgets.QMainWindow()
        self.admin_search_verb_page.setupUi(self.admin_search_verb_window)

        ### VocabsEasy Search Verb Result Window object creation
        self.admin_search_verb_result_page = Ui_Search_Verb_ResultWindow()
        self.admin_search_verb_result_window = QtWidgets.QMainWindow()
        self.admin_search_verb_result_page.setupUi(self.admin_search_verb_result_window)

        ## Admin access only: Insert verb page
        self.vocabseasyy_main_page.actionInsert_Verb.triggered.connect(self.access_insert_verb_page)
        ### Insert Verb page
        self.admin_insert_verb_page.insert_verb_browse_pushButton.clicked.connect(self.open_file_dialog)
        self.admin_insert_verb_page.insert_verb_submit_pushButton.clicked.connect(self.interact_with_mongodb)
        self.admin_insert_verb_page.insert_verb_reset_pushButton.clicked.connect(self.reset_all)

        ## Admin access only: Search verb page
        self.vocabseasyy_main_page.actionSearch_Verb.triggered.connect(self.access_search_verb_page)
        ### Search Verb Page
        self.admin_search_verb_page.search_verb_searchbar_lineEdit.textChanged.connect(self.activate_show_record_pushbutton)

        self.admin_search_verb_page.search_verb_show_record_pushButton.clicked.connect(self.show_search_result)


        ### Search Verb Result Page
        self.admin_search_verb_result_page.ok_pushButton.clicked.connect(self.close_search_result_window)

        names=["apple", "banana","air","break"]
        self.completer = QCompleter(names,self.admin_search_verb_result_window)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.admin_search_verb_page.search_verb_searchbar_lineEdit.setCompleter(self.completer)

    def login_mongo(self):
        """Check if login is successful"""

        # host = self.admin_login_page.host_lineEdit.text()
        # port = self.admin_login_page.port_lineEdit.text()
        host,port='localhost','27017'
        if host=='localhost' and port=='27017':
            try:

                # if QMessageBox.information(self.vocabseasyy_main_page,"Connect with mongoDB","Congratulations! Connection is successful!")==QMessageBox.Ok:
                #     print("Yeah")
                    # self.access_insert_verb_page()
                self.connection_successful()
            except Exception as e:
                print(e)
        else:

            self.popup_wrong_entry()

    def connection_successful(self):
        """Connection is successful"""
        msg = QMessageBox()
        msg.setWindowTitle("Connect with mongoDB")
        msg.setText("Congratulations! Connection is successful!")
        clicked_button = msg.exec()
        if clicked_button==QMessageBox.Ok:
            self.vocabseasyy_main_window.show()
            self.vocabseasyy_login_window.hide()



    def popup_wrong_entry(self):
        """Invalid credentials message box"""
        entry_msg=QMessageBox()
        entry_msg.setWindowTitle("Invalid entry!")
        entry_msg.setText("Enter valid credentials!")
        entry_msg.setIcon(QMessageBox.Critical)
        x=entry_msg.exec_()

    def access_insert_verb_page(self):
        """Access the Verb Target page"""
        self.admin_insert_verb_window.show()
        self.insert_verb_initial_load()
        # self.vocabseasyy_main_window.hide()


    def insert_verb_initial_load(self):
        """Disable the pushbuttons available"""
        # self.admin_insert_verb_page.insert_verb_submit_pushButton.setEnabled(False)
        self.admin_insert_verb_page.insert_verb_tabview_pushButton.setEnabled(False)
        self.admin_insert_verb_page.insert_verb_treeview_pushButton.setEnabled(False)
        self.admin_insert_verb_page.insert_verb_conj_pushButton.setEnabled(False)

    def interact_with_mongodb(self):
        """Connect with mongo db and add data"""
        try:
            connect(db='VocabsEasyy', host='localhost', port=27017)
            print('Connected successfully')

            if len(self.admin_insert_verb_page.insert_verb_mverb_lineEdit.text()):
                verb_obj=Verb(verb_name=self.admin_insert_verb_page.insert_verb_mverb_lineEdit.text())
                verb_obj.eng_meaning = self.admin_insert_verb_page.insert_verb_engmeaning_lineEdit.text()
                verb_obj.hin_meaning = self.admin_insert_verb_page.insert_verb_hindimeaning_lineEdit.text()
                verb_obj.satz = self.admin_insert_verb_page.insert_verb_satz_lineEdit.text()
                verb_obj.level=self.admin_insert_verb_page.insert_verb_level_comboBox.currentText()
                verb_obj.type = self.admin_insert_verb_page.insert_verb_type_comboBox.currentText()
                verb_obj.subtype = self.admin_insert_verb_page.insert_verb_subtype_comboBox.currentText()
                verb_obj.case = self.admin_insert_verb_page.insert_verb_case_comboBox.currentText()
                # Load image to mongo db
                if path.exists(self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.text()):
                    with open(self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.text(), 'rb') as fd:
                        verb_obj.input_pic.put(fd, content_type='image/jpeg')


                verb_obj.save()
                print("Data successfully loaded to db!")
                QMessageBox.information(self.admin_insert_verb_window, "Entry successful", "Document successfully loaded to database!")
            else:
                QMessageBox.critical(self.admin_insert_verb_window,"Invalid Entry","Please Enter Verb Info")
        except Exception as e:
            print(e)


        finally:
            disconnect()


    def open_file_dialog(self):
        """Opens the file dialog box when Browse button is clicked"""

        try:
            filename = QFileDialog.getOpenFileName(self.admin_insert_verb_window,
                                                   ("Open Image"), ".",
                                                   ("Image Files (*.png *.jpg)"))
            self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.setText(filename[0])
            self.admin_insert_verb_page.insert_verb_picpreview_pushButton.clicked.connect(self.show_image)

        except Exception as e:
            print(e)

    def show_image(self):
        """Image appears on the window"""
        # print(self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.text())
        pixmap=QPixmap(self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.text())
        self.admin_insert_verb_page.insert_verb_img_label.setPixmap(pixmap)
        self.admin_insert_verb_page.insert_verb_img_label.resize(pixmap.width(),pixmap.height())

    def reset_all(self):
        """Reset all fields in the Insert Verb window"""
        self.admin_insert_verb_page.insert_verb_mverb_lineEdit.clear()
        self.admin_insert_verb_page.insert_verb_engmeaning_lineEdit.clear()
        self.admin_insert_verb_page.insert_verb_hindimeaning_lineEdit.clear()
        self.admin_insert_verb_page.insert_verb_satz_lineEdit.clear()
        self.admin_insert_verb_page.insert_verb_level_comboBox.setCurrentIndex(0)
        self.admin_insert_verb_page.insert_verb_type_comboBox.setCurrentIndex(0)
        self.admin_insert_verb_page.insert_verb_subtype_comboBox.setCurrentIndex(0)
        self.admin_insert_verb_page.insert_verb_case_comboBox.setCurrentIndex(0)

        self.admin_insert_verb_page.insert_verb_inputpic_lineEdit.clear()
        self.admin_insert_verb_page.insert_verb_img_label.clear()



    def access_search_verb_page(self):
        """Shows the Search Verb Page for admin only"""
        self.admin_search_verb_window.show()
        self.admin_search_verb_page.search_verb_show_record_pushButton.setEnabled(False)


    def activate_show_record_pushbutton(self):
        """Activate push button only when line edit is changed"""
        try:
            print("hiiiii1")
            # names=["apples","alps","apparatus"]
            # completer=QCompleter(names)
            # self.admin_search_verb_page.search_verb_searchbar_lineEdit.setCompleter(completer)
            # self.admin_search_verb_page.search_verb_show_record_pushButton.setEnabled(True)
            # print("hiiiii2")

        except Exception as e:
            print(e)
            print("In exception")
        print("Outside except")

    ### Search Verb result window

    def show_search_result(self):
        """Show search result on searching"""
        print("show button1")
        search_by_txt=self.admin_search_verb_page.search_verb_by_comboBox.currentText()
        search_txt=self.admin_search_verb_page.search_verb_searchbar_lineEdit.text()
        print("show button2")
        print("Search by text:",search_by_txt)
        print("Search text:", search_txt)
        connect(db='VocabsEasyy', host='localhost', port=27017)
        print('Connected successfully for searching')
        try:
            if search_by_txt=='German Verb':

                self.current_verb=Verb.objects(verb_name=search_txt).get()
                self.fetch_result_from_db()

            else:

                self.current_verb=Verb.objects(eng_meaning__contains=search_txt).get()
                self.fetch_result_from_db()



        except MultipleObjectsReturned as e:
            self.admin_search_verb_result_window.hide()
            self.popup_be_specific()

        except DoesNotExist  as e:
            self.admin_search_verb_result_window.hide()
            self.popup_no_results()

        finally:
            disconnect()






    ### Search Verb Result window
    def close_search_result_window(self):
        """Close the result window"""
        self.admin_search_verb_result_window.close()


    def fetch_result_from_db(self):
        """Shows the result in the search result window"""

        self.admin_search_verb_result_window.show()
        self.admin_search_verb_result_page.main_verb_label.setText(self.current_verb.verb_name)
        self.admin_search_verb_result_page.eng_meaning_verb_label.setText(self.current_verb.eng_meaning)
        self.admin_search_verb_result_page.hin_meaning_verb_label.setText(self.current_verb.hin_meaning)
        self.admin_search_verb_result_page.satz_verb_label.setText(self.current_verb.satz)
        self.admin_search_verb_result_page.level_verb_label.setText(self.current_verb.level)
        self.admin_search_verb_result_page.type_verb_label.setText(self.current_verb.type)
        self.admin_search_verb_result_page.subtype_verb_label.setText(self.current_verb.subtype)
        self.admin_search_verb_result_page.case_verb_label.setText(self.current_verb.case)

        photo=self.current_verb.input_pic.read()
        ba = QtCore.QByteArray(photo)
        pixmap = QtGui.QPixmap()

        if self.current_verb.input_pic.content_type == "image/jpeg":
            pixmap.loadFromData(ba, "JPEG")

        if self.current_verb.input_pic.content_type == "image/png":
            pixmap.loadFromData(ba, "PNG")

        self.admin_search_verb_result_page.img_label.clear()
        self.admin_search_verb_result_page.img_label.updatesEnabled()
        self.admin_search_verb_result_page.img_label.setPixmap(pixmap.scaled(300,300))
        self.admin_search_verb_result_page.img_label.update()

        ## Clear contents of line edit and disable show record pushbutton
        self.admin_search_verb_page.search_verb_searchbar_lineEdit.clear()
        self.admin_search_verb_page.search_verb_show_record_pushButton.setEnabled(False)




    def popup_no_results(self):
        """Shows popup saying no results found"""

        no_results_msg = QMessageBox()
        no_results_msg.setWindowTitle("No results found!")
        no_results_msg.setText("Sorry, there was no results found in DB!")
        no_results_msg.setIcon(QMessageBox.Critical)
        x = no_results_msg.exec_()


    def popup_be_specific(self):
        """Shows popup saying be specific with your result"""

        specific_msg = QMessageBox()
        specific_msg.setWindowTitle("Be specifc with ypur search")
        specific_msg.setText("Please narrow down your search, multiple matches found")
        specific_msg.setIcon(QMessageBox.Critical)
        x = specific_msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_window = QtWidgets.QMainWindow()
    main_obj = DBManager(my_window)
    sys.exit(app.exec_())
