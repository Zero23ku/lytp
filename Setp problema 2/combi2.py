import itertools #Módulo que tiene la función para obtener las k-combinaciones de un junto

#Funcionb que determina las k combinaciones posibles de un set determinado
def combinatoria2(conjunto,k):
    
    #Lista vacia
    lista_aux=[]

    #Ciclo que va obteniendo las diferentes combinaciones posibles (sin repetir)
    for combinacion in itertools.combinations(conjunto,k):
        lista_aux.append(combinacion) #Agrega la combinacion obtenida al final de una lista
    

    return lista_aux #Retorna la lista con todas las combinaciones posibles


conjunto = set() #Variable tipo set vacia

#Ciclo que DEBERIA repetirse hasta que lo que ingrese el usuario sea un entero igual o mayor a 1
while True:
    cantidad=int(input("Ingrese la cantidad de elementos que desea ingresar al conjunto "))

    
    #Comprueba que el entero ingresado sea mayor a 1
    if cantidad < 1:
        print("Error, usted no ha ingresado un numero inferior a 1")
    else:
        #Ciclo que se repetira tantas veces como elementos desee ingresar el usuario (Entero ingresado anteriormente por el usuario)
        for i in range(0,cantidad):
            elemento=input("Ingrese un elemento: ")
            conjunto.add(elemento) #Se añade el elemento al set declarado previamente
        break

#Ciclo que DEBERIA repetirse hasta que el 'k' ingresado por el usuario sea valido
while True:
    print("Ingrese un numero 'k' mayor a 0 y menor o igual a",cantidad)
    k=int(input())

    if k > cantidad or k < 1:
        print("Error, k no valido")
    else:
        break
    

#Variable tipo lista que recibe todas las combinaciones posibles del un set determinado por el usuario
lista_combinaciones=combinatoria2(conjunto,k)

#Imprime la lista con todas las combinaciones posibles del set
for elemento in lista_combinaciones:
    print(elemento,"\n")
