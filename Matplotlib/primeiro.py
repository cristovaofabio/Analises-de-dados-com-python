import matplotlib.pyplot as plt
from pylab import *
#geracao de mapas
from mpl_toolkits.mplot3d import Axes3D #para geracao de gráficos 3D
from mpltoolkits.basemap import Basemap

x=[1,2,3,4,5,6,7,8] #quantidade de pessoas
y=[2,5,7,9,2,2,5,9]
idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130] #intervalos
x2=[8,6,4,2]
y2=[3,4,8,5]
atividades=['dormir','comer','trabalhar','passear']
Corcolunas=['c','m','r','k']

def graficoLinha(x,y):
	plt.plot(x,y, label='Legenda da linha')
	plt.xlabel("Variavel x")
	plt.ylabel("Variavel y")
	plt.title("Teste Plot")
	plt.legend()
	plt.show()

def graficoBarra(x,y,x2,y2):
	plt.bar(x,y, label="Legenda Barra 1", color ='r')#red
	plt.bar(x2,y2, label="Legenda Barra 2", color ='g')#green
	plt.legend()
	plt.show()

def histograma(idades,bins):
	plt.hist(idades,bins,histtype='bar', rwidth=1)
	plt.show()

def scatterplot(x,y):
	plt.scatter(x,y,label='Pontos',color='r',marker='o',s=100)
	plt.legend()
	plt.show()

def graficoPizza(fatias,atividades,colunas):
	plt.pie(fatias,labels=atividades,colors=colunas,startangle=90, shadow=True, explode=(0,0.1,0,0))
	plt.show()

#varios graficos em uma única imagem
'''_,ax=plt.subplots(2,3) #duas linhas e tres colunas
ax[0,0].hist(idades,bins)
ax[0,0].set_title('Histograma')
ax[0,2].plot(x,y)
ax[0,1].scatter(x,y,color='red')
ax[0][1].grid(True) #adicionar grid
plt.show()'''


