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
    plataforma = ''
    
    if cadastro.radioButton.isChecked():
        sleep(1)
        print('Nome do Jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('PS4/PS5 selecionado.')
        plataforma = 'PS4/PS5'
    
    elif cadastro.radioButton_2.isChecked():
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('XboX selecionado')
        plataforma = 'XboX'

    
    elif cadastro.radioButton_3.isChecked():
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('PC selecionado')
        plataforma = 'PC'
        
    else:
        sleep(1)
        print('Nome do jogo cadastrado: ', nome_do_jogo)
        print('Ano do Lançamento: ', ano_lancamento)
        print('"Outros" foi a plataforma selecionada.')
        plataforma = 'Outros'

    cursor = banco_de_dados.cursor()
    inserir_no_SQL = "INSERT INTO Games (Nome_do_Jogo, Ano_Lancamento, Plataforma) VALUES (%s, %s, %s)"
    jogos = (str(nome_do_jogo), str(ano_lancamento), plataforma)
    cursor.execute(inserir_no_SQL, jogos)
    banco_de_dados.commit()

    cadastro.lineEdit.clear()
    cadastro.lineEdit_2.clear()
    cadastro.radioButton.setChecked(False)
    
app = QtWidgets.QApplication([])
cadastro = uic.loadUi('cadastro.ui')
cadastro.pushButton.clicked.connect(cadastro_de_jogos)

sleep(1.5)
cadastro.show()
app.exec()
