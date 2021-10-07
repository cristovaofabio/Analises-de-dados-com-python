import sqlite3
#criando/conectando ao banco de dados
con=sqlite3.connect('escola.db')
#criando um cursor para percorrer o banco de dados
cur=con.cursor()
#variavel para receber instrução sql
'''sql_create = 'create table cursos(id integer primary key,titulo varchar(100),categoria varchar(140))'
#executar instrução sql
cur.execute(sql_create)
#variavel para inserir registros
sql_insert='insert into cursos values(?,?,?)'
#dados
dados=[(1000,'Ciencia de dados','Data Science'),(1001,'Fundamentos de Big Data','Big Data'),(1002,'Fundamentos de python','Analise de dados')]
#inserindo os dados
for linha in dados:
	cur.execute(sql_insert,linha)
#Grava a transacao
con.commit()
#intrucao sql para selecionar registros
sql_select='select * from cursos'
#selcionar todos os registros
cur.execute(sql_select)
#recuperar os resultados
valores = cur.fetchall()

for linha in valores:
	print('Id Curso: %d, Titulo: %s, Categoria: %s'%linha)'''

sql_insert='insert into cursos values(?,?,?)'
OutrosDados = [(1003,'Gestao de dados','Big Data'),(1004,'Fundamentos de R','Analise de daddos')]

for linha in OutrosDados:
	cur.execute(sql_insert,linha)
con.commit()
cur.execute('select * from cursos')
valores = cur.fetchall()

for linha in valores:
	print('Id Curso: %d, Titulo: %s, Categoria: %s'%linha)
con.close()
