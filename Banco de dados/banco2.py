import sqlite3
import random
import time
import matplotlib.pyplot as plt
import datetime
#criando/conectando ao banco de dados
conexao=sqlite3.connect('dsa.db')
#criando um cursor para percorrer o banco de dados
c=conexao.cursor()
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS prod(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_nome VARCHAR(100), valor REAL)')

def dat_insert():
	c.execute("INSERT INTO prod VALUES(1,'2016-05-02','Teclado',90)")
	conexao.commit()
	c.close()
	conexao.close()

def view_insert():
	c.execute('SELECT * FROM prod')
	dados = c.fetchall()
	for dado in dados:
		print('Id: %d, date: %s, nome: %s, valor: %d'%dado)

def data_insert_var():
	new_date=datetime.datetime.now()
	new_prod_name='Monitor'
	new_valor=random.randrange(50,100)
	c.execute("INSERT INTO prod(date,prod_nome,valor) values(?,?,?)",(new_date,new_prod_name,new_valor))
	conexao.commit()

def dados_grafico():
	c.execute("SELECT id,valor from prod")
	ids=[]
	valores=[]
	dados=c.fetchall()
	for linha in dados:
		ids.append(linha[0])
		valores.append(linha[1])
	plt.bar(ids,valores)
	plt.show()

create_table()

#dat_insert()

view_insert()

#for i in range(10):
#	data_insert_var()
#	time.sleep(1)

dados_grafico()

c.close()
conexao.close()
