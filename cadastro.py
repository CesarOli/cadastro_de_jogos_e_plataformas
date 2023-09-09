from PyQt5 import uic, QtWidgets
import mysql.connector
from time import sleep

app = QtWidgets.QApplication([])

banco_de_dados = mysql.connector.connect(    
    host='localhost',
    user='root',
    password='SENHA_DESEJADA',
    database='Estante_Virtual_de_Games_e_Plataformas'
)

tela_lista_de_jogos = uic.loadUi('lista_de_jogos.ui')
tabela = tela_lista_de_jogos.tableWidget


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
    inserir_no_SQL = "INSERT INTO Games (ID, Nome_do_Jogo, Ano_Lancamento, Plataforma) VALUES (%s, %s, %s)"
    jogos = (str(nome_do_jogo), str(ano_lancamento), plataforma)
    cursor.execute(inserir_no_SQL, jogos)
    banco_de_dados.commit()

    cadastro.lineEdit.clear()
    cadastro.lineEdit_2.clear()
    cadastro.radioButton.setChecked(False)

def chama_tela_lista_de_jogos():
    tela_lista_de_jogos.show()

    cursor = banco_de_dados.cursor()
    seleciona_a_tabela = "SELECT * FROM  Games"
    cursor.execute(seleciona_a_tabela)
    dados_recebidos = cursor.fetchall()

    colunas = ['ID', 'Nome_do_Jogo', 'Ano_Lancamento', 'Plataforma']

    tela_lista_de_jogos.tableWidget.setRowCount(len(dados_recebidos) + 1)
    tela_lista_de_jogos.tableWidget.setColumnCount(len(colunas))

    for j in range(len(colunas)):
        tela_lista_de_jogos.tableWidget.setItem(0, j, QtWidgets.QTableWidgetItem(colunas[j]))

    for i in range(len(dados_recebidos)):
        for j in range(len(dados_recebidos[i])):
            item = dados_recebidos[i][j] if j < len(dados_recebidos[i]) else ""
            tela_lista_de_jogos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))

    
cadastro = uic.loadUi('cadastro.ui')
tela_lista_de_jogos = uic.loadUi('lista_de_jogos.ui')
cadastro.pushButton_3.clicked.connect(cadastro_de_jogos)
cadastro.pushButton_4.clicked.connect(chama_tela_lista_de_jogos)

sleep(1.5)
cadastro.show()
app.exec()
