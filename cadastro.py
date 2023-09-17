from PyQt5 import uic, QtWidgets
import mysql.connector
from time import sleep

app = QtWidgets.QApplication([])

id_games = 0 

banco_de_dados = mysql.connector.connect(    
    host='localhost',
    user='root',
    password='SENHA_DESEJADA',
    database='Estante_Virtual_de_Games_e_Plataformas'
)

tela_lista_de_jogos = uic.loadUi('lista_de_jogos.ui')
tabela = tela_lista_de_jogos.tableWidget


#Função responsável por cadastro de jogos e suas informações
def cadastro_de_jogos():
    nome_do_jogo = cadastro.lineEdit.text()
    ano_lancamento = cadastro.lineEdit_2.text()
    plataforma = ''
    
    #Condicionais que verifica qual plataforma de jogo foi selecionada pelo usuário
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


    #Inseri jogos no banco de dados MySQL
    cursor = banco_de_dados.cursor()
    inserir_no_SQL = "INSERT INTO Games (Nome, Ano, Plataforma) VALUES (%s, %s, %s)"
    jogos = (str(nome_do_jogo), str(ano_lancamento), plataforma)
    cursor.execute(inserir_no_SQL, jogos)
    banco_de_dados.commit()

    #Limpa os campos do formulário depois que o usuário clica em 'Enviar'
    cadastro.lineEdit.clear()
    cadastro.lineEdit_2.clear()
    cadastro.radioButton.setChecked(False)


#Função responsável por exibir a lista de jogos cadastrados
def chama_tela_lista_de_jogos():
    tela_lista_de_jogos.show()

    #consulta jogos ba tabela Games do banco de dados
    cursor = banco_de_dados.cursor()
    seleciona_a_tabela = "SELECT * FROM Games"
    cursor.execute(seleciona_a_tabela)
    dados_recebidos = cursor.fetchall()


    #Configura a lista de jogos
    num_colunas = len(cursor.description)
    colunas = [desc[0] for desc in cursor.description]
    tela_lista_de_jogos.tableWidget.setColumnCount(num_colunas)
    tela_lista_de_jogos.tableWidget.setHorizontalHeaderLabels(colunas)
    tela_lista_de_jogos.tableWidget.setRowCount(len(dados_recebidos))

    #Preenche a tabela com as informações dos jogos
    for i in range(len(dados_recebidos)):
        for j in range(num_colunas):
            item = dados_recebidos[i][j] if j < len(dados_recebidos[i]) else ""
            tela_lista_de_jogos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))

#Função responsável pela exclusao de jogos na listagem
def excluir_jogos():
    linha = tela_lista_de_jogos.tableWidget.currentRow()
    tela_lista_de_jogos.tableWidget.removeRow(linha)

    #Identifica o id a ser excluído
    cursor = banco_de_dados.cursor()
    cursor.execute('SELECT id FROM Games')
    dados_recebidos = cursor.fetchall()
    id = dados_recebidos[linha][0]
    cursor.execute('DELETE FROM Games WHERE id='+ str(id))

#Função responsável por abrir tela para editar informaçoes dos jogos
def telinha_edicao_de_jogos():
    
    global id_games

    linha = tela_lista_de_jogos.tableWidget.currentRow()

    cursor = banco_de_dados.cursor()
    cursor.execute('SELECT id FROM Games')
    dados_recebidos = cursor.fetchall()
    id = dados_recebidos[linha][0]
    cursor.execute('SELECT * FROM Games WHERE id='+ str(id))
    jogo = cursor.fetchall()
    tela_edicao_de_jogos.show()
    id_games = id

    tela_edicao_de_jogos.lineEdit.setText(str(jogo[0][0]))
    tela_edicao_de_jogos.lineEdit_2.setText(str(jogo[0][1]))
    tela_edicao_de_jogos.lineEdit_3.setText(str(jogo[0][2]))
    tela_edicao_de_jogos.lineEdit_4.setText(str(jogo[0][3]))

#Função para salvar alterações nos jogos editados
def salvar_games_editados():
    global id_games
    nome = tela_edicao_de_jogos.lineEdit_2.text()
    ano = tela_edicao_de_jogos.lineEdit_3.text()
    plataforma = tela_edicao_de_jogos.lineEdit_4.text()
    
    # atualiza edição feita no banco de dados
    cursor = banco_de_dados.cursor()
    cursor.execute('UPDATE Games SET nome = "{}", ano = "{}", plataforma = "{}" WHERE id = {}'.format(nome, ano, plataforma, id_games))
    tela_edicao_de_jogos.close()
    chama_tela_lista_de_jogos() 
     
#Carregamento das interfaces gráficas
cadastro = uic.loadUi('cadastro.ui')
tela_lista_de_jogos = uic.loadUi('lista_de_jogos.ui')
tela_edicao_de_jogos = uic.loadUi('edita_jogo.ui')


#Conecta botões as funções
cadastro.pushButton_3.clicked.connect(cadastro_de_jogos)
cadastro.pushButton_4.clicked.connect(chama_tela_lista_de_jogos)
tela_lista_de_jogos.pushButton.clicked.connect(excluir_jogos)
tela_lista_de_jogos.pushButton_2.clicked.connect(telinha_edicao_de_jogos)
tela_edicao_de_jogos.pushButton. clicked.connect(salvar_games_editados)

#Inicia o aplicativo
sleep(1.5)
cadastro.show()
app.exec()
