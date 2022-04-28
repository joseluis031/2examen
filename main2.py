if __name__ == "__main__":
        main = int(input("Que quieres calcular:la media(1),la desviacion tipica(2),68%(3),95%(4) o 99.7%(5):"))
        from Clases.ejercicio import *
        ejercicio = Ejercicio("entrenador 1.csv")
        ejercicio2 = Ejercicio("entrenador 2.csv")
        if main == 1:
            print("La media del entrenador 1 en total es: " ,ejercicio.calculo_media(), ",en HP es: ",ejercicio.calculo_media_hp(), ",en ataque es: ", ejercicio.calculo_media_ataque(),",en defensa es: ",ejercicio.calculo_media_defense())
            print("La media del entrenador 2 en total es: " ,ejercicio2.calculo_media(), ",en HP es: ",ejercicio2.calculo_media_hp(), ",en ataque es: ", ejercicio2.calculo_media_ataque(),",en defensa es: ",ejercicio2.calculo_media_defense())
            