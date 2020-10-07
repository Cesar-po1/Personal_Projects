"""
Cesar Ponce de la Fuente A01027756
03/10/2019
Memoria-reto
"""
import sys
def main(): #funcion principal de aqui parten todas
    #variables
    menu1=0
    seleccion=0
    acum=0
    player1=0
    player2=0
    seleccion=menu() #se llama a la funcion menu para empezar
    if seleccion<4: #para que se corra el programa debe de ser una opcion distinta a salir
        selec=procesaLaOpcion(seleccion)
        numeros=acomodo() #da valor a cada posicion
        simbolos=tableroGral(numeros) #tabla principal qeu se imprime
        cartas=tablero(simbolos) #tabla de simbolos sin valor
        while acum<18: #valida que el numero de pares no sea mayor a 18 y si no termina el programa
            player1+=jugador1(simbolos,numeros) #llama a los juegos de cada jugador
            player2+=jugador2(simbolos,numeros)
            acum=player1+player2 #Hace el acumulado de pares
        if player2 < player1: #Define quien es el ganador
            print("Jugador 1 es el campeon")
        elif player1 < player2:
            print("Jugador 2 es el campeon")
        else:
            ("Es un empate, buen juego")
        print()
        print()
        menu()
    else: #regresa el menú
        print(" (ง'̀-'́)ง Hasta nunca (•̀o•́)ง ".center(50, "-")) #mensaje si se selecciono salir
    
    #Fin del while que llama infinitamente a menu
#Fin de main

def menu():
    #variables
    opcion=0 #aqui almacenamos la opcion que quiere el ususario
    print("Memoria".center(50, "-"))
    print("1)Jugar")
    print("2)Instrucciones")
    print("3)Reiniciar")
    print("4)Salir")
    opcion=int(input("Que opcion deseas?   ")) #pide que opcion se procesara
    print()
    while opcion>4:
        print("Selecciona una opcion viable")
        print()
        opcion=int(input("Que opcion deseas?   "))
        print()
    if opcion==4:
        sys.exit()
    return opcion
#Fin de menu
    
def procesaLaOpcion(seleccion):
    if (seleccion==1):
        print("Vamos a jugar M E M O R I A DE CESAR".center(50, "-")) #Primer imagen que se muestra
        return #es para regresar y empezar el juego
    elif (seleccion==2): #instrucciones
        print("2 jugadores\nSelecciona 2 coordenadas del 0-5, una para las coordenadas y y otra las coordenadas x \nAl destapar todas las cartas el jugador que haya hecho mas pares gana")
        print()
        main()
    elif (seleccion==3): #se reinicia el juego
        print("El juego se reiniciara")
        print("3...2...1...")
        print("""/¯¯¯¯¯¯¯¯¯¯¯¯¯\  |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|  |¯¯¯¯¯¯¯¯¯¯¯¯¯¯| |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯| |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n
                 |  |¯¯¯¯¯¯¯¯¯¯¯¯  |     |¯¯¯¯¯¯¯¯    |   |¯¯¯¯¯¯¯¯¯¯| |   |¯¯¯¯¯¯¯|  |  |  |¯¯¯¯¯¯¯¯¯¯|   |\n
                 |  |              |      ¯¯¯¯¯¯¯¯|   |___________   |  |   |_______|  |  |  ¯¯¯¯¯¯¯¯¯¯¯    |\n
                 |  |              |     |¯¯¯¯¯¯¯¯¯               |  |  |   |       |  |  |   \   \¯¯¯¯¯¯¯¯¯¯¯\n
                 |  |___________   |     |__________   ___________|  |  |   |       |  |  |   |\   \\n
                 \_______________\ |_______________|   |_____________|  |___|       |__|  |___| \___\ """)
        print()
        print()
        main()
        
def acomodo(): #shufflea los numeros de la lista
    import random
    lista=0
    matriz=0
    lista=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
    random.shuffle(lista)
    matriz=lista[:6],lista[6:12],lista[12:18],lista[18:24],lista[24:30],lista[30:36]
    return matriz
    
def tableroGral(matriz):
    y=0
    x=0       #es la lista que se usara y en la cual se sustituiran los numeros en la lista
    t=[]
    for y in range (0,len(matriz),1):
        t.append([])
        for x in range(0,len(matriz[y]),1):
            t[y].append("♠")
    return t

def tablero(matriz): #es la funcion que imrpime el tablero
    y=0
    x=0
    for y in range (0,len(matriz),1):
        for x in range(0,len(matriz[y]),1):
            print(matriz [y][x], end=" ")
        print()
    print()
    
