from operator import itemgetter

diccionario_cuento={} #Deficion del diccionario que tendrá cada palabra del cuento

archivo=open('funes.txt',encoding='utf-8') #Se abre el cuento
cuento=archivo.read()   #guarda todo el cuento en forma de String en la variable "cuento"
archivo.close()         #cierra el archivo de texto
cuento=cuento.lower()   #transforma el string con todo el cuento al mismo string con solo minusculas
lista_cuento = cuento.split()   #crea una lista con cada palabra del cuento, esto incluye palabras repetidas
diccionario_cuento = dict.fromkeys(lista_cuento,0)  #crea un diccionario a partir de la lista previamente creada, cada 'key' del diccionario es inicializada con el valor 0

#Recorre la lista con las palabras del cuento
for i in lista_cuento:

    #Si la palabra que está en la lista se encuentra en el diccionario se suma 1 al valor de la respectiva 'key' en el diccionario
    if i in diccionario_cuento:
        diccionario_cuento[i] = int(diccionario_cuento[i]+1)

#Se crea una lista que contiene tuplas de cada 'key' del diccionario con su respectivo valor, ordenadas por su valor de menor a mayor
diccionario_ordenado=sorted(diccionario_cuento.items(), key=itemgetter(1), reverse=True)

#Imprime la lista de tuplas ya previamente ordenada con un salto de linea
for i in diccionario_ordenado:
    print(i,"\n")
