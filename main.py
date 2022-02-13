# 101 browser based on pyqt
# author: jeli-t
# https://github.com/I-Z-P/browser


from typing import Type
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
        "    min-width: 90px;\n"
        "    max-width: 90px;\n"
        "}\n"
        "QTabBar::tab:hover{\n"
        "    border: 2px solid rgb(107, 248, 255);\n"
        "}\n"
        "QTabBar::tab:focus{\n"
        "    background-color: rgb(159, 159, 159);\n"
        "    border: 2px solid rgb(0, 170, 255);\n"
        "}\n"
        "QTabBar::tab:selected{\n"
        "    background-color: rgb(159, 159, 159);\n"
        "    border: 2px solid rgb(0, 170, 255);\n"
        "}")
        self.tabWidget.setDocumentMode(True)
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
        self.new_tab = QtWidgets.QWidget()
        self.new_tab.setObjectName("new_tab")
        self.tabWidget.addTab(self.new_tab, "")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "DuckDuckGo")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_tab), "+")

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
        self.tabWidget.currentChanged.connect(self.change_tab)
        self.web_engine.loadFinished.connect(self.change_tab_name)


    def change_site(self, search_field = None, web_engine = None):
        if search_field:
            search_text = str(search_field.text())
        else: search_text = str(self.search_field.text())
        if 'http://' in search_text or 'https://' in search_text:
            url = QtCore.QUrl(search_text)
        else:
            url = QtCore.QUrl('https://duckduckgo.com/?q={}&atb=v312-5__&ia=web'.format(search_text))
        url.setScheme('http')
        if web_engine:
            web_engine.setUrl(url)
        else: self.web_engine.setUrl(url)

    def page_back(self, web_engine = None):
        if web_engine:
            web_engine.back()
        else: self.web_engine.back()

    def page_forward(self, web_engine = None):
        if web_engine:
            web_engine.forward()
        else: self.web_engine.forward()

    def page_reload(self, web_engine = None):
        if web_engine:
            web_engine.reload()
        else: self.web_engine.reload()

    def settings(self):
        print('settings')

    def change_url(self, search_field = None, web_engine = None):
        try:
            if search_field and web_engine:
                new_url = web_engine.url()
                search_field.setText(new_url.toString())
            else:
                new_url = self.web_engine.url()
                self.search_field.setText(new_url.toString())
        except: pass

    def change_tab(self):
        if self.tabWidget.currentIndex() == self.tabWidget.count() -1:
            self.create_new_tab()
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.new_tab))
            # BUG third and next tabs are all named +
            # print('curent:', self.tabWidget.currentIndex(), 'count:', self.tabWidget.count())
            self.tabWidget.setTabText(self.tabWidget.count() -1, '+')

    def change_tab_name(self, web_engine = None):
        # BUG first tab title doesn't change
        try:
            if web_engine:
                self.tabWidget.setTabText(self.tabWidget.currentIndex(), web_engine.page().title())
            else:
                self.tabWidget.setTabText(self.tabWidget.currentIndex(), self.web_engine.page().title())
        except: pass

    def create_new_tab(self):
        # gui definition
        new_tab = QtWidgets.QWidget()
        new_tab.setObjectName("new_tab")
        verticalLayout = QtWidgets.QVBoxLayout(new_tab)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(0)
        verticalLayout.setObjectName("verticalLayout")
        search_bar = QtWidgets.QHBoxLayout()
        search_bar.setContentsMargins(10, 10, 10, 10)
        search_bar.setSpacing(10)
        search_bar.setObjectName("search_bar")
        page_back_button = QtWidgets.QPushButton(new_tab)
        page_back_button.setMinimumSize(QtCore.QSize(40, 40))
        page_back_button.setMaximumSize(QtCore.QSize(40, 40))
        page_back_button.setStyleSheet("QPushButton{\n"
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
        page_back_button.setText("")
        page_back_button.setObjectName("page_back_button")
        search_bar.addWidget(page_back_button)
        page_forward_button = QtWidgets.QPushButton(new_tab)
        page_forward_button.setMinimumSize(QtCore.QSize(40, 40))
        page_forward_button.setMaximumSize(QtCore.QSize(40, 40))
        page_forward_button.setStyleSheet("QPushButton{\n"
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
        page_forward_button.setText("")
        page_forward_button.setObjectName("page_forward_button")
        search_bar.addWidget(page_forward_button)
        page_reload_button = QtWidgets.QPushButton(new_tab)
        page_reload_button.setMinimumSize(QtCore.QSize(40, 40))
        page_reload_button.setMaximumSize(QtCore.QSize(40, 40))
        page_reload_button.setStyleSheet("QPushButton{\n"
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
        page_reload_button.setText("")
        page_reload_button.setObjectName("page_reload_button")
        search_bar.addWidget(page_reload_button)
        search_field = QtWidgets.QLineEdit(new_tab)
        search_field.setMinimumSize(QtCore.QSize(0, 40))
        search_field.setMaximumSize(QtCore.QSize(16777215, 40))
        search_field.setStyleSheet("QLineEdit{\n"
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
        search_field.setObjectName("search_field")
        search_field.setPlaceholderText("Search here...")
        search_bar.addWidget(search_field)
        settings_button = QtWidgets.QPushButton(new_tab)
        settings_button.setMinimumSize(QtCore.QSize(40, 40))
        settings_button.setMaximumSize(QtCore.QSize(40, 40))
        settings_button.setStyleSheet("QPushButton{\n"
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
        settings_button.setText("")
        settings_button.setObjectName("settings_button")
        search_bar.addWidget(settings_button)
        verticalLayout.addLayout(search_bar)
        web_engine_box = QtWidgets.QVBoxLayout()
        web_engine_box.setSpacing(0)
        web_engine_box.setObjectName("web_engine_box")
        verticalLayout.addLayout(web_engine_box)
        verticalLayout.setStretch(0, 1)
        verticalLayout.setStretch(1, 8)
        url = QtCore.QUrl("https://start.duckduckgo.com/")
        web_engine = QWebEngineView()
        web_engine.setUrl(url)
        web_engine_box.addWidget(web_engine)
        # add tab to list
        index = self.tabWidget.addTab(new_tab, "")
        self.tabWidget.setTabText(index, "DuckDuckGo")
        # drivers
        search_field.returnPressed.connect(lambda: self.change_site(search_field, web_engine))
        page_back_button.clicked.connect(lambda: self.page_back(web_engine))
        page_forward_button.clicked.connect(lambda: self.page_forward(web_engine))
        page_reload_button.clicked.connect(lambda: self.page_reload(web_engine))
        web_engine.urlChanged.connect(lambda: self.change_url(search_field, web_engine))
        web_engine.loadFinished.connect(lambda: self.change_tab_name(web_engine))
        settings_button.clicked.connect(self.settings)


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