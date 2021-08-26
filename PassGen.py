from PyQt5 import QtCore, QtGui, QtWidgets
import languages, random, string, pyperclip, webbrowser
from LIBS import StandartStyleSheets
from LIBS import Theme_change_styleSheets
from LIBS import copy_password_styleSheets
from LIBS import generate_password_styleSheets

class Ui_PassGen_Window(object):
    def setupUi(self, PassGen_Window):

        #-------------------------------------------
        self.Copy_btn_color = False
        self.password_area_color = False
        #-------------------------------------------

        self.description, self.generate, self.copy, self.copy2, self.dark, self.light, self.area = languages.en()

        PassGen_Window.setObjectName("PassGen_Window")
        PassGen_Window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        PassGen_Window.resize(850, 476)
        PassGen_Window.setMinimumSize(QtCore.QSize(850, 476))
        PassGen_Window.setMaximumSize(QtCore.QSize(850, 476))
        PassGen_Window.setStyleSheet(StandartStyleSheets.PassGen_Window_standart_styleSheet)
        self.centralwidget = QtWidgets.QWidget(PassGen_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.Generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Generate_btn.setGeometry(QtCore.QRect(430, 270, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Generate_btn.setFont(font)
        self.Generate_btn.setStyleSheet(StandartStyleSheets.Generate_btn_standart_styleSheet)
        self.Generate_btn.setObjectName("Generate_btn")
        self.Generate_btn.setText(self.generate)

        self.Copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_btn.setGeometry(QtCore.QRect(620, 270, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Copy_btn.setFont(font)
        self.Copy_btn.setStyleSheet(StandartStyleSheets.Copy_btn_standart_StyleSheet)
        self.Copy_btn.setObjectName("Copy_btn")
        self.Copy_btn.setText(self.copy)

        self.password_area = QtWidgets.QLineEdit(self.centralwidget)
        self.password_area.setGeometry(QtCore.QRect(430, 180, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.password_area.setFont(font)
        self.password_area.setStyleSheet(StandartStyleSheets.password_area_standart_setStyleSheet)
        self.password_area.setText("")
        self.password_area.setMaxLength(20)
        self.password_area.setAlignment(QtCore.Qt.AlignCenter)
        self.password_area.setPlaceholderText(self.area)
        self.password_area.setObjectName("password_area")

        self.Exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_btn.setGeometry(QtCore.QRect(800, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Exit_btn.setFont(font)
        self.Exit_btn.setStyleSheet(StandartStyleSheets.Exit_btn_standart_setStyleSheet)
        self.Exit_btn.setObjectName("Exit_btn")

        self.Theme_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Theme_btn.setGeometry(QtCore.QRect(700, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Theme_btn.setFont(font)
        self.Theme_btn.setStyleSheet(StandartStyleSheets.Theme_btn_standart_setStyleSheet)
        self.Theme_btn.setObjectName("Theme_btn")
        self.Theme_btn.setText(self.light)

        self.Language_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Language_Btn.setGeometry(QtCore.QRect(760, 10, 31, 31))
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Theme_btn.setFont(font)
        self.Language_Btn.setFont(font)
        self.Language_Btn.setText('En')
        self.Language_Btn.setStyleSheet(StandartStyleSheets.Language_Btn_standart_setStyleSheet)
        self.Language_Btn.setObjectName("Language_Btn")

        self.description_area = QtWidgets.QLabel(self.centralwidget)
        self.description_area.setGeometry(QtCore.QRect(20, 200, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        self.description_area.setFont(font)
        self.description_area.setText(self.description)
        self.description_area.setStyleSheet(StandartStyleSheets.description_area_standart_setStyleSheet)
        self.description_area.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.description_area.setObjectName("description_area")

        self.instagram_btn = QtWidgets.QPushButton(self.centralwidget)
        self.instagram_btn.setGeometry(QtCore.QRect(20, 430, 41, 31))
        self.instagram_btn.setStyleSheet(StandartStyleSheets.instagram_btn_standart_setStyleSheet)
        self.instagram_btn.setText("")
        self.instagram_btn.setObjectName("instagram_btn")

        self.developer_insta_text = QtWidgets.QLabel(self.centralwidget)
        self.developer_insta_text.setGeometry(QtCore.QRect(60, 429, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.developer_insta_text.setFont(font)
        self.developer_insta_text.setStyleSheet(StandartStyleSheets.developer_insta_text_standart_setStyleSheet)
        self.developer_insta_text.setObjectName("developer_insta_text")

        PassGen_Window.setCentralWidget(self.centralwidget)
        self.retranslateUi(PassGen_Window)
        QtCore.QMetaObject.connectSlotsByName(PassGen_Window)

        # ----------------------------------------------------------
        self.Language_Btn.clicked.connect(self.language_change)
        self.Generate_btn.clicked.connect(self.generate_password)
        self.Copy_btn.clicked.connect(self.copy_password)
        self.Exit_btn.clicked.connect(self.exit)
        self.Theme_btn.clicked.connect(self.theme_change)
        self.instagram_btn.clicked.connect(self.instagram)
        # ----------------------------------------------------------

    def retranslateUi(self, PassGen_Window):
        _translate = QtCore.QCoreApplication.translate
        PassGen_Window.setWindowTitle(_translate("PassGen_Window", "MainWindow"))
        self.Exit_btn.setText(_translate("PassGen_Window", "X"))
        self.developer_insta_text.setText(_translate("PassGen_Window", "emircandkmn"))

    def exit(self):
            exit()

    def instagram(self):
            webbrowser.open_new_tab('https://www.instagram.com/emircandkmn/')

    def theme_change(self):
        if self.Theme_btn.text() == self.light:
            self.Theme_btn.setText(self.dark)
            PassGen_Window.setStyleSheet(Theme_change_styleSheets.PassGen_Window_dark_setStyleSheet)
            self.Generate_btn.setStyleSheet(Theme_change_styleSheets.Generate_btn_dark_setStyleSheet)

            if self.Copy_btn_color == True:
                self.Copy_btn.setStyleSheet(Theme_change_styleSheets.Copy_btn_True_dark_setStyleSheet)

            else:
                self.Copy_btn.setStyleSheet(Theme_change_styleSheets.Copy_btn_False_dark_setStyleSheet)

            if self.password_area_color == True:
                self.password_area.setStyleSheet(Theme_change_styleSheets.password_area_True_dark_setStyleSheet)

            else:
                self.password_area.setStyleSheet(Theme_change_styleSheets.password_area_False_dark_setStyleSheet)

            self.Theme_btn.setStyleSheet(Theme_change_styleSheets.Theme_btn_dark_setStyleSheet)
            self.Exit_btn.setStyleSheet(Theme_change_styleSheets.Exit_btn_dark_setStyleSheet)
            self.Language_Btn.setStyleSheet(Theme_change_styleSheets.Language_Btn_dark_setStyleSheet)

        elif self.Theme_btn.text() == self.dark:
            self.Theme_btn.setText(self.light)
            PassGen_Window.setStyleSheet(Theme_change_styleSheets.PassGen_Window_light_setStyleSheet)
            self.Generate_btn.setStyleSheet(Theme_change_styleSheets.Generate_btn_light_setStyleSheet)

            if self.Copy_btn_color == True:
                self.Copy_btn.setStyleSheet(Theme_change_styleSheets.Copy_btn_True_light_setStyleSheet)

            else:
                self.Copy_btn.setStyleSheet(Theme_change_styleSheets.Copy_btn_False_light_setStyleSheet)

            if self.password_area_color == True:
                self.password_area.setStyleSheet(Theme_change_styleSheets.password_area_True_light_setStyleSheet)

            else:
                self.password_area.setStyleSheet(Theme_change_styleSheets.password_area_False_light_setStyleSheet)

            self.Theme_btn.setStyleSheet(Theme_change_styleSheets.Theme_btn_light_setStyleSheet)
            self.Exit_btn.setStyleSheet(Theme_change_styleSheets.Exit_btn_light_setStyleSheet)
            self.Language_Btn.setStyleSheet(Theme_change_styleSheets.Language_Btn_light_setStyleSheet)

    def copy_password(self):
        self.Copy_btn_color = True
        password = self.password_area.text()
        if password != '':
            pyperclip.copy(password)
            self.Copy_btn.setText(self.copy2)
            self.Copy_btn.setStyleSheet(copy_password_styleSheets.Copy_btn_setStyleSheet)

    def generate_password(self):
        self.Copy_btn_color = False
        self.password_area_color = True

        lenght = random.randint(12, 20)
        all = string.ascii_letters + string.punctuation + string.digits
        data = random.sample(all, lenght)
        password = ''.join(data)
        self.password_area.setText(password)
        self.Copy_btn.setText(self.copy)

        if self.Theme_btn.text() == self.dark:
            self.Copy_btn.setStyleSheet(generate_password_styleSheets.Copy_btn_dark_setStyleSheet)
            self.password_area.setStyleSheet(generate_password_styleSheets.password_area_dark_setStyleSheet)
            self.Exit_btn.setStyleSheet(generate_password_styleSheets.Exit_btn_dark_setStyleSheet)
            self.Language_Btn.setStyleSheet(generate_password_styleSheets.Language_Btn_dark_setStyleSheet)

        elif self.Theme_btn.text() == self.light:
            self.Copy_btn.setStyleSheet(generate_password_styleSheets.Copy_btn_light_setStyleSheet)
            self.password_area.setStyleSheet(generate_password_styleSheets.password_area_light_setStyleSheet)
            self.Exit_btn.setStyleSheet(generate_password_styleSheets.Exit_btn_light_setStyleSheet)
            self.Language_Btn.setStyleSheet(generate_password_styleSheets.Language_Btn_light_setStyleSheet)

    def language_change(self):
        if self.Language_Btn.text() == 'En':
            self.description, self.generate, self.copy, self.copy2, self.dark, self.light, self.area = languages.tr()
            self.Language_Btn.setText('Tr')

            if self.Copy_btn.text() == 'Copied':
                self.Copy_btn.setText(self.copy2)
                self.description_area.setText(self.description)
                self.password_area.setPlaceholderText(self.area)
                self.Generate_btn.setText(self.generate)

                if self.Theme_btn.text() == 'Dark':
                    self.Theme_btn.setText(self.dark)

                elif self.Theme_btn.text() == 'Light':
                    self.Theme_btn.setText(self.light)

            elif self.Copy_btn.text() == 'Copy':
                self.Copy_btn.setText(self.copy)
                self.description_area.setText(self.description)
                self.password_area.setPlaceholderText(self.area)
                self.Generate_btn.setText(self.generate)

                if self.Theme_btn.text() == 'Dark':
                    self.Theme_btn.setText(self.dark)

                elif self.Theme_btn.text() == 'Light':
                    self.Theme_btn.setText(self.light)

        elif self.Language_Btn.text() == 'Tr':
            self.description, self.generate, self.copy, self.copy2, self.dark, self.light, self.area = languages.en()
            self.Language_Btn.setText('En')

            if self.Copy_btn.text() == 'Kopyalandı':
                self.Copy_btn.setText(self.copy2)
                self.description_area.setText(self.description)
                self.password_area.setPlaceholderText(self.area)
                self.Generate_btn.setText(self.generate)

                if self.Theme_btn.text() == 'Koyu':
                    self.Theme_btn.setText(self.dark)

                elif self.Theme_btn.text() == 'Açık':
                    self.Theme_btn.setText(self.light)

            elif self.Copy_btn.text() == 'Kopyala':
                self.Copy_btn.setText(self.copy)
                self.description_area.setText(self.description)
                self.password_area.setPlaceholderText(self.area)
                self.Generate_btn.setText(self.generate)

                if self.Theme_btn.text() == 'Koyu':
                    self.Theme_btn.setText(self.dark)

                elif self.Theme_btn.text() == 'Açık':
                    self.Theme_btn.setText(self.light)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PassGen_Window = QtWidgets.QMainWindow()
    ui = Ui_PassGen_Window()
    ui.setupUi(PassGen_Window)
    PassGen_Window.show()
    sys.exit(app.exec_())