# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniCalculatrice.ui'
#
# Created: Thu Sep 12 09:34:34 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import fonction

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
   

class Ui_MainWindow(object):
    def quitter(self):
       MainWindow.close()
       
    def reponse(self):
        a=self.nombre1.value()
        b=self.nombre2.value()
        op=self.operateur.currentText() #signe de l'operation

        if op=="+":
            rep=fonction.addition(a,b)
        elif op=="-":
            rep=fonction.soustraction(a,b)
        elif op=="x":
            rep=fonction.multiplication(a,b)
        elif op== "/":
            rep=fonction.division(a,b)
        elif op=="Mod":
             rep=fonction.modulo(a,b)
        elif op=="^":
             rep=fonction.puissance(a,b)
        c=type("ok")
        if type(rep)==c:
            self.resultat.setText(_translate("MainWindow", rep, None))
        else:
            self.resultat.setNum(rep)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(665, 129)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(613, 129))
        MainWindow.setMaximumSize(QtCore.QSize(690, 129))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(647, 70))
        self.stackedWidget.setMaximumSize(QtCore.QSize(700, 70))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.operateur = QtGui.QComboBox(self.page)
        self.operateur.setMinimumSize(QtCore.QSize(60, 30))
        self.operateur.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.operateur.setFont(font)
        self.operateur.setStyleSheet(_fromUtf8("border:1px solid black;\n"
"border-radius:7px;\n"
"background-color: rgb(170, 170, 255);\n"
"text-align:center;"))
        self.operateur.setFrame(True)
        self.operateur.setObjectName(_fromUtf8("operateur"))
        self.operateur.addItem(_fromUtf8(""))
        self.operateur.addItem(_fromUtf8(""))
        self.operateur.addItem(_fromUtf8(""))
        self.operateur.addItem(_fromUtf8(""))
        self.operateur.addItem(_fromUtf8(""))
        self.operateur.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.operateur, 0, 2, 1, 1)
        self.nombre2 = QtGui.QDoubleSpinBox(self.page)
        self.nombre2.setMinimumSize(QtCore.QSize(115, 30))
        self.nombre2.setMaximumSize(QtCore.QSize(115, 30))
        self.nombre2.setMinimum(-999999999.0)
        self.nombre2.setMaximum(999999999.0)
        self.nombre2.setObjectName(_fromUtf8("nombre2"))
        self.gridLayout.addWidget(self.nombre2, 0, 4, 1, 1)
        self.egal = QtGui.QPushButton(self.page)
        self.egal.setMinimumSize(QtCore.QSize(114, 30))
        self.egal.setMaximumSize(QtCore.QSize(114, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.egal.setFont(font)
        self.egal.setStyleSheet(_fromUtf8(""))
        self.egal.setObjectName(_fromUtf8("egal"))
        self.gridLayout.addWidget(self.egal, 0, 6, 1, 1)
        self.nombre1 = QtGui.QDoubleSpinBox(self.page)
        self.nombre1.setMinimumSize(QtCore.QSize(114, 30))
        self.nombre1.setMaximumSize(QtCore.QSize(114, 30))
        self.nombre1.setMinimum(-999999999.0)
        self.nombre1.setMaximum(999999999.0)
        self.nombre1.setObjectName(_fromUtf8("nombre1"))
        self.gridLayout.addWidget(self.nombre1, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.resultat = QtGui.QLabel(self.page)
        self.resultat.setMinimumSize(QtCore.QSize(110, 52))
        self.resultat.setMaximumSize(QtCore.QSize(220, 52))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resultat.setFont(font)
        self.resultat.setObjectName(_fromUtf8("resultat"))
        self.gridLayout.addWidget(self.resultat, 0, 8, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName(_fromUtf8("menuAide"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuiter = QtGui.QAction(MainWindow)
        self.actionQuiter.setObjectName(_fromUtf8("actionQuiter"))
        self.actionComportement_de_l_application = QtGui.QAction(MainWindow)
        self.actionComportement_de_l_application.setObjectName(_fromUtf8("actionComportement_de_l_application"))
        self.menuFichier.addAction(self.actionQuiter)
        self.menuAide.addAction(self.actionComportement_de_l_application)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
       #QtCore.QObject.connect(self.actionQuiter, QtCore.SIGNAL(_fromUtf8("triggered()")), self,QtCore.SLOT(self.quitter(MainWindow)))

        #rehefa miClique  @ quitter de mifermer ni window
        self.actionQuiter.triggered.connect(self.quitter)
        #---------------------------------------------------------------#

        #rehefa miclique @ egal de manome resultat
        self.egal.clicked.connect(self.reponse)
        ##+++++++++++++++++++++++++++++++++++++#
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MiniCalculatrice", None))
        self.operateur.setItemText(0, _translate("MainWindow", "+", None))
        self.operateur.setItemText(1, _translate("MainWindow", "-", None))
        self.operateur.setItemText(2, _translate("MainWindow", "x", None))
        self.operateur.setItemText(3, _translate("MainWindow", "/", None))
        self.operateur.setItemText(4, _translate("MainWindow", "Mod", None))
        self.operateur.setItemText(5, _translate("MainWindow", "^", None))
        self.egal.setText(_translate("MainWindow", "=", None))
        self.resultat.setText(_translate("MainWindow", "Resultat", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.actionQuiter.setText(_translate("MainWindow", "Quiter", None))
        self.actionComportement_de_l_application.setText(_translate("MainWindow", "comportement de l\'application", None))
        
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

