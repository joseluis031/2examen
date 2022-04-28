import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt



class Grafico:
    def __init__(self,dataset,col1,col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2
        
    def grafico(self,title):
        self.dataset = pd.read_csv("Pokemon.csv")
        self.dataset.groupby(self.col1)[self.col2].sum().plot(kind="bar")
        plt.title(title)
        plt.xlabel(None)
        plt.show()
        
grafico2 = Grafico("Pokemon.csv","Attack","Defense")
grafico2.grafico("Grafico Ataque-Defensa")