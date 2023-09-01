from PyQt5 import uic, QtWidgets

def cadastro_de_jogos():
    print('Funcionou!!')

app = QtWidgets.QApplication([])
cadastro = uic.loadUi('cadastro.ui')
cadastro.pushButton.clicked.connect(cadastro_de_jogos)  # Correção aqui

cadastro.show()
app.exec()
