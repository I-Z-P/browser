# 101 browser based on pyqt
# author: jeli-t
# https://github.com/I-Z-P/browser


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *


##########################################
#         GUI DEFINITION
##########################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
        "    background-color:rgb(129, 129, 129);\n"
        "    border: 2px solid rgb(255, 255, 255);\n"
        "    border-radius: 10px;\n"
        "    margin-bottom: -10px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "    font: 12pt \"Bahnschrift\";\n"
        "    padding: 12px;\n"
        "    min-width: 70px;\n"
        "}\n"
        "QTabBar::tab:hover{\n"
        "    border: 2px solid rgb(107, 248, 255);\n"
        "}\n"
        "QTabBar::tab:focus{\n"
        "    background-color: rgb(159, 159, 159);\n"
        "    border: 2px solid rgb(0, 170, 255);\n"
        "}")
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_bar = QtWidgets.QHBoxLayout()
        self.search_bar.setContentsMargins(10, 10, 10, 10)
        self.search_bar.setSpacing(10)
        self.search_bar.setObjectName("search_bar")
        self.page_back_button = QtWidgets.QPushButton(self.tab)
        self.page_back_button.setMinimumSize(QtCore.QSize(40, 40))
        self.page_back_button.setMaximumSize(QtCore.QSize(40, 40))
        self.page_back_button.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(129, 129, 129);\n"
        "    border: 3px solid rgb(255, 255, 255);\n"
        "    border-radius: 20px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    border: 3px solid rgb(0, 255, 255);\n"
        "}\n"
        "QPushButton:focus{\n"
        "    background-color: rgb(140, 140, 140);\n"
        "    border: 3px solid rgb(0, 170, 255);\n"
        "}")
        self.page_back_button.setText("")
        self.page_back_button.setObjectName("page_back_button")
        self.search_bar.addWidget(self.page_back_button)
        self.page_forward_button = QtWidgets.QPushButton(self.tab)
        self.page_forward_button.setMinimumSize(QtCore.QSize(40, 40))
        self.page_forward_button.setMaximumSize(QtCore.QSize(40, 40))
        self.page_forward_button.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(129, 129, 129);\n"
        "    border: 3px solid rgb(255, 255, 255);\n"
        "    border-radius: 20px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    border: 3px solid rgb(0, 255, 255);\n"
        "}\n"
        "QPushButton:focus{\n"
        "    background-color: rgb(140, 140, 140);\n"
        "    border: 3px solid rgb(0, 170, 255);\n"
        "}")
        self.page_forward_button.setText("")
        self.page_forward_button.setObjectName("page_forward_button")
        self.search_bar.addWidget(self.page_forward_button)
        self.page_reload_button = QtWidgets.QPushButton(self.tab)
        self.page_reload_button.setMinimumSize(QtCore.QSize(40, 40))
        self.page_reload_button.setMaximumSize(QtCore.QSize(40, 40))
        self.page_reload_button.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(129, 129, 129);\n"
        "    border: 3px solid rgb(255, 255, 255);\n"
        "    border-radius: 20px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    border: 3px solid rgb(0, 255, 255);\n"
        "}\n"
        "QPushButton:focus{\n"
        "    background-color: rgb(140, 140, 140);\n"
        "    border: 3px solid rgb(0, 170, 255);\n"
        "}")
        self.page_reload_button.setText("")
        self.page_reload_button.setObjectName("page_reload_button")
        self.search_bar.addWidget(self.page_reload_button)
        self.search_field = QtWidgets.QLineEdit(self.tab)
        self.search_field.setMinimumSize(QtCore.QSize(0, 40))
        self.search_field.setMaximumSize(QtCore.QSize(16777215, 40))
        self.search_field.setStyleSheet("QLineEdit{\n"
        "    background-color:rgb(129, 129, 129);\n"
        "    border: 3px solid rgb(255, 255, 255);\n"
        "    border-radius: 20px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "    padding-left: 10px;\n"
        "    padding-right: 10px;\n"
        "    font: 14pt \"Bahnschrift\";\n"
        "}\n"
        "QLineEdit:hover{\n"
        "    border: 3px solid rgb(107, 248, 255);\n"
        "}\n"
        "QLineEdit:focus{\n"
        "    background-color: rgb(159, 159, 159);\n"
        "    border: 3px solid rgb(0, 170, 255);\n"
        "}")
        self.search_field.setObjectName("search_field")
        self.search_bar.addWidget(self.search_field)
        self.settings_button = QtWidgets.QPushButton(self.tab)
        self.settings_button.setMinimumSize(QtCore.QSize(40, 40))
        self.settings_button.setMaximumSize(QtCore.QSize(40, 40))
        self.settings_button.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(129, 129, 129);\n"
        "    border: 3px solid rgb(255, 255, 255);\n"
        "    border-radius: 20px;\n"
        "    border-color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    border: 3px solid rgb(0, 255, 255);\n"
        "}\n"
        "QPushButton:focus{\n"
        "    background-color: rgb(140, 140, 140);\n"
        "    border: 3px solid rgb(0, 170, 255);\n"
        "}")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.search_bar.addWidget(self.settings_button)
        self.verticalLayout.addLayout(self.search_bar)
        self.web_engine_box = QtWidgets.QVBoxLayout()
        self.web_engine_box.setSpacing(0)
        self.web_engine_box.setObjectName("web_engine_box")
        self.verticalLayout.addLayout(self.web_engine_box)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.page_back_button, self.page_forward_button)
        MainWindow.setTabOrder(self.page_forward_button, self.page_reload_button)
        MainWindow.setTabOrder(self.page_reload_button, self.settings_button)
        MainWindow.setTabOrder(self.settings_button, self.search_field)
        MainWindow.setWindowTitle("IZP browser")
        self.search_field.setPlaceholderText("Search here...")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "New Tab")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "New Tab")

        # web engine
        self.web_engine = QWebEngineView()
        self.web_engine.setObjectName('web_engine')
        self.web_engine.setUrl(QtCore.QUrl("https://start.duckduckgo.com/"))
        self.web_engine_box.addWidget(self.web_engine)


##########################################
#         GUI DRIVERS
##########################################

        self.search_field.returnPressed.connect(self.change_site)
        self.page_back_button.clicked.connect(self.page_back)
        self.page_forward_button.clicked.connect(self.page_forward)
        self.page_reload_button.clicked.connect(self.page_reload)
        self.settings_button.clicked.connect(self.settings)
        self.web_engine.urlChanged.connect(self.change_url)


    def change_site(self):
        search_text = str(self.search_field.text())
        if 'http://' in search_text or 'https://' in search_text:
            url = QtCore.QUrl(search_text)
        else:
            url = QtCore.QUrl('https://duckduckgo.com/?q={}&atb=v312-5__&ia=web'.format(search_text))
        url.setScheme('http')
        self.web_engine.setUrl(url)

    def page_back(self):
        self.web_engine.back()

    def page_forward(self):
        self.web_engine.forward()

    def page_reload(self):
        self.web_engine.reload()

    def settings(self):
        print('settings')

    def change_url(self):
        new_url = self.web_engine.url()
        self.search_field.setText(new_url.toString())


##########################################
#         MAIN FUNCTION
##########################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())