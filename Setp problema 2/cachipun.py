def cachipun(jugadores):
    
    if len(jugadores) != 2: #Comprueba que solo hayan dos jugadores
        raise Exception("Cantidad de jugadores incorrecta")
    else:
       
        if (jugadores[0][1] == 'R' or jugadores[0][1] == 'T' or jugadores[0][1] == 'P') and (jugadores[1][1] == 'R' or jugadores[1][1] == 'T' or jugadores[1][1] == 'P'):
           
            #Comprueba si el jugadorea 1 le gana o empata al jugador 2, si eso pasa, jugador 1 gana
            if jugadores[0][1] == 'R' and jugadores[1][1] == 'T' or jugadores[0][1] == 'P' and jugadores[1][1] == 'R' or jugadores[0][1] == 'T' and jugadores[1][1] == 'P' or jugadores[0][1] == jugadores[1][1]: #Comprueba si el jugador 1 gana
                print("Jugador",jugadores[0][0],"gana")
            #Si no se cumple alguna de las condiciones para que el jugador 1 gane, gana el jugador 2
            else:
                print("Jugador",jugadores[1][0],"gana")
        else:
            raise Exception("Jugada no valida")
                                                        




#Ingresa los jugadores y su jugada
jugadores = [[input("Ingrese el nombre del primer jugador"),input("Ingrese su jugada(Piedra=R,Papel=P,Tijeras=T)")],[input("Ingrese el nombre del segundo jugador"),input("Ingrese su jugada(Piedra=R,Papel=P,Tijeras=T)")]]    

#Transforma la jugada a mayuscula
jugadores[0][1]=jugadores[0][1].upper()
jugadores[1][1]=jugadores[1][1].upper()

#Llamado de la función
cachipun(jugadores)

