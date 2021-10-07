import pandas as pd
#df_data={'pais':['Brasil','Argentina','Argentina','Brasil','Chile','Chile'],'ano':[2005,2006,2005,2006,2007,2008],'populacao':[170.1,30.5,32.2,172.6,40.8,42.0]}
#df = pd.DataFrame(df_data)

dataset=pd.read_csv('train.csv')

#TRATANDO CAMPOS NULOS

#print(dataset['age'].isnull()) #verificar compos nulos no DataFrame
print(dataset.isnull().any())	#quais colunas tem campos nulos
#print(dataset.dropna().head()) #remove todas linhas com pelo menos um campo nulo
#a funcao fillna() serve para preencher valores inexistentes, contudo, por padrao ela retorna um novo objeto. Caso queira apenas modifica o objeto original ela deve ser utilizada em conjunto com o argumento inplace=True.

dataset['age'].fillna(dataset['age'].mean(),inplace=True)
dataset['embarked'].fillna(dataset['embarked'].mode()[0],inplace=True)

print(dataset.isnull().any())	#quais colunas tem campos nulos

#ALGUMAS ANALISES ESTATISTICAS

#print(dataset.describe())#calcula estatisticas para cada coluna
#print(dataset.head()) #mostra as cinco primeiras linhas
#print(len(dataset[dataset.sex=="female"]))
#print(len(dataset))
