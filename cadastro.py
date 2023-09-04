from PyQt5 import uic, QtWidgets
import mysql.connector
from time import sleep

banco_de_dados = mysql.connector.connect(
    
    host='localhost',
    user='root',
    password='SENHA_DESEJADA',
    database='Estante_Virtual_de_Games_e_Plataformas'

)

def cadastro_de_jogos():
    nome_do_jogo = cadastro.lineEdit.text()
    ano_lancamento = cadastro.lineEdit_2.text()

    if cadastro.radioButton.isChecked():
        sleep(1)
        print('Nome do Jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('PS4/PS5 selecionado.')        
    
    elif cadastro.radioButton_2.isChecked():
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('XboX selecionado')
    
    elif cadastro.radioButton_3.isChecked():
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('PC selecionado')
        
    else:
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('"Outros" foi a plataforma selecionada.')

cursor = banco_de_dados.cursor()
app = QtWidgets.QApplication([])
cadastro = uic.loadUi('cadastro.ui')
cadastro.pushButton.clicked.connect(cadastro_de_jogos)
sleep(1.5)
cadastro.show()
app.exec()
