import pandas as pd                 
import matplotlib.pyplot as plt    
import numpy as np

df=pd.read_csv("pima-data.csv")
#print (df.shape) #mostra a quantidade de linhas e colunas

#print(df.isnull().values.any()) #verificar valores nulos

# Identificando a correlação entre as variáveis
# Correlação não implica causalidade
#print(df.corr()) #DataFrame

diabetes_map={True:1,False:0}
df['diabetes'] = df['diabetes'].map(diabetes_map)
print(df.head())
