#Funcion que calcula los resultados de una ecuacion cuadratica
def raices(a,b,c):

    res1= (-b-(b^2+4*a*c)**(1/2))/(2*a) #Resultado 1
    res2= (-b+(b^2+4*a*c)**(1/2))/(2*a) #Resultado 2

    #Imprime resultado 1
    print("El primer resultado de la ecuacion cuadratica es",res1,"del tipo",type(res1))

    #Imprime resultado 2
    print("El primer resultado de la ecuacion cuadratica es",res2,"del tipo",type(res2))




def main():

    #Pide el valor del coeficiente que acompaña a x^2
    a=input("Ingrese el termino 'a' de la ecuacion cuadratica ")

    #Comprueba que a no sea 0
    if a==0:
        print("ERROR, a no puede ser 0")
        return 0
    #Pide el valor del coeficiente que acompaña a x
    b=input("Ingrese el termino 'b' de la ecuacion cuadratica ")

    #Pide el valor del coeficiente que no lleva x
    c=input("Ingrese el termino 'c' de la ecuacion cuadratica ")
    
    #Funcion que calcula los valores de la
    #funcion cuadratica a partir de los valores dados
    raices(int(a),int(b),int(c))

    return 0


if __name__ == '__main__':
    main()
