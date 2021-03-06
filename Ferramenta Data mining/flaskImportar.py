from flask import Flask, make_response, request, render_template
import pandas as pd
from werkzeug import secure_filename
import io
import numpy as np
import csv

app = Flask(__name__)

def transform(text_file_contents):
	return text_file_contents.replace("=", ",")

@app.route('/')
def form():
	return render_template('PaginaUpload.html')

@app.route('/transform', methods=["POST"])
def transform_view():
	f = request.files['data_file']
	if not f:
		return "No file"
	stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
	dataset=pd.read_csv(stream)
	elementosNulos=CamposNulos(dataset)
	return render_template('PaginaUpload.html',df=dataset.head().to_html(),valores=elementosNulos)

def CamposNulos(dataset):
	v=dataset.isnull().any() #quais colunas tem campos nulos
	variaveis=v.index #Atributos da tabela
	valores=v.values #Valores da tabela
	elementosNulos=[]
	for x in range(len(variaveis)):
		if(valores[x]==True):
			elementosNulos.append(variaveis[x])
	return elementosNulos

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)
