from PyQt5 import QtCore, QtGui, QtWidgets

import Clairvoyance-Operation-master as bd

class CheckableComboBox(QtWidgets.QComboBox):
    
    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
    
    def itemChecked(self, index):
        item = self.model().item(i,0)
        return print(item.checkState() == QtCore.Qt.Checked)

class Ui_MainWindowd(object):
    def setupUi(self, MainWindowd):
        #criação da tela principal    
        MainWindowd.setObjectName("MainWindowd")
        MainWindowd.resize(298, 201)
        #criação de um layout para itens se adaptarem ao tamanho da tela
        self.centralwidget = QtWidgets.QWidget(MainWindowd)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #label com o nome do programa
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        
        #criação de um layout para itens se adaptarem ao tamanho da tela
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #box dos herois
        self.heroes = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.heroes.setFont(font)
        self.heroes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heroes.setObjectName("heroes")
        self.heroes.addItem("")
        self.heroes.addItem("")
        self.horizontalLayout.addWidget(self.heroes)
        
        #box das features 
        self.feature = CheckableComboBox(MainWindowd)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.feature.setFont(font)
        self.feature.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.feature.setObjectName("feature")
        self.horizontalLayout.addWidget(self.feature)
        
        #box dos métodos
        self.method = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.method.setFont(font)
        self.method.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.method.setObjectName("method")
        self.method.addItem("")
        self.horizontalLayout.addWidget(self.method)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        #botão para pesquisar
        self.search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setObjectName("search")
        self.verticalLayout.addWidget(self.search)
        MainWindowd.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindowd)
        self.statusbar.setObjectName("statusbar")
        MainWindowd.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowd)
        QtCore.QMetaObject.connectSlotsByName(MainWindowd)
        MainWindowd.setTabOrder(self.feature, self.method)
        MainWindowd.setTabOrder(self.method, self.search)

    #definindo as variáveis
    def retranslateUi(self, MainWindowd):
        _translate = QtCore.QCoreApplication.translate
        MainWindowd.setWindowTitle(_translate("MainWindowd", "Clairvoyance Operation"))
        self.label.setText(_translate("MainWindowd", "Clairvoyance Operation"))
        #para testes
        self.heroes.setItemText(0, _translate("MainWindowd", "Heroi 1"))
        self.heroes.setItemText(1, _translate("MainWindowd", "Heroi 2"))
        for i in range(6):
            self.feature.addItem("poder" + str(i))
        self.method.setItemText(0, _translate("MainWindowd", "Metodo 1"))
        
        self.search.setText(_translate("MainWindowd", "Pesquisar"))

#iniciando o programa 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowd = QtWidgets.QMainWindow()
    mainWidget = QtWidgets.QWidget()
    MainWindowd.setCentralWidget(mainWidget)  
    ui = Ui_MainWindowd()
    ui.setupUi(MainWindowd)
    MainWindowd.show()
    sys.exit(app.exec_())
    

