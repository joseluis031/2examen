import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.N = self.datos["#"].sum()

    def calculo_media(self):
        suma = self.datos["Total"].sum()
        return suma/self.N
    
    def calculo_desvi(self):
        suma_desvi = self.datos["Total"].sum() * self.datos[("#"- self.calculo_media)**2]
        return sqrt(suma_desvi/self.N)
