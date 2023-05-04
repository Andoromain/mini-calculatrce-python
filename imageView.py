# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageView.ui'
#
# Created: Sat Sep 14 11:45:45 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def ouvrirFichier(self):
        titre=str("selectionnez le fichier")
        directory=str("D:\multimedia ")
        filtre=str("Image (*.jpg);;Tous (*.*)")
        fichier=QtGui.QFileDialog.getOpenFileName(MainWindow, titre,directory,filtre)
        url="border-image: url("+str(fichier)+");"
        self.image.setStyleSheet(_fromUtf8(url))
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(504, 344)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("D:/logiciel/Junior Icon/Junior Icon 79.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.image = QtGui.QGraphicsView(self.centralwidget)
        self.image.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.image.setObjectName(_fromUtf8("image"))
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuiter = QtGui.QAction(MainWindow)
        self.actionQuiter.setObjectName(_fromUtf8("actionQuiter"))
        self.menuFichier.addAction(self.actionOpen)
        self.menuFichier.addAction(self.actionQuiter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuiter.triggered.connect(MainWindow.close)
        self.actionOpen.triggered.connect(self.ouvrirFichier)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageViewer", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionQuiter.setText(_translate("MainWindow", "quiter", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

