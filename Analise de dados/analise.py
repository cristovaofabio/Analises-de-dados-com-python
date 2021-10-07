import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys


plt.style.use('seaborn-talk')
df=pd.read_csv('Dados-Pesquisa-2016.csv',sep=',',low_memory=False)
#print(df.head()) #apenas as cinco primeiras linhas
#print(df.describe()) #media,mediana,desvio padrao...quartis,percentis

#distribuicao das idade
def DistribuicaoIdade():
	df.Age.hist(bins=60)#histograma de idade em 60 intervalos
	plt.xlabel('Idade')
	plt.ylabel('Numero de profissionais')
	plt.title('Distribuicao das idades')
	plt.show()

#distribuicao por sexo
def histograma():
	DistribuicaoSex=df.Gender.value_counts() #quantidade de pessoas por sexo
	tipos=DistribuicaoSex.index #apenas os nomes
	valores=[]

	for x in range(len(tipos)):
		valores.append(DistribuicaoSex[tipos[x]])
		print(tipos[x],valores[x])

	fatias,texto=plt.pie(valores,startangle=90, shadow=True)
	plt.axes().set_aspect('equal','datalim')
	plt.legend(fatias,tipos,bbox_to_anchor=(1.05,1))
	plt.title("Distribuicao por sexo")
	plt.show()


'''num=len(df.EmploymentField.value_counts().index) #quantidade de diferentes campos de atuacao

#criando uma cor para cada campo de atucacao
listaFaixaCor=[(x*1.0/num,0.5,0.5) for x in range(num)]
listaCor=list(map(lambda x: colorsys.hsv_to_rgb(*x),listaFaixaCor))

#gerando grafico pizza
fatias,texto=plt.pie(df.Gender.value_counts(),colors=listaCor,startangle=90)
plt.axes().set_aspect('equal','datalim')
plt.legend(fatias,tipos,bbox_to_anchor=(1.05,1))
plt.title("Sexo")
plt.show()'''
