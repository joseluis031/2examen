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
    
    def calculo_media_ataque(self):
        suma = self.datos["Attack"].sum()
        return suma/self.N
    
    def calculo_media_defense(self):
        suma = self.datos["Defense"].sum()
        return suma/self.N
    
    def calculo_media_hp(self):
        suma = self.datos["HP"].sum()
        return suma/self.N
    
    
    
    
    def calculo_desvi(self):
        suma_desvi = self.datos["Total"].sum() * self.datos[("#"- self.calculo_media)**2]
        return sqrt(suma_desvi/self.N)
