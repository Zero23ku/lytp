from random import * #Modulo con función que retorna un número entero al azar

def scrap(pierdes,ganas):
    jugar = True #Variable que repetira el juego si es que se llega sacar un punto hasta que se gane o se pierda

    lanzamiento = (randint(1,6),randint(1,6))   #Lanzamiento del dado
    print("Lanzamiento: "+ str(lanzamiento))    #Muestra el lanzamiento
    if lanzamiento in pierdes:  #Si el lanzamiento está en "pierdes", pierdes
        print("Pierdes")
    else:
        if lanzamiento in ganas:    #Si el lanzamiento está en "ganas", ganas
            print("Ganas")
        else:                   #Si el lanzamiento no está ni en "ganas" ni "pierdes", obtienes un punto
            print("Punto")
            
            puntaje = lanzamiento[0] + lanzamiento[1]   #Se obtiene el puntaje del primer lanzamiento
            
            while jugar:   #Este ciclo se repetirá hasta que se gane o se pierda
                
                lanzamiento_punto = (randint(1,6),randint(1,6)) #Nuevo lanzamiento
               
                print("Lanzamiento: "+ str(lanzamiento_punto))  #Imprime el nuevo lanzamiento

                if puntaje == 7:    #Si el puntaje es 7, se pierde
                    print("Pierdes")
                    jugar = False
                else:
                    if lanzamiento_punto == lanzamiento:    #Si el puntaje del nuevo lanzamiento es igual al puntaje del primer lanzamiento, ganas.
                        print("Ganas")
                        jugar = False
        
        



dado = [] #Lista vacia donde se guardaran todas las combinaciones posibles con 2 dados

for i in range(13):
    dado.append(set())  #Añade 12 conjuntos vacios a la lista

#Se crean todas las combinaciones posibles y se guardan dentro de la lista
#El indice del al ista indica la suma de los dados que corresponden a dicho set
for i in range(1,7):
    for j in range(1,7):
        dado[i+j].add((i,j))

pierdes = dado[2]|dado[3]|dado[12] #Lanzamiento que te hacen perder

ganas = dado[7]|dado[11]    #Lanzamientos que te hacen ganar

punto = dado[4]|dado[5]|dado[6]|dado[8]|dado[9]|dado[10] #Lanzaqmientos que te dan un punto

scrap(pierdes,ganas)

