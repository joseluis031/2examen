# 2examen

El link de este repositorio es: [GitHUb](https://github.com/joseluis031/2examen.git)

He dividido el dataset en 2 y he dado a cada entrenador la mitad de pokemon, luego he analizado cada dataset individualmente sacando de cada uno la media de algunas variables, asi como la desviacion tipica y los porcentajes, ademas de eso he conseguido el grafico de la media de la variable total de todos los pokemon

## Main
```
if __name__ == "__main__":
        main = int(input("Que quieres calcular:la media(1),la desviacion tipica(2),68%(3),95%(4) o 99.7%(5):"))
        from Clases.ejercicio import *
        ejercicio = Ejercicio("entrenador 1.csv")
        ejercicio2 = Ejercicio("entrenador 2.csv")
        if main == 1:
            print("La media del entrenador 1 en total es: " ,ejercicio.calculo_media(), ",en HP es: ",ejercicio.calculo_media_hp(), ",en ataque es: ", ejercicio.calculo_media_ataque(),",en defensa es: ",ejercicio.calculo_media_defense())
            print("La media del entrenador 2 en total es: " ,ejercicio2.calculo_media(), ",en HP es: ",ejercicio2.calculo_media_hp(), ",en ataque es: ", ejercicio2.calculo_media_ataque(),",en defensa es: ",ejercicio2.calculo_media_defense())
        elif main == 2:
            print("La media del entrenador 1 en total es: " ,ejercicio.calculo_desvi())
            print("La media del entrenador 1 en total es: " ,ejercicio2.calculo_media())
        elif main == 3:
            ejercicio.calculo_porcent_68()
        elif main == 4:
            ejercicio.calculo_porcent_95()
        elif main == 5:
            ejercicio.calculo_porcent_99_7()
              
```


## Codigo
```
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
```
