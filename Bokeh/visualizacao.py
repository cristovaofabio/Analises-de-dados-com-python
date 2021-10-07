import bokeh
from bokeh.plotting import figure,output_file,show
from bokeh.charts import Bar,output_notebook,show
import numpy as np
from bokeh.layouts import gridplot

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = [50, 40, 65, 10, 25, 37, 80, 60]
data = {"valores": [1, 2, 3, 4, 5]}

def grafico_linha():
	output_file("Bokeh-Grafico-Interativo.html")
	p=figure()
	p.line([1,2,3,4,5],[6,7,2,4,5],line_width=2)
	p.circle([1,2,3,4,5], [6,7,2,4,5], fill_color="white", size=8)
	show(p)

def grafico_barra():
	output_file('vbar.html')
	p = figure(width=400, height=400)
	p.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[1, 4, 9], color="black")
	show(p)

def circulo_e_letras(x,factors):
	output_file("categorical.html")
	p = figure(y_range=factors) #nao modificar
	p.circle(x, factors, size=10, color="navy", alpha=0.5)
	show(p)

def GraficosTela():

	# output to static HTML file
	output_file("graficos.html")

	# create a new plot
	p1 = figure(width=400, height=400)
	p1.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[1, 4, 9], color="green")

	# NEW: create a new plot and share both ranges
	p2=figure(width=400, height=400)
	p2.line([1,2,3,4,5],[6,7,2,4,5],line_width=2, color="blue")

	# NEW: create a new plot and share only one range
	p3 = figure(width=400, height=400,y_range=["a", "b", "c", "d", "e", "f", "g", "h"]) #nao modificar
	p3.circle([50, 40, 65, 10, 25, 37, 80, 60], ["a", "b", "c", "d", "e", "f", "g", "h"], size=10, color="navy", alpha=0.5)

	# NEW: create a new plot and share only one range
	p5 = figure(width=400, height=400,y_range=["a", "b", "c", "d", "e", "f", "g", "h"],title='quadrado')
	p5.square([40, 35, 55, 5, 15, 32, 70, 55], ["a", "b", "c", "d", "e", "f", "g", "h"], size=10, color="orange", alpha=0.5)

	# NEW: put the subplots in a gridplot
	p = gridplot([[p1, p2,p3], [p5,None,None]] ) #forma de exposicao

	# show the results
	show(p)

GraficosTela()