def jugador1(simbolos,numeros): #juego para el jugador 1
    print()
    #variables
    a="JUGADOR 1"
    num1=0
    num2=0
    acum1=0
    x=0
    y=0
    fila1=0
    fila2=0
    colum1=0
    colum2=0
    print(a.center(50, "-")) #Imprime el jugador
    while num1==num2: #establece que si el jugador no saca pares le toca al otro jugador
        fila1=int(input("Seleccione la fila del primer numero "))
        colum1=int(input("Seleccione la columna del primer numero "))
        if fila1>len(numeros) or colum1>len(numeros[fila1]): #si los valores estan fuera de rango se piden de nuevo
            fila1=int(input("Seleccione la fila del primer numero "))
            colum1=int(input("Seleccione la columna del primer numero "))
        fila2=int(input("Seleccione la fila del segundo numero "))
        colum2=int(input("Seleccione la columna del segundo numero "))
        if fila2>len(numeros) or colum2>len(numeros[fila2]): #si los valores estan fuera de rango se piden de nuevo
            fila2=int(input("Seleccione la fila del segundo numero "))
            colum2=int(input("Seleccione la columna del segundo numero "))
        if fila2==fila1 and colum2==colum1: #si se escogen los mismos valores en ambas selecciones se piden de nuevo
            print()
            print("Debes seleccionar 2 casillas diferentes ")
            fila2=int(input("Seleccione la fila del segundo numero "))
            colum2=int(input("Seleccione la columna del segundo numero "))
        for y in range (0,len(numeros),1): #ve que valores se encuentran en las casillas seleccionadas
            for x in range(0,len(numeros[y]),1):
                if y==fila1 and x==colum1:
                    simbolos[y][x]
                elif y==fila2 and x==colum2:
                    simbolos[y][x]
        simbolos[fila1][colum1]=numeros[fila1][colum1]
        simbolos[fila2][colum2]=numeros[fila2][colum2]
        tablero(simbolos) #imprime el tablero
        num1=numeros[fila1][colum1]
        num2=numeros[fila2][colum2]
        if num1==num2: #contador si se escogen pares
            acum1+=1
            print(a," Hiciste un par!, tu turno de nuevo")
            simbolos[fila1][colum1]=num1
            simbolos[fila2][colum2]=num2
            tablero(simbolos) #imprime el tablero
        else:
            print(a," Fallaste, turno del otro jugador")
            simbolos[fila1][colum1]="♠"
            simbolos[fila2][colum2]="♠"
            tablero(simbolos) #imprime el tablero
#        seguir=input("¿Quieres seguir jugando? y/n ")
#        if seguir=="y":#que hacer si se quiere segui jugando
#            continue #se continua el juego
#        elif seguir=="n": #que hacer si no se quiere segui jugando
#            print(a, "tiene", acum1, "pares")
#            print("JUGADOR 2", "tiene", acum1, "pares")
#            sys.exit()
    else:
        return acum1 #regresa a main para ejercutarse otra vez

def jugador2(simbolos,numeros):
    print()
    a="JUGADOR 2"
    num1=0
    num2=0
    acum2=0
    x=0
    y=0
    fila1=0
    fila2=0
    colum1=0
    colum2=0
    print(a.center(50, "-"))
    while num1==num2: #establece que si el jugador no saca pares le toca al otro jugador
        fila1=int(input("Seleccione la fila del primer numero "))
        colum1=int(input("Seleccione la columna del primer numero "))
        if fila1>len(numeros) or colum1>len(numeros[fila1]): #si los valores estan fuera de rango se piden de nuevo
            fila1=int(input("Seleccione la fila del primer numero "))
            colum1=int(input("Seleccione la columna del primer numero "))
        fila2=int(input("Seleccione la fila del segundo numero "))
        colum2=int(input("Seleccione la columna del segundo numero "))
        if fila2>len(numeros) or colum2>len(numeros[fila2]): #si los valores estan fuera de rango se piden de nuevo
            fila2=int(input("Seleccione la fila del segundo numero "))
            colum2=int(input("Seleccione la columna del segundo numero "))
        if fila2==fila1 and colum2==colum1: #si se escogen los mismos valores en ambas selecciones se piden de nuevo
            print()
            print("Debes seleccionar 2 casillas diferentes ")
            fila2=int(input("Seleccione la fila del segundo numero "))
            colum2=int(input("Seleccione la columna del segundo numero "))
        for y in range (0,len(numeros),1): #ve que valores se encuentran en las casillas seleccionadas
            for x in range(0,len(numeros[y]),1):
                if y==fila1 and x==colum1:
                    simbolos[y][x]
                elif y==fila2 and x==colum2:
                    simbolos[y][x]
        simbolos[fila1][colum1]=numeros[fila1][colum1]
        simbolos[fila2][colum2]=numeros[fila2][colum2]
        tablero(simbolos)
        num1=numeros[fila1][colum1]
        num2=numeros[fila2][colum2]
        if num1==num2: #contador si se escogen pares
            acum2+=1
            print(a," Hiciste un par!, tu turno de nuevo")
            simbolos[fila1][colum1]=num1
            simbolos[fila2][colum2]=num2
            tablero(simbolos) #imprime el tablero
        else:
            print(a," Fallaste, turno del otro jugador")
            simbolos[fila1][colum1]="♠"
            simbolos[fila2][colum2]="♠"
            tablero(simbolos) #imprime el tablero
        seguir=input("¿Quieres seguir jugando? y/n ")
        if seguir=="y": #que hacer si se quiere segui jugando
            continue #se continua el juego
        elif seguir=="n": #que hacer si no se quiere segui jugando
            print(a, "tiene", acum2, "pares")
            print("JUGADOR 1 tiene", acum2, "pares")
            sys.exit()
    else:
        return acum2   #regresa a main para ejercutarse otra vez
main()
#termina el programa
