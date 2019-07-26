from PyQt5 import QtCore, QtGui, QtWidgets
import base_superpower as bd
sp = bd.SuperPower()


#classe para fazer uma ComboBox ser uma Checkable
class CheckableComboBox(QtWidgets.QComboBox):
    
    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
    
    def itemChecked(self, index):
        item = self.model().item(i,0)
        return print(item.checkState() == QtCore.Qt.Checked)

class Main(object):
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
        self.search.clicked.connect(self.exibir)
        
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
        sp.criarListas()
        lAUX = sp.retornarNames()
        for i in range(0, len(lAUX)):
            self.heroes.addItem(lAUX[i])
        lAUX = sp.retornarSuperPower()
        for i in range(0, len(lAUX)):
            self.feature.addItem(lAUX[i])    
        lAUX = sp.retornarDistancias()
        for i in range(0, len(lAUX)):
            self.method.addItem(lAUX[i])
        
        self.search.setText(_translate("MainWindowd", "Pesquisar"))

    def exibir(self):
        t = Resultado()
        t.setupUi(MainWindowd)
        MainWindowd.show
        
class Resultado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUia(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUia(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clairvoyance Operation"))
        self.label.setText(_translate("MainWindow", "Clairvoyance Operation"))

        
#iniciando o programa 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowd = QtWidgets.QMainWindow()
    mainWidget = QtWidgets.QWidget()
    MainWindowd.setCentralWidget(mainWidget)  
    ui = Main()
    ui.setupUi(MainWindowd)
    MainWindowd.show()
    sys.exit(app.exec_())
    

