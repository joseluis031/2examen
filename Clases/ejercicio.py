import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        
    def calculo_media(self):
        