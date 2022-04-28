import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

class Ejercicio: 
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.N = self.datos["#"].count()

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
        suma_desvi = self.datos["Total"].sum() * ((self.N- self.calculo_media)**2)
        return sqrt(suma_desvi/self.N)

    def calculo_porcent_68(self):
        intervalo = []
        inferior = self.calculo_media() - self.calculo_desvi()
        superior = self.calculo_media() + self.calculo_desvi()
        for i in range(400):
            if self.datos["#"][i]>inferior and self.datos["#"][i]<superior:
                intervalo.append(self.datos[self.N][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))
    
    def calculo_porcent_95(self):
        intervalo = []
        inferior = self.calculo_media() - 2*self.calculo_desvi()
        superior = self.calculo_media() + 2*self.calculo_desvi()
        for i in range(400):
            if self.datos["#"][i]>inferior and self.datos["#"][i]<superior:
                intervalo.append(self.datos[self.N][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))
    
    def calculo_porcent_99_7(self):
        intervalo = []
        inferior = self.calculo_media() - 3*self.calculo_desvi()
        superior = self.calculo_media() + 3*self.calculo_desvi()
        for i in range(400):
            if self.datos["#"][i]>inferior and self.datos["#"][i]<superior:
                intervalo.append(self.datos[self.N][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))
