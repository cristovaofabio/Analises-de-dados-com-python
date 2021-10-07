import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression #Modulo de regressao linear y=a+bx

def precisao():
	#Dados de treino
	Diametros=[[7],[10],[15],[30],[45]]
	Precos=[[8],[11],[16],[38.5],[52]]

	#Modelo
	modelo=LinearRegression()

	#Treinando o modelo
	modelo.fit(Diametros,Precos)

	valores=[12,20,50]#valores que quero descobrir

	for x in range(len(valores)):
		print('Uma pizza de %i cm de diametro deve custar: R$%.2f'%(valores[x],modelo.predict(valores[x])))


precisao()

'''plt.figure()
plt.xlabel('Diametro(cm)')
plt.ylabel('Preco(R$)')
plt.title('Diametro x Preco')
plt.plot(Diametros,Precos, 'k.')
plt.axis([0,60,0,60])
plt.grid(True)
plt.show()'''
