from bokeh.charts import Histogram, output_file, show
import pandas as pd

data_frame=pd.read_csv('HR_comma_sep.csv')
#print(type(data_frame['age']))
#print(data_frame['age']) #mostra as cinco primeiras linhas
p = Histogram(data_frame['satisfaction_level'], title="Satisfation Leval")
output_file("histogram.html",)

show(p)
