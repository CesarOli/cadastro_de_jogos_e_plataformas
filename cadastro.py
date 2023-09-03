from PyQt5 import uic, QtWidgets
from time import sleep

def cadastro_de_jogos():
    nome_do_jogo = cadastro.lineEdit.text()
    ano_lancamento = cadastro.lineEdit_2.text()

    if cadastro.radioButton.isChecked():
        
    elif cadastro.radioButton_2.isChecked():
        
    elif cadastro.radioButton_3.isChecked():
        
    else:
        

app = QtWidgets.QApplication([])
cadastro = uic.loadUi('cadastro.ui')
cadastro.pushButton.clicked.connect(cadastro_de_jogos)
sleep(1.5)
cadastro.show()
app.exec()