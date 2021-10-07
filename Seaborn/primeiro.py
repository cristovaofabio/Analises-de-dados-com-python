import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sea
dados = sea.load_dataset("tips")

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot("total_bill", "tip", dados, kind = 'reg')
