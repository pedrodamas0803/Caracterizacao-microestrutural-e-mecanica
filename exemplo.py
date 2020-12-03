import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mechtest_ufmg.Properties import *

dados = pd.read_csv('dados/astm1055.tsv', sep = '\t', decimal = ',')

strain = dados['Strain']
stress = dados['Stress']

plot_eng_SSC(strain, stress, fig_label = 'Aço 1055', show_plot = True, save = True,
name = 'engineering_1055')